arr = []


for i in range(4) :
    arr2 = [*input()]
    arr.append(arr2)

arr = sum(arr,[])

if "A" in arr and 'B' in arr :
    print('대발견')
elif "A" in arr or 'B' in arr :
    print("중발견")
else :
    print("미발견")