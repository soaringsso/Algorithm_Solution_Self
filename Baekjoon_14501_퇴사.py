def func(s):
    li_t, li_p = [t[s]], [p[s]]
    i = 0
    while(1):
        i = s + t[s]
        if i >= len(t):
            break
        if sum(li_t) + t[i] <= N:
            li_p.append(p[i])
            li_t.append(t[i])
            s = i
    return sum(li_p), li_p

if __name__ == "__main__":
    N = int(input())
    t, p = [], []
    for i in range(N):
        T, P = map(int, input().split())
        if i + T <= N :
            t.append(T)
            p.append(P)
    print(p)
    print(func(0))