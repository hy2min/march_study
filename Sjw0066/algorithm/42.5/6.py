str1=list(input())
N=int(input())
used=[[0]*len(str1) for _ in range(len(str1))]
Max=-21e8

def check_score(lst):
     Sum=0
     for i in range(len(lst)-1):
        if lst[i] == lst[i+1] : Sum-=50
        if abs(ord(lst[i]) - ord(lst[i+1]))<=5:Sum+=3
        if abs(ord(lst[i]) - ord(lst[i+1]))>=20:Sum+=10

     return Sum

def dfs(level,lst):
        global Max

        if level==N:
            ret=check_score(lst)
            if Max<ret:
                Max=ret
            return

        temp=lst[:]

        for i in range(len(lst)):
            for j in range(i,len(lst)):
                lst[i],lst[j] = lst[j] ,lst[i]
                dfs(level+1,lst)
                lst=temp[:]

dfs(0,str1)
print(Max)