## 创建新节点和查找节点的方法
### 创建新节点：
createAttribute(): creates a new attribute node, and returns it.

createCDATASection(): creates a new CDATA section node, and returns it.

createComment(): creates a new comment node, and returns it.

createDocumentFragment(): Creates a new empty DocumentFragment.

createElement(): creates the HTML element specified by tagName, or an HTMLUnknownElement if tagName isn't recognized.

createElementNS(): creates an element with the specified namespace URI and qualified name.

createTextNode(): creates a new Text node.

~~createNode()~~
### 查找节点：
getElementById()

getElementsByClassName()

getElementsByName()

getElementsByTagName()

getElementsByTagNameNS(): Returns a list of elements with the given tag name belonging to the given namespace.

----------
Geeook created at 2017/8/9 23:02:06 
## 浏览器如何渲染一棵DOM树