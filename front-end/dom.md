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
Geeook created at 2017/8/9 23:02:06 
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
Geeook @ 2017/8/25 16:49:11 
## 低版本浏览器如何兼容HTML5标签
HTML5的语义化标签以及属性，可以让开发者非常方便地实现清晰的web页面布局，加上CSS3的效果渲染，快速建立丰富灵活的web页面显得非常简单。
- `<header>`定义页面或区段的头部；
- `<footer>`定义页面或区段的尾部；
- `<nav>`定义页面或区段的导航区域；
- `<section>`定义页面的逻辑区域或内容组合；
- `<article>`定义正文或一篇完整的内容；
- `<aside>`定义补充或相关内容；

使用它们能让代码语义化更直观，而且更方便SEO优化。但是HTML5新标签在IE6/IE7/IE8上并不能识别，需要进行JavaScript处理。以下就介绍几种方式。
### 手动创建HTML5标签
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
**CSS：**
```css
/*html5*/
article, aside, dialog, footer, header, section, nav, figure, menu { display: block }
```
### 使用Google的html5shiv（推荐）
```javascript
<!--[if lt IE 9]> 
    <script src="bower_components/html5shiv/dist/html5shiv.js"></script>
<![endif]-->
```

----------
Geeook @ 2017/8/25 20:29:39 
## 对HTML5标签语义化的理解

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
Geeook @ 2017/8/26 13:54:06 

## 鼠标移动事件
`mouseenter` vs `mouseover`

mouseenter不会冒泡，mouseover会冒泡，i.e.鼠标滑过绑定元素以及子元素都会触发mouseover事件。

`mouseleave` vs `mouseout`

mouseleave不会冒泡，mouseout会冒泡。

对于mouseover和mouseout事件，有一个相关目标的属性（`relatedTarget`）。通过判断相关目标可以防止事件冒泡。

**mouseover：**主目标是获得焦点的元素，相关目标是失去焦点的元素（<=IE8: `fromElement`）。

**mouseout：**主目标是失去焦点的元素，相关目标是获得焦点的元素（<=IE8: `toElement`）。

----------
Geeook @ 2017/8/26 13:53:38 