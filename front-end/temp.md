## 创建对象的方法
### 工厂模式
在函数中封装了创建对象，添加属性的细节，返回新创建的对象。
```
function createPerson(name, age) {
  var o = new Object()
  o.name = name
  o.age = age
  return o
}
```
**缺点：**不能用**instanceof**检测对象类型，没有解决对象识别的问题。
### 构造函数模式
```
function Person(name, age) {
  this.name = name
  this.age = age
  this.sayName = function() {
    alert(this.name)
  }
}

var p = new Person("geeook", 23)
```
### 原型模式
### 组合使用构造函数模式和原型模式
### 动态原型模式