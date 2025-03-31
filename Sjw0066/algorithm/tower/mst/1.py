V,E=map(int,input().split())
arr= [list(map(int,input().split())) for _ in range(E)]
arr.sort(key = lambda x:(x[2]))
cnt=0
parent=list(range(V+1))
Sum=0


def find_boss(member):

    if parent[member] == member:
        return member

    ret= find_boss(parent[member])
    parent[member]=ret
    return ret

def union(a,b,c):
    global cnt,Sum,arr

    bossA,bossB=find_boss(a),find_boss(b)

    if bossA == bossB:
        return

    Sum+=c
    parent[bossB] = bossA


for lst in arr :
    union(lst[0],lst[1],lst[2])

print(Sum)