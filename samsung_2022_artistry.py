def in_range(x, y): #격자 안에 존재하는지
    if x >= 0 and x < n and y >= 0 and y < n:
        return True
    return False

def dfs(i, j):
    xl, yl = [0, 1, 0, -1], [1, 0, -1, 0]
    for x, y in zip(xl, yl):
        nx, ny = i + x, j - y
        if in_range(nx, ny) == True and arr[i][j] == arr[nx][ny] and visited[nx][ny] == 0:
            # 격자 안에 존재하고, 방문 안했고, 숫자가 같다면
            group_li[nx][ny] = group_num
            group_cnt[group_num-1] += 1
            visited[nx][ny] = 1   #방문 했다고 표시
            dfs(nx, ny)


def make_group():
    global group_num
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:  # 방문 안했다면
                group_num +=1
                group_li[i][j] = group_num
                group_cnt[group_num - 1] = 1
                visited[i][j] = 1   #방문 했다고 표시
                dfs(i, j)

def get_score():
    global group_cnt
    for i in range(len(group_cnt)):
        if group_cnt[i] == 0:
            group_cnt = group_cnt[:i]
            break

    score = 0
    xl, yl = [0, 1, 0, -1], [1, 0, -1, 0]
    for i in range(n):
        for j in range(n):
            for x, y in zip(xl, yl):
                nx, ny = i + x, j - y
                if in_range(nx, ny) == True and group_li[i][j] != group_li[nx][ny]:
                    a, b = group_li[i][j], group_li[nx][ny]
                    score += (group_cnt[a-1] + group_cnt[b-1]) * arr[i][j] * arr[nx][ny]
    score = score // 2
    return score

def ten_spin(): #십자 스핀
    global new_arr
    mid = n // 2
    for i in range(n):
        for j in range(n):
            #십자스핀 세로
            if j == mid:    #세로
                new_arr[j][i] = arr[i][j]
            if i == mid:    #가로
                if j < mid: #왼쪽
                    new_arr[i + mid - j][mid] = arr[i][j]
                if j > mid: #오른쪽
                    new_arr[i - j + mid][mid] = arr[i][j]

def square_spin(x, y):   # 네모스핀
    global new_arr
    mid = n // 2
    nn = 0
    if y > mid:
        y -= mid+1
        nn += 1
    if x > mid:
        x -= mid+1
        nn += 2
    for i in range(x, x + mid):
        for j in range(y, y + mid):
            if nn == 0: # 2사분면
                new_arr[j][mid-1-i] = arr[i][j]
            if nn == 1: # 1사분면
                new_arr[j][2*mid - i] = arr[i][j+mid+1]
            if nn == 2: # 3사분면
                new_arr[j+mid+1][mid-1-i] = arr[i+mid+1][j]
            if nn == 3: #4사분면
                new_arr[j+mid+1][2*mid - i] = arr[i+mid+1][j+mid+1]

def total_spin():
    mid = n // 2
    ten_spin()
    square_spin(0, 0)
    square_spin(0, mid+1)
    square_spin(mid+1, 0)
    square_spin(mid+1, mid+1)

n = int(input())
arr = []
for i in range(n):
    x = list(map(int, input().split()))
    arr.append(x)

result = 0
for i in range(4):
    #초기화
    visited = [[0] * n for _ in range(n)]
    group_li = [[0] * n for _ in range(n)]
    group_num = 0
    group_cnt = [0] * n * n
    new_arr = [[0] * n for _ in range(n)]

    make_group()
    s = get_score()
    result += s
    total_spin()
    for i in range(n):
        for j in range(n):
            arr[i][j] = new_arr[i][j]
print(result)


# for i in range(n):
#     print(new_arr[i])


#print(result)
# for i in range(1):
#     ten_spin()
#     #total_spin()
#     for j in range(n):
#         print(new_arr[i])
#     result += get_score()
# (result)

