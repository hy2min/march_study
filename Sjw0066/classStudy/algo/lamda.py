lst1=[1,2,3,4,5]
lst2=[6,7,8,9,10]
# 두 리스트 세로로 더한값 출력


lst3=list(map((lambda x,y:x+y),lst1,lst2))
print(lst3)