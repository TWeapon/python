# 字典（Dictionary）
# 特性：可变，不是序列
# 字典用花括号定义，每个元素都是键值对的形式key:value
# 字典的键不能存在可变的数据；值没有限制
# 字典的键如果重复，会自动去重，保留第一个重复键，并且其它重复的键
# 对应的值还会对第一个 重复键对应的值进行修改；值可以重复
# 当字典作为一个iterable对象参与操作时，只有键参与迭代
# 创建字典的多种方式
# 直接在空字典里面写键值对
d = {'name': 'Tom', 'age': 28}
print(d)
# 定义一个空字典，再往里面添加键值对
d = {}
d['name'] = 'Tom'
d['age'] = 28
print(d)
# 把键值对作为关键字参数传入
d = dict(name='Tom', age=28)
print(d)
# 用映射结构来构建字典
d = dict(zip(['name', 'age'], ['Tom', 28]))
print(d)
# dict(**kwarge)/dict(mapping)/dict(iterable)
# 用于创建一个字典并返回
print(dict())
print(dict(one=1, two=2, three=3))
print(dict(zip(['one', 'two', 'three'], [1, 2, 3])))
print(dict([('one', 1), ('two', 2), ('three', 3)]))
