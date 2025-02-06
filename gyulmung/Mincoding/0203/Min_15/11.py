arr = [[] for _ in range(4)]
for i in range(4):
    string = input()
    arr[i] = string

arr=''.join(arr)

if 'A' in arr and 'B' in arr:
    print('대발견')
elif 'A' in arr or 'B' in arr:
    print('중발견')
else:
    print('미발견')