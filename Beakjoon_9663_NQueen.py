#https://www.acmicpc.net/problem/9663

# def possible_li(c, r, visited):
#     li, new, x = [], [], []
#     for i in range(input):
#         if abs(i-r) > c - i and i not in visited:
#             new.append([c+1, i])
#     for i in range(len(new)-1):
#         for j in range(i+1, len(new)):
#             if abs(new[i][0] - new[j][0]) == (new[i][1] - new[j][1]):
#                 x.append(new[j])
#     for i in range(len(x)):
#         if x[i] in new:
#             new.remove(x[i])
#     for i in range(len(new)):
#         li.append(new[i][1])
#     return li

# def Nqueen(c, r):   # 0, 0
#     global result, visited
#     if len(visited) == input:   #마지막 줄까지 갔을 때 리턴
#         result += 1
#         return
#     li = possible_li(c, r, visited)
#     if len(li) == 0:    #갈 수 있는 위치가 없을 때
#         return
#     for i in range(len(li)):
#         q[c+1][li[i]] = 1 #방문!
#         visited.append(li[i])
#         Nqueen(c+1, li[i])
#         q[c][r] = 0
#         visited.pop()
#     return result
#
# if __name__ == "__main__":    #input 8 output 92
#     input = 5   #int(input())
#     output = 0
#     # for i in range(input):  #0, 1, 2, 3
#     i = 0
#     q = [[0 for col in range(input)] for row in range(input)]  # col가로
#     q[0][i] = 1
#     result = 0
#     visited = [i]
#     print(Nqueen(0, i))
#     #print(output)


# def Nqueen(x, max_depth):   #x는 현재값
#     global result, li
#     if x == max_depth:   #마지막 줄까지 갔을 때 리턴
#         result += 1
#         return
#     for i in range(1, max_depth+1):
#         yes = 0
#         if i in li: continue    #같은 행에 있으면 pass
#         for j in range(x):
#             if abs(li[j]-i) == abs(x-j):    #같은 대각선에 있으면
#                 yes = 1
#         if yes == 1:    continue
#         li[x] = i   # 현재 위치x에 y값을 넣어줌
#         Nqueen(x+1, max_depth)
#         li[x] = 0
#     return result
#
# if __name__ == "__main__":
#     global li
#     n = int(input())
#     li = [0 for col in range(n)]
#     result = 0
#     print(Nqueen(0, n))
