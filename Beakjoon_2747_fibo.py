#0, 1, 1, 2, 3, 5, 8, 13
def fibo(cnt):
    if cnt == 0:
        return 0
    if cnt == 1:
        return 1
    else:   # cnt > 1일 때
        return fibo(cnt-1) + fibo(cnt-2)

if __name__ == "__main__":
    n = int(input())    #n개의 수
    print(fibo(n))