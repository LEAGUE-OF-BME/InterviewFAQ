## 创建对象的方法
### 工厂模式
在函数中封装了创建对象，添加属性的细节，返回新创建的对象。
```javascript
function createPerson(name, age) {
  var o = new Object()
  o.name = name
  o.age = age
  return o
}
```
**缺点：** 不能用instanceof检测对象类型，没有解决对象识别的问题。
### 构造函数模式
```javascript
function Person(name, age) {
  this.name = name
  this.age = age
  this.sayName = function() {
    alert(this.name)
  }
}

var p = new Person("geeook", 23)
```
**缺点：** 解决了对象识别问题，但是每个方法都要在每个实例上重新创建一遍，浪费内存。

**修改：**
```javascript
function Person(name, age) {
  this.name = name
  this.age = age
  this.sayName = sayName
}

function sayName() {
  alert(this.name)
}

var p1 = new Person("Geeook", 23)
var p2 = new Person("Kelly", 23)
```
**缺点：**
1. 在全局作用域中定义的函数只是为了某个对象服务，全局作用域“名不副实”。
2. 如果对象需要定义很多方法，如果全部在全局作用域中定义，这样毫无封装性可言。
### 原型模式
原型的用途就是包含所有实例共享的属性和方法。
```javascript
function Person() { }

Person.prototype.name = "Geeook"
Person.prototype.age = 23
Person.prototype.sayName = function () {
  alert(this.name)
}

var p = new Person()
```
**缺点：**（成也共享，败也共享）
1. 没有初始化参数，所有实例共享相同的属性值。
2. 方法共享非常合适，包含基本值的属性可以通过在实例上添加同名属性覆盖，但是对于包含引用值的属性来说，问题就很严重。

**e.g.**
```javascript
function Person() { }

Person.prototype = {
  constructor: Person,
  name: "Geeook",
  age: 23,
  friends: ["Kelly", "RengJruin", "Coder"]
}

var p1 = new Person()
var p2 = new Person()

p1.friends.push("Kai")
alert(p1.friends)
alert(p2.friends)
alert(p1.friends === p2.friends) // true
```
如果我们的初衷就是像这样在所有实例中共享一个数组，那么就没有问题，但是实例一般都是要有属于自己的全部属性。正是如此，我们很少单独使用原型模式。
### 组合使用构造函数模式和原型模式
<a name="1" id="1"> </a>创建自定义对象的最常见的方式就是组合使用构造函数模式和原型模式。构造函数用于定义实例属性，原型模式用于定义方法和共享属性。
```javascript
function Person(name, age) {
  this.name = name
  this.age = age
  this.friends = ["Kelly", "RengJruin", "Coder"]
}

Person.prototype = {
  constructor: Person,
  sayName: function () {
    alert(this.name)
  }
}

var p1 = new Person("Geeook", 23)
var p2 = new Person("Kai", 23)

p1.friends.push("Young")
alert(p1.friends)
alert(p2.friends)
alert(p1.friends === p2.friends) // false
alert(p1.sayName == p2.sayName) // true
```
这种模式是目前在ECMAScript中使用最广泛、认同度最高的创建自定义类型的方法。
### 动态原型模式
独立的构造函数和原型可能会令一些有其他OO语言经验的开发人员感到困惑。动态原型模式将所有信息都封装在构造函数中。
```javascript
function Person(name, age) {
  this.name = name
  this.age = age
  this.friends = ["Kelly", "RengJruin", "Coder"]
  if (typeof this.sayName != "function") {
    Person.prototype.sayName = function () {
      alert(this.name)
    }
  }
}

var p1 = new Person("Geeook", 23)
p1.sayName()
```
通过检查某个应该存在的方法是否有效，来决定是否初始化原型。只有在sayName方法不存在的情况下，才将它添加到原型中。这段代码只会在初次调用构造函数时才会执行。此后原型已经完成了初始化，不需要修改。

**注意：** 在使用动态原型模式时，不能用对象字面量重写原型，因为在已经创建实例的情况下重写原型会切断现有实例和新原型之间的联系。
### 寄生构造函数模式
在前述几种模式都不适用的情况下可以使用寄生构造函数模式。基本思想就是创建一个函数，封装创建对象的代码，并返回新创建的对象；但从表面上看又像是典型的构造函数。
```javascript
function Person(name, age) {
  var o = new Object()
  o.name = name
  o.age = age
  return o
}

var p = new Person("Geeook", 23)
```
除了使用new操作符之外，和工厂模式没有区别。构造函数在无返回值的情况下默认返回新对象实例，而如果返回另一个对象实例将重写构造函数的返回值。

**使用场景：** 在特殊情况下为对象创建构造函数。比如：想创建具有额外方法的特殊数组。在不直接修改Array构造函数和原型的前提下可以使用这个模式。

**e.g.**
```javascript
function SpecialArray() {
  var values = new Array()
  values.push.apply(values, arguments)
  values.toPipedString = function () {
    return this.join("|")
  }
  return values
}

var colors = new SpecialArray("red", "blue", "green")
colors.toPipedString() // red|blue|green
```
**缺点：** 很明显，不能用instanceof检测对象类型。建议在可以使用其他模式的情况下不要使用这种模式。
### 稳妥构造函数模式
道格拉斯发明了JavaScript中的**稳妥对象**这个概念。指的是没有公共属性，方法不引用this的对象。稳妥对象适合在安全的环境中，或者防止数据被其他程序修改时使用。稳妥构造函数和寄生构造函数类似，有两点不同：
1. 新创建对象的实例方法不引用this。
2. 不使用new操作符调用构造函数。
``` javascript
// 这样看起来真的超级安全
function Person(name, age) {
  var o = new Object
  // 可以在这里定义私有变量和函数
  o.sayName = function () {
    alert(name)
  }
  return o
}

var p = Person("Geeook", 23)
p.sayName()
```
这样创建的对象除了使用sayName方法之外，无法访问name属性。

**缺点：** 同寄生构造函数模式一样，无法使用instanceof检测对象类型。
### create()方法
<a name="2" id="2"> </a>ECMAScript5提出Object.create()方法，直接利用对象生成实例，不需要new关键字。
```javascript
var Person = {
  name: "Geeook",
  sayName: function () {
    alert(this.name)
  }
}

var p = Object.create(Person)
```
**内部实现原理：** 原型式继承
```javascript
Object.create = function (o) {
  function F() { }
  F.prototype = o
  return new F
}
```
通过create方法创建的实例，__proto__都指向传入函数的对象，所以共享属性。

**缺点：** 不能用instanceof判断对象类型。
### class关键字
ECMAScript6中定义了class、extends、super关键字，简化了JavaScript中类的实现和继承。
```javascript
// 定义类
class Person {
  constuctor(name, age) {
    this.name = name
    this.age = age
  }

  setName(name) {
    this.name = name
  }

  getName(name) {
    return this.name
  }

  toString() {
    return "name: " + this.name + ", age: " + this.age
  }
}

// 创建实例
var p = new Person("Geeook", 23)
p instanceof Person // true

// 继承
class Man extends Person {
  constructor(name, age, gender) {
    super(name, age)
    this.gender = gender
  }

  setGender(gender) {
    this.gender = gender
  }

  getGender() {
    return this.gender
  }

  toString() {
    return super.toString() + ", gender: " + this.gender
  }
}

var m = new Man("Geeook", 23, "male")
m instanceof Man // true
m instanceof Person // true
```
### new一个对象的过程
1. 创建新对象。
2. 将新对象的\__proto\__属性指向构造函数的prototype。
3. 调用构造函数，将其作用域赋给新对象，即把this绑定到新对象。
4. 执行构造函数中的代码，即为新对象的属性赋值。
5. 返回新对象。
> 你在阅读此文档时，可能ES8甚至9已经推出，ES6的这种写法应该很常见了，前面几种古董方法估计都没人用了。

----------
Geeook 于 2017/8/8 21:56:06 
## 继承
### 原型链
```javascript
function Person() {
  this.name = "Geeook"
}

function Man() {
  this.gender = "male"
}

// 继承
Man.prototype = new Person

var m = new Man
console.log(m.name) // Geeook
```
**注意：**
1. 现在m.constructor指向Person，是因为Man的原型对象指向Person的原型对象，然后这个原型对象的constructor属性指向Person。
2. 默认原型都指向Object.prototype。
3. 确定原型和实例的关系：instanceof操作符和isPrototypeOf方法。
4. 添加原型方法的代码一定要在替换原型之后，且不能用对象字面量的形式。

**问题：**
1. 包含引用类型值的原型。通过原型实现继承时，一个实例变成了另一个类型的原型，实例属性变成原型属性，不想被共享的属性现在被共享了。

**e.g.**
```javascript
function Person() {
  this.name = "Geeook"
  this.friends = ["Kelly", "RengJruin", "Coder"]
}

function Man() {
  this.gender = "male"
}

Man.prototype = new Person

var m1 = new Man
m1.friends.push("Kai")
console.log(m1.friends)
var m2 = new Man
console.log(m2.friends)
```
2. 创建子类型的实例时，不能向超类型的构造函数传递参数。应该说是没有办法在不影响所有对象实例的情况下给超类型的构造函数传递参数。
### 借用构造函数
为了解决原型中包含引用值类型问题，引入了**借用构造函数**的技术（又称为伪造对象或经典继承）。基本思想就是在子类的构造函数中调用父类的构造函数。
```javascript
function Person() {
  this.friends = ["Kelly", "RengJruin", "Coder"]
}

function Man() {
  // 继承
  Person.call(this)
}

var m1 = new Man
m1.friends.push("Kai")
console.log(m1.friends) // ["Kelly", "RengJruin", "Coder", "Kai"]
var m2 = new Man
console.log(m2.friends) // ["Kelly", "RengJruin", "Coder"]
```
**优势：** 可以在子类构造函数中向父类构造函数传递参数。注意先调用构造函数，再添加新属性，避免覆盖。
```javascript
function Person(name) {
  this.name = name
}

function Man() {
  // 继承
  Person.call(this, "Geeook")
  this.age = 23
}

var m = new Man
console.log(m.name)
console.log(m.age)
```
**问题：** 如果仅仅是借用构造函数，就无法避免构造函数模式存在的问题——方法不能复用。而且在父类原型上定义的方法对子类实例是不可见的。
### 组合继承
组合继承又称为伪经典继承，组合使用原型链和借用构造函数技术。通过原型链实现对原型属性和方法的继承，通过借用构造函数实现对实例属性的继承。（哇，这句话好熟悉。没错！在<a href="#1">创造对象的组合模式</a>中也有这么一句话。）
```javascript
function Person(name) {
  this.name = name
  this.friends = ["Kelly", "RengJruin", "Coder"]
}

Person.prototype.sayName = function () {
  console.log(this.name)
}

function Man(name, age) {
  Person.call(this, name) // 第二次调用Person()
  this.age = age
}

Man.prototype = new Person // 第一次调用Person()
Man.prototype.constructor = Man
Man.prototype.sayAge = function () {
  console.log(this.age)
}

var m1 = new Man("Geeook", 23)
m1.friends.push("Kai")
console.log(m1.friends)
m1.sayName()
m1.sayAge()

var m2 = new Man("Young", 24)
console.log(m2.friends)
m2.sayName()
m2.sayAge()
```
组合继承是JavaScript中最常用的继承模式，而且可以用 **instanceof** 和 **isPrototypeOf()** 判断对象类型。

**缺点：** 调用两次父类构造函数。如上代码注释所示：一次是在创建子类原型的时候，另一次是在子类构造函数内部。所以本来子类型的实例通过原型链会包含父类型对象的全部实例属性，但我们不得不在调用子类型的构造函数时重写这些属性。
### 原型式继承
道格拉斯引入了原型式继承，这种方法没有严格意义上的构造函数，主要思想就是借助原型可以基于已有的对象创建新的对象，同时不需要创建自定义类型。
```javascript
// 道格拉斯给出如下函数，从本质上来看就是对传入对象执行了一次浅复制
function object(o) {
  function F() { }
  F.prototype = o
  return new F
}

var person = {
  name: "Geeook",
  friends: ["Kelly", "RengJruin", "Coder"]
}

var anotherPerson = object(person)
anotherPerson.name = "Kelly"
anotherPerson.friends.push("Kai")

var yetAnotherPerson = object(person)
yetAnotherPerson.name = "Young"
yetAnotherPerson.friends.push("Hang")

console.log(person.friends) // ["Kelly", "RengJruin", "Coder", "Kai", "Hang"]
```
ECMAScript5新增<a href="#2">Object.create()</a>方法规范化了原型式继承。

**优势：** 在不愿意创建构造函数，只是想让一个对象和另一个对象保持类似的情况下使用原型式继承非常方便。

**缺点：** 原型模式普遍存在的问题——引用类型的属性被共享。
### 寄生式继承
道格拉斯推广了寄生式继承，思路就是创建一个仅用于封装继承过程的函数，函数内部增强对象并返回。
```javascript
function object(o) {
  function F() { }
  F.prototype = o
  return new F
}

function createAnother(original) {
  var clone = object(original) // 创建
  clone.sayName = function () { // 增强
    console.log(this.name)
  }
  return clone
}

var person = {
  name: "Geeook",
  friends: ["Kelly", "RengJruin", "Coder"]
}

var another = createAnother(person)
another.sayName()
```
**优势：** 在主要考虑对象，而不想自定义类型和构造函数的情况下，使用寄生式继承很方便。

**缺点：** 与构造函数模式类似的问题——函数不能被复用。
### 寄生组合式继承
为了解决前述组合继承存在的调用两次父类构造函数的问题，引入了寄生组合式继承。我们不必为了指定子类的原型而调用父类的构造函数，我们所需要的无非就是父类原型的副本，或者说无非就是想让子类的原型指向父类的原型。所以我们就可以使用寄生式继承来继承父类的原型，然后将结果指定给子类的原型。
```javascript
function inheritPrototype(subType, superType) {
  var prototype = object(superType.prototype) // 前面已经定义过了，不再重复
  prototype.constuctor = subType
  subType.prototype = prototype
}

function Person(name) {
  this.name = name
  this.friends = ["Kelly", "RengJruin", "Coder"]
}

Person.prototype.sayName = function () {
  console.log(this.name)
}

function Man(name, age) {
  Person.call(this, name)
  this.age = age
}

// 只需要替换这一句就行
// Man.prototype = new Person
inheritPrototype(Man, Person)

Man.prototype.sayAge = function () {
  console.log(this.age)
}

var m1 = new Man("Geeook", 23)
m1.friends.push("Kai")
console.log(m1.friends)
m1.sayName()
m1.sayAge()

var m2 = new Man("Young", 24)
console.log(m2.friends)
m2.sayName()
m2.sayAge()
```
**优势：** 
1. 这种模式的高效体现在只调用了一次父类的构造函数，避免了在子类的原型上创建不必要的多余属性。
2. 保持原型链不变，可以使用**instanceof**和**isPrototypeOf()**。

开发人员普遍认为这是引用类型最理想的继承范式。

----------
Geeook created at 2017/8/10 14:02:11 
## \__proto\__和prototype的区别
![](/image/原型链图解1.png)
![](/image/原型链图解.png)
![](/image/原型链图解2.png)

**详解：**
1. 所有的对象都有一个内置属性\__proto\__（隐式原型）或者说是 [[prototype]]，在ES5之前没有标准的方法访问这个内置属性，但是大多数浏览器都支持通过\__proto\__来访问。ES5中有了对于这个内置属性标准的Get方法**Object.getPrototypeOf()**。
2. 所有的函数都有prototype属性，并且只有函数有。不过通过**Function.prototype.bind**方法构造出来的函数是个例外，它没有prototype属性。
3. 在声明函数的时候，会自动创建一个对象(原型)，将引用赋给了函数的prototype属性，并且原型的constructor属性指向该函数，如果修改了函数的prototype属性，那么原型的constructor属性也会跟着改变，于是constructor属性和原来的构造函数也就切断了联系。
4. 用该函数创建实例时，所有实例的\__proto\__属性都指向刚创建的原型，constructor属性（通过原型对象）都指向构造函数。
5. 原型链是基于\__proto\__属性链接起来的，所有对象都继承于Object，所以原型链的最顶端是**Object.prototype**。
6. instanceof操作符的内部实现机制和隐式原型、显式原型有直接的关系。instanceof的左值一般是一个对象，右值一般是一个构造函数，用来判断左值是否是右值的实例，其原理就是沿着\__proto\__一直查找到原型链的顶端。

**一个有趣的例子：**
```javascript
Function instanceof Object // true 
Object instanceof Function // true 
Function instanceof Function //true
Object instanceof Object // true
```

----------
Geeook created at 2017/8/12 12:30:49 
## null vs undefined
大多数计算机语言，有且仅有一个表示"无"的值。有点奇怪的是，JavaScript语言居然有两个表示"无"的值：undefined和null。
### 相似性：
1. 变量赋值时几乎无区别
```javascript
var a = undefined;
var a = null;
```
2. 条件判断时都自动转为false
```javascript
if (!undefined) 
    console.log('undefined is false');
// undefined is false

if (!null) 
    console.log('null is false');
// null is false

undefined == null
// true
```
### 历史原因：
在JavaScript刚诞生时只设置了null。
```javascript
Number(null) // 0
5 + null // 5
```
但设计者觉得这样设计有两个问题：
1. null像在Java里一样被当成是一个对象，但JavaScript中的数据类型分为原始数据类型和Object对象，设计者觉得表示"无"的值最好不是对象。
2. JavaScript的最初版本没有包括错误处理机制，发生数据类型不匹配时，往往是自动转换类型或者默默地失败。如果null自动转为0，很不容易发现错误。

所以又设计了一个undefined。

### 区别和用法：
```javascript
Number(undefined) // NaN
5 + undefined // NaN
```
**null表示"没有对象"，即该处不应该有值。**
1. 作为函数的参数，表示该函数的参数不是对象。
2. null可以理解为占位符，在你需要表示这是一个对象而不是其他类型的时候使用。

**undefined表示"缺少值"，就是此处应该有一个值，但是还没有定义。**
1. 变量被声明了，但没有赋值时，就等于undefined。
2. 调用函数时，应该提供的参数没有提供，该参数等于undefined。
3. 对象没有赋值的属性，该属性的值为undefined。
4. 函数没有返回值时，默认返回undefined。

> 转载自：[阮一峰的网络日志：undefined与null的区别](http://www.ruanyifeng.com/blog/2014/03/undefined-vs-null.html)

----------
Geeook 于 2017/8/9 22:29:31 
## JavaScript的严格模式

## 🤜 异常处理
### 👉 `try...catch`语句
`try...catch`是JavaScript中处理异常的一种标准方式。
```javascript
try {
  ...
} catch (error) { // error 是必需的，即使你不想使用
  alert(error.message) // 对象中包含的属性因浏览器而异，但是都有message和name属性(保存错误类型)
} finally {
  ... // finally 子句是可选的，但是一经使用，其中的代码必须执行。
  ... // 甚至return语句都不会阻止，此时try和catch中的return将被忽略。
}
```
#### 错误类型
- Error：基类型
- EvalError：没有把`eval()`当成函数调用
- RangeError：数值超出相应范围
- ReferenceError：找不到对象
- SyntaxError：`eval()`中传入语法错误的执行语句
- TypeError：在变量中保存着意外的类型时，或者访问不存在的方法时，归根结底是在执行特定于类型的操作时，变量类型不符合要求
- URIError：在使用`encodeURI()`和`decodeURI()`时，URI格式不正确
#### 合理使用`try...catch`
1. `try...catch`可以实现自定义的错误类型。
2. `try...catch`最适合处理我们无法控制的错误。比如使用一个大型的JavaScript库时程序可能会抛出错误，而我们又不能轻易修改源码，可以使用`try...catch`。
3. 在明白自己的代码会发生错误时，要思考如何规避和处理错误和不是使用`try...catch`捕获错误。
#### `throw` vs `try...catch`
一句话总结：只捕获那些确切知道如何处理的错误，不能处理就抛出，抛出错误时要提供错误发生的具体原因。
### 👉 错误（error）事件
```javascript
// 只能使用DOM0级
window.onerror = function (message, url, line) {
  ...
}
```
任何没有通过`try...catch`处理的错误都会触发window的error事件，甚至浏览器插件的js异常。
### 👉 异步编程中的异常处理
因为异步函数的回调是在事件队列里单独拉出来执行的。所以在异步函数外面包裹`try...catch`是无法捕捉到回调函数里抛出的异常的。因为当回调函数从队列里被拉出来执行的时候`try...catch`所在的代码块已经执行完毕了。在浏览器里可以通过`window.onerror`，在node里通过`process.uncaughtException`可以捕获此类异常。
```javascript
process.on('uncaughtException', function(err) {
    console.error('Error caught in uncaughtException event:', err)
})
```
除此之外，还有一些方法。
#### callback
通过回调函数可以比较方便地进行异常处理，例如：
```javascript
function async(callback, errback) {
  setTimeout(function () {
    var rand = Math.random()
    if (rand < 0.5) {
      errback('async error')
    } else {
      callback(rand)
    }
  }, 1000)
}

async(function (result) {
  console.log('scucess:', result)
}, function (err) {
  console.log('fail:', err)
})
```
有时候为了方便，也会将callback和errback合并为一个回调函数，这也是Node风格回调处理。
```javascript
function async(callback) {
  setTimeout(function () {
    var rand = Math.random()
    if (rand < 0.5) {
      callback('async error')
    } else {
      callback(null, rand)
    }
  }, 1000)
}

async(function (err, result) {
  if (err) {
    console.log('fail:', err)
  } else {
    console.log('success:', result)
  }
})
```
不过在多异步串行的情况下，使用回调函数的方式，会出现callback hell，代码可读性变差。这就需要用到第二种方法。
#### promise
```javascript
function async() {
  return new Promise(function (resolve, reject) {
    setTimeout(function () {
      var rand = Math.random()
      if (rand < 0.5) {
        reject('async error')
      } else {
        resolve(rand)
      }
    }, 1000)
  })
}

async().then(function (result) {
  console.log('success:', result)
}, function (err) {
  console.log('fail:', err)
})
```
或者使用catch的方式：
```javascript
function async() {
  return new Promise(function (resolve, reject) {
    setTimeout(function () {
      var rand = Math.random()
      if (rand < 0.5) {
        reject('async error')
      } else {
        resolve(rand)
      }
    }, 1000)
  })
}

async().then(function (result) {
    console.log('success:', result)
  })
  .catch(function (err) {
    console.log('fail:', err)
  })
```
对于多异步操作串行的问题，使用promise的方式会使得代码简洁优雅，可读性也很强。代码如下：
```javascript
function async() {
  return new Promise(function (resolve, reject) {
    setTimeout(function () {
      var rand = Math.random()
      if (rand < 0.7) {
        reject('async error')
      } else {
        resolve(rand)
      }
    }, 1000)
  })
}

function onResolved(result) {
  console.log('success:', result)
}

function onRejected(err) {
  console.log('fail:', err)
}

async().then(onResolved)
  .then(async)
  .then(onResolved)
  .then(async)
  .then(onResolved)
  .catch(onRejected) // 前面任一次回调发生异常都可以捕获到。
```
> 大部分转载自：[异步编程中的异常处理](http://syaning.com/2015/08/10/asynchronous-error-handling/)

----------
Geeook @ 2017/9/1 1:43:02 
## setTimeout vs setInterval
1. setTimeout延时函数；setInterval定时函数。
2. 取消setTimeout用`clearTimeout`，取消setInterval用`clearInterval`。
3. 由于setInterval定时函数可能会让回调函数轮空或者无间隔，所以可以用嵌套的setTimeout模拟setInterval，增加灵活性，并且可以保证最小间隔时间。
```javascript
function setMyInterval(func, wait, ...args) {
  let inter = function () {
    func.apply(null, args)
    if (!inter.stop) {
      setTimeout(inter, wait, ...args)
    }
  }
  setTimeout(inter, wait)
  return inter
}

function clearMyInterval(foo) {
  foo.stop = true
}
```
4. 延时为零的setTimeout函数可以用来安排一个回调函数在当前代码执行完之后立即执行。一些应用场景：
    - 分割CPU计算量大的任务，防止页面假死。
    - 让浏览器可以在间歇之中完成一些其他的操作，比如绘制进度条。
5. setTimeout中的回调函数在被调用之前一直存在于内存中；setInterval中的回调函数常驻内存除非手动`clearInterval`。这样很容易造成内存泄漏。因为如果回调函数引用了外部的变量（数据量较大），那么这个变量不会被GC回收，占用的内存远远超过了回调函数自身。

----------
Geeook @ 2017/8/25 21:59:18 
## 内存溢出
### 简介
内存溢出指的是：应用不需要的内存没有及时被回收。JavaScript有垃圾回收机制，通过周期性地检查之前分配的内存是否还能被应用访问来确定是否回收。
### 内存溢出的情况
1. 意外的全局变量
```javascript
// 函数内未用var声明的变量
function foo(arg) {
    bar = "this is an explicit global variable";
}
// 函数内用this创建的变量
function foo() {
    this.variable = "potential accidental global";
}
foo();
```
2. 被遗忘的定时函数和回调函数
```javascript
var someResource = getData();
// 如果Node节点被移除，定时函数就是无效的，但是someResource（如果是大量数据）不会被回收。
setInterval(function() {
    var node = document.getElementById('Node');
    if(node) {
        // Do stuff with node and someResource.
        node.innerHTML = JSON.stringify(someResource));
    }
}, 1000);
```
```javascript
// 元素的监听事件在元素被移除之后，浏览器会自动回收事件的引用。但最好是手动移除监听事件。
var element = document.getElementById('button');
function onClick(event) {
    element.innerHtml = 'text';
}
element.addEventListener('click', onClick);
element.removeEventListener('click', onClick);
element.parentNode.removeChild(element);
// Now when element goes out of scope,
// both element and onClick will be collected even in old browsers that don't handle cycles well.
```
3. 多余的DOM节点引用
```javascript
// 在JavaScript中手动创建的节点引用不会在节点被移除时被回收。
// 在JavaScript中引用的某个节点的父节点被移除了，但父节点依旧在内存中。
var elements = {
    button: document.getElementById('button'),
    image: document.getElementById('image'),
    text: document.getElementById('text')
};

function doStuff() {
    elements.image.src = 'http://some.url/image';
    elements.button.click();
    console.log(elements.text.innerHTML);
}

function removeButton() {
    // The button is a direct child of body.
    document.body.removeChild(document.getElementById('button'));
    // At this point, we still have a reference to #button in the global
    // elements dictionary. In other words, the button element is still in
    // memory and cannot be collected by the GC.
}
```
4. 闭包
```javascript
// 闭包引用的包裹函数中的变量常驻在内存中，使用不当容易造成内存溢出。
// unused函数没有被使用过，但是由于它引用的变量originalThing导致unused函数不会被回收。
var theThing = null;
var replaceThing = function () {
  var originalThing = theThing;
  var unused = function () {
    if (originalThing)
      console.log("hi");
  };
  theThing = {
    longStr: new Array(1000000).join('*'),
    someMethod: function () {
      console.log(someMessage);
    }
  };
};
setInterval(replaceThing, 1000);
```

----------
Geeook @ 2017/8/25 19:05:13 
## 如何实现Ajax请求
原生的JavaScript代码完成Ajax请求：
```javascript
var xhr = new XMLHttpRequest() // 创建xhr实例
xhr.onload = function (e) {
  if ((xhr.status >= 200 && xhr.status < 300) || xhr.status == 304) {} else {}
}

xhr.onprogress = function (e) {
  if (e.lengthComputable) {
    var status = e.position + " of " + e.totalSize;
  }
}

xhr.onerror = function () {} // 请求错误监听事件
xhr.open("get", url, false) // 请求方法、请求地址、是否异步
xhr.timeout = 1000 // 超时时间   
xhr.ontimeout = function () {} // 超时事件监听
xhr.setRequestHeader(key, val) // 设置自定义头部
xhr.send(data) // 发送数据：POST请求时发送；GET请求不传参
xhr = null // 用完之后释放引用，不建议重用

// 发送同步请求时监听响应的代码，放在send()之后
if ((xhr.status >= 200 && xhr.status < 300) || xhr.status == 304) {} else {}

// 发送异步请求时监听响应的代码，放在open()之前
xhr.onreadystatechange = function () {
  if (xhr.readyState == 4) {
    if ((xhr.status >= 200 && xhr.status < 300) || xhr.status == 304) {} else {}
  }
}
```
原生的xhr有6个事件：
- loadstart：接收到响应的第一个字节时触发。
- progress：接收响应期间持续触发。
- error：请求错误触发。
- abort：调用abort()方法终止连接时触发。
- load：接收到完整响应数据时触发。
- loadend：通信完成、触发error、abort或load事件后触发。

----------
Geeook @ 2017/8/27 12:57:45 
## JavaScript的浅复制和深复制
### 浅复制
浅复制（***shallow copy***）通俗来讲就是值复制，把原始对象中所有属性的值都复制了一份，如果是基本数据类型，如果属性是对象的引用，那么仅仅是引用地址被复制，也就是说源对象和拷贝对象的该属性都指向同一个对象。
#### 方法一
`Object.assign(target, ...sources)`

注意：
1. 目标对象属性会被源对象同名属性覆盖，源对象从右往左，属性也会覆盖。
2. 只复制可枚举的自身属性，会触发源对象的getter方法。
3. String和Symbol类型的属性会被复制，属性值为null和undefined的不会被复制。
4. 如果目标对象某属性是不可写的，源对象中具有同名属性，复制过程抛出TypeError异常，异常前的属性被复制。

#### 方法二
```javascript
var newObj = Object.create(
  Object.getPrototypeOf(obj), 
  Object.getOwnPropertyDescriptors(obj)
)
```
可以复制getter方法而不是触发。
#### 方法三
```javascript
Object.defineProperties(
  target,
  Object.getOwnPropertyDescriptors(source)
)
```
结果同方法二
#### 方法四
```javascript
var newObj = jQuery.extend({}, oldObj)
```
### 深复制
深复制（***deep copy***）是在浅复制的基础上，对于属性是对象引用的，复制时不仅仅是复制引用，而是创建一个等价的对象并引用。
#### 方法一
```javascript
// JSON trick
var newObj = JSON.parse(JSON.stringify(obj))
```
不能包含function，适用于属性是简单object、array、string、boolean和number类型。
#### 方法二
```javascript
var newObj = jQuery.extend(true, {}, oldObj)
```
#### 方法三
```javascript
// 递归遍历属性并判断
function cloning(obj) {
  let copy
  if (obj === null || typeof obj !== "object") {
    return obj
  }
  if (obj instanceof Date) {
    copy = new Date()
    copy.setTime(obj.getTime())
    return copy
  }
  if (obj instanceof Array) {
    copy = []
    for (let i = 0, len = obj.length; i < len; i++) {
      copy[i] = cloning(obj[i])
    }
    return copy
  }
  if (obj instanceof RegExp) {
    return new RegExp(obj)
  }
  // there is no need to copy function
  // if (obj instanceof Function) {
  //   return obj.bind(null)
  //   eval('copy = ' + obj.toString());
  //   return copy
  // }
  if (obj instanceof Object) {
    copy = {}
    for (let key in obj) {
      copy[key] = cloning(obj[key])
    }
    return copy
  }
}
```

----------
Geeook @ 2017/8/27 14:49:08 
## 经典JS笔试题#1
```javascript
function Foo() {
  getName = function () {
    alert(1)
  }
  return this
}

Foo.getName = function () {
  alert(2)
}
Foo.prototype.getName = function () {
  alert(3)
}

var getName = function () {
  alert(4)
}

function getName() {
  alert(5)
}

Foo.getName() // 2
getName() // 4
Foo().getName() // 1
getName() // 1
new Foo.getName() // 2
new Foo().getName() // 3
new new Foo().getName() // 3
```
此题设计知识点：变量定义提升，函数声明提升，this，作用域链，运算符优先级，原型和继承，全局变量污染，对象属性和原型属性。
### 第二问
考察变量定义提升和函数声明提升。
```javascript
function Foo() {
  getName = function () {
    alert(1)
  }
  return this
}
var getName // 只提升变量声明
// 提升函数声明，覆盖getName的声明
function getName() {
  alert(5)
}
Foo.getName = function () {
  alert(2)
}
Foo.prototype.getName = function () {
  alert(3)
}
// 再次覆盖getName声明
getName = function () {
  alert(4)
}
getName() // 所以最终输出4
```
### 第三问
考察this指向，作用域链，全局变量污染。

Foo()执行之后，覆盖了window的全局变量getName；函数返回的this指向window。
### 第五问
考察运算符优先级。

![](/image/priority.png)

由图可知：成员访问`.`的优先级高于`new(无参数列表)`。所以：`new Foo.getName()` => `new ((Foo.getName)())`，实际上将`Foo`的`getName`函数作为构造函数执行。
### 第六问
考察构造函数的返回值、运算符优先级。

由于`new(带参数列表)`的优先级和成员访问`.`相同，所以从左至右执行。`new Foo().getName()` => `((new Foo()).getName)()`，实际上调用的是`Foo.prototype`上的`getName`函数。
### 第七问
还是考察运算符的优先级。

`new new Foo().getName()` => `new (new Foo()).getName()` => `new ((new Foo()).getName)()` => `new (((new Foo()).getName)())`

实际上是用`new`运算符调用`Foo.prototype`的`getName`函数。
### 补充：
构造函数的返回值问题：
- 无返回值，返回实例化对象。
- 返回值是非引用类型，也返回实例化对象。
- 返回值是引用类型，返回该值。

----------
Geeook @ 2017/8/27 23:12:11 
## 函数
### 函数表达式VS函数声明
ECMA解释说函数表达式和函数声明的区别主要在于函数声明必须有一个Identifier（或者说是函数名字）而函数表示式可以没有。

函数声明：`function Identifier(FormalParameterList opt) { FunctionBody }`

函数表达式：`function Identifier opt(FormalParameterList opt) { FunctionBody }`

没有名字时，一定是匿名函数表达式；如果有名字，就需要通过所处上下文来判断。如果是传参、赋值或者new运算符，就应该是函数表达式；如果是孤零零地在函数体内或者全局域中，就应该是函数声明。**e.g.**：
```javascript
function foo() {} // declaration, since it's part of a Program
var bar = function foo() {}; // 表达式, 因为是赋值
new function bar() {}; // expression, since it's part of a NewExpression
(function () {
  function bar() {} // declaration, since it's part of a FunctionBody
})(); // 括号包含的是匿名函数表达式
```
**区别：**
1. 函数声明提前。
2. 通过条件语句控制函数声明的行为并未标准化，因此不同环境下可能会得到不同的结果，所以永远都不要依赖条件控制来声明函数，而应该使用函数表达式。**e.g.**
```javascript
// Never do this!
// Some browsers will declare `foo` as the one returning 'first',
// while others — returning 'second'
if (true) {
  function foo() {
    return 'first'
  }
} else {
  function foo() {
    return 'second'
  }
}
// Instead, use function expressions:
var foo
if (true) {
  foo = function () {
    return 'first'
  }
} else {
  foo = function () {
    return 'second'
  }
}
foo()
```
### 函数特性、模式和高级用法
#### 函数特性
1. 函数是一等对象（***first-class***）。
    - 可以在程序执行时动态创建函数。
    - 可以将函数赋值给变量，可以将函数的引用拷贝给另一个变量，可以扩充和删除。
    - 可以将函数作为参数传递，可以作为返回值返回。
    - 可以添加属性和方法。
2. 函数提供作用域支持，在JavaScript中没有块级作用域，只有函数作用域。
> 我们首先当它是一个对象，具有可执行的特性。

#### 常见模式
**回调模式：**

1. 最简单的回调：函数接受一个函数作为参数并在函数中调用传入的函数。此时，传入的函数就叫做回调函数。
2. 回调和作用域：如果回调函数是匿名函数或者全局函数，在函数中就可以直接调用。如果回调函数是对象的方法并使用了对象的属性，此时就需要注意作用域的问题。除了传入回调函数，还需要传入回调函数所属的对象，并在函数中利用call()和apply()指定回调函数的作用域。
3. 异步事件监听和延时：JavaScript中的事件监听和延时函数都用到了回调函数。
4. 类库中的回调：在类库的设计时经常使用回调模式。设计时着重核心功能的实现，尽可能保持可复用和通用，但同时提供回调的入口作为“钩子（***hook***）”，定制需要的特性使类库变得可扩展和可定制。

**函数的懒惰定义：**

函数可以在运行中动态定义，用新函数覆盖掉旧函数。

当函数中包含一些初始化操作并只需要执行一次时，或者函数里面的控制流每次都是一样时，这种模式非常合适，可以避免执行重复的代码，提高应用的执行效率。这种模式也被称为**函数的懒惰定义**。

**缺陷**：原函数的功能丢失；如果这个函数被重定义为不同的名字，被赋值给不同的变量，或者是作为对象的方法使用，那么重定义的部分并不会生效，原来的函数依然会被执行。

**记忆模式：**

将函数执行结果保存为函数的自定义属性，避免函数下次调用时重复复杂的计算。**e.g.**
```javascript
var myFunc = function foo() {
  var cachekey = JSON.stringify(Array.prototype.slice.call(arguments)),
    result;
  if (!foo.cache[cachekey]) {
    result = {}
    // 复杂计算
    foo.cache[cachekey] = result
  }
  return foo.cache[cachekey]
}

// 缓存
myFunc.cache = {}
```

**函数柯里化(Currying）：**

让函数理解并处理部分应用的过程叫做柯里化。柯里化是一个变换函数的过程。可以将函数需要的参数分多次传入。

通用的柯里化函数：
```javascript
function curry(func) {
  let slice = Array.prototype.slice
  let oldArgs = slice.call(arguments, 1)
  return function () {
    return func.apply(null, oldArgs.concat(slice.call(arguments)))
  }
}
// 普通函数
function add(a, b, c, d, e) {
  return a + b + c + d + e
}
// 参数个数可以随意分割
curry(add, 1, 2, 3)(5, 5) // 16
// 两步柯里化
var addOne = curry(add, 1)
addOne(10, 10, 10, 10) // 41
var addSix = curry(addOne, 2, 3)
addSix(5, 5) // 16
```
**使用场景：**

当你发现自己在调用同样的函数并且传入的参数大部分都相同的时候，就是考虑柯里化的理想场景了。你可以通过传入一部分的参数动态地创建一个新的函数。这个新函数会存储那些重复的参数（所以你不需要再每次都传入），然后再在调用原始函数的时候将整个参数列表补全。
### NFE
具有Identifier（或者说函数名字）的函数表达式被称作具名函数表达式（***Named Function Expression***）。

`var bar = function foo() {}` 只能在函数内部访问具名函数表达式的名字foo。

具名函数表达式的作用主要是追踪栈中有函数名，利于调试。其次可以在递归时使用（代替`arguments.callee`）。
### IIFE
立即执行函数表达式（***Immediately Invoked Function Expression***）的形式如下：
```javascript
(function(){
    //...
})()
```
立即执行函数表达式是指程序运行到此时函数立即执行。用法：
1. 传递参数为window，可以更快地访问全局作用域里面的变量，不需要沿着作用域链进行查找。
2. 传递参数为函数。
3. 利用函数作用域创建块级作用域，防止全局变量污染。
4. 模块化编程、测试和部署。
### Closure
闭包（closure）是Javascript语言的一个难点，也是它的特色。
#### 闭包的特性
- 函数嵌套
- 函数内部可以引用外部的参数和变量
- 参数和引用变量不会被垃圾回收机制回收
#### 闭包的定义和优缺点
定义1：有权访问另一个函数作用域中的变量的函数。

定义2：当一个内部函数被其外部函数之外的变量引用时，就形成了一个闭包。

创建闭包的最常见的方式就是在函数内创建函数。
#### 闭包的用法
1. 通常和 IIFE 一起使用，模块化代码，避免全局变量的污染。
```javascript
let foo = (function () {
  let a = 1
  return function () {
    a++
    console.log(a)
  }
})()
foo() // 2
foo() // 3
```
2. 创建私有成员
```javascript
let foo = (function () {
  let a = 1

  function b() {
    a++
    console.log(a)
  }

  function c() {
    a++
    console.log(a)
  }
  return {
    b: b,
    c: c
  }
})()
// 此时a是私有成员，只能通过函数方法 b() 和 c() 访问
foo.b() // 2
foo.c() // 3
```

----------
Geeook @ 2017/8/28 16:45:15
## 对象属性遍历
| 方法 | 所有属性 | 可枚举属性 | 包括原型属性 | 自身属性 |
|------|:----------:|:-----------:|:--------------:|:----------:|
| `Object.keys(obj)`|  | ✔️ |  | ✔️ |
| `for...in` |  | ✔️ | ✔️ |  |
| `Object.getOwnPropertyNames()` | ✔️ |  |  | ✔️ |

三种方式遍历的顺序是一致的。

----------
Geeook @ 2017/8/29 13:43:53 
## 自己手写的常用小函数
```javascript
function isEmpty(obj) {
  return (Object.prototype.toString.call(obj) == "[object Object]") && (Object.getOwnPropertyNames(obj).length == 0)
}
```
```javascript
function getUrlParam(sUrl, sKey) {
  var result = {}
  sUrl.replace(/\??(\w+)=(\w+)&?/g, function (a, k, v) {
    if (result[k] !== undefined) {
      var t = result[k]
      result[k] = [].concat(t, v)
    } else {
      result[k] = v
    }
  })
  if (sKey === undefined) return result
  else return result[sKey] || ''
}
```
```javascript
function formatDate(date, format) {
  var obj = {
    yyyy: date.getFullYear(),
    yy: ("" + date.getFullYear()).slice(-2),
    M: date.getMonth() + 1,
    MM: ("0" + (date.getMonth() + 1)).slice(-2),
    d: date.getDate(),
    dd: ("0" + date.getDate()).slice(-2),
    H: date.getHours(),
    HH: ("0" + date.getHours()).slice(-2),
    h: date.getHours() % 12,
    hh: ("0" + date.getHours() % 12).slice(-2),
    m: date.getMinutes(),
    mm: ("0" + date.getMinutes()).slice(-2),
    s: date.getSeconds(),
    ss: ("0" + date.getSeconds()).slice(-2),
    w: ['日', '一', '二', '三', '四', '五', '六'][date.getDay()]
  }
  return format.replace(/[a-z]+/ig, function (str) {
    return obj[str]
  })
}
```
```javascript
// 五种方法实现循环添加延时事件（回调函数引用遍历索引）
for (var i = 1; i <= 5; i++) {
  (function (i) {
    setTimeout(function timer() {
      console.log(i);
    }, i * 1000);
  })(i)
}

for (var i = 1; i <= 5; i++) {
  setTimeout((function (i) {
    return function () {
      console.log(i);
    }
  })(i), i * 1000);
}

for (var i = 1; i <= 5; i++) { 
  setTimeout(function timer(i) {
    console.log(i);
  }, i * 1000, i);
}

for (var i = 1; i <= 5; i++) { 
  setTimeout(function timer(i) {
    console.log(i);
  }.bind(null, i), i * 1000);
}

for (let i = 1; i <= 5; i++) { 
  setTimeout(function timer() {
    console.log(i);
  }, i * 1000);
}
```
```javascript
function isAvailableEmail(sEmail) {
    return /^\w+(\.\w+)*@\w+(\.\w+)+$/g.test(sEmail)
}
```
```javascript
function rgb2hex(sRGB) {
  var arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f"]
  var rgb = /^rgb\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})\)$/gi
  var res = rgb.exec(sRGB)
  if (!res) return sRGB
  if (res.slice(1).some(function (item) {
      return item > 255 || item < 0
    })) return sRGB
  return res.slice(1).reduce(function (hex, item) {
    var fir = Math.floor(item / 16)
    var sec = item - fir * 16
    return hex + arr[fir] + arr[sec]
  }, "#")
}
```
```javascript
function cssStyle2DomStyle(sName) {
  var arr = sName.match(/\w+/g)
  return arr.slice(1).reduce(function (res, item) {
    return res + item.substring(0, 1).toUpperCase() + item.substring(1)
  }, arr[0])
}
// better solution
function cssStyle2DomStyle(sName) {
  return sName.replace(/\-[a-z]/g, function (a, b) {    
    return b == 0 ? a.replace('-', '') : a.replace('-', '').toUpperCase(); 
  });
}
```
```javascript
function count(str) {
  var res = {}
  str.split("").forEach(function (item) {
    if (item !== " ") (!res[item]) ? res[item] = 1 : res[item]++
  })
  return res
}
// better solution
function count(str) {
  var obj = {}
  str.replace(/\S/g, function (s) { !obj[s] ? obj[s] = 1 : obj[s]++ })
  return obj
}
```

----------
Geeook @ 2017/9/1 1:48:47 