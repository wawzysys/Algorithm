# try:
#     print(x)
# except:
#     print("Something went wrong")
# finally:
#     print("The try except is finished")

list1 = [2, 4, 6, 8, 10, "python", (1,), {2, 3}, {1: 'one'}]
print(list1[::2])
print(list1[-2:])
print(list1[1::2])
print(list1[-2::])
def func(s, i, j):
    if i < j:
        func(s, i + 1, j - 1)
        s[i], s[j] = s[j], s[i]

def main():
    a = [10, 6, 0, 3]
    func(a, 0, len(a) - 1)
    for i in range(4):
        print(a[i])

main()
