# https://www.acmicpc.net/problem/2581

def isNum(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True #소수임

if __name__ == "__main__":
    M = int(input())
    N = int(input())
    result = []
    for i in range(M, N+1):
        if isNum(i) == True:
            result.append(i)
    if len(result) > 0:
        print(sum(result))
        print(min(result))
    else:
        print('-1')