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