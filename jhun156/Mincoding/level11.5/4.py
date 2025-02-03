arr = [
    ['a','b','a','c','z'],
    ['c','t','a','c','d'],
    ['c','c','c','c','a'],
]

a = input()

count = 0

for i in range(3):
    result = arr[i].count(a)
    count += result

if count >= 7:
    print("세상에")
elif count >= 5:
    print("와우")
elif count >= 3:
    print("이야")
else:
    print("이런")