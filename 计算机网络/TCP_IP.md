# TCP/IP

### 1.TCP三次握手、四次挥手

#### tcp三次握手的详细创建过程

[![100327002629](https://www.centos.bz/wp-content/uploads/2012/08/100327002629.png)](https://www.centos.bz/wp-content/uploads/2012/08/100327002629.png)

**第一次握手:**
客户端发送一个TCP的SYN标志位置1的包指明客户打算连接的服务器的端口，以及初始序号X,保存在包头的序列号(Sequence Number)字段里。
[![100327002911](https://www.centos.bz/wp-content/uploads/2012/08/100327002911.png)](https://www.centos.bz/wp-content/uploads/2012/08/100327002911.png)
**第二次握手:**
服务器发回确认包(ACK)应答。即SYN标志位和ACK标志位均为1同时，将确认序号(Acknowledgement Number)设置为客户的I S N加1以.即X+1。
[![100327003054](https://www.centos.bz/wp-content/uploads/2012/08/100327003054.png)](https://www.centos.bz/wp-content/uploads/2012/08/100327003054.png)

**第三次握手：**
客户端再次发送确认包(ACK) SYN标志位为0,ACK标志位为1.并且把服务器发来ACK的序号字段+1,放在确定字段中发送给对方.并且在数据段放写ISN的+1
[![100327003214](https://www.centos.bz/wp-content/uploads/2012/08/100327003214.png)](https://www.centos.bz/wp-content/uploads/2012/08/100327003214.png)

### TCP四次挥手详细过程

[![100327022731](https://www.centos.bz/wp-content/uploads/2012/08/100327022731.jpg)](https://www.centos.bz/wp-content/uploads/2012/08/100327022731.jpg)



### 2.TCP拥塞控制（过程、阈值）



### 3.流量控制与滑动窗口



### 4.TCP与UDP区别



### 5.子网划分



### 6.DDos攻击

