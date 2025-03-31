import sys
sys.stdin = open('input.txt','r')

member = input()
N = int(input())
path = [0]*N

def candi(level):
    if level == N:
        print(*path, sep='')
        return

    for i in range(len(member)):
        path[level] = member[i]
        candi(level+1)

candi(0)