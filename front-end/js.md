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

## try catch无法捕捉异步操作的错误，如何处理？

## 提取url的查询字符串并输出对象形式
```javascript
function findQuery(url) {
  if (typeof url !== "string") return
  if (url.indexOf("?")) return {}
  let queryObj = {};
  url.substring(url.indexOf("?") + 1).split("&").forEach(function (item) {
    let key = item.split("=")[0]
    let val = item.split("=")[1]
    queryObj[key] = val
  });
  return queryObj
}
```

----------
Geeook @ 2017/8/25 21:48:48 
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