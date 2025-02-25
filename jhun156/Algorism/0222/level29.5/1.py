n = int(input())
arr = [3,1,2,1,3,2,1,2,1]
n -= 1
# index 번호

def jump(num,level):

    if level == 0:
        print("시작",end=' ')

    if num >= 8:
        print("도착",end=' ')
        return

    else:
        print(arr[num],end=' ')
        if num > 8:
            jump(8,level+1)
        else:
            jump(num+arr[num],level+1)
        print(arr[num],end=' ')

    if level == 0:
        print("시작")

jump(n,0)