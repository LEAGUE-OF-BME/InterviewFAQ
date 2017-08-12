## 建立TCP连接的三次握手

## HTTP和HTTPS
### HTTP介绍
HTTP是互联网的基础协议，处于TCP/IP协议簇的第三层——应用层，主要规定了客户端和服务器之间的通信格式。
#### 请求格式
.......................................................

请求方法 + 协议版本

请求头部

**空行（\r\n）**

请求数据
.......................................................
#### 响应格式
.......................................................

协议版本 + 状态码 + 状态描述

响应头部

**空行（\r\n）**

响应数据

.......................................................
#### 响应头部之Content-Type
由于数据可以是任何格式，因此服务器需要告诉客户端数据格式。常见的Content-Type字段值：
> - text/plain
- text/html
- text/css
- image/jpeg
- image/png
- image/svg+xml
- audio/mp4
- video/mp4
- application/javascript
- application/pdf
- application/zip
- application/atom+xml

这些数据类型总称为**MIME type**，形式：一级类型/二级类型。还可以添加编码格式的参数：
> Content-Type: text/html; charset=utf-8

客户端请求时可以用**Accept**字段表明可以接受的数据格式。
#### 响应头部之Content-Encoding
表明数据压缩的方法。
> Content-Encoding: gzip
> 
> Content-Encoding: compress
> 
> Content-Encoding: deflate

客户端请求时可以用**Accept-Encoding**字段表明可以接受的压缩方法。

#### 我有管道，我很持久
**HTTP/1.1**引入了持久连接（persistent connection），TCP连接默认不关闭，可以被多个请求复用，无需申明Connection：keep-alive。对于同一个域名，大多数浏览器允许同时建立6个持久连接。

**HTTP/1.1**还引入了管道机制（pipelining），即在同一个TCP连接里面，客户端可以同时发送多个请求。

管道机制和持久连接大大改进了HTTP协议的效率。
#### 响应头部之Content-length
一个TCP连接现在可以传送多个响应，势必就要有一种机制，区分数据包是属于哪一个响应。这就是**Content-length**字段的作用，声明本次回应的数据长度。
> Content-Length: 3495 // 表明本次回应的长度是3495个字节，后面的字节就属于下一个回应了

#### 响应头部之Transfer-Encoding
对于耗时的动态操作，服务器的处理方法是：产生一块数据，就发送一块，采用"流模式"（stream）取代"缓存模式"（buffer）。因此可以不使用Content-Length字段，而使用"分块传输编码"（chunked transfer encoding）。只要请求或响应的头部有Transfer-Encoding字段，就表明响应将由数量未定的数据块组成。
> HTTP/1.1 200 OK</br>
> Content-Type: text/plain</br>
> Transfer-Encoding: chunked</br>
> 
> 25&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*// 16进制，表示块的长度*</br>
> This is the data in the first chunk
> 
> 1C</br>
> and this is the second one
> 
> 3</br>
> con
> 
> 8</br>
> sequence
> 
> 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*// 数据发送完毕*

#### 请求方法
HTTP定义了一组请求方法：
- GET
- POST
- PUT
- DELETE
- HAED
- OPTIONS
- PATCH

**特性：**
- **安全**：请求不改变服务器的状态（只读）。比如：GET、HEAD和OPTIONS。
- **幂等**：在服务器处于相同状态时，进行一次或多次请求的效果相同，**i.e.** 幂等方法没有副作用。比如：GET，HEAD，PUT和DELETE。但是多次DELETE请求，返回的状态码不一样。
- **可缓存的**：HTTP响应可以被缓存以备下次使用。但并不是所有的响应都能被缓存，约束有：
    1. 请求方法本身是可缓存的，比如GET或者HEAD，而PUT或者DELETE不是可缓存的。
    2. 如果响应的状态码对于应用缓存是已知的，那么他们可以认为是可缓存的。
    3. 设置响应头部**Cache-Control: no-cache**可以防止缓存。

#### PUT vs POST
|   | PUT | POST|
|:--|:-----|:------|
| 理论用法 | 将请求实体放在给定的请求路径下，如果请求路径下已经存在资源，就更新，否则就创建。| 将请求实体放在请求路径的次级目录中，意味着请求路径应该是一个集合的URI。|
| 请求示例 | PUT /questions/{question-id} | POST /questions |
| 是否幂等 | **是** | **否**，如果你请求多次，将会在不同的URI下创建多个资源 |
| 是否可缓存 | **否** | **否**。除非响应头部明确包含Cache-Control或者Expires字段 |
| 实际用法 | 通常用于UPDATE | 通常用于CREATE |

但其实PUT和POST都可以用于CREATE和UPDATE，在RESTful API设计时主要考虑幂等性质，具体使用时取决于你指定的请求路径。

**POST:**

Modify and update a resource:

POST /questions/(existing_question) HTTP/1.1</br>
Host: www.example.com/

Create a resource:

POST /questions HTTP/1.1</br>
Host: www.example.com/

**PUT:**

For a new resource:

PUT /questions/(new_question) HTTP/1.1</br>
Host: www.example.com/

To overwrite an existing resource:

PUT /questions/(existing_question) HTTP/1.1</br>
Host: www.example.com/
</div>

> 转载自：[REST – PUT vs POST](http://restfulapi.net/rest-put-vs-post/)
> 
> 更多详情请见：[PUT vs POST](https://stackoverflow.com/questions/630453/put-vs-post-in-rest)

#### GET vs POST
|   | GET | POST|
|:--|:-----|:------|
| 理论用法 | 获取指定路径下的资源 | 修改或者创建资源 |
| 请求示例 | GET /answers/{answer-id} | POST /questions |
| 是否安全* | **是** | **否** |
| 是否幂等 | **是** | **否** |
| 请求方式 | 在URL上附带请求参数 | 请求数据封装在请求体中 |
| 是否可缓存 | **是** | **否**。除非响应头部明确包含Cache-Control或者Expires字段 |
| 安全性 | 将数据明文放在URL上，不安全，并且可能造成CSRF | POST比GET高 |
| 实际用法 | 有时候也用于修改资源 | 对于资源的增删查改其实都可以用过GET和POST完成，但其实不满足HTTP的设计初衷和规范 |

*这里的是否安全指的是否会改变资源的状态，GET只读不写，所以安全。
#### HTTP缓存机制
#### HTTP的缺点
HTTP/1.1的缺点：虽然1.1版允许复用TCP连接，但是同一个TCP连接里面，所有的数据通信是按次序进行的。服务器只有处理完一个回应，才会进行下一个回应。要是前面的回应特别慢，后面就会有许多请求排队等着。这称为"队头堵塞"（Head-of-line blocking）。
### HTTPS介绍
TCP/IP协议族分为四层：应用层、传输层、网络层和数据链路层。其中HTTP协议处于应用层，TCP位于传输层和IP位于网络层。由于HTTP协议传输的数据是明文的，存在数据嗅探和篡改的安全问题。于是就有了**SSL**（Secure Sockets Layer）/**TLS**（Transport Layer Security）协议，用于对HTTP协议传输的数据进行加密，从而诞生了HTTPS。
#### 原理
先看一张图片：

![](http://image.beekka.com/blog/2014/bg2014092013.png)

（爱丽丝是客户端，鲍勃是服务端）
1. 爱丽丝给出协议版本号、一个客户端生成的随机数（Client random），以及客户端支持的加密方法。
2. 鲍勃确认双方使用的加密方法，并给出数字证书、以及一个服务器生成的随机数（Server random）。
3. 爱丽丝确认数字证书有效，然后生成一个新的随机数（Premaster secret），并使用数字证书中的公钥，加密这个随机数，发给鲍勃。
4. 鲍勃使用自己的私钥，获取爱丽丝发来的随机数（即Premaster secret）。
5. 爱丽丝和鲍勃根据约定的加密方法，使用前面的三个随机数，生成"对话密钥"（session key），用来加密接下来的整个对话过程。

更清晰的解释：

![](http://image.beekka.com/blog/2014/bg2014092003.png)

在整个过程中，TLS/SSL使用了对称加密、不对称加密以及HASH算法。其中，非对称加密（服务器的公钥和私钥）用于加密握手过程中生成的密码，对称加密用于对真正传输的数据进行加密和解密（对话密钥），而HASH算法用于验证数据的完整性。整个对话（握手和之后的对话）中，服务器的公钥和私钥只需用一次。
#### HTTPS的优势
1. 使用HTTPS协议可以认证用户和服务器，确保数据发送到正确的客户端和服务器上；
2. HTTPS协议是由SSL/TLS+HTTP协议构建的可加密传输、身份认证的网络协议，比HTTP更加安全，可防止数据在传输过程中被窃取和改变，确保数据的完整性；
3. HTTPS是现行架构下最安全的解决方案，虽然不是绝对安全，但至少大幅度增加了中间人攻击的额成本；

### HTTP升级为HTTPS需要哪些操作

### HTTP/2介绍




## DNS解析的方法

## 跨域方法

## 网络安全之XSS和CSRF

### 模拟XSS攻击

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