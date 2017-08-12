## post和get的区别

## HTTP和HTTPS
### HTTP升级为HTTPS需要哪些操作

## HTTP缓存机制

## HTTP/2介绍

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
2. 通过“URL的首部”来识别是否同域，而不会去尝试判断相同的ip地址对应着两个域或两个域是否在同一个ip上
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