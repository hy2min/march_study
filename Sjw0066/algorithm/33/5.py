N=int(input())
ingu=list(map(int,input().split()))
case=int(input())

class unionfind:

    def __init__(self,n):
        self.parent=list(map(lambda x:chr(x),range(65,65+n)))
        self.rank=[1]*n


    def find(self,member):
        idx=ord(member)-65

        if self.parent[idx]==member:
            return member

        ret = self.find(self.parent[idx])
        self.parent[idx] = ret
        return ret

    def union(self,a,b):
        parent_a,parent_b=self.find(a),self.find(b)
        aidx=ord(parent_a)-65
        bidx=ord(parent_b)-65
        if parent_a==parent_b:
            return

        if self.rank[aidx] > self.rank[bidx]:
            self.parent[bidx] = parent_a
        elif self.rank[aidx] < self.rank[bidx]:
            self.parent[aidx] = parent_b
        else:
            self.parent[bidx] = parent_a
            self.rank[aidx] += 1

    def get_group(self):
        groups={}

        for i in range(len(self.rank)):
            root=self.find(chr(i+65))
            groups.setdefault(root,[])

        for i in range(len(self.rank)):
            root = self.find(chr(i+65))
            groups[root].append(chr(i+65))

        return groups

def war(lst,c1,c2):

    s1=0
    cnt1=0
    for i in range(len(lst)):
        if c1 in lst[i]:
            for j in lst[i]:
                s1+=ingu[ord(j)-65]
                cnt1+=1
    s2=0
    cnt2=0
    for i in range(len(lst)):
        if c2 in lst[i]:
            for j in lst[i]:
                s2 += ingu[ord(j) - 65]
                cnt2+=1
    if s1-s2>0:
        return N-cnt2
    else:
        return N-cnt1

ans=0
uf=unionfind(N)

for i in range(case):
    command,con1,con2=input().split()
    if command=='alliance':
        uf.union(con1,con2)
    else:
        gr=uf.get_group()
        groups=list(gr.values())
        ans=war(groups,con1,con2)
print(ans)