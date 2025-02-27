arr=[['A','B','K','T'],['K','F','C','F'],['B','B','Q','Q'],['T','P','Z','F']]

a,b= map(str,input().split())
answer=0
for i in arr:
    answer+=i.count(a)+i.count(b)

print(answer)
