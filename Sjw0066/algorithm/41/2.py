
n=int(input())
map=list(map(int,input().split()))
map.insert(0,0)
jump_range=[2,7]
Max=-21e8
loc_score=[-21e8]*(n+1)

def jump(now,score):
    global Max

    if now>n:
        if Max<score:
            Max=score
        return

    if score<=loc_score[now]:
        return
    loc_score[now]=score

    jump(now+2,score+map[now])
    jump(now+7,score+map[now])

jump(0,0)
print(Max)

'''
150
4 1 6 4 -3 -4 -2 -6 -8 -9 -9 -8 -6 -12 -4 50 4
 1 2 1 6 -4 -8 5 4 3 -1 -1 -2 -3 -4 -5 -6 -7 -8 
 34 1 2 6 4 7 2 -3 -4 -7 -8 1 2 4 1 6 4 -3 -4 -2 
 -6 -8 -9 -9 -8 -6 -12 -4 50 4 1 2 1 6 -4 -8 5 4 
 3 -1 -1 -2 -3 -4 -5 -6 -7 -8 34 1 2 6 4 7 2 -3 -4 
 -7 -8 1 2 4 1 6 4 -3 -4 -2 -6 -8 -9 -9 -8 -6 -12 
 -4 50 4 1 2 1 6 -4 -8 5 4 3 -1 -1 -2 -3 -4 -5 -6 
 -7 -8 34 1 2 6 4 7 2 -3 -4 -7 -8 1 2 3 1 5 21 15 23
'''