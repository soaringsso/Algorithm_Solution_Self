#https://www.acmicpc.net/problem/1520

def dfs(x, y, visited):
    global num
    if x == m-1 and y == n-1:
        num += 1
        return
    for i in range(4):
        new_x, new_y = x + li[i][0], y + li[i][1]
        if 0 <= new_x < m and 0 <= new_y < n and H[new_x][new_y] < H[x][y]:
            visited.append(H[new_x][new_y])
            dfs(new_x, new_y, visited)
            visited.pop(-1)

if __name__ == "__main__":
    m, n = map(int, input().split())
    H = list(input().split() for i in range(m))
    li = (0, 1), (0, -1), (-1, 0), (1, 0)
    num = 0
    dfs(0, 0, [H[0][0]])
    print(num)