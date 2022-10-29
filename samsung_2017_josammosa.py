# def per(idx):
#     if idx == n:
#         print(arr)
#     else:
#         for i in range(idx, n):
#             arr[idx], arr[i] = arr[i], arr[idx]
#             per(idx+1)
#             arr[idx], arr[i] = arr[i], arr[idx]
#
# arr = [1,2,3]
# n = 3
# per(0)

# def com(idx, li):
#     if len(li) == 2:
#         answer.append(li)
#         return
#     for i in range(idx, len(arr)):
#         com(i+1, li+[arr[i]])
#
# arr = [1,2,3,4]
# n = 2
# answer = []
# com(0, [])
# print(answer)

def com(idx, li):
    if len(li) == n/2:
        out.append(li)
        return
    for i in range(idx, len(arr)):
        com(i+1, li+[arr[i]])

def make_po_li(li):
    po_li = []
    for i in range(n//2):
        for j in range(n//2):
            if arr[i] == arr[j]:
                continue
            x = [li[i], li[j]]
            po_li.append(x)
    return po_li

def make_sum(li):
    sum = 0
    for i in range(len(li)):
        x, y = int(li[i][0]), int(li[i][1])
        sum += ex[x][y]
    return sum

n = int(input())
ex = []
for i in range(n):
    li = list(map(int, input().split()))
    ex.append(li)

arr = [i for i in range(n)]
out = []    #조합 경우의 수
com(0, [])

m = 10000
num = len(out)
for i in range(num//2):
    li = [out[i]] + [out[num-i-1]]
    a, b = make_po_li(li[0]), make_po_li(li[1])
    x, y = make_sum(a), make_sum(b)
    if abs(x-y) < m:
        m = abs(x-y)
print(m)

# ex = [[0, 100, 1, 1, 1, 1],
# [1, 0, 30, 30, 1, 1],
# [1, 1, 0, 1, 1, 1],
# [1, 1, 1, 0, 1, 1],
# [1, 1, 1, 1, 0, 1],
# [1, 1, 1, 1, 40, 0]]