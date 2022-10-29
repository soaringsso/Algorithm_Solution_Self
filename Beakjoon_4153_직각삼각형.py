def isTri(li):
    m = max(li)
    li.remove(m)
    if m**2 == li[0]**2 + li[1]**2:
        return "right"
    return "wrong"

if __name__ == "__main__":
    result = []
    while(1):
        x, y, z = map(int, input().split())
        if x == 0 and y == 0 and z == 0:
            break
        li = [x, y, z]
        result.append(isTri(li))
    for i in result:
        print(i)