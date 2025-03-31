import sys
sys.stdin=open('input.txt','r')


N = int(input())

def password(level):
    global count
    if level == 4:
        count += 1
        if path == list(word):
            print(count)
        return


    for i in range(len(arr)):
        path[level] = arr[i]
        password(level+1)



for i in range(N):
    word = input()
    path = [0]*4
    count = 0
    arr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    password(0)

