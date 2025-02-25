str1 = list(input())
check = list(input().split())
P = len(str1)
index_list = []
for i in range(2):
    a = str1.index(check[i])
    index_list.append(a)

for index in index_list:
    left = index - 1
    right = index + 1
    if left < 0 and right <= P - 1:
        str1[right] = "#"
    elif left >= 0 and right > P - 1:
        str1[left] = "#"
    else:
        str1[left],str1[right] = "#","#"

for i in range(P):
    print(str1[i],end='')