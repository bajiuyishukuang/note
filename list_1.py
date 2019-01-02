dict1 = {"name": 1, "age": 2}


# 列表生成
nums = [num for num in range(99)]
resultList = [num ** 2 for num in nums if num % 2 != 0]
print(resultList)


# 增
nums.append(100)
# dic[key] = value
# 当key在原字典中不存在时,即为新增操作


# 插
# 在第二个位置插入2（index ，object）
nums.insert(1, 2)  # 无返回值
# l.extend(iterable) iterable可以是列表 元祖 字符串
nums.extend(nums)  # 无返回值


# 运算
# 各项相乘
print(nums*3)
# 相加
# ["a"] + ["b", "c"] = ["a", "b", "c"]
# 和extend区别，只能列表类型和列表类型相加


# 删
# 按照索引删
del nums[1]  # 删除第二个元素
res = nums.pop(-1)  # 删除nums最后一个元素并返回
# 按照内容删
nums.remove(2)  # 删除2这个元素  无返回值
# 清空列表
nums = []
# 在左右两边删
str(nums).lstrip("0").rstrip("-")
# 删字典
# del dict1[key]
# 删除指定的键值对, 并返回对应的值
v = dict1.pop("name")

# 删除字典内所有键值对
dict1.clear()

# 删除按升序排序后的第一个键值对, 并以元组的形式返回该键值对
# 如果字典为空, 则报错
d = {"name": "sz", "zge": 18, "a": 123}
result = d.popitem()
print(result, d)


# 改（只能按照索引改）
# 改列表
nums[2] = 3  # 第三个元素改成2
# 改字典
# 只能改值, 不能改key
# 修改单个键值对
# dic[key] = value

# 批量修改键值对
# oldDic.update(newDic)
# 根据新的字典, 批量更新旧字典中的键值对
# 如果旧字典没有对应的key, 则新增键值对


# 查
num = nums.index(2)  # 获取2元素的位置
c = nums.count(5)   # 获取5元素的个数
pic = nums[1:7:2]  # items[start:end:step]
# 查字典
# 方式1
# dic[key]

# 方式2
# dic.get(key[, default])
# 如果不存在对应的key, 则取给定的默认值default
d = {"name": "sz", "age": 18, 0: "666"}
v1 = d.get("age1", 666)
print(v1, d)

# 方式3
# dic.setdefault(key[, default])
# 获取指定key对应的值
# 如果key不存在, 则设置给定默认值, 并返回该值
# 如果默认值没给定
# 则使用None代替
# d = {"name": "sz", "age": 18, 0: "666"}
# v = d.setdefault("age1", 666)
# print(v, d)
# 获取所有的值
dict1.values()

# # 获取所有的键
dict1.keys()
ks = d.keys()

# 获取字典的键值对
dict1.items()
its = d.items()


# 判定
# 	元素 in  列表
# 	元素 not in 列表

# 反转列表
nums.reverse()
# 反转字符串
s = "-11"
print(s[2:0:-1])

# 排序
nums.sort()  # 无返回值
nums1 = sorted(nums)  # 排序之后返回
