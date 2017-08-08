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
**缺点：** 不能用instanceof检测对象类型，没有解决对象识别的问题。
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
**缺点：**解决了对象识别问题，但是每个方法都要在每个实例上重新创建一遍，浪费内存。

**修改：**
```
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
```
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
```
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
创建自定义对象的最常见的方式就是组合使用构造函数模式和原型模式。构造函数用于定义实例属性，原型模式用于定义方法和共享属性。
```
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
```
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

**注意：**在使用动态原型模式时，不能用对象字面量重写原型，因为在已经创建实例的情况下重写原型会切断现有实例和新原型之间的联系。
### 寄生构造函数模式
在前述几种模式都不适用的情况下可以使用寄生构造函数模式。基本思想就是创建一个函数，封装创建对象的代码，并返回新创建的对象；但从表面上看又像是典型的构造函数。
```
function Person(name, age) {
  var o = new Object()
  o.name = name
  o.age = age
  return o
}

var p = new Person("Geeook", 23)
```
除了使用new操作符之外，和工厂模式没有区别。构造函数在无返回值的情况下默认返回新对象实例，而如果返回另一个对象实例将重写构造函数的返回值。

**使用场景：**在特殊情况下为对象创建构造函数。比如：想创建具有额外方法的特殊数组。在不直接修改Array构造函数和原型的前提下可以使用这个模式。

**e.g.**
```
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
**缺点：**很明显，不能用instanceof检测对象类型。建议在可以使用其他模式的情况下不要使用这种模式。
### 稳妥构造函数模式
道格拉斯发明了JavaScript中的**稳妥对象**这个概念。指的是没有公共属性，方法不引用this的对象。稳妥对象适合在安全的环境中，或者防止数据被其他程序修改时使用。稳妥构造函数和寄生构造函数类似，有两点不同：
1. 新创建对象的实例方法不引用this
2. 不使用new操作符调用构造函数
``` 
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

**缺点：**同寄生构造函数模式一样，无法使用instanceof检测对象类型。

----------
Geeook 于 2017/8/8 17:02:22 
