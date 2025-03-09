# 已知 lst = [1, 3, 2, 6, 4], 程序实现: 删除lst元素中的中位数（只考虑列表中元素个数为奇数的情况）
lst = [1, 3, 2, 6, 4]
lst.sort()
lst.pop((len(lst) // 2))
print(lst)

# 已知 lst = [1, 3, 2, 6, 4], 程序实现: 删除lst元素中的最大值和最小值（不考虑多个最值情况）
lst = [1, 3, 2, 6, 4]
lst.sort()
lst.pop(0)
lst.pop(len(lst)-1)
print(lst)
print("###################")
lst = [1, 3, 2, 6, 4]
lst.sort()
print(lst[1:len(lst)-1])


"""
编写程序实现: 请用户输入用逗号隔开的一串数字, 输出转化成元组后的数据

例:
用户输入:  1,2,3,45,678
程序输出:  ('1', '2', '3', '45', '678')
"""
inputValue = input("用户输入:\n")
tup = tuple(inputValue.split(','))
print(tup)


"""
实现一个程序:
用户输入一串小写的英文字母, 求出英文字母有几种？并格式化输出

例如： 
输入 appgbcdcdho    输出：其中有 a b c d g h o p 8种英文字母
"""
inputValue = input("请输入一串小写字母\n")
dic = dict(zip(inputValue, inputValue))  # 将输入的字符串转化成字典,字典会自动去重
ls = list(dic.keys())   # 取出字典的key转为key的新视图再转为列表
ls.sort()   # 对列表进行升序排序
itemStr = ''  # 定义空字符串进行结果字符串的重组
for item in ls:
    itemStr += item  # 循环取出列表中的每个元素进行字符串拼接
res = ' '.join(itemStr)  # 将取出的字符串进行空格格式
print(f"其中有 {res} {len(ls)}种英文字母")
