def returnOnly(li):
    c = [0, 0]
    new_li = list(set(li))
    for i in range(2):
        c[i] = li.count(new_li[i])
    return new_li[c.index(1)]

if __name__ == '__main__':
    li_x, li_y = [], []
    for _ in range(3):
        x, y = map(int, input().split())
        li_x.append(x)
        li_y.append(y)
    print(returnOnly(li_x), returnOnly(li_y))