#https://www.acmicpc.net/problem/2739

def timetable(cnt):
    if cnt == 9:    #개수 맞았으면 리턴
        return
    print(n, ' * ',cnt+1, ' = ', n * (cnt+1))
    timetable(cnt+1)

if __name__ == "__main__":
    n = int(input())
    timetable(0)