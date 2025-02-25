# import sys
# sys.stdin = open("input.txt","r")

def triangle(num):
    lst = [[] for _ in range(num)]
    for i in range(num):
        for j in range(i+1):
            if j == 0 or j == i:
                lst[i].append(1)
            else:
                lst[i].append(lst[i-1][j-1]+lst[i-1][j])
    return lst

T = int(input())
for tc in range(1,T+1):
    ans = triangle(tc)
    print(f"#{tc}")
    for i in range(tc):
        print(*ans[i])