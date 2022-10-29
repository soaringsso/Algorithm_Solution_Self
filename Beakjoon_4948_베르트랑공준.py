def isNum(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    li = list(range(2, 500000))
    out = []
    for i in li:
        if isNum(i):
            out.append(i)   #소수가 존재하는 리스트
    while True:
        n = int(input())
        if n == 0:
            break
        new = [x for x in out if x > n and x <= 2*n]
        print(len(new))

#######################################################################
# 입력 받을 때마다 소수를 구하니 시간초과됨.
# 미리 소수 리스트를 구한 뒤에 그 범위에 맞는 개수를 리턴하는 것이 좋음.
# def isNum(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# if __name__ == "__main__":
#     li = []
#     while(1):
#         n = int(input())
#         if n == 0:
#             break
#         li.append(n)
#     for i in range(len(li)):
#         num = 0
#         for j in range(li[i]+1, 2*li[i] + 1):
#             if isNum(j):
#                 num += 1
#         print(num)