T= int(input())

def dfs(balloon,total):
    global Max_score

    if len(balloon)==1:
        total+=balloon[0]
        if Max_score<total:
            Max_score=total
        return

    score=0

    for i in range(len(balloon)):
        left=i-1
        right=i+1

        if left<0 :
            score = balloon[right]
        elif right>len(balloon)-1:
            score = balloon[left]
        else:
            score = balloon[left]*balloon[right]

        new_balloon=balloon[:i]+balloon[i+1:]
        dfs(new_balloon,total+score)



for tc in range(1,T+1):
    N=int(input())

    lst=list(map(int,input().split()))
    Max_score=-21e8
    dfs(lst,0)
    print(Max_score)