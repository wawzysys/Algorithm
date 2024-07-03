strs = ['a', 'ab', 'abc', "python"]
y = filter(lambda s : len(s) < 2, strs)
tmp = list (map(lambda s : s.upper(), y))
print(tmp)

strs = 'I like python'
print(strs.find('n'))
print(strs.rfind('n'))

n1 = [1, 2,5, 3, 5]
n1.append(4)
n1.insert(0, 7)
n1.sort()
print(n1)

# dicts = {}
# dicts[([1,2])] = 'a'
# print(dicts)

str = "hello python"
suffix = "python"
print(str.endswith(suffix, 2))

a = [1, 2, 3, 4, 5]
sums = sum(map(lambda x : x * 3, a[2::3]))
print(sums)

# a = "1" or 90 True | -1
# print(a)

lists  = [1, 2, 2, 3, 4, 4 ,5]
print(lists.index(4))
dicts = {}
dicts[(1,)] = ({3, (4, 5)})
print(dicts)


lists = [1, 2, 3, 4 ,5]
print(lists[0::2])

strs = "abbacabb"
print(strs.strip("bc"))

str1 = ''
if not str1:
    print(0)

trupls = [(1, 2), (2,3,4)]
lists = []
for tru in trupls:
    for num in tru:
        lists.append(num)
print(lists)

lis = [1, 3, 2]
a = id(lis)
lis += [4, 5]
b = id(lis)
print(a == b)

tup = (1, 3, 2)
a = id(tup)
tup += (4, 5)
b = id(tup)
print(a == b)

tup = (1, 3, 2)
a = id(tup)
tup = sorted(tup)
b = id(tup)
print(a == b)

lis = [1, 3, 2]
a = id(lis)
lis = sorted(lis)
b = id(lis)
print(a == b)