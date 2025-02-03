arr = ['D','F','G','D','A','Q']

ch1, ch2 = input().split()

count = 0

for j in range(ord(ch1),ord(ch2)+1):
    result = arr.count(chr(j))
    count += result

if count > 0:
    print("발견!!!")
else:
    print("미발견!!!")
