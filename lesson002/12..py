# Python 学习
# hqzhu
# 开发时间：23/2/8 19:48

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print("排序前的数组：", arr)

arr = bubble_sort(arr)

print("排序后的数组：", arr)