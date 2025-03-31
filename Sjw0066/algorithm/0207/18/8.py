train = [3, 7, 6, 4, 2, 9, 1, 7]
target=list(map(int,input().split()))
st_index=0
end_index=0
for i in range(len(train)-2):
    if train[i] != target[0] :
        continue
    if train[i:i+3] == target:
       flag=1
       st_index=i
       end_index=i+2

print(f'{st_index}번~{end_index}번 칸')

