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

f = open('/Users/yuwenbin/Documents/jason/python/files/jason.txt','w')
#f = open('../files/jason.txt','r+')
#f.write('hello python')
#print(f.read())

# 循环读取文件内容
# for line in f :
#     print(line)

f.write('i love angel \n')
f.write('angel loves jason')
list4 = ['1','2','3','4']
f.writelines(list4)

f.close()
















