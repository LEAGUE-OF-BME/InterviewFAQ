## 1、Spring事务分析 

### 1.1 事务的传播行为 ##
|常量|说明|
|---|---|
|PROPAGATION_REQUIRED|支持当前事务，如果没有事务就新建一个事务，这是最常见的选择|
|PROPAGATION_SUPPORTS|支持当前事务，如果没有事务，就以非事务方式执行|
|PROPAGATION_MANDATORY|支持当前事务，如果没有事务，就抛出异常|
|PROPAGATION_REQUIRES_NEW|新建事务，如果当前存在事务，就把当前事务挂起|
|PROPAGATION_NOT_SUPPORT|以非事务的方式执行操作，如果存在当前事务，就把当前事务挂起|
|PROPAGATION_NEVER|以非事务的方式执行，如果当前存在事务，则抛出异常|
|PROPAGATION_NESTED|如果当前存在事务，则在嵌套事务内执行，如果没有当前事务，则进行与PROPAGATION_REQUIRED类似的操作|

### 1.2 编程式事务 ##
事务管理的代码内嵌在普通的逻辑代码中，需要使用PlatformTransactionManager， TransactionDefinition和TransactionStatus三个核心接口，代码如下：
```java
public class BankServiceImpl implements BankService {
	private BankDao bankDao;
	private TransactionDefinition txDefinition;
	private PlatformTransactionManager txManager;
	......
	public boolean transfer(Long fromId， Long toId， double amount) {
		TransactionStatus txStatus = txManager.getTransaction(txDefinition);
		boolean result = false;
		try {
			result = bankDao.transfer(fromId， toId， amount);
			txManager.commit(txStatus);
		} catch (Exception e) {
			result = false;
			txManager.rollback(txStatus);
			System.out.println("Transfer Error!");
		}
		return result;
	}
}
```

### 1.3 声明式事务
Spring的声明式事务管理在底层是建立在AOP之上的。其本质是对方法前后进行拦截，然后在目标方法开始之前创建或者加入一个事务，在执行完目标方法之后根据执行情况提交或者回滚事务
目前最常用的是基于注解的配置方式，代码如下
```java
@Transactional(propagation = Propagation.REQUIRED)
public boolean transfer(Long fromId， Long toId， double amount) {
	return bankDao.transfer(fromId， toId， amount);
}
```


# Spring AOP实现原理 #
Spring AOP基于动态代理实现，所谓代理，即通过一个代理类去提供一个与源类相同的接口，代理类内部保留一个源类的对象。访问代理类的接口时，代理类接口调用源类的接口实现具体功能。使用代理类可以将业务逻辑与其他代码（如日志）分离。不过，前述的方式只是静态代理，在业务代码量非常大的情况下，使用静态代理需要写非常多的代理类，会使工程非常冗长庞大。 而动态代理能够以一种优雅的方式实现代理功能。所谓动态代理即在运行时动态的创建代理类，可以在运行过程中为被代理的类添加多种行为，这正是AOP的核心。
以下代码演示了如何使用Java JDK反射实现一个动态代理
首先，我们假设有一个User的管理类，这个类是我们的业务逻辑代码
```java
public interface UserMgr {
    void addUser();
    void delUser();
}
```
```java
public class UserMgrImpl implements UserMgr {
    @Override
    public void addUser(){
        System.out.println("add user ...");
    }

    @Override
    public void delUser(){
        System.out.println("delete user ...");
    }
}

```
我们需要有一个类能够为UserMgr动态的创建一个代理类，即通过反射，获取UserMgr的方法名等信息，通过字符串拼接的方式生成一个类。但是，在此之前，我们要明确一点创建代理类的目的是什么。我们的目的是能够在源类方法执行的前后添加一些行为。显然，我们不能直接将这些行为通过拼接字符串的方式添加到动态创建的代理类里面。所以我们需要一个类，这个类能够提供统一的接口供我们调用，此接口能够调用源类的方法，并且能够让我们在其调用前后添加行为。我们把这个类型抽象出来的interface作为我们动态创建的代理类的一个依赖。这样字符串的拼接就有一个通用的模式。
下面的代码是我们抽象出来的接口：
```java
public interface InvocationHandler {
    public void invoke(Object o, Method m);
}
```
我们可以随意实现这个接口，具体实现后面再讲。到此，我们需要一个创建代理类的类，代码如下
```java
public class DynamicProxy {

    public static Object newProxyInstance(Class infce, InvocationHandler handler) throws Exception {
        String methodStr = "";
        String rt = "\r\n";

        Method[] methods = infce.getMethods();

        // construct all method
        for (Method m : methods) {
            methodStr +=
                    "    @Override" + rt +
                            "     public  " + m.getReturnType() + " " + m.getName() + "() {" + rt +
                            "        try {" + rt +
                            "        Method md = " + infce.getName() + ".class.getMethod(\"" + m.getName() + "\");" + rt +
                            "        h.invoke(this, md);" + rt +
                            "        }catch(Exception e) {e.printStackTrace();}" + rt +
                            "      }" + rt;
        }

        //construct java file
        String srcCode =
                "import java.lang.reflect.Method;" + rt +
                        "public class $Proxy1 implements " + infce.getName() + "{" + rt +
                        "    public $Proxy1(InvocationHandler h) {" + rt +
                        "        this.h = h;" + rt +
                        "    }" + rt +
                        "    InvocationHandler h;" + rt +
                        methodStr + rt +
                        "}";

        //write java file to src path
        String fileName = "c:/GIT/MINE/LearnEverything/Solution/src/$Proxy1.java";
        File f = new File(fileName);
        FileWriter fileWriter = new FileWriter(f);
        fileWriter.write(srcCode);
        fileWriter.flush();
        fileWriter.close();

        //compile .java
        JavaCompiler compiler = ToolProvider.getSystemJavaCompiler();
        StandardJavaFileManager fileManager = compiler.getStandardFileManager(null, null, null);
        Iterable units = fileManager.getJavaFileObjects(fileName);
        JavaCompiler.CompilationTask t = compiler.getTask(null, fileManager, null, null, null, units);

        t.call();
        fileManager.close();


        //load .class
        URL[] urls = new URL[]{new URL("file:/" + "c:/GIT/MINE/LearnEverything/Solution/src/")};
        URLClassLoader ul = new URLClassLoader(urls);

        Class clazz = ul.loadClass("$Proxy1");
        Constructor constructor = clazz.getConstructor(InvocationHandler.class);

        // construct proxy object
        Object m = constructor.newInstance(handler);
        return m;
    }
}
```
代码中的注解已经说明，此类接受一个目标类型和一个InvocationHandler。通过反射获取目标类型的方法，以字符串拼接的方式生成一个Java类文件并进行编译加载。可以发现，生成的代理类接收一个InvocationHandler，并在内部执行invoke()方法。
下面我们看一下如何实现一个InvocationHandler，假设我们希望为每一个方法都添加一个事务，并且监测方法的调用时间与结束时间。这时我们可以创建两个handler类型，如下
```java
public class TransactionHandler implements InvocationHandler {


    private Object target;

    public TransactionHandler(Object target) {
        this.target = target;
    }

    @Override
    public void invoke(Object o, Method method) {
        System.out.println("transaction start ...");
        try {
            method.invoke(target);
        } catch (IllegalAccessException | InvocationTargetException ex) {
            ex.printStackTrace();
        }
        System.out.println("commit transaction");
    }


}

```

```java

public class TimeHandler implements InvocationHandler {

    private Object target;

    public TimeHandler(Object target) {
        this.target = target;
    }
    @Override
    public void invoke(Object o, Method method) {
        System.out.println("Start time " + new Date().toString());
        try {
            method.invoke(target);
        } catch (IllegalAccessException | InvocationTargetException ex) {
            ex.printStackTrace();
        }
        System.out.println("End time " + new Date().toString());
    }

}
```
这里handler会接收一个业务逻辑中定义的对象，在invoke()调用时会执行其对应method的调用，并且在其前后添加不同的行为。

这时我们就可以使用动态代理为我们的业务类添加额外的行为了，代码如下
```java
public class Client {

    public static void main(String[] args) throws Exception {
        UserMgr mgr = new UserMgrImpl();

        //add transaction manager
        InvocationHandler transactionHandler = new TransactionHandler(mgr);
        UserMgr u = (UserMgr) DynamicProxy.newProxyInstance(UserMgr.class, transactionHandler);

        //add time handler
        InvocationHandler timeHandler = new TimeHandler(u);
        u = (UserMgr) DynamicProxy.newProxyInstance(UserMgr.class, timeHandler);

        u.addUser();
        u.delUser();
    }
}

```
由于动态创建出的代理类型继承了业务类型，所以我们可以级联多个handler以为业务类型添加多种行为。上述代码输出如下
```
Start time Thu Aug 17 11:12:06 CST 2017
transaction start ...
add user ...
commit transaction
End time Thu Aug 17 11:12:06 CST 2017
Start time Thu Aug 17 11:12:06 CST 2017
transaction start ...
delete user ...
commit transaction
End time Thu Aug 17 11:12:06 CST 2017

```


## JAVA实现AOP的方法


