## 建立TCP连接的三次握手

## HTTP和HTTPS
### HTTP介绍
HTTP是互联网的基础协议，处于TCP/IP协议簇的第三层——应用层，主要规定了客户端和服务器之间的通信格式。
#### 请求格式
.......................................................

请求方法 + 协议版本

请求头部

**空行（\r\n）**

请求数据</br>
.......................................................
#### 响应格式
.......................................................

协议版本 + 状态码 + 状态描述

响应头部

**空行（\r\n）**

响应数据</br>
.......................................................
#### 响应头部之Content-Type
由于数据可以是任何格式，因此服务器需要告诉客户端数据格式。常见的Content-Type字段值：
> - text/plain
> - text/html
> - text/css
> - image/jpeg
> - image/png
> - image/svg+xml
> - audio/mp4
> - video/mp4
> - application/javascript
> - application/pdf
> - application/zip
> - application/atom+xml

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

![](/image/SSL五次握手.png)

（爱丽丝是客户端，鲍勃是服务端）
1. 爱丽丝给出协议版本号、一个客户端生成的随机数（Client random），以及客户端支持的加密方法。
2. 鲍勃确认双方使用的加密方法，并给出数字证书、以及一个服务器生成的随机数（Server random）。
3. 爱丽丝确认数字证书有效，然后生成一个新的随机数（Premaster secret），并使用数字证书中的公钥，加密这个随机数，发给鲍勃。
4. 鲍勃使用自己的私钥，获取爱丽丝发来的随机数（即Premaster secret）。
5. 爱丽丝和鲍勃根据约定的加密方法，使用前面的三个随机数，生成"对话密钥"（session key），用来加密接下来的整个对话过程。

更清晰的解释：

![](http://image.beekka.com/blog/2014/bg2014092004.png)

在整个过程中，TLS/SSL使用了对称加密、不对称加密以及HASH算法。其中，非对称加密（服务器的公钥和私钥）用于加密握手过程中生成的密码，对称加密用于对真正传输的数据进行加密和解密（对话密钥），而HASH算法用于验证数据的完整性。整个对话（握手和之后的对话）中，服务器的公钥和私钥只需用一次。
#### 优势：
1. 使用HTTPS协议可以认证用户和服务器，确保数据发送到正确的客户端和服务器上。
2. HTTPS协议是由SSL/TLS+HTTP协议构建的可加密传输、身份认证的网络协议，比HTTP更加安全，可防止数据在传输过程中被窃取和改变，确保数据的完整性。
3. HTTPS是现行架构下最安全的解决方案，虽然不是绝对安全，但至少大幅度增加了中间人攻击的额成本。
#### 缺点：
1. HTTPS会使页面的加载时间延长，连接缓存不如HTTP高效，对服务器端资源占用高，增加数据开销和功耗。
2. HTTPS协议的加密范围有限，对黑客攻击、服务器劫持等方面几乎不起作用，而且SSL证书的信用链体系并不安全。
3. SSL证书需要花钱购买，并且在绑定IP时不能绑定多个域名。
### HTTP升级为HTTPS需要哪些操作
#### 1. 获取证书
**1.1 证书作用：**

证书，即：CA证书、SSL 证书。是指由电子证书认证机构（CA, Certificate Authority）所版发的数字证书，可用于认证网站身份、加密通讯内容。证书中内容包括：
- 所有者的身份信息
- 证书序列号及到期时间
- 加密公钥
- 证书颁发机构的数字签名

**1.2 购买证书：**

向CA厂商购买证书，并进行身份认证。

**按照认证级别分类：**
- 域名认证(DV SSL，Domain Validation)：申请流程较为简单，认证级别最低，可以验证申请人对域名的所有权。客户端验证成功后，一般会在浏览器地址栏显示一把锁
- 组织认证(OV SSL，Organization Validation)：申请流程较为复杂，认证级别较高，可以验证域名及组织的合法性。
- 扩展认证(EV SSL，Extended Validation)：申请时申请人必须通过严谨的扩展验证流程，认证级别最高。客户端验证成功后，会浏览器地址栏会显示公司名

**按照适用范围分类：**
- 单域名SSL：证书只能用于一个网站。如：itbilu.com的证书将不能用于www.itbilu.com
- 多域名SSL：证书可以用于多个网站。如：用于www.itbilu.com证书也可用于www.itbilu.cn、www.itbilu2.com等
- 通配符SSL：证书可以用于某个及其所有一级子域名。如：*.itbilu.com的证书，也可用于www.itbilu.com、cdn.itbilu.com等
#### 2. 安装证书
根据厂商提供的证书安装教程进行安装，一般都会修改站点配置：监听443端口，启用SSL/TLS服务；配置HTTP转发。
#### 3. 调整资源连接
站点静态资源同样需要使用https连接，尤其是js脚本和css样式表，图片最好也该用HTTPS连接。
### HTTP/2介绍
HTTP/2只在 HTTPS 环境才会生效。
#### 二进制协议
HTTP/1.1 版的头信息肯定是文本（ASCII编码），数据体可以是文本，也可以是二进制。HTTP/2 则是一个彻底的二进制协议，头信息和数据体都是二进制，并且统称为"帧"（frame）：头信息帧和数据帧。
#### 多工
HTTP/2 复用TCP连接，在一个连接里，客户端和浏览器都可以同时发送多个请求或回应，而且不用按照顺序一一对应，这样就避免了"队头堵塞"。这样双向的、实时的通信，就叫做多工（Multiplexing）。
#### 数据流
因为 HTTP/2 的数据包是不按顺序发送的，同一个连接里面连续的数据包，可能属于不同的回应。因此，必须要对数据包做标记，指出它属于哪个回应。

HTTP/2 将每个请求或回应的所有数据包，称为一个数据流（stream）。每个数据流都有一个独一无二的编号。数据包发送的时候，都必须标记数据流ID，用来区分它属于哪个数据流。另外还规定，客户端发出的数据流，ID一律为奇数，服务器发出的，ID为偶数。

客户端和服务器都可以发送信号（RST_STREAM帧）取消数据流。
#### 头信息压缩
HTTP 协议不带有状态，每次请求都必须附上所有信息。所以，请求的很多字段都是重复的，比如Cookie和User Agent，一模一样的内容，每次请求都必须附带，这会浪费很多带宽，也影响速度。

HTTP/2 对这一点做了优化，引入了头信息压缩机制（header compression）。一方面，头信息使用**gzip**或**compress**压缩后再发送；另一方面，客户端和服务器同时维护一张头信息表，所有字段都会存入这个表，生成一个索引号，以后就不发送同样字段了，只发送索引号，这样就提高速度了。
#### 服务器推送
HTTP/2 允许服务器未经请求，主动向客户端发送资源，这叫做服务器推送（server push）。

常见场景是客户端请求一个网页，这个网页里面包含很多静态资源。正常情况下，客户端必须收到网页后，解析HTML源码，发现有静态资源，再发出静态资源请求。其实，服务器可以预期到客户端请求网页后，很可能会再请求静态资源，所以就主动把这些静态资源随着网页一起发给客户端了。

> 参考链接：
> 
> [HTTP 协议入门](http://www.ruanyifeng.com/blog/2016/08/http.html)
> 
> [图解SSL/TLS协议](http://www.ruanyifeng.com/blog/2014/09/illustration-ssl.html)
> 
> [HTTPS 升级指南](http://www.ruanyifeng.com/blog/2016/08/migrate-from-http-to-https.html)

## DNS解析的方法

## 跨域方法
### 同源策略（协议、域、端口）
| URL | 说明 | 是否允许通信 |
|:----|:-----|:-----------:|
| http://www.a.com/a.js</br>http://www.a.com/b.js</br> | 同一域名下 | 允许 |
| http://www.a.com/lab/a.js</br>http://www.a.com/script/b.js</br> | 同一域名下不同文件夹 | 允许 |
| http://www.a.com:8000/a.js</br>http://www.a.com/b.js</br> | 同一域名，不同端口 | 不允许 |
| http://www.a.com/a.js</br>https://www.a.com/b.js</br> | 同一域名，不同协议 | 不允许 |
| http://www.a.com/a.js</br>http://70.32.92.74/b.js</br> | 域名和域名对应ip | 不允许 |
| http://www.a.com/a.js</br>http://script.a.com/b.js</br> | 主域相同，子域不同 | 不允许 |
| http://www.a.com/a.js</br>http://a.com/b.js</br> | 同一域名，不同二级域名（同上） | 不允许 |
| http://www.cnblogs.com/a.js</br>http://www.a.com/b.js</br> | 不同域名 | 不允许 |

**注意：**
1. 如果是协议和端口造成的跨域问题，“前台”是无能为力的。
2. 通过“URL的首部”来识别是否同域，而不会去尝试判断相同的ip地址对应着两个域或两个域是否在同一个ip上。
### CORS

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