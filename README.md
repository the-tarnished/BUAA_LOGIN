# Readme
## 文件介绍
`connect_with_page`文件在运行的时候会弹出浏览器窗口</br>
`connect_without_page`文件在运行的时候不会弹出浏览器窗口

请自行选择合适的文件
## 前置条件
### python运行环境
自行下载python运行环境
### 下载第三方库

```
pip install -r .\requirements.txt
```

### 下载浏览器驱动(支持Edge,Chrome,Firefox)
[Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
[Chrome](http://chromedriver.storage.googleapis.com/index.html)
[Firefox](https://github.com/mozilla/geckodriver/releases)
下载时记得核对自己浏览器和浏览器驱动版本
建议选择Chrome,代码在Chrome爬取时使用了CDP,能一定程度上反屏蔽

### 添加系统路径
在代码运行时需要寻找对应驱动,因此记得将内核的地址放在环境变量中
这里特别推荐将内核放入Python的Scripts文件夹中,这样就可以不用在环境变量中特别增加关于内核的变量,效果如下:
![图 1](../images/f219870bcdc39f63b8922ab54183bb61f33b092ad463181ccaf1157c589fb19c.png)  


## 修改Config
进入代码,Config区域中有
```python
###CONFIG
username = ""
password = ""
typeOfDriver = "Firefox" ##Firefox Edge Chrome
url = "https://gw.buaa.edu.cn/srun_portal_pc?ac_id=1&theme=buaa"
### END CONFIG
```
修改对应的`username`,`password`即可

## 结束语
代码编写仓促,如有bug,请联系作者