def isNum(n):
    if n < 2:   return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:  return False
    return True

def get_result(x):
    if x in new_sosu and num-x in new_sosu:
        return x, num - x
    return get_result(x-1)

if __name__ == "__main__":
    T = int(input())
    sosu = []   #10000 까지 소수를 담을 리스트
    result = [] # 최종 output
    for i in range(10001):
        if isNum(i):
            sosu.append(i)
    for i in range(T):
        num = int(input())
        new_sosu = [x for x in sosu if x < num] # 범위에 맞는 소수 리스트
        result.append(get_result(num//2))
    for i in result:
        print(str(i)[1:-1].replace(',', ''))

#######################################################################################

# from itertools import combinations_with_replacement
#
# def isNum(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True
#
# def getLi(new_li, num):
#     out = []
#     for i in combinations_with_replacement(new_li, 2):
#         if sum(i) == num:
#             out.append(i)
#     return out
#
# if __name__ == "__main__":
#     x = list(range(10000))
#     li = []    #소수가 담긴 리스트
#     for i in x:
#         if isNum(i):
#             li.append(i)   #소수가 담긴 리스트
#     T = int(input())
#     result = []
#     for i in range(T):
#         num = int(input())
#         new_li = [x for x in li if x < num]  # n값보다 작은 수의 소수를 새롭게 저장
#         out = getLi(new_li, num)
#         if len(out) > 1:    # 여러개의 케이스가 있는 경우, 차이가 적은 케이스를 출력
#             m = []
#             for i in range(len(out)):
#                 m.append(abs(out[i][0] - out[i][1]))
#             result.append(str(out[m.index(min(m))])[1:-1] )
#         else:   # 하나의 케이스만 존재할 때
#             out = str(out)[2:6]
#             result.append(out)
#     for i in result:
#         i = i.replace(',', '')
#         print(i)

#######################################################################################

# def get_sosu_list(num):
#     li = []
#     for i in range(2, num + 1):
#         flag = 1
#         for j in range(2, i//2 +  1):
#             if i % j == 0:
#                 flag = 0
#                 break
#         if flag == 1:
#             li.append(i)
#     return li
#
# def get_num_binary(mid, M):  # 2, 3, 5, 7, 11, 13
#     global m, output
#     if (num - mid) in m:
#         output = [num-mid, mid]
#         return output
#     new_mid = M[len(M)//2 -1]
#     get_num_binary(new_mid, M)
#     return output
#
# if __name__ == "__main__":
#     T = int(input())
#     sosu = get_sosu_list(10000)
#     result = []
#     for i in range(T):
#         num = int(input())
#         new_sosu = [x for x in sosu if x < num] # 범위에 맞는 소수 리스트
#         mid = sosu[len(new_sosu)//2]
#         m, M = new_sosu[:len(new_sosu)//2 + 1], new_sosu[len(new_sosu)//2 + 1:]
#         result.append(get_num_binary(mid, M))
#     for i in result:
#         print(i)
