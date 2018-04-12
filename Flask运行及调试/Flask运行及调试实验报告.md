# Flask运行及调试实验报告
本实验通过一个小小的应用来对flask的功能进行演示

## 1. 代码
一个最小的flask应用看起来是这样的：
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
```

这段代码做了以下几个事情：
1. 导入了类Flask，这个类的实例是WSGI应用；
2. 创建了一个Flask类的实例。
3. 使用装饰器route()告诉Flask那个URL才能触发下边的函数hello_world()，在本例中，这个URL是"http://127.0.0.1:5000"，可能是它默认的，并且只能在自己的计算机上访问，想要让服务器对外可用，需要关闭debug，并且在run()中添加host，即类似run(host = '0.0.0.0')。
4. 定义一个函数，这个函数名是给特定函数生成URLs，并且返回我们想要显示在用户浏览器上的信息。
5. 使用run()来启动应用。

由此可见，Flask类的实例能够创建一个Web应用。正如实验中介绍的：**Flask是一个轻量级Web应用框架**。我们可以通过调用Flask类来构造一个Web应用。

## 2. 练习
开发一个小应用，URL地址输入http://127.0.0.1:5000/shiyanlou，输出"fuck shiyanlou"
```python
## 导入Flask类并构造一个实例
from flask import Flask
app = Flask(__name__)

## 输入http://127.0.0.1:5000 时让屏幕上显示Hello World
@app.route('/')
def hello_world():
    return "Hello fucking world!"

## 输入http://127.0.0.1:5000/shiyanlou 时让屏幕上显示Hello shiyanlou
@app.route('/shiyanlou')
def hello_shiyanlou():
    return "Oh you fucking asshole! Fucking shiyanlou!"

## 运行
if __name__ == '__main__':
    app.debug = False
    app.run()
```