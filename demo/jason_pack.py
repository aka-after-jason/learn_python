### 将源程序打包成可执行文件
# 使用 Pyinstaller 库
import turtle # turtle库的使用

turtle.setup(600,400)
jason = turtle.Turtle()
for i in range(30):
    jason.forward(i * 15)
    jason.right(144)
turtle.done()