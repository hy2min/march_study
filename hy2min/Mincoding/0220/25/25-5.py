arr = input().split('|')
for i in range(len(arr)):
    name = arr[i].split('@')[0]
    domain = arr[i].split('@')[1].split('.')[0]
    print(f'[#{name}] {domain}')