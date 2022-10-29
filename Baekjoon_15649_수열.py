# https://www.acmicpc.net/problem/15649

def dfs(cnt):
    if cnt == s:    #개수 맞았으면 프린트 후 리턴
        print(result)
        return
    for i in range(n):
        if visited[i] == 0: #탐색하지 않았으면
            visited[i] = 1  #탐색하고 완료했다고 표시
            result.append(i+1)
            dfs(cnt+1)
            visited[i] = 0
            result.pop()

if __name__ == "__main__":
    n , s = map(int, input().split())
    visited = [0 for _ in range(n)] #탐색하지 않았다고 표시
    result = []
    print(dfs(0))

# def dfs(n, m, output):
#     if len(output) == m:
#         print(output)
#         return
#     for i in range(1, n+1):
#         if i in output: continue
#         dfs(n, m, output+[i])
# if __name__ == "__main__":
#     n , m = 4, 4#map(int, input().split()) #4, 2
#     dfs(n, m, [])