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
1. 新创建对象的实例方法不引用this
2. 不使用new操作符调用构造函数
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
1. 现在m.constructor指向Person，是因为Man的原型指向Person的原型，然后这个原型对象的constructor属性指向Person。
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
组合继承是JavaScript中最常用的继承模式，而且可以用**instanceof**和**isPrototypeOf()**判断对象类型。

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
2. 保持原型链不变，可以使用**instanceof**和**isPrototypeOf()**

开发人员普遍认为这是引用类型最理想的继承范式。

----------
Geeook created at 2017/8/10 14:02:11 
## \__proto\__和prototype的区别
## Session、Cookie、 LocalStorage、 SessionStorage对比
### 基本概念
由于HTTP协议是无状态的，所以服务器无法知道两次请求是否来自同一个用户、同一个浏览器，于是就有了session和cookie来记住状态信息。
#### 1. Session
Session是一种记录用户状态的机制，不同的是Cookie保存在客户端浏览器中，而Session保存在服务器上。客户端浏览器访问服务器的时候，服务器把客户端信息以某种形式记录在服务器上（内存、文件等）。这就是Session。客户端浏览器再次访问时只需要从该Session中查找该客户的状态就可以了。

用户首次访问服务器，服务器会为每个用户单独创建一个session对象(HttpSession)，并为每个session分配唯一个id(sessionId)，sessionId通过cookie保存到客户端。当用户再次访问服务器时，需将对应的sessionId携带给服务器，服务器通过这个唯一sessionId就可以找到用户对应的session对象，从而达到管理用户状态。
#### 2. Cookie
Cookie实际上是一小段的文本信息。客户端请求服务器，如果服务器需要记录该用户状态，就使用response向客户端浏览器颁发一个Cookie。客户端浏览器会把Cookie保存起来。当浏览器再次发出请求时将携带该Cookie，服务器检查该Cookie，以此来辨认用户状态。服务器还可以根据需要修改Cookie的内容。对了，Cookie也不可以跨域。

**主要目的：**
1. 会话管理：记录用户登录信息、购物车、游戏分数以及其他服务器应该记住的任何内容
2. 个性化： 用户的偏好设置
3. 跟踪：记录和分析用户的行为

**分类：**
1. 会话cookie：浏览器关闭时被删除，没有指定过期日期。
2. 持久cookie：浏览器关闭时不被删除，到了指定的过期日期（以客户端时间为准）失效。
3. 安全cookie：只通过基于HTTPS协议的加密请求发送到服务器。
4. HttpOnly cookie：无法通过JavaScript的Document.cookie API访问，只是发送给服务器，用于持久化一个服务器端的会话。可以防止跨站点脚本（XSS）攻击。

cookie曾经用于客户端存储，虽然是合法的，但仅仅是因为别无他法。现在客户端存储推荐使用现代的Web存储API（LocalStorage和SessionStorage）和IndexedDB。
#### 3. LocalStorage 和 SessionStorage
功能和API几乎完全相同，并且都遵循同源策略，唯一的区别就是生命周期。顾名思义，sessionStorage只能在会话期间可用，刷新页面数据不丢失，在标签页或者窗口关闭之后被删除；localStorage是永久的并且特定于网站，只能通过用户明确地删除。
### 对比
|   | Cookie | LocalStorage | SessionStorage |
|:--|:--------|:---------------|:------------------|
| 生命周期 | 一般由服务器生成，可设置失效时间。如果在浏览器端生成Cookie，默认是关闭浏览器后失效 | 除非被清除，否则永久保存 | 仅在当前会话下有效，关闭页面或浏览器后被清除 |
| 存放数据大小 | 4Kb左右 | 一般为5Mb，和浏览器有关 | 一般为5Mb，和浏览器有关 |
| 是否与服务器通信 | 每次HTTP请求都会将cookie携带在HTTP头部，保存过多的数据可能会带来性能问题 | 客户端存储，不与服务器通信 | 客户端存储，不与服务器通信 |
| 是否安全 | 不同的cookie安全性不同，可能存在cookie拦截和会话劫持，具体见网络安全部分 | 由于Storage存储的数据能够很容易被修改，所以不要用他们存储敏感数据 | 由于Storage存储的数据能够很容易被修改，所以不要用他们存储敏感数据 |
| 应用场景 | 记录用户登录信息和用户偏好设置等，跟踪用户行为 | HTML5游戏的本地数据，购物车数据等 | 将内容丰富的表单页面拆分成多个子页面，利用sessionStorage暂存数据 |

----------
Geeook 于 2017/8/9 10:51:08 
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