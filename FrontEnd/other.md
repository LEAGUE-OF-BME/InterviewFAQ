# 关于面试
## 1 小米面试
### 1.1 getElementById 实现原理
Q：getElementById 实现的原理？

`getElementById()` 不是JavaScript语言的功能，而是浏览器作为JavaScript的host环境注册给JavaScript的host函数，由浏览器内部实现。

以 Chrome 为例，底层实现的代码是：
```cpp
Element* TreeScope::getElementById(const AtomicString& elementId) const
{
    if (elementId.isEmpty())
        return 0;
    if (!m_elementsById)
        return 0;
    return m_elementsById->getElementById(elementId, this);
}
```
所以底层原理是利用了哈希表记录 ID 到 dom 节点的映射关系，每当有一个新的 ID 添加到 dom 节点，相应的映射关系就会被加到这个哈希表里。

**延伸：其他获取 DOM 节点的方法比较**

`getElementsByClassName()` 和 `getElementsByTagName()` 遍历 DOM 树（具体如何遍历不了解），返回 Array-Like Object `HTMLCollection`，而且是 live reference。

The methods getElementsByClassName and getElementsByTagName return an HTMLCollection object that acts like an array. That collection is "live", which means the collection is updated if additional elements with tag name or class name are added to the document.

`querySelectorAll()` 返回 Array-Like Object `NodeList`，不过是静态的。

The method querySelectorAll() returns a NodeList, which also acts like an array. That list is "static", which means that the list won't update even if new matching elements are added to the page.
### 1.2 AJAX 相关
Q：AJAX 产生背景，在 AJAX 出现之前一般是怎么做的？

在应用 AJAX 之前，传统的 web 应用在不需要进行大量内容更新时也要刷新整个页面。AJAX（***Asynchronous JavaScript And XML***）的出现使得我们可以1. 在页面加载好了之后更新部分内容；2. 在页面加载好了之后向服务器请求数据或者发送数据，优化了用户体验。

AJAX 技术的核心是 `XMLHttpRequest`对象，XHR 为 web 应用和服务器通信提供了接口。具体的对象属性和方法以及通信的实现细节可以复习 `js.md` 中的`如何实现 AJAX 请求`。

在 AJAX 出现之前，采用的一些 hack 手段：（复习`web.md`中的`跨域方法`）
1. `<iframe>`
2. JSONP
3. `<img>`

其他：虽然 AJAX 名字里面是 xml，其实 AJAX 通信时支持的 MIME 类型包括：JSON、JSONP、text、xml、html 等。
### 1.3 jQuery 相关
Q：简要介绍一下 jQuery 的大致功能，相比原生JavaScript 带来了哪些便利，项目中使用了那些功能？

jQuery 是一套跨浏览器的 JavaScript 开源库，简化了 HTML 和 JavaScript之间的操作，封装了一些常用的功能，并且可以扩展，是目前最受欢迎的 JavaScript 库。

jQuery 的功能和优势：
1. 简化了 DOM 元素选择
2. 浏览器兼容性很好
3. 内置了可自定义参数的动画效果，简化了应用动画效果的过程
4. 事件处理更加简单
5. 封装了很多功能，简化了常用的 JavaScript 操作
6. 支持 CSS3 标准
7. 提供了一整套 AJAX 相关操作的方法，大大方便了异步通信的开发和使用
8. 基于开源的 jQuery 还有很多的插件可以使用
9. 轻量级脚本，生态社区好，文档齐全，学习成本低

项目中主要使用了 jQuery 的 DOM 选择器，以及封装好的 AJAX 方法。

为了防止被问，总结一下：

