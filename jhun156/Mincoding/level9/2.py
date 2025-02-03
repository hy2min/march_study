arr = [
    ['A','B','C','D','E'],
    ['E','A','B','A','B'],
    ['A','C','D','E','R'],
]

a = input()
count = 0

for i in range(3):
    for j in range(5):
        if arr[i][j] == a:
            count += 1

if count >= 3:
    print("대발견")
elif 1 <= count < 3:
    print("발견")
else:
    print("미발견")
