arr = [3,5,1,1,2,3,2]

arr2 = list(map(int, input().split()))

for i in range(len(arr2)) :
    print(f"{arr2[i]}={arr.count(arr2[i])}개")


# for i in range(len(arr)) :
#     for j in range(len(arr2)) :
#         arr.count()