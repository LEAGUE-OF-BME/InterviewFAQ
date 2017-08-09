## IE盒模型和标准盒模型
### 标准盒模型
![](https://mdn.mozillademos.org/files/13647/box-model-standard-small.png)
width和height只包含content。

在IE中使用标准盒模型：
1. 添加文档声明 < !DOCTYPE html >
2. < meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" >

### IE盒模型
![](https://mdn.mozillademos.org/files/13649/box-model-alt-small.png)
width和height包含content、padding和border

在非IE中使用IE盒模型：在CSS中设置box-sizing属性为border-box（默认是content-box）

**最佳实践：**
```css
box-sizing: border-box;
-moz-box-sizing: border-box;
-webkit-box-sizing: border-box;
```
这样可以多浏览器兼容，保持一致。

----------
Geeook 于 2017/8/9 21:45:13 