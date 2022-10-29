from math import sqrt

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        d = sqrt((x1-x2)**2 + (y1-y2)**2)
        if d == 0 and r1 == r2:
            print(-1)
        if r1+r2 == d or abs(r1-r2) == d:
            print(1)
        if abs(r1-r2) < d < r1+r2:
            print(2)
        else:
            print(0)