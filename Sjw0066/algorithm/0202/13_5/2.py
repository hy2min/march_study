distance=[4,2,5,1,6,7,3]

country=list(map(str,input().split()))

country.sort()

index_c1=ord(country[1])-65

index_c2=ord(country[0])-65

result=0


for i in range(index_c2+1,index_c1):
    result+=distance[i] 

print(result)