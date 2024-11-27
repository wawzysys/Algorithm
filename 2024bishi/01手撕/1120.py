def merge_sort(data,l,r):
    if l >= r:
        return
    mid = l + r >> 1
    # 左右递归
    merge_sort(data,l,mid)
    merge_sort(data,mid+1,r)
    # 用来临时保存归并好的一组数据
    tmp = []
    i = l
    j = mid + 1
    # 归并过程
    while i <= mid and j <= r:
        if data[i] <= data[j]:
            tmp.append(data[i])
            i += 1
        else:
            tmp.append(data[j])
            j += 1
    # 当一边已经结束后直接把另一边的剩余数据加入到tmp中
    tmp += data[i:mid+1]
    tmp += data[j:r+1]
    # 将结果返回到data中
    data[l:r+1] = tmp
data = [int(x) for x in input().split()]
n = len(data)
merge_sort(data,0,n-1)
print(" ".join(map(str,data)))
