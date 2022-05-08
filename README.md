# Readme
## 文件介绍
`connect_with_page.py`文件在运行的时候会弹出浏览器窗口</br>
`connect_without_page.py`文件在运行的时候不会弹出浏览器窗口
`run.exe`文件可以直接运行,下面分别介绍

## py文件的前置条件
### python运行环境
自行下载python运行环境
### 下载第三方库

```
pip install -r .\requirements.txt
```

### 下载浏览器驱动(支持Chrome,Firefox)
[Chrome](http://chromedriver.storage.googleapis.com/index.html)
[Firefox](https://github.com/mozilla/geckodriver/releases)
下载时记得核对自己浏览器和浏览器驱动版本
建议选择Chrome,代码在Chrome爬取时使用了CDP,能一定程度上反屏蔽

### 添加系统路径
在代码运行时需要寻找对应驱动,因此记得将内核的地址放在环境变量中
这里特别推荐将内核放入Python的Scripts文件夹中,这样就可以不用在环境变量中特别增加关于内核的变量,效果如下:
![图 1](../images/f219870bcdc39f63b8922ab54183bb61f33b092ad463181ccaf1157c589fb19c.png)  

### 修改Config
进入代码的Config区域,修改对应的Config
```
###CONFIG
username = ""
password = ""
typeOfDriver = "Firefox" ##Firefox Edge Chrome
url = "https://gw.buaa.edu.cn/srun_portal_pc?ac_id=1&theme=buaa"
### END CONFIG
```
### 运行
需要手动运行py文件,每次联网较为麻烦,可手动打包为`exe`文件

## exe文件的前置条件
### 修改Config
进入config.json文件，修改对应的值
```json
{
    "username":"", //input username
    "password":"", //input passw
    "typeOfDriver":"Chrome"  //input Chrome of Firefox
}
```
### 运行
点击`exe`文件即可运行,也可以加入开机启动项,每次打开电脑就连上校园网.

## 结束语
代码编写仓促,如有bug,请联系作者