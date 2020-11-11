print('Python 中有3个重要的基本输入，输出函数，用于输入，转换和输出。 分别是 input(), eval(), print()')

# print() 作用 有3中用法
#   1. 仅用于输出字符串  print('hello world')
#   2. 用于输出一个或多个变量 print(name,age)
#   3. 用于混合输出字符串与变量值 print('hello'.format(name,age))
age: int = 28
name: str = 'Jason'
print('my name is {}, and my age is {}'.format(name,age))

# input() 函数
#   作用： 从控制台获得用户的一行输入，无论用户输入什么内容， input() 函数都以字符串类型返回
#yourname = input('please input your name')
#print(yourname)

# eval(字符串) 函数
#   作用： 用来执行一个字符串表达式，并返回表达式的值
#    eval() 函数通常和input()函数一起使用，用来获取用户输入的数字
num = 3
res = eval('2 * num')
print(res)

# 字符串
# 字符串的切片
# 字符串的两种序号体系
#   反向递减序号 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
#   反向递增序号 0 1 2 3 4 5 6 7 8 9 10
#   可以采用 [n : m] 格式来获取字符串的子串，这个操作被形象的称为切片。 【n : m】获取字符串中从 n 到 m （不包含m）间连续的子字符串
string = '对酒当哥，人生几何'
# len() 函数获取字符串的长度，一个中文字符和西文字符的长度为1
print(len(string))
print(string[4:5])

# 交换ab的值
a,b = 1,2
print(a,b)
a,b = b,a
print(a,b)

################# num
# python提供了3中数字类型  整数类型， 浮点数类型，复数类型
# 浮点数
num_float = 100.0
print(num_float)
# 用来计算 x^y 的值
print(pow(2,3))
# 浮点数中的特殊问题
print(0.1+0.2) # 0.30000000000000004
# 如何解决不确定尾数的问题？
# round(x,d) 作用： 对 x 进行四舍五入，其中参数 d 指定保留的小数位数
print(round((0.1+0.2),1))
print(round(1.23456,3)) # 1.235  四舍五入了

### 复数类型
#   python中，复数可以看做是二元有序实数对(a,b),表示为：a + bj, 其中，a 是实部，b 是虚部。
#             虚部通过后缀 'j'或 'J'表示。需要注意，当b为1时，1不能省略，即 1j 表示复数
#
#             复数类型中实部和虚部都是浮点类型，对于复数 z，可以用 z.real 和 z.imag 分别获得它的实数部分和虚数部分
z = 11.3 + 3j
print('实部：',z.real)
print('虚部：',z.imag)

### 数字运算
# 数值运算操作符
#   x // y : x 与 y 的整数商， 即： 不大于 x与y的商的最大整数
print(2 // 4) # 2/4原始结果为0.5  所以小于0.5的最大整数是0
#   x % y 求余
#   x**y    x的y次幂 即：x^y
print(2**3)

# python 解释器提供了一些内置函数，在这些函数中有6个函数与数值运算相关
#   abs(x) : 求x的绝对值
#   divmod(x,y) : (x//y,x%y),输出为二元数组形式（也称为元组类型）
#   pow(x,y)
#   round(x,d)
#   max(x1,x2,...)
#   mix(x1,x2,...)
print(divmod(2,3))

### 函数  使用 def 关键字来定义函数
def sum(a,b) :
    return a + b

print(sum(1,2))

def fact_1() :
    for i in range(4) :
        print('hello world')

fact_1()

#### 组合数据
# 常用的组合数据类型有 3大类
# 集合类型： 是一个元素集合，元素之间无序，相同元素在集合中唯一存在。 集合 set （和数学里面的集合概念类似）
# 序列类型： 是一个元素向量，元素之间存在先后顺序，通过序号访问，元素之间不排他。序列类型的典型代表是字符串 str，list，tuple
# 映射类型： 是 "键值" 数据项的组合，每个元素是一个键值对，表示为（key，value）。映射类型的典型代表是字典 dict

## 栗子
# 集合{},没有索引和位置的概念，使用 set()函数将其他的组合数据类型变成集合类型
s = {1010,'def','123',78.9}
print(s)
# 差集(-)，交集(&)，补集(^)，并集(|)
s1 = {1010,'python',78.9}
s2 = {1010,'set',12.3,1010}
print('s1 :',s1)
print('s2 :',s2)
print('差集：',s1 - s2) # 返回一个新集合包括在集合s1中，但不包括集合s2中的元素
print('交集：',s1 & s2) # 返回一个新集合包括同时在s1和s2中的元素
print('补集：',s1 ^ s2) # 返回一个新集合包括集合s1和s2中非共同元素
print('并集：',s1 | s2) # 返回一个新集合包括集合s1和s2中所有的元素
# 集合常用的操作函数和方法
# s.add(x)
# s.remove(x)
# s.clear()
# len(s)
# x in s
# x not in s

# 列表类型[],列表没有长度，元素类型可以不同。 通过 list()函数将集合或字符串类型转换成列表类型
#       列表属于序列类型，所以列表类型支持序列类型对应的操作
list1 = [1,2,3,4,'list']
list2 = ['jason','angel',100,101,'python']
print('list : ',list1)
print(list(s1))
name = 'jason'
print(list(name))
## list 通用的操作符合函数
# x in list
# x not in list
# list1 + list2 : 连接list1和list2
# list * n 或 n * list : 将list复制n次
# list[i]
# list[i:j] ： 切片，返回包含序列list第i到j个元素的子序列，不包含j个元素
# list[i:j:k] : 步骤切片，返回包含序列list第i到j个元素，以k为步长的子序列
# len(list)
# min(list)
# max(list)
# list.index(x) : 序列list中第一次出现元素x的位置
# list.count(x) : 序列list中出现元素x的总次数
print(list1 + list2)
print(list1.index('list'))
print(list2.count(100))

## 列表的操作方法
# list.append(x) : 在list最后增加一个元素
# list.insert(i,x) ： 在list第i位置增加元素x
# list.clear()
# list.pop(i) : 将list中第i项元素取出并删除该元素
# list.remove(x) : 将list中出现的第一个元素x删除
# list.reverse() : list中元素反转
# list.copy() : 生成一个新的列表，复制list中所有的元素
list1.append('haha')
print(list1)
list2.insert(1,'hehe')
print(list2)
print(list1.pop(0))
print(list1)
list3 = list2.copy()
print(list2 == list3)

# 可以使用 Python 中保留字 del 对列表元素或片段进行删除
print(list3)
del list3[1]
del list3[1:3]
print(list3)

### 元组与列表类似，不同之处在于元组的元素不能修改。元组使用小括号(),列表使用方括号[]
touple_1 = (1,2,3)
# 获取元组里面的元素
print(touple_1[0])
print(touple_1[1])
print(touple_1[2])
# 元组不能被修改，如果修改了的话会报下面的异常
# touple_1[0] = 2 # TypeError: 'tuple' object does not support item assignment

### 字典使用大括号{} 建立，每个元素是一个键值对。
# 大括号表示集合，所以字典类型也具有和集合类似的性质，即键值对之间没有顺序且不能重复
dict_1 = {'name' : 'jason','age' : 28,'address':'shanghai'}
print(dict_1)
# 获取字典里面的值
print(dict_1['name'])
print(dict_1['age'])
# 修改字典
dict_1['name'] = 'angel'
print(dict_1)
## 字典的操作函数
# len(dic)
# min(dic)
# max(dic)
# dict() : 生成一个空字典

## 字典类型常用的操作方法
# dic.keys()
# dic.values()
# dic.items()
# dic.get(key,default) : 键存在则返回相应的值，否则返回默认值
# dic.pop(key,default) : 键存在则返回相应的值，同时删除键值对，否则返回默认值
# dic.popitem() : 随机从字典中取出一个键值对，以元组(key,value)形式返回
# dic.clear()
print(dict_1.keys())
print(dict_1.values())
print(dict_1.items())
print(dict_1.get('name'))
print(dict_1.get('age'))
# print(dict_1.pop('age')) # 返回值 并删除键值对
print(dict_1)
print(dict_1.popitem())


### 文件的使用
## 文件两种类型
# 文本文件 ： 由单一特定编码的字符组成 eg ： txt 文件
# 二进制文件： 二进制文件直接由比特0 和 比特1 组成，文件内部数据的组织格式与文件用途有关
# Python 对文本文件和二进制文件都有统一的操作步骤， 即 "打开----操作----关闭"
# 操作文件流程：
#   1. 打开文件
#   2. 读取文件、写入文件、删除文件、修改文件
#   3. 关闭文件

# 内置函数 open() 可以用指定模式打开指定文件并创建文件
# 使用方法 : 变量名 = open(文件路径及文件名，模式)
# 模式:
    # r : 只读模式，如果文件不存在，返回异常 FileNotFoundError,默认值
    # w : 覆盖写模式，文件不存在则创建，存在则完全覆盖源文件
    # x : 创建写模式，文件不存在则创建，存在则返回异常 FileExistsError
    # a : 追加写模式，文件不存在则创建，存在则在源文件最后追加内容
    # b : 二进制文件模式
    # t : 文本文件模式，默认值
    # + : 与 r / w / x / a 一同使用，在原功能基础上增加同时读写功能
# 打开模式中，'r'、'w'、'x'、'a' 可以和 'b'、't'、'+' 组合使用，形成既表达读写又表达文件模式的方式。
# 文件使用结束后要用 close()方法关闭，释放文件的使用授权

### 文件读写
# 假如文件变量为 f
# f.read(size=-1): 从文件中读入整个文件内容
#   参数可选，如果给出则读入前 size 长度的字符串或字节流。其结果是一个字符串

# f.readline(size=-1): 从文件中读入一行内容
#   参数可选，如果给出，读入该行前 size 长度的字符串或字节流。 其结果是一个字符串

# f.readlines(hint=-1): 从文件中读入所有行，以每行为元素形成一个列表
#   参数可选，如果给出，读入 hint 行

# 文件打开后，对文件的读写有一个读取指针，当文件中读入内容后，读取指针将向前进再次读取的内容将从指针的新位置开始
# f.seek(offset): 改变当前文件操作指针的位置。
# offset 的取值   0 : 文件开头  2 ： 文件末尾

### 文件写入
# f.write(s): 向文件写入字符串s，每次写入后，将会记录一个写入指针。该方法可以反复调用，将在写入指针后分批写入内容，直至文件关闭
# f.writelines(lines): 直接将列表类型的各元素连接起来写入文件f。
# 文件路径： 相对路径、绝对路径

# f = open('/Users/yuwenbin/Documents/jason/python/files/jason.txt','w')
#f = open('../files/jason.txt','r+')
#f.write('hello python')
#print(f.read())

# 循环读取文件内容
# for line in f :
#     print(line)

# f.write('i love angel \n')
# f.write('angel loves jason')
# list4 = ['1','2','3','4']
# f.writelines(list4)

# f.close()


### .csv 格式的文件
# 一种通用的，相对简单的文件格式，存储的文件一般采用 .csv 为扩展名。
# 一维数据保存为 csv 格式后，各元素采用逗号分隔，形成一行，这里的逗号是英文逗号。
# 在商业和科学上广泛应用，大部分编辑器都支持直接读入或保存为csv格式


### 一维数据的读写
# 写入文件
# list5 = ['Shanghai','Beijing','Manila','Pasig']
# f = open('../files/jason.csv','w')
# f.write(','.join(list5)+'\n')
# f.close()

# 读取文件内容
# f = open('../files/jason.csv','r')
# list6 = f.read().strip('\n').split('.') # 这里以列表的形式返回
# f.close()
# print(list6)


### 二维数据的读写
## 二维数据的写入
# list7 = [
#     ['Shanghai','Beijing','Tianjin'],
#     ['Anhui','Hunan','Zhejiang']
# ]
# f = open('../files/jason.csv','w')
# for row in list7 :
#     f.write(','.join(row)+'\n')
#
# f.close()

## 二维数据的读取
f = open('../files/jason.csv','r')
list8 = []
for line in f :
    list8.append(line.strip('\n').split(','))

f.close()
print(list8)

#### 面向对象
# 类 继承 导入类

## 创建一个Car 类
class Car() :
    """ 类的文档说明 : 汽车目前价值估计程序 """
    def __init__(self,make,model,year): ## self 必不可少，且必须位于其他形参前面
        ## 可通过对象访问的变量称为属性
        self.make = make
        self.model = model
        self.year = year
        self.current_year = 2018 # 设置默认值， 如果外面没有修改这个值，默认是2018

    # 通过方法来修改默认值
    def update_year(self,new_year):
        self.current_year = new_year

    def detection(self):
        duration = self.current_year - self.year
        price = 30 - 2 * duration
        long_name = '你的' + self.make + self.model + '到目前已经行驶了' + str(duration) + '年' + '目前价值' + str(price) + '万'
        return long_name

## 实例化car对象
my_car = Car('Audi','A6',2013)
print(my_car.year)
#my_car.current_year = 2020 # 这里修改了默认值
my_car.update_year(2020)
result = my_car.detection()
print(result)

your_car = Car('BMW','c300',2014)
print(your_car.year)
print(your_car.detection())

### 类的继承， 在 python里面 父类要位于子类的前面（同一个文件）
# 创建一个子类
class ElectricCar(Car):

    def __init__(self,make,model,year): # 子类的构造函数中需要和父类的构造函数中的参数相同
        # super 函数将父类和子类关联起来。 让 python 调用 ElectricCar 的父类的方法 __init__()
        super().__init__(make,model,year)

    # 子类特有的方法
    def battery(self,capacity):
        self.capacity_num = capacity
        print('您选择的电池容量为：',self.capacity_num,'kwh')

    # 重写父类的方法
    def detection(self):
        duration = self.current_year - self.year
        price = 30 - duration - (500 / self.capacity_num)
        long_name = '你的' + self.make + self.model + '到目前已经行驶了' + str(duration) + '年' + '目前价值' + str(price) + '万'
        return long_name


## 实例化汽车对象
my_tesla = ElectricCar('tesla','s',2017)
print(my_tesla.battery(200))
print(my_tesla.year)
print(my_tesla.detection())

### python 类的引入
# python 中四种 import
# 1. from 模块名 import 类名  eg: from car_file import Car
# 2. 也可以一个模块中一次性导入多个类 eg: from car_file import Car, ElectricCar
# 3. import 模块名（导入整个模块，在使用过程中需要以句点的形式访问模块中的类 eg ： car_file.Car, car_file.ElectricCar）
# 4. 导入模块中的所有类   from 模块名 import *


##### python 中库的使用（标准库 和  三方库）

## 标准库 time库、random库、turtle库
## import time
## import random
## import turtle

# time 库
# time库是python提供的处理时间标准库。 time 库提供系统级精确计时器的计时功能，
#   可以用来分析程序性能，也可以让程序暂停运行时间
# time 库的功能主要分为 3 个方面：
#   1. 时间处理
#   2. 时间格式化
#   3. 计时
# 常用方法：
#   时间处理：
#   time.time() : 获取当前时间戳。当前时间与1970年1月1日0时0分0秒的时间差（以秒为单位）
#   time.gmtime() ： 获取当前时间戳对应的 struct_time 对象
#   time.localtime()：获取当前时间戳对应的本地时间的 struct_time 对象。 注意结果与 gmtime 的区别，UTC 时间以自动转化为北京时间
#   time.ctime()：获取当前时间戳对应的易读字符串表示，内部会调用 time.localtime() 函数以输出当地时间
#
#   时间格式化：
#   time.mktime(t)：函数将 struct_time 对象 t 转换为时间戳，注意 t 代表当地时间
#   time.strftime(t)：该方法利用一个格式字符串，对时间格式进行表达
#   time.strptime()：与 strftime() 方法完全相反，用于提取字符串中时间来生成 struct_time 对象，可以很灵活的作为 time 模块的输入接口
#
#   计时：
#   time.sleep()：推迟调用线程的运行，可通过参数 secs 指定秒数，表示进程挂起(睡眠)的时间
#   time.monotonic()：
#   time.perf_counter()：返回一个性能计数器的值(在分秒内)，即一个具有最高可用分辨率的时钟，以测量短时间
import time # 引入time库

## 时间戳处理函数
# 获得当前时间戳
print(time.time())
# 获取本地时间，以全球时间为标准
print(time.gmtime())
# 获取本地时间 以北京时间为标准
print(time.localtime())
# 以易读字符串的形式显示时间，内部会调用time.localtime()函数
print(time.ctime())

## 时间格式化函数
# 将 struct_time 对象转换为时间戳
localtime = time.localtime()
print(time.mktime(localtime))
# time.strftime()函数是时间格式化最有效的方法，几乎可以以任何通用格式输出时间。该方法利用一个格式字符串，对时间格式进行表达
print(time.strftime('%Y-%m-%d %H:%M:%S',localtime))
# time.strptime()方法与 time.strftime() 方法完全相反，用于提取字符串中时间来生成 struct_time 对象
#timeString = '2020-11-11 10:45:10'
#print(time.strptime(timeString,'%Y-%m-%d %H:%M:%S'))
timeString = '2020-11-11'
print(time.strptime(timeString,'%Y-%m-%d')) # 这里的格式要与定义的字符串格式一一对应

## 计时

# 获取时间差
# start_time = time.time()
# time.sleep(2)
# last_time = time.time()
# print(last_time-start_time)

# time.perf_counter() 可以用来计算时间差
time1 = time.perf_counter()
time2 = time.perf_counter()
print(time1,time2)

## 模拟进度条显示
scale = 50
print('------------程序开始执行')
start_time = time.perf_counter()
for i in range(scale + 1) :
    a = '*' * i
    b = '.' * (scale - i)
    c = (i / scale) * 100
    dur = time.perf_counter() - start_time
    print('\r{:^3.0f}%[{}->{}]{:.2f}s'.format(c,a,b,dur),end='') # \r 表示将光标的位置回退到本行的开头位置
    time.sleep(0.02)
print('\n------------程序结束')



# random 库
# 使用 random 库主要目的是生成随机数
# 常用函数
# random()：生成一个 [0.0,1.0]之间的随机小数
# seed(a=None)：初始化随机数种子，默认值为当前系统时间
# randint(a,b)：生成一个[a,b]之间的整数
# randrange(start,stop,[step])：生成一个[start,stop]之间以step为步长的随机整数
# uniform(a,b)：生成一个[a,b]之间的随机小数
# choice(seq)：从序列类型(如列表)中随机返回一个元素
# shuffle(seq)：将序列类型中元素随机排列，返回打乱后的序列
# sample(pop,k)：从 pop 类型中随机选取 k 个元素，以列表类型返回
import random # 引入random 库
# print(random.random())
# print(random.seed())
# print(random.randint(0,10))
# print(random.randrange(1,20,2))
# print(random.uniform(10,20))
# print(random.choice([1,2,3,4]))
# list9 = [1,2,3,4,5,6]
# print(list9)
# random.shuffle(list9)
# print(list9)
# print(random.sample(list9,3))

# turtle 库
# turtle 库是能够进行基本的图形绘制的标准库
# turtle 库包含100多个功能函数，主要包括3类：
#   1.窗体函数
#   2.画笔状态函数
#   3.画笔运动函数
#
#   turtle库绘制图形基本框架：
#   一个小海龟在坐标系中爬行，其爬行轨迹形成了绘制图形。对于小海龟来说，有"前进"、"后退"、"旋转"等爬行行为，对坐标系的探索
#   也通过"前进方向"、"后退方向" 和 "右侧方向" 等小海龟自身角度方位来完成

## 窗体函数
#   turtle.setup(width,height,startx,starty)
#   作用：设置主窗体的大小和位置
#   参数说明：
#   width : 窗口宽度，如果是整数值，表示像素值，如果是小数，表示窗口宽度与屏幕的比例
#   height : 如果是整数值，表示像素值，如果是小数，表示窗口高度与屏幕的比例
#   startx : 窗口左侧与屏幕左侧的像素距离，如果值是 None，窗口位于屏幕水平中央
#   starty : 窗口顶部与屏幕顶部的像素距离，如果值是 None，窗口位于屏幕垂直中央
#   需要与 turtle.done() 进行配合

#   画笔运动函数
#   forward()：沿着当前方向前进指定距离
#   backward()：沿着当前相反方向后退指定距离
#   right(angle)：向右旋转angle角度
#   left(angle)：向左旋转angle角度
#   goto(x,y)：移动到绝对坐标(x,y)处
#   setx()：将当前x轴移动到指定位置
#   sety()：将当前y轴移动到指定位置
#   seth(angle)：设置当前朝向为angle角度
#   home()：设置当前画笔位置为原点，朝向东
#   circle(radius,e)：绘制一个指定半径r和角度e的圆或弧形
#   dot(r,color)：绘制一个指定半径r和颜色color的圆点
#   undo()：撤销画笔最后一个动作
#   speed()：设置画笔的绘制速度，参数为0-10之间

#   画笔状态函数
#   pendown()：放下画笔
#   penup()：提起画笔，与 pendown()配对使用
#   pensize(width)：设置画笔线条的粗细
#   color()：设置画笔的颜色
#   begin_fill()：填充图形前，调用该方法
#   end_fill()：填充图形结束
#   filling()：返回填充的状态， True 为填充，False为未填充
#   clear()：清空当前窗口，但不改变当前画笔的位置
#   reset()：清空当前窗口，并重置位置等状态为默认值
#   screensize()：设置画布的长和宽
#   hideturtle()：隐藏画笔的turtle形状
#   showturtle()：显示画笔的turtle形状
#   isvisible()：如果turtle可见，则返回True
import turtle # turtle库的使用

# turtle.setup(600,400)
# jason = turtle.Turtle()
# for i in range(30):
#     jason.forward(i * 15)
#     jason.right(144)
# turtle.done()


### 第三方库
# 常用第三方库
# 网络爬虫：requests, scrapy
# 数据分析：numpy, scipy, pandas
# 文本处理：pdfminer, openpyxl, python-docx, beautifulsoup4
# 数据可视化：matplotlib, TVTK, mayavi
# 用户图形界面：PyQt5, wxPython, PyGTK
# 机器学习：scikit-learn, TensorFlow, Theano
# Web开发：Django, Pyramid, Flask
# 游戏开发：Pygame, Panda3D, cocos2d
# 更多第三方库：PIL, SymPy, NLTK, WeRoBot, MyQR

# 网络爬虫
# 网络爬虫是自动进行HTTP访问并捕获HTML页面的程序
# request库
#   是一个简洁且简单的处理HTTP请求的第三方库。优点：程序编写过程更接近正常URL访问过程，该库建立在 urllib3 基础上

# scrapy库
#   是python开发的一个快速的、高层次的web获取框架。不同于简单的网络爬虫功能，
#   scrapy框架本身包含了成熟网络爬虫系统所应该具有的部分共用功能，它是一个半成品，任何人都可以根据
#   需求方便的利用框架已有的功能经过简单扩展实现专业的网络爬虫系统

# 数据分析
# numpy库
#   是一种开源数值计算扩展第三方库，用于处理数据类型相同的多维数组，可以用来存储和处理大型矩阵，
#   比python语言提供的列表要高效得多
# scipy库
#   是一款方便、易用、转为科学和工程设计的python工具包，它是在numpy库的基础上增加了众多的数学、科学以及工程计算中常用的库函数
# pandas库
#   pandas是基于numpy扩展的一个重要第三方库，pandas最初被作为金融数据分析工具而开发

# 文本处理
# pdfminer库
#   是一个可以从PDF文档中提取各类信息的第三方库，能够完全获取并分析PDF的文本数据，并且获取PDF中文本的准确位置、字体、行数等信息
# openpyxl库
#   是一个处理Excel文档的python第三方库
# python-docx库
#   是一个处理word文档的python第三方库
# beautifulsoup4库
#   用于解析HTML和XML

# 数据可视化
# 数据可视化是指根据数据特点将其展示位易于理解的图形过程。
# matplotlib库
#   主要进行二维图标数据展示，广泛用于科学计算的数据可视化
# TVTK库
#   是一个开源、跨平台、支持平行处理的图形应用函数库，它是专业可编程的三维可视化工具
# mayavi库
#   在VTK基础之上开发的，可以更为方便开发实用的三维可视化工具

# 用户图形界面
# python标准库内置了一个GUI库(Tkinter),但过于陈旧，开发控件也很有限。
# PyQt5库
#   它有超过620个类和近6000个函数和方法。它是python中最为成熟的商业级第三方库，可以在Windows、Linux和macOS 等操作系统上跨平台使用
# wxPython库
#   可以轻松的创建健壮可靠、功能强大的图形用户界面
# PyGTK库
#   PyGTK具有跨平台性，利用它编写的代码能够不加修改的稳定运行在各个操作系统中

# 机器学习
# 机器学习是人工智能领域的一个重要分支，python也是机器学习和人工智能的重要基础语言
# scikit-learn库
#   是一个简单高效的数据挖掘和数据分析工具，基于numpy、scipy 和 matplotlib库构建，专门针对机器学习应用而发展起来
#   的一款开源框架，基本功能包括：分类、回归、聚类、数据降维、模型选择和数据预处理
# TensorFlow库
#   是谷歌基于DistBelief进行研发的第二代人工智能学习系统，也是用来支撑AlphaGo系统的后台框架。应用十分广泛，
#   从语音识别或图像识别到机器翻译或自动跟踪等，既可以运行在万台服务器的数据中心，也可以运行在智能手机或嵌入式设备中。
# Theano库
#   为执行深度学习中大规模神经网络算法的运算而设计，擅长处理多维数组，偏向底层开发

# web开发
# Django库
#   Diango是python生态中最流行的开源web应用框架。提供了开发网站经常用到的模块，
#   Django的开发理念鼓励快速开发，减少程序员建立一个高性能web应用所花费的时间和精力，形成一站式解决方案
# Pyramid库
#   是一个通用、开源的python web 应用程序开发框架，让python开发者更简单的创建web应用。
#   相比 Django 是一个小巧、快速、灵活的开源python web框架
# Flask库
#   是轻量级web应用框架，相比 Django 和 Pyramid,它也被称为微框架。使用Flask开发web应用十分方便，甚至几行代码即可建立一个小型网站

# 游戏开发
# Pygame库
#   是面向游戏开发入门的第三方库，除了制作游戏外，还用于制作多媒体应用程序
# Panda3D库
#   是一个开源、跨平台的3D渲染和游戏开发库，简单说，它是一个3D游戏引擎，支持Python和C++两种语言
# cocos2d库
#   是一个构建2D游戏和图形界面交互式应用的框架，能够利用GPU进行加速



























