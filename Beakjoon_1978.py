def isNum(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    n = int(input())
    li = list(map(int, input().split()))
    num = 0
    for i in li:
        if isNum(i):
            num += 1
    print(num)