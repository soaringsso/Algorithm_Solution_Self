# https://www.acmicpc.net/problem/11653

def fun(n):
    global li
    if n == 1:
        return
    for i in range(2, n+1):
        if n % i == 0:
            print(i)
            fun(n//i)
            return

if __name__ == "__main__":
    n = int(input())
    fun(n)