# in 基本
test1 = [0, 1, 2]
print(1 in test1)

test2 = (0, 1, 2)
print(1 in test2)

# if 基本
i = 100

if i in test1:
    print(f"{i} is a member of {test1}")
else:
    print(f"{i} is not a member of {test1}")

if test1:
    print("not empty")
else:
    print("empty")

d = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

print('key3' in d)
print('value2' in d.values(), "ok1")
print(('key1', 'value2') in d.items(), "No!")

# str型
print('h' in 'hello', "ok2")
print('hl' in 'hello', "no!!")

# not in 基本
print(100 not in test1, "not in")
print(not 100 in test1, "???")

# in 複数
print([0,1] in test1, "no!!!")
print([0, 1] in [[0, 1], [1, 0]], "ok3")

# set
l1 = [0, 1, 2, 3, 4]
l2 = [0, 1, 2]
l3 = [0, 1, 5]
l4 = [5, 6, 7]

print(set(l2) <= set(l1), "set 基本")
# print(set(l2) or set(l4))
print(set(l2).isdisjoint(set(l4)))

print(dict(zip(l2, l3)))