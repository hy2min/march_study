vect = [3,5,1,1,2,3,2]

arr = [i for i in map(int,input().split())]
result_list = []

for i in range(4):
    result = 0
    for j in range(len(vect)):
        if arr[i] == vect[j]:
            result += 1
    result_list.append(result)
for i in range(4):
    print(f"{arr[i]}={result_list[i]}개")