## 创建新节点和查找节点的方法
### 创建新节点：
createAttribute(): creates a new attribute node, and returns it.

createCDATASection(): creates a new CDATA section node, and returns it.

createComment(): creates a new comment node, and returns it.

createDocumentFragment(): creates a new empty DocumentFragment.

createElement(): creates the HTML element specified by tagName, or an HTMLUnknownElement if tagName isn't recognized.

createElementNS(): creates an element with the specified namespace URI and qualified name.

createTextNode(): creates a new Text node.

~~createNode()~~
### 查找节点：
getElementById()

getElementsByClassName()

getElementsByName()

getElementsByTagName()

getElementsByTagNameNS(): returns a list of elements with the given tag name belonging to the given namespace.

----------

## DOM reflow
HTML使用的是flow based layout，也就是流式布局。所以如果某元素的几何尺寸发生了变化，需要重新布局，也就叫reflow。
元素发生reflow会重新计算尺寸和位置，并且会触发子元素和父元素的reflow事件。reflow事件成本非常高，但却很容易被触发。

### reflow 发生条件
当你：
- 增加、删除、修改DOM结点时
- 移动DOM的位置时
- 为元素增加动画时
- 改变页面内容时
- 修改样式，增加样式，移除样式时
- 滚动屏幕时
- 改变窗口大小时
- 计算元素的属性时
    - offsetTop, offsetLeft, offsetWidth, offsetHeight
    - scrollTop/Left/Width/Height
    - clientTop/Left/Width/Height
    - IE中的 getComputedStyle(), 或 currentStyle

都会触发reflow事件。

### 如何尽量减少reflow
1. 浏览器对于一些连续的样式改动会异步reflow或者说是增量reflow。
2. 尽管如此，我们也要避免一条一条地修改CSS样式，应该预先定义好一个样式，直接修改DOM的className。
3. DOM离线后修改：
    - 使用documentFragment
    - 先把DOM`display:none`，全部修改完了之后显示
    - clone一个待修改的DOM节点，修改完了之后与之交换
4. 不要在循环里获取元素的计算属性。
5. 为动画的HTML元件使用fixed或absoulte的position。
6. 尽量不使用table布局，因为可能很小的一个小改动会造成整个table的reflow。

----------

## HTML5
### 简介
#### 历史
- 2008 年，第一版 HTML5 草稿发布。
- 2014 年，HTML5 正式发布，W3C推荐使用。

HTML5 的 DOCTYPE 声明十分简单：`<!DOCTYPE html>`，charset 声明也十分简单：`<meta charset="UTF-8">`。
### HTML5 新特性
#### 与服务器的通信
**Web Sockets**

**Server-sent events**

**WebRTC**

#### 离线存储
**在线和离线事件**

**客户端会话和持久化存储**

**IndexedDB**

#### 性能优化
**Web Workers**

**XMLHttpRequest Level 2**

**History API**

**drag & drop**

**HTML 中的焦点管理**

**requestAnimationFrame**
#### 设备访问
**使用Camera API**

**使用地理位置定位**



#### HTML5 新增标签
1. 新增语义化/文档结构标签

| Tag | Description |
|-----|-------------|
| article | Defines an article in a document |
| aside |	Defines content aside from the page content |
| bdi | Isolates a part of text that might be formatted in a different direction from other text outside it |
| details |	Defines additional details that the user can view or hide |
| dialog | Defines a dialog box or window |
| figcaption | Defines a caption for a `<figure>` element |
| figure | Defines self-contained content |
| footer | Defines a footer for a document or section |
| header | Defines a header for a document or section |
| main | Defines the main content of a document |
| mark | Defines marked/highlighted text |
| menuitem | Defines a command/menu item that the user can invoke from a popup menu(only supported in FF now) |
| meter | Defines a scalar measurement within a known range (a gauge) |
| nav | Defines navigation links |
| progress | Represents the progress of a task |
| section | Defines a section in a document |
| summary | Defines a visible heading for a `<details>` element |
| time | Defines a date/time |
| wbr | Defines a possible line-break |


2. 新增表单标签

| Tag | Description |
|-----|-------------|
| datalist | Specifies a list of pre-defined options for input controls |
| keygen | Defines a key-pair generator field (for forms) |
| output | Defines the result of a calculation |


3. 新增图形标签

| Tag | Description |
|-----|-------------|
| canvas | Draw graphics, on the fly, via scripting (usually JavaScript) |
| svg | Draw scalable vector graphics |


4. 新增媒体标签

| Tag | Description |
|-----|-------------|
| audio | Defines sound content |
| embed | Defines a container for an external (non-HTML) application |
| source | Defines multiple media resources for media elements (`<video>` and `<audio>`) |
| track | Defines text tracks for media elements (`<video>` and `<audio>`) |
| video | Defines video or movie |

<br>

#### HTML5 新增输入类型和输入属性

**输入类型:**
- color
- date
- datetime
- datetime-local
- email
- month
- number
- range
- search
- tel
- time
- url
- week

**输入属性：**
- autocomplete
- autofocus
- form
- formaction
- formenctype
- formmethod
- formnovalidate
- formtarget
- height and width
- list
- min and max
- multiple
- pattern (regexp)
- placeholder
- required
- step

### 对 HTML5 标签语义化(Semantic)的理解
语义是指语言中单词和短语的含义，语义元素 = 具有意义的元素。语义元素清楚地描述了它对于机器和开发者的含义。在 HTML5 之前，开发人员利用`<div>` + `id` + `class` 创建元素，包括：头部、导航、侧边栏、内容、文章、菜单、容器等，从而构建页面，但这样的网页内容对搜索引擎很不友好，很难正确识别网页内容。HTML5 新增的许多标签（`<header>` `<footer>` `<nav>` `<section>` `<article>`）都明确定义了标签的内容，更加语义化。说到这儿，需要先弄明白除了对搜索引擎友好之外为什么要推行 web 语义化。

**从机器角度来看：**

HTML(***a universally understood language***)是联系大多数 Web 资源的纽带，也是内容的载体，最终由机器读取、解析和渲染，或者被挖掘出有用的信息为其他应用提供支持。所以需要机器能够很好地读懂 web 上发布的内容。
> 虽然 HTML 在刚开始设计出来的时候就是带有一定的「语义」的，包括段落、表格、图片、标题等等，但这些更多地只是方便浏览器等 UA 对它们作合适的处理。但逐渐地，机器也要借助 HTML 提供的语义以及自然语言处理的手段来「读懂」它们从网上获取的 HTML 文档，然而它们无法读懂例如「红色的文字」或者是深度嵌套的表格布局中内容的含义。

> 当前能够看得见摸得着的 Web 语义化，是对已经有的被广泛认可的 HTML 标准做改进。回归内容本身，将内容本身的语义合理地表述出来，再为不同的用户代理设计不同的样式描述，也就是我们说的内容与样式分离。这样我们在提供内容的时候，首先要做的就是将内容本身进行合理的描述，暂时不用考虑它的最终呈现会是什么样子。

> 其实 HTML 规范一直在往语义化的方向上努力，许多元素、属性在设计的时候，就已经考虑了如何让各种用户代理甚至网络爬虫更好地理解 HTML 文档。HTML5 更是在之前规范的基础上，将所有表现层（presentational）的语义描述都进行了修改或者删除，增加了不少可以表达更丰富语义的元素。为什么这样的语义元素是有意义的？因为它们被广泛认可。所谓语义本身就是对符号的一种共识，被认可的程度越高、范围越广，人们就越可以依赖它实现各种各样的功能。

> <small>摘抄自[如何理解 Web 语义化？](https://www.zhihu.com/question/20455165)</small>

**从开发者角度来看：**

web 语义化，不仅可以使机器易于理解，也方便了开发者快速构建页面和团队协作，减少了维护成本。

关于 HTML5 新增的语义化标签的介绍和使用场景可以查看**参考资料**。
> 参考资料：
> 
> [如何理解 Web 语义化？](https://www.zhihu.com/question/20455165)
>
> [Semantic HTML](http://justineo.github.io/slideshows/semantic-html/#/)
> 
> [HTML5 语义元素](https://www.w3schools.com/html/html5_semantic_elements.asp)
>
> [HTML 5的革新——语义化标签(一)](http://www.html5jscss.com/html5-semantics-section.html)

-------------------------

### 低版本浏览器如何兼容 HTML5 标签
HTML5的语义化标签以及属性，可以让开发者非常方便地实现清晰的web页面布局，加上CSS3的效果渲染，快速建立丰富灵活的web页面显得非常简单。使用它们能让代码语义化更直观，而且更方便SEO优化。但是HTML5新标签在IE6/IE7/IE8上并不能识别，需要进行JavaScript处理。以下就介绍几种方式。
1. **手动创建HTML5标签**
```javascript
<!--[if lt IE 9]>
<script>
(function () {
  var e = "abbr, article, aside, audio, canvas, datalist, details, dialog, eventsource, figure, footer, header, hgroup, mark, menu, meter, nav, output, progress, section, time, video".split(', ')
  var i = e.length
  while (i--) {
    document.createElement(e[i])
  }
})()
</script>
<![endif]-->
```
```css
/*html5*/
article, aside, dialog, footer, header, section, nav, figure, menu { display: block }
```
2. **使用Google的html5shiv（推荐）**
```javascript
<!--[if lt IE 9]> 
    <script src="bower_components/html5shiv/dist/html5shiv.js"></script>
<![endif]-->
```

----------

## 点击相关事件触发顺序
**HTML**
```html
<button id="aa">a</button>
```
**JavaScript**
```javascript
var a = document.getElementById("aa")

a.onmousedown = function() {
  console.log("down")
}

a.onmouseup = function() {
  console.log("up")
}

a.onclick = function(){
  console.log("click")
}

a.onfocus = function() {
  console.log("focus")
}
```
**Console**

事件触发顺序是：`down focus up click`。

----------


## 鼠标移动事件
`mouseenter` vs `mouseover`

mouseenter不会冒泡，mouseover会冒泡，i.e.鼠标滑过绑定元素以及子元素都会触发mouseover事件。

`mouseleave` vs `mouseout`

mouseleave不会冒泡，mouseout会冒泡。

对于mouseover和mouseout事件，有一个相关目标的属性（`relatedTarget`）。通过判断相关目标可以防止事件冒泡。

**mouseover**：主目标是获得焦点的元素，相关目标是失去焦点的元素（<=IE8: `fromElement`）。

**mouseout**：主目标是失去焦点的元素，相关目标是获得焦点的元素（<=IE8: `toElement`）。

----------
