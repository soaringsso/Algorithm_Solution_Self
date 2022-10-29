# https://www.acmicpc.net/problem/1987

def dfs(x, y, num):
    global answer
    answer = max(num, answer)
    for j in range(4):
        new_x, new_y = x + li_x[j], y + li_y[j]
        if 0 <= new_x < r and 0 <= new_y < c and visited[alpha[new_x][new_y]] != 1:
            #visited.append(alpha[new_x][new_y])
            visited[alpha[new_x][new_y]] = 1
            dfs(new_x, new_y, num+1)
            # visited.remove(alpha[new_x][new_y])
            visited[alpha[new_x][new_y]] = 0

if __name__ == "__main__":
    r, c = map(int, input().split())
    alpha = [list(map(lambda x: ord(x)-65, input())) for i in range(r)]
    #li = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    li_x = [0, 0, -1, 1]
    li_y = [1, -1, 0, 0]
    visited = [0] * 26 # 알파벳 26자를 방문하지 않았다고 0으로 초기화
    visited[alpha[0][0]] = 1
    #visited = [alpha[0][0], ]
    answer = 0
    dfs(0, 0, 1) # 가장 첫 step을 추가함
    print(answer)