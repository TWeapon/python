# int([x],base=10)
# x:数字或字符串
# base:进制数，默认十进制（当base传参时，x必须为字符串）
# 将x转换为十进制整数并返回，如果没有指定x,则返回0
print(int())  # 0
print(int(3.99))  # 3
print(int("12"))  # 12

# ValueError: 字符串中包含了一个小数点，无法被解释为整数
# print(int("12.1"))

# 将二进制的“101010”转为十进制的整数
print(int("101010", base=2))  # 42
print(int("0b101010", 2))  # 42
# 将八进制的“11”转为十进制的整数
print(int("11", base=8))  # 9
print(int("0o11", base=8))  # 9
# 将十六进制的“3d”转为十进制的整数
print(int('3d', base=16))  # 61
print(int("0x3d", base=16))

# bin(x)/ oct(x) / hex(x)
# 返回整数类型的二进制表示形式（前缀为“0b”）
# 返回整数类型的八进制表示形式（前缀为“0o”）
# 返回整数类型的十六进制表示形式（前缀为“0x”）
num = 47
print(bin(num))  # '0b101111'
print(oct(num))  # '0o57'
print(hex(num))  # '0x2f'
print(int("0b101111", base=2))
print(int("0o57", base=8))
print(int("0x2f", base=16))

# float([x])
# x:数字或字符串
# 将x转换成浮点数并返回，不指定x,则返回0.0
print(float())  # 0.0
print(float(123))  # 123.0
print(float('123'))  # 123.0
print(float('1.23'))  # 1.23
print(float('3.99'))  # 3.99
print(float('-3.99'))  # -3.99
print(float(True))  # 1.0
print(float(False))  # 0.0

# bool([x])
# 根据指定的x,返回布尔值
# 如果没有指定x,则返回False
"""
数字0,0.0,0j,False,
空字符串,空列表,空元组,
空字典,空集合,关键字None
...
以上这些数据bool判定为False
其它通常判定为True
"""
print(bool())  # False
print(bool(0))  # False
print(bool(0.0))  # False
print(bool(0.0))  # False
print(bool(0j))  # False
print(bool(False))  # False
print(bool(''))  # False
print(bool([]))  # False
print(bool(()))  # False
print(bool({}))  # False
print(bool(set()))  # False
print(bool(None))  # False
print(bool(' '))  # True
print(bool('None'))  # True
print(bool('False'))  # True

# complex([real[, imag]])
# 返回一个real+imag*1j的复数
# 如果第一个参数是字符串，它将被解释为复数，此时不能传第二个参数
# 如果没有指定实参，则返回0j
print(complex())  # 0j
print(complex(3.2, 4))  # (3.2+4j)
print(complex(3.2))  # (3.2+0j)
print(complex('3.2'))  # (3.2+0j)
print(complex("3.2+4j"))  # (3.2+4j)

# 字符串（String）
# 特性：不可变，是序列
# 单行字符串：用一对单引号或一对双引号定义
# 多行字符串：用三个单引号或三个双引号定义
s1 = '这是一个单行字符串'
s2 = "这是一个单行字符串"
s3 = '''这是一个单行字符串'''
s4 = """这是一个单行字符串"""
print(s1, s2, s3, s4)
# str(object='')
# 返回object的字符串格式
print(str())  # '' 没有空格字符
print(str(1234))  # '1234'
print(str(-1.23))  # '-123'

# Raw 字符串
# 如果希望字符串中的转义字符不发生转义效果，可以在字符串前面加一个字母r，表示原始字符串

print(R'https:\\www.example.com\nuxy\tngj')

# %格式化
# %s 格式化为字符串
# %d、%i 格式化为十进制整数，仅适用于数字
# %f、%F 格式化为浮点数，默认精确到小数点后六位，仅适用于数字

print('它说它叫%s,今年%d岁,每天睡%f小时！' % ('旺财', 2, 8.5))
# %.nf 表示精确到小数点后n位
print('今天买了%s斤青菜，%s元/斤，花了%.2f元！' % (3.5, 2.59, 3.5 * 2.59))
# format方法格式化
name = '旺财'
age1 = 2
age2 = 3
# 传位置参数，实参按照从左往右的顺序传入占位符{}
print('它说它叫{}，它今年{}岁，它宝宝{}个月了！'.format(name, age1, age2))
# 传关键字参数
print('它说它加{n}，它今年{a1}岁，它宝宝{a2}个月了！'.format(a1=age1, n=name, a2=age2))
# 根据实参的下标传参
print('它说它叫{1}，它今年{0}岁，它宝宝{2}个月了！'.format(age1, name, age2))
# f-string格式化 *********
print(f'它说它加{name}，它今年{age1}岁，它宝宝{age2}个月了！')
print(fr'它说它加{name}，它今年{age1}岁，它宝宝{age2}个月了！')
# {value:.nf} 表示精确到小数点后n位
print(fr'今天买了{3.5}斤青菜，{2.59}元/斤，花了{3.5 * 2.59:.2f}元！')

# 字符串方法
# str.replace(old,new,count=-1)
# old:旧字符串
# new:新字符串
# count:要替换的最大次数，默认不限制替换次数
# 用新字符串替换旧字符串并返回
s = "Line1 Line2 Line4"
# 用“b”替换所有的“Li”
print(s.replace("Li", "b"))
print(s.replace("Li", "b", 2))

# str.strip([chars])
# chars:指定要移除的字符，如果没有指定，则默认移除空白字符（空格符，换行符，制表符）
# 删除字符串左右两边指定的字符

# 删除字符串左右两边指定的字符
str1 = ' \thello wrold h \n'
print(str1.strip())

# 删除字符串两边的‘o’字符
str2 = "ooho hello wrold"
print(str2.strip('o'))

# 删除字符串两边的‘c','w','o','m'
str3 = 'www.example.com'
print(str3.strip("cwom"))

# str.startswith(prefix[,start[,end]])
# prefix:匹配的前缀，可以是字符串或者字符串组成的元组（元组中只要一个元素满足即可）
# start:开始索引，不指定则默认为0
# end:结束索引（开区间），不指定则默认为len(str)
# 判定字符串是否以prefix指定的值开始（start和end参数用来控制字符串的判定区间）
str1 = "hello world"
print(str1.startswith("h"))
print(str1.startswith("he"))
print(str1.startswith("wo"))
print(str1.startswith("wo", 1, 3))
print(str1.startswith(("wo", "h")))  # 元组中只要一个元素满足即可
print('################################')
# str.endswith(suffix[,start[,end]])
# suffix:匹配的前缀，可以是字符串或者字符串组成的元组（元组中只要一个元素满足即可）
# start:开始索引，不指定则默认为0
# end:结束索引（开区间），不指定则默认为len(str)
# 判定字符串是否以suffix指定的值结束（start和end参数用来控制字符串的判定区间）
str1 = "hello world"
print(str1.endswith("d"))
print(str1.endswith("ld"))
print(str1.endswith("lo"))
print(str1.endswith("lo", 1, 5))  # 结尾是开区间
print(str1.endswith(("d", "lo")))  # 元组中只要一个元素满足即可
print('################################')
# str.isdigit()
# 判定字符串中的每个字符是否都为数字型的字符
string = '1234'  # true
print(string.isdigit())

string = '-1234'  # false
print(string.isdigit())

string = '1.234'  # false
print(string.isdigit())

# str.split(sep=None, maxsplit=-1)
# sep:分隔符，不指定时默认所有的空白符（空格、换行、制表符），并丢弃结果中的空字符串
# maxsplit:最大分隔符次数，默认不限制分割次数
# 通过指定的分隔符对字符串进行分割，以列表的形式返回
s = " Line \nLine2    \tLine3"
print(s.split('Li'))
print(s.split(' '))
print(s.split())
print(s.split('Li', 2))

# str.join(iterable)
# iterable:包括string,list,tuple,dict,set等等
# 将可迭代对象中的元素（元素必须是字符串）以指定的字符串连接，返回新的字符串
# iterable里的除最后一个字符外，其余字符每个字符后面都加上str
s = '-.'
s1 = 'hello world'
print(s.join(s1))  # h-.e-.l-.l-.o-. -.w-.o-.r-.l-.d
s2 = ['1', '2', '3', '4']
print(s.join(s2))  # 1-.2-.3-.4
s3 = ('1', '2', '3', '4')
print(s.join(s3))  # 1-.2-.3-.4
print('##########################')
# 字典作为iterable，只有键参与迭代
s4 = {'height': 175, 'weight': 65}
print(s.join(s4))
s5 = {'5', 'hello', '789', 'world'}
print(s.join(s5))
print('##########################')
# str.count(sub,[start[,end])
# sub:需要查找的字符串
# start:开始索引，默认为0
# end:结束索引（开区间），默认为len(str)
# 返回sub在字符串中出现的非重叠的次数
s = "hello world"
print(s.count('l'))
print(s.count('l', 3))
print(s.count('l', 3, 6))
print(s.count('l', 4, 6))
print('##########################')
# str.find(sub[,start[,end]])
# 返回从左边开始第一次找到指定字符串时的正向索引，找不到就返回-1
# str.rfind(sub[,start[,end]])
# 返回从右边开始第一次找到指定字符串时的正向索引，找不到就返回-1
# str.index(sub[,start[,end]])
# 返回从左边开始第一次找到指定字符串时的正向索引，找不到就报错
# str.rindex(sub[,start[,end]])
# 返回从右边开始第一次找到指定字符串时的正向索引，找不到就报错
# sub:需要查找的字符串
# start:开始索引，默认为0
# end:结束索引（开区间），默认为len(str)
s = 'hello world'
print(s.find('l'))  # 2
print(s.rfind('l'))  # 9
print(s.find('lo'))  # 3
print(s.rfind('lo'))  # 3

print(s.index('l'))  # 2
print(s.rindex('l'))  # 9
print(s.index('lo'))  # 3
print(s.rindex('lo'))  # 3

print(s.find('ol'))  # -1
print(s.rfind('ol'))  # -1

print('##########################')
s = '你好hELlo wo?rLD世界TuP'
# 将字符串的首字母变成大写，其他字母变小写，并返回
print(s.capitalize())  # 你好hello wo?rld世界tup
# 将字符串中所有单词的首字母变成大写，其他字母变小写，并返回
print(s.title())  # 你好Hello Wo?Rld世界Tup
# 将字符串中所有字符变成大写，并返回
print(s.upper())  # 你好HELLO WO?RLD世界TUP
# 将字符串中所有大写字符变成小写，小写字符变大写，并返回
print(s.swapcase())  # 你好HelLO WO?Rld世界tUp

# 列表
# 特性：可变、是序列
# 列表用方括号定义，元素没有类型限制

list0 = []
list1 = ['China', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
list4 = ["red", "green", "blue", "yellow", "white", 'black']

# 修改列表
# 列表是可变的，可以通过索引和切片的方式来对列表的元素重新赋值
lst = [567, 'hello', 78.9, 'world', False]
"""
针对一个元素：
格式：lst[index] = object
"""
lst[2] = 9.87
lst[3] = 'dlrow'
print(lst)

"""
针对多个元素：
格式： lst[start:end:step]=iterable
"""

# 1 vs 1
lst[2:3] = [9.87]
# n vs n
lst[2:4] = [9.87, 'dlrow']

# step 为1，可以 1 vs n

lst[2:3] = [7, 8, 9]

# step为1，可以 n vs m
lst[2:4] = [1, 2, 3]
lst[1:4] = [1, 2]

# step为1,可以1 vs 0
lst[2:3] = []

# step为1，可以 n vs 0

lst[1:4] = []

# step不为1，只能n vs n
# lst[1::2] = ['a', 'b']

# 插入一个元素
lst[0:0] = ['a']
lst[1:1] = ['b']
lst[len(lst):] = ['c']

# 插入多个元素
lst[0:0] = ['a', 'b', 'c']
lst[1:1] = ['d', 'f']
lst[len(lst):] = ['x', 'y', 'z']
print(lst)

# list([iterable])
# 将一个iterable对象转化为列表并返回，如果没有实参，则返回空列表
print(list())
print(list("hello"))
print(list((1, 2, 3)))

# 字典作为一个iterable,只有键参与迭代
print(list({1: 2, 3: 4}))
print(list({'a', 'b', 'c', 789, 456}))

# list.append(object)
# 往列表中追加一个元素，无返回值，相当于lst[len(lst):]=[object]
lst = [1, 2, 3]
lst.append(4)
print(lst)
lst.append([5, 6])
print(lst)
# list.extend(iterable)
# 使用iterable中的所有元素来扩展列表，无返回值，相当于lst[len(lst):]=iterable
lst = [1, 2, 3]
lst.extend([5, 6])
print(lst)

# list.insert(index,object)
# index:要插入元素的位置
# object:要插入的元素
# 在指定位置插入一个元素，无返回值
lst = [1, 2, 3, 4]
lst.insert(1, ['a', 'b'])
print(lst)

# list.sort([key],reverse = False)
# key:指定一个函数，在排序之前，列表每个元素先应用这个函数
# 再根据函数的返回值对原数据进行排序
# reverse:默认为False,代表升序，指定为True则为降序
# 对原列表进行排序，无返回值
lst = [1, 2, -5, -3]
# 升序排序
lst.sort()
print(lst)  # [-5, -3, 1, 2]

lst = [1, 2, -5, -3]
lst.sort(reverse=True)  # [2, 1, -3, -5]
print(lst)

# chr(i) 返回Unicode码位为指定整数的字符
# ord(c) 返回指定字符对应的Unicode码位
print(chr(97))  # a
print(ord('a'))  # 97

# 字符串在大小比较时是逐个字符进行比较的
# 根据字符在编码表里的位置
lst = ['10', '2', '1', '-3', '101']
print(ord('1'))  #
print(ord('2'))  #
print(ord('1'))  #
print(ord('-'))  #
print(ord('1'))  #
print(ord('0'))  #

lst.sort()
print(lst)

# abs(number) 内置函数，返回number的绝对值
print(abs(9))
print(abs(9.89))
print(abs(0))
print(abs(-9))
print(abs(-9.87))
print(abs(True))  # 1
print(abs(False))  # 0
print(abs(3 + 4j))  # 求模，5.0 模为 sqrt(3^2 + 4^2)，即 sqrt(9 + 16)，结果为5.0

"""

对lst中的元素按照绝对值的大小降序排序

把lst中的每个元素依次作为实参传递给key所指定的函数去调用，即：
abs(1) abs(2) abs-5) abs(-3)
返回值分别为：1,2,5,3
根据返回值的大小对原数据进行排序
"""
lst = [1, 2, -5, -3]
lst.sort(key=abs, reverse=True)
print(lst)

# sorted(iterable,[key],reverse=False)
# iterable:要排序的可迭代对象
# key:指定一个函数，在排序之前，每个元素都先应用这个函数
# 之后再排序
# reverse:默认为False,代表升序，指定为True则为降序
# 对可迭代对象进行排序，以列表形式返回排序之后的结果

lst = [1, 2, -5, -3]
# 升序排序
print(sorted(lst))
# 降序排序
print(sorted(lst, reverse=True))

# 对lst中的元素按照绝对值的大小降序排序
print(sorted(lst, key=abs, reverse=True))
# 对字符串排序
print(sorted('hello world'))

# list.reverse()
# 把列表中的元素倒过来，无返回值
lst = [1, 3, 5, 2]
lst.reverse()
print(lst)
lst = [1, 3, 5, 2]
print(lst[::-1])
# list.count(x)
# 返回元素x在列表中出现的次数
lst = [1, 2, 3, '23', [2, 4]]
print(lst.count(2))  # 1

# list.index(x[,start[,end]])
# x:要找的值
# start:起始索引，默认为0
# end:结束索引(闭区间)，默认为len(lst)
# 返回从左边开始第一次找到指定值时的正向索引，找不到报错
lst = [1, 2, 3, 4, '23', [2, 4]]
print(lst.index(2))
# lst.index(2, 4)  # valueError
# list.pop(i=-1)
# i:要删除并返回的元素的索引
# 删除列表中指定索引的元素并返回该元素，默认最后一个
# 索引超出范围，则报错
lst = [567, 'hello', True, False, 456]
print(lst.pop(1))  # 'hello'
print(lst)  #
# list.remove(x)
# 删除列表中从左往右遇到的第一个x元素，无返回值
# 如果没有这样的元素，则报错
lst = [1, 2, 4, 2, 3, 3]
lst.remove(2)
lst.remove(2)
print(lst)
# list.copy()
# 返回该列表的一个副本，等价于lst[:]
lst = [567, 'hello', True, False, 456]
new_lst = lst.copy()
print(new_lst)

# list.clear()
# 移除列表中的所有元素，无返回值，等价于del lst[:]
lst = [567, 'hello', True, False, 456]
lst.clear()
print(lst)      # []
