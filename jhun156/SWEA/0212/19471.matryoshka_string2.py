# import sys
# sys.stdin = open("input.txt","r")

def Matryoshka(string,x,num):
    for i in range(num//2):
        if string[x+i] != string[x+num-1-i]:
            return 0
    else:
        return num

for tc in range(1,11):
    test_case = int(input())
    arr = [list(input()) for _ in range(100)]
    arr.extend(list(zip(*arr)))
    # arr = 100 * 200 사이즈
    Max = 0
    for i in range(200):
        for j in range(100):
            for k in range(100-j,0,-1):
                ans = Matryoshka(arr[i],j,k)
                if ans > Max:
                    Max = ans
    print(f"#{tc} {Max}")