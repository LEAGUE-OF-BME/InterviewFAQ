## HTTP和HTTPS
### HTTP介绍
HTTP是互联网的基础协议，处于TCP/IP协议簇的第五层——应用层，主要规定了客户端和服务器之间的通信格式。
#### 请求格式
> 请求方法 + 协议版本 </br>
> 请求头部 </br>
> **空行（\r\n）** </br>
> 请求数据</br> 

#### 响应格式
> 协议版本 + 状态码 + 状态描述</br>
> 响应头部</br>
> **空行（\r\n）**</br>
> 响应数据</br>

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
#### 状态码
|         | 类别 | 说明 |
|:-----:|:-----|:------|
| 1XX | Information（信息型状态码） | 接受请求正在处理 |
| 2XX | Success（成功状态码） | 请求正常处理完毕 |
| 3XX | Redirection（重定向状态码） | 需要进行附加操作已完成请求 |
| 4XX | Client Error（客户端错误状态码） | 服务器无法处理请求 |
| 5XX | Server Error（服务器错误状态码） | 服务器处理请求错误 |

常用13种

**2XX**

200：OK

204：No Content 请求成功，响应不包括实体。

206：Partial Content 请求指定范围的实体成功。

**3XX**

301：Moved Permanently 永久性重定向，请求资源已被分配新的URI，希望用户以后都用新URI访问。

302：Found 临时性重定向，请求资源已被分配新的URI，希望用户本次用新URI访问。

303：See Other 请求对应的资源存在另一个URI，应使用GET方法定向获取请求的资源。

304：Not Modified 请求的资源和本地缓存相同。

**4XX**

400：Bad Request 请求存在语法错误。

401：Unauthorized 请求没有认证（第一次）或者认证失败。

403：Forbidden 对请求资源的访问被拒绝。

404：Not Found 服务器上无法找到请求资源。

**5XX**

500：Internal Server Error 服务器执行请求时发生错误，可能是因为临时故障或者Web应用的bug。

503：Service Unavailable 服务器暂时超负载或者停机维护，无法处理请求。
#### HTTP的缺点
HTTP/1.1的缺点：虽然1.1版允许复用TCP连接，但是同一个TCP连接里面，所有的数据通信是按次序进行的。服务器只有处理完一个回应，才会进行下一个回应。要是前面的回应特别慢，后面就会有许多请求排队等着。这称为"队头堵塞"（Head-of-line blocking）。
#### HTTP缓存机制
**相关头部字段**
1. 通用头部

| 名称 | 说明 |
|:-----|:------|
| Cache-Control | 控制缓存的行为 |
| Pragma | HTTP1.0 的字段，值为no-cache时禁用缓存 |
2. 请求头部

| 名称 | 说明 |
|:-----|:------|
| If-Match | 比较文件的ETag是否一致 |
| If-None-Match | 比较文件的ETag是否不一致 |
| If-Modified-Since | 比较资源最后更新时间是否一致 |
| If-Unmodified-Since | 比较资源最后更新时间是否不一致 |
3. 响应头部

| 名称 | 说明 |
|:-----|:------|
| ETag | 用于匹配资源的标识文件唯一性的信息 |
4. 实体头部


| 名称 | 说明 |
|:-----|:------|
| Expires | HTTP1.0的字段，过期时间 |
| Last-Modified | 资源上一次修改时间 |

**缓存存储策略**

缓存存储策略决定客户端是否缓存。
1. **Pragma**

Pragma是HTTP1.0的字段，为了兼容，现在的HTTP通信依旧会携带这个字段。值为no-cache时禁用缓存，优先级高于Cache-Control。
```html
// 不缓存
Cache-Control: public, max-age=86400
Pragma: no-cache
```
2. **Cache-Control**

作为请求头部时的取值：

![](http://7tszky.com1.z0.glb.clouddn.com/FkctxGN8VXdie7M8Fbx6U5Bpfi4c)

作为响应头部时的取值：

![](http://7tszky.com1.z0.glb.clouddn.com/FixnilG9OWm4w4qUNZGKSkYXZ4gu)

常用值：

| 指令 | 说明 |
|:-----|:------|
| public | 所有内容都将被缓存(客户端和代理服务器都可缓存) |
| private | 内容只缓存到私有缓存中(仅客户端可以缓存，代理服务器不可缓存) |
| max-age=xxx  | 缓存的内容将在 xxx 秒后失效，失效前可以直接使用本地缓存，失效后必须向服务器确认资源是否已经改变。 |
| no-store | 完全不在客户端缓存 |
| no-cache | 等同于max-age=0的情况，i.e.将response缓存在客户端，但每次都向服务器确认资源是否已经改变 |

Cache-Control 允许自由组合可选值，例如：
```html
Cache-Control: max-age=3600, must-revalidate
```
注意：若报文中同时出现了 Expires 和 Cache-Control，则以 Cache-Control 为准。
也就是说优先级从高到低分别是 Pragma -> Cache-Control -> Expires 。

**缓存过期策略**

缓存过期策略决定了客户端存储在本地的缓存数据是否已过期，如未过期则可以直接使用本地存储的数据，否则就需要发请求到服务端尝试重新获取数据。

1. **Expires**

Expires是HTTP1.0的字段，为了兼容，现在的HTTP通信依旧会携带这个字段。 Expires的值对应一个GMT（格林尼治时间），比如 **Mon, 22 Jul 2002 11:12:01 GMT** 来告诉浏览器资源缓存过期时间，如果还没过该时间点则不发请求。注意：Pragma优先级高于Expires。

响应报文中Expires所定义的缓存时间是相对服务器上的时间而言的，如果客户端上的时间跟服务器上的时间不一致（特别是用户修改了自己电脑的系统时间），那缓存时间可能就没啥意义了。

2. **Cache-Control**

对，又是Cache-Control。在HTTP1.0时期，用**Pragma**和**Expires**共同决定是否缓存和过期时间，但是Expires时间是相对服务器而言，无法保证和客户端时间统一。为了解决这个问题，HTTP1.1新增Cache-Control字段来代替Pragma和Expires。

**缓存校验/对比策略**

如果客户端上某个资源的缓存过期了，但服务器并没有更新过这个资源，就需要验证客户端的缓存和服务器的资源是否相同。

最先想到的就是文件修改时间。

1. **Last-Modified、If-Modified-Since和If-Unmodified-Since**

服务器将资源传递给客户端时，会将资源最后更改的时间以“Last-Modified: GMT”的形式加在实体首部上一起返回给客户端。
```html
Last-Modified: Fri, 22 Jul 2016 01:47:00 GMT
```
缓存过期再次请求时，会把该时间附带在请求报文中发送给服务器，若传递的时间值与服务器上该资源最终修改时间是一致的，则说明该资源没有被修改过，直接返回304状态码即可，否则重新请求最新资源。

传递标记时间的请求头部字段有两个：**If-Modified-Since**和**If-Unmodified-Since**。

如果服务器上某资源被修改了，但实际内容根本没发生改变，会因为Last-Modified时间匹配不上而返回了整个实体给客户端，所以需要直接比较文件内容。

2. **ETag**

服务器给资源计算出一个唯一标志符（默认是由文件的索引节（INode），大小（Size）和最后修改时间（MTime）进行Hash后得到的），在响应头部加上“ETag: 唯一标识符”一起返回给客户端。
```html
ETag: "17fd8-5291a5f96fd20"
```
客户端会保留该 ETag 字段，在下一次请求时将其附在请求头部发送给服务器。服务器只需要比较客户端传来的ETag跟自己服务器上该资源的ETag是否一致，就能很好地判断资源相对客户端而言是否被修改过了。请求报文中有两个首部字段可以带上 ETag 值：**If-None-Match**和**If-Match**。

如果 Last-Modified 和 ETag 同时使用，则要求它们的验证都必须通过才会返回304，若其中某个验证没通过，则服务器会按常规返回资源实体及200状态码。

**缓存实践**

1. **Expires / Cache-Control**

考虑兼容，同时使用Expires和Cache-Control，会优先使用Cache-Control。

2. **from-cache / 304**

对于所有可缓存资源，指定Expires和Cache-Control max-age以及一个Last-Modified或ETag至关重要。同时使用前者和后者可以很好的相互适应。

3. **静态资源**

页面的静态资源以版本形式发布，常用的方法是在文件名或参数带上一串md5或时间标记符：
```html
https://hm.baidu.com/hm.js?e23800c454aa573c0ccb16b52665ac26
http://tb1.bdstatic.com/tb/_/tbean_safe_ajax_94e7ca2.js
http://img1.gtimg.com/ninja/2/2016/04/ninja145972803357449.jpg
```
可以看到上面的例子中有不同的做法，有的在URI后面加上了md5参数，有的将md5值作为文件名的一部分，有的将资源放在特定版本的目录中。

那么在文件没有变动的时候，浏览器不用发起请求直接可以使用缓存文件；而在文件有变化的时候，由于文件版本号的变更，导致文件名变化，请求的url变了，自然文件就更新了。这样能确保客户端能及时从服务器收取到新修改的文件。通过这样的处理，增长了静态资源，特别是图片资源的缓存时间，避免该资源很快过期，客户端频繁向服务端发起资源请求，服务器再返回304响应的情况（有Last-Modified/Etag）。
### HTTPS介绍
<a id="tls" name="tls"></a>TCP/IP协议族分为四层：应用层、传输层、网络层和数据链路层。其中HTTP协议处于应用层，TCP位于传输层和IP位于网络层。由于HTTP协议传输的数据是明文的，存在数据嗅探和篡改的安全问题。于是就有了**SSL**（Secure Sockets Layer）/**TLS**（Transport Layer Security）协议，用于对HTTP协议传输的数据进行加密，从而诞生了HTTPS。
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
#### 优势
1. 使用HTTPS协议可以认证用户和服务器，确保数据发送到正确的客户端和服务器上。
2. HTTPS协议是由SSL/TLS+HTTP协议构建的可加密传输、身份认证的网络协议，比HTTP更加安全，可防止数据在传输过程中被窃取和改变，确保数据的完整性。
3. HTTPS是现行架构下最安全的解决方案，虽然不是绝对安全，但至少大幅度增加了中间人攻击的额成本。
#### 缺点
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
- 域名认证(DV SSL，Domain Validation)：申请流程较为简单，认证级别最低，可以验证申请人对域名的所有权。客户端验证成功后，一般会在浏览器地址栏显示一把锁。
- 组织认证(OV SSL，Organization Validation)：申请流程较为复杂，认证级别较高，可以验证域名及组织的合法性。
- 扩展认证(EV SSL，Extended Validation)：申请时申请人必须通过严谨的扩展验证流程，认证级别最高。客户端验证成功后，会浏览器地址栏会显示公司名。

**按照适用范围分类：**
- 单域名SSL：证书只能用于一个网站。如：itbilu.com的证书将不能用于www.itbilu.com。
- 多域名SSL：证书可以用于多个网站。如：用于www.itbilu.com证书也可用于www.itbilu.cn、www.itbilu2.com等。
- 通配符SSL：证书可以用于某个及其所有一级子域名。如：*.itbilu.com的证书，也可用于www.itbilu.com、cdn.itbilu.com等。
#### 2. 安装证书
根据厂商提供的证书安装教程进行安装，一般都会修改站点配置：监听443端口，启用SSL/TLS服务；配置HTTP重定向。
#### 3. 调整资源连接
站点静态资源同样需要使用https连接，尤其是js脚本和css样式表，图片最好也该用HTTPS连接。

#### 安全问题
**HTTP Strict Transport Security(HSTS)**

访问网站时，用户很少直接在地址栏输入https://，总是通过点击链接，或者3xx重定向，从HTTP页面进入HTTPS页面。攻击者完全可以在用户发出HTTP请求时，劫持并篡改该请求。

另一种情况是恶意网站使用自签名证书，冒充另一个网站，这时浏览器会给出警告，但是许多用户会忽略警告继续访问。

HSTS的作用就是强制浏览器只能发出HTTPS请求，并阻止用户接受不安全的证书。它在网站的响应头里面，加入一个强制性声明：
> Strict-Transport-Security: max-age=31536000; includeSubDomains
> 
> （1）在接下来的一年（即31536000秒）中，浏览器只要向example.com或其子域名发送HTTP请求时，必须采用HTTPS来发起连接。用户点击超链接或在地址栏输入http://www.example.com/ ，浏览器应当自动将http转写成https，然后直接向https://www.example.com/ 发送请求。
> 
> （2）在接下来的一年中，如果example.com服务器发送的证书无效，用户不能忽略浏览器警告，将无法继续访问该网站。

HSTS 很大程度上解决了 SSL 剥离攻击。只要浏览器曾经与服务器建立过一次安全连接，之后浏览器会强制使用HTTPS，即使链接被换成了HTTP。
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

----------

## DNS解析的过程
当用户在浏览器中输入ke.qq.com并按下回车键后：
1. 查找**浏览器缓存**
> 浏览器会检查缓存中有没有这个域名对应的解析过的IP地址，如果缓存中有，这个解析过程就将结束。浏览器缓存域名也是有限制的，不仅浏览器缓存大小有限制，而且缓存的时间也有限制，通常情况下为几分钟到几小时不等。这个缓存时间太长和太短都不好，如果缓存时间太长，一旦域名被解析到的IP有变化，会导致被客户端缓存的域名无法解析到变化后的IP地址，以致该域名不能正常解析，这段时间内有可能会有一部分用户无法访问网站。如果时间设置太短，会导致用户每次访问网站都要重新解析一次域名。

2. 查找**系统缓存**
> 如果用户的浏览器缓存中没有，浏览器会查找操作系统缓存中是否有这个域名对应的DNS解析结果。其实操作系统也会有一个域名解析的过程，在Windows中可以通过C:\Windows\System32\drivers\etc\hosts文件来设置，你可以将任何域名解析到任何能够访问的IP地址。如果你在这里指定了一个域名对应的IP地址，那么浏览器会首先使用这个IP地址。正是因为有这种本地DNS解析的规程，所以黑客就有可能通过修改你的域名解析来把特定的域名解析到它指定的IP地址上，导致这些域名被劫持。

3. 查找**路由器缓存**
> 如果系统缓存中也找不到，那么查询请求就会发向路由器，它一般会有自己的DNS缓存。

4. 查找**ISP DNS 缓存**
> 运气实在不好，就只能查询ISP DNS 缓存服务器了。在我们的网络配置中都会有"DNS服务器地址"这一项，操作系统会把这个域名发送给这里设置的DNS，也就是本地区的域名服务器，通常是提供给你接入互联网的应用提供商。这个专门的域名解析服务器性能都会很好，它们一般都会缓存域名解析结果，当然缓存时间是受域名的失效时间控制的，一般缓存空间不是影响域名失效的主要因素。大约80%的域名解析都到这里就已经完成了，所以ISP DNS主要承担了域名的解析工作。

5. 逐级搜索
> 在前面都没有办法命中的DNS缓存的情况下：
> 
> (1)本地 DNS服务器即将该请求转发到互联网上的根域（即一个完整域名最后面的那个点，通常省略不写）。
> 
> (2)根域将所要查询域名中的顶级域（假设要查询ke.qq.com，该域名的顶级域就是com）的服务器IP地址返回到本地DNS。
> 
> (3) 本地DNS根据返回的IP地址，再向顶级域（就是com域）发送请求。
> 
> (4) com域服务器再将域名中的二级域（即ke.qq.com中的qq）的IP地址返回给本地DNS。
> 
> (5) 本地DNS再向二级域发送请求进行查询。
> 
> (6) 之后不断重复这样的过程，直到本地DNS服务器得到最终的查询结果，并返回到主机。这时候主机才能通过域名访问该网站。

**DNS有关的安全问题**
1. DNS欺骗</br>
**DNS欺骗**即域名信息欺骗是最常见的DNS安全问题。当一个DNS服务器掉入陷阱，使用了来自一个恶意DNS服务器的错误信息，那么该DNS服务器就被欺骗了。DNS欺骗会使那些易受攻击的DNS服务器产生许多安全问题，例如：将用户引导到错误的互联网站点，或者发送一个电子邮件到一个未经授权的邮件服务器。网络攻击者通常通过三种方法进行DNS欺骗。
    1. 缓存感染</br>
    黑客会熟练的使用DNS请求，将数据放入一个没有设防的DNS服务器的缓存当中。这些缓存信息会在客户进行DNS访问时返回给客户，从而将客户引导到入侵者所设置的运行木马的Web服务器或邮件服务器上，然后黑客从这些服务器上获取用户信息。
    2. DNS信息劫持</br>
    入侵者通过监听客户端和DNS服务器的对话，通过猜测服务器响应给客户端的DNS查询ID。每个DNS报文包括一个相关联的16位ID号，DNS服务器根据这个ID号获取请求源位置。黑客在DNS服务器之前将虚假的响应交给用户，从而欺骗客户端去访问恶意的网站。
    3. DNS重定向</br>
    攻击者能够将DNS名称查询重定向到恶意DNS服务器。这样攻击者可以获得DNS服务器的写权限。
2. 拒绝服务攻击</br>
黑客主要利用一些DNS软件的漏洞使DNS服务关闭。如果得不到DNS服务，那么就会产生一场灾难：由于网址不能解析为IP地址，用户将无方访问互联网。这样，DNS产生的问题就好像是互联网本身所产生的问题，这将导致大量的混乱。
3. 分布式拒绝服务攻击</br>
DDOS 攻击通过使用攻击者控制的几十台或几百台计算机攻击一台主机，使得服务拒绝攻击更难以防范，更难以通过阻塞单一攻击源主机的数据流，来防范服务拒绝攻击。
4. 缓冲区漏洞溢出攻击</br>
黑客利用DNS服务器软件存在漏洞，比如对特定的输入没有进行严格检查，那幺有可能被攻击者利用，攻击者构造特殊的畸形数据包来对DNS服务器进行缓冲区溢出攻击。如果这一攻击成功，就会造成DNS服务停止，或者攻击者能够在DNS服务器上执行其设定的任意代码。
> 转载自：[DNS解析](http://imweb.io/topic/55e3ba46771670e207a16bc8)

----------


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
### 1. CORS
默认情况下，XHR对象只能访问与包含它的页面位于同一域中的资源。CORS（跨域资源共享）定义了在必须访问跨域资源时，浏览器和服务器应该如何沟通。

基本思想就是使用自定义的HTTP头部Origin，包含请求页面的源信息（协议、域名和端口），以便服务器根据头部信息决定是否响应。如果请求被接受，就在响应头部Access-Control-Allow-Origin中回发相同的源信息。浏览器检验响应头部信息，如果头部不存在或者源信息不一致，浏览器驳回请求。**注：请求和响应中都不包含cookie信息。**
#### IE对CORS的实现
IE8之后引入了XDR，实现了安全可靠的跨域通信。所有的XDR请求都是异步执行的。响应有效触发load事件，失败触发error事件。只能获得响应的原始文本，不能确定响应的状态代码。

XDR的特点：
- 只能设置请求头部的Content-Type字段（在发送POST请求时设置数据格式）
- 不能访问响应头部
- 只能发送POST和GET请求
- 请求和响应都不包含cookie

#### 非IE对CORS的实现
非IE的XHR对象实现了对CORS的原生支持。只需在open()方法中传入绝对URL即可。

跨域XHR对象的特点：
- 可以访问status和statusText
- 支持同步请求
- 不能使用setRequestHeader设置自定义头部
- 不能发送和接受cookie

附加：
1. CORS可以通过**Preflighted Requests**的透明服务器验证机制支持使用自定义头部、GET和POST以外的方法以及不同类型的主体内容。
2. CORS通过将**withCredentials**属性设置为true可以指定某请求应该发送凭据。如果服务器接受带凭据的请求，就在响应头部加上`Access-Control-Allow-Credentials: true`。
### 2. 图像ping
`<img>`标签的src属性。通过动态创建图像并监听load和error事件实现与服务器进行简单的单向通信。

**应用示例**：跟踪用户点击页面或动态广告曝光次数。

**缺点**：只能GET请求；无法访问服务器的响应文本。
### 3. JSONP
*JSON with padding*的简写，是被包含在函数调用中的JSON。形式如：
`callback({"name": "xxx"})`

JSONP由两部分组成：回调函数和数据。回调函数是响应到来时调用的函数，函数名字在请求中指定。通过动态创建`<script>`元素，设置src为跨域的URL。请求完成之后，JSONP作为有效的JavaScript代码加载到页面中立即执行。

**优点**：简单易用、双向通信、兼容老浏览器。

**缺点**：可能会不安全，其他域可能会夹带恶意代码；很难确定JSONP请求是否失败；只支持GET请求。
### 4. document.domain + iframe
可以解决主域相同，子域不同的跨域通信。在当前页面和iframe中都设置document.domain = 主域。

**缺点**：一个站点受到攻击后，另一个站点会因此引起安全漏洞；主域必须相同。
### 5. location.hash + iframe
在不同域需要通信的页面中创建隐藏的iframe，利用location.hash互相传值。

**优点**：可以解决域名完全不同的跨域请求；并且是双向通信。

**缺点**：数据量受到url大小的限制，而且传递的数据类型有限；数据直接暴露在url中，存在安全问题；需要通过轮询得知hash的变化；有的浏览器会在hash变化是增加一条历史记录，这样会影响用户体验。
### 6. window.name + iframe
`window.name`属性用于获取/设置窗口的名称。其特征在于：一个窗口的生命周期内，窗口载入的所有页面共享该值，且都具有对该属性的读写权限。这意味着如果不修改该值，那么在不同页面加载之后该值也不会变，且其支持长达 2MB 的存储量。

**优点**：巧妙地绕过了浏览器的跨域访问限制，但同时它又是安全操作；可传输数据量大。
### 7. postMessage（HTML5中的XMLHttpRequest Level 2中的API）
发送方：隐藏的iframe+postMessage(data, targetOrigin)。

接收方：监听`message`事件。
### 8. web sockets
web sockets是一种浏览器的API，它的目标是在一个单独的持久连接上提供全双工、双向通信。(同源策略对web sockets不适用)

只要服务器支持web sockets，就可以通过它进行跨域通信。

----------

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


## 从输入URL到网页完全加载都经历了哪些过程
这是一道古老而经典的面试题，转载自
> [当···时发生了什么？](https://github.com/skyline75489/what-happens-when-zh_CN)

摘选了其中重要易懂的部分，并查阅了相关资料做了一些补充。
### 解析URL
浏览器通过 URL 能够知道下面的信息：
- Protocol："http"（使用HTTP协议）
- Resource："/"（请求的资源是主页）

当协议或主机名不合法时，浏览器会将地址栏中输入的文字传给默认的搜索引擎。

浏览器检查输入是否含有不是 `a-z， A-Z，0-9， - `或者` . `的字符，如果有的话，浏览器会对主机名部分使用 Punycode 编码。
### 检查 HSTS 列表
浏览器检查自带的“预加载 HSTS（HTTP严格传输安全）”列表，这个列表里包含了那些请求浏览器只使用HTTPS进行连接的网站，如果网站在这个列表里，浏览器会使用 HTTPS 而不是 HTTP 协议，否则，最初的请求会使用HTTP协议发送。
### DNS查询
1. 浏览器检查域名是否在缓存当中。
2. 如果没有找到或者缓存已经失效，则搜索操作系统的DNS缓存。
3. 如果没有找到或者缓存已经失效，则检查域名是否在本地 hosts 里。
4. 如果没有找到域名的缓存记录，也没有在 hosts 里找到，它将会向 DNS 服务器发送一条 DNS 查询请求。DNS 服务器是由网络通信栈提供的，通常是本地路由器或者 ISP 的缓存 DNS 服务器。
5. 查询本地 DNS 服务器，如果 DNS 服务器没有找到结果，它会发送一个递归查询请求，一层一层向高层 DNS 服务器做查询，直到查询到起始授权机构，如果找到会把结果返回。
6. 浏览器获得域名对应的IP地址之后发起TCP三次握手。
### TCP三次握手

![](/image/TCP.jpg)

1. 客户端发送序列号seq = x，标志位是SYN（synchronous）。
2. 服务端接收到序列号x之后，返回新的序列号seq = y，标志位是SYN，并将x + 1返回，标志位ACK（acknowledgement）。
3. 客户端接收到服务端的ACK，知道服务端已经收到了x，同样也将y + 1再次发送给服务端，标志位ACK。
### TLS握手
如果是HTTPS协议，在TCP三次握手之后，还会有TLS五次握手。详情请见：<a href="#tls">TLS五次握手</a>。
### HTTP请求处理
连接建立之后，浏览器就可以向服务器发送HTTP请求（请求网页，发送GET请求）。

HTTPD(HTTP Daemon)在服务器端处理请求。最常见的 HTTPD 有 Linux 上常用的 Apache 和 nginx，以及 Windows 上的 IIS。
1. HTTPD 接收请求。
2. 服务器把请求拆分为以下几个参数：
    - HTTP 请求方法，直接在地址栏中输入 URL 这种情况下，使用的是 GET 方法
    - 域名
    - 请求路径/页面
3. 服务器验证其上已经配置了该域名的虚拟主机。
4. 服务器验证该域名接受 GET 方法。
5. 服务器验证该用户可以使用 GET 方法(根据 IP 地址，身份信息等)。
6. 如果服务器安装了 URL 重写模块（例如 Apache 的 mod_rewrite 和 IIS 的 URL Rewrite），服务器会尝试匹配重写规则，如果匹配上的话，服务器会按照规则重写这个请求。
7. 服务器根据请求信息获取相应的响应内容，处理之后返回给浏览器。
### 浏览器加载页面
当服务器提供了资源之后（HTML，CSS，JS，图片等），浏览器会执行下面的操作：

**解析** —— HTML，CSS，JS

**渲染** —— 构建 DOM 树 -> 渲染 -> 布局 -> 绘制

![](http://coolshell.cn//wp-content/uploads/2013/05/Render-Process.jpg)

1. 浏览器解析：
    - 一个是HTML/SVG/XHTML，事实上，Webkit有三个C++的类对应这三类文档。解析这三种文件会产生一个DOM Tree。
    - CSS，解析CSS会产生CSS规则树。
    - Javascript，主要是通过DOM API和CSSOM API来操作DOM Tree和CSS Rule Tree。
2. 解析完成后，浏览器引擎会通过DOM Tree 和 CSS Rule Tree 来构造 Rendering Tree。注意：
    - Rendering Tree 渲染树并不等同于DOM树，因为一些像Header或display:none的东西就没必要放在渲染树中了。
    - CSS 的 Rule Tree主要是为了完成匹配并把CSS Rule附加上Rendering Tree上的每个Element。也就是DOM结点。也就是所谓的Frame。
    - 然后，计算每个Frame（也就是每个Element）的位置，这又叫layout和reflow过程。
3. 最后通过调用操作系统Native GUI的API绘制。

----------

## SEO
### 简介
SEO是搜索引擎优化的缩写（***Search Engine Optimization***）。SEO是指在了解搜索引擎自然排名机制的基础之上，通过对网站进行站内优化和修复(网站Web结构调整、网站内容建设、网站代码优化和编码等)和站外优化，从而提高网站的网站关键词排名以及公司产品的曝光度。
### 搜索引擎不优化的网站的特征
- 网页中大量采用图片或者Flash等富媒体（Rich Media）形式，没有可以检索的文本信息，而SEO最基本的就是文章SEO和图片SEO。
- 网页没有标题，或者标题中没有包含有效的关键词。
- 网页正文中有效关键词比较少。
- 网站导航系统让搜索引擎“看不懂”。
- 大量动态网页影响搜索引擎检索。
- 没有其他被搜索引擎已经收录的网站提供的链接。
- 网站中缺少原创的内容，完全照搬硬抄别人的内容等。
### 内部优化
- META标签优化：例如：TITLE，KEYWORDS，DESCRIPTION等的优化。
- 内部链接的优化，包括相关性链接（Tag标签），锚文本链接，各导航链接及图片链接。
- 网站内容更新：每天保持站内的更新(主要是文章的更新等)。
- 网站主页唯一性，网站内页链向主页，301，404等改进。
- 建立网站地图sitemap，同时把网站地图的链接放在首页上。
- 每个网页最多距离首页三次点击就能到达。
- 网站的导航系统最好使用文字链接。
### 外部优化
- 尽量保持外部链接的多样性。
- 每天添加一定数量的外部链接，使关键词排名稳定提升。
- 与一些和你网站相关性比较高，整体质量比较好的网站交换友情链接，巩固稳定关键词排名。

----------

## amd、cmd、es6的模块特点和区别

## 异步编程的几种方式

## 前端工程化技术，如何实现自动化增量部署

## 前端优化
### 代码优化
### 网站性能优化
CDN加速
Lazy load
缓存
HTTP2.0
## 移动端适配

## Backbone.js
***Backbone.js***：前端框架（MVC）。

**Model：**
- 组织数据和业务逻辑
- 和数据库交互
- 数据变化时触发事件

Model可复用，可以在app中传递。

**View：**
- 监听数据变化和重新渲染页面
- 处理用户的输入和交互
- 发送捕捉的输入到Model

View是一块独立的UI，从一个或多个models中渲染数据，也可以不需要数据。Models应该不感应views的变化，相反，views监听model的变化，重新渲染页面或者作出适当的反应。

**Collection：**

Collection帮助处理一组相关的models，加载和保存新的models到服务器，提供models集成和计算的方法。除了models自己的事件之外，collections可以集中代理models的所有事件。如图所示：

![](/image/collection.png)

----------

## 🤜 Node.js初探（一）
