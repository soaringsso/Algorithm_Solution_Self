#https://www.acmicpc.net/problem/2023

# 메모리 초과 - 대입할 리스트를 만들어서 하지 말아야함 !
# from itertools import product
#
# def isNum(num):
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:
#             return False
#     return True #소수임
#
# def dfs(num, i):
#     if i == n:
#         return
#     if isNum(num) == True:  #소수이면
#         a = dfs(num//10, i+1)
#         if a != 1:  #모든 부분이 소수라면
#             return num
#     return 1    #만약 소수가 아닌 부분이 존재하면 1을 리턴
#
# if __name__ == "__main__":
#     n = int(input())
#     li, result = [], []
#     #li = list(range(int(str(1) + str(0)*(n-1)), int(str(9) * n) + 1)) #가능한 모든 리스트
#     for i in product(['1', '2', '3', '5', '7', '9'], repeat = n):
#         x = int(''.join(i))
#         if x % 2 != 0:    #홀수이면
#             li.append(x)    #소수가 될 가능성이 있는 리스트
#     for i in range(len(li)):
#         a = dfs(li[i], 0)
#         if a != 1:
#             result.append(a)
#     print(result)

############################################################################

# def isNum(num):
#     num = int(num)
#     for i in range(2, int(num ** 0.5)+1):
#         if num % i == 0:
#             return False
#     return True  # 소수임
#
# def dfs(num):
#     if len(num) == n:
#         print(num)
#         return
#     for i in range(4):
#         a = str(num) + str(last[i])
#         if isNum(a) == True:
#             dfs(a)
#
# if __name__ == "__main__":
#     last = [1, 3, 7, 9]
#     n = int(input())
#     dfs('2')
#     dfs('3')
#     dfs('5')
#     dfs('7')

##############################################################################

def dfs(num, i):
    if i == 1:
        print(num)
        return
    a = int(num//i)
    if a in result:
        dfs(num, i/10)
    return

if __name__ == "__main__":
    # n = int(input())
    n = int(100000000**0.5)
    result = [2, 3] # n자리수까지의 소수가 모두 담긴 리스트
    for i in range(4, n):
        li = 1
        for j in result:
            if i % j == 0:
                li = 0
            if not li:
                break
        if li:
            result.append(i)
    print(result)

#####################################################################

# def isNum(num):
#     num = int(num)
#     for i in range(2, int(num ** 0.5)+1):
#         if num % i == 0:
#             return False
#     return True  # 소수임
#
# def dfs(num, i):
#     if i == n:
#         return
#     a = num//10
#     if isNum(a) == True:  #소수이면
#         if dfs(num//10, i+1) != 1:  #모든 부분이 소수라면
#             return num
#     return 1   #만약 소수가 아닌 부분이 존재하면 1을 리턴
#
# if __name__ == "__main__":
#     n = int(input())
#     min = int(str(1) + str(0)*(n-1))
#     max = int(str(9) * n)
#     li = list(range(min, max+1))
#     result = [] #n자리의 소수가 담길 리스트
#     for i in li:
#         if isNum(i) == True:
#             result.append(i)
#     output = [] #최종 출력할 리스트
#     for num in result:
#         a = dfs(num, 0)
#         if a != 1:
#             output.append(a)
#     print(output)
