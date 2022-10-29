# def func(x, y, r, c, length):
#     result = 0
#     if x == r and y == c:
#         return result
#     if length == 1:
#         result += 1
#     else:
#         result += length * length
#         return result
#
# if __name__ == "__main__":
#     n, r, c = map(int, input().split())
#     print(func(0, 0, r, c, 2**n))




def func(x, y):
    if x == r and y == c:
        return
    if x == 1 or y == 1:pass




if __name__ == "__main__":
    N, r, c = map(int, input().split()) #2, 3, 1
    print(func(0, 0))