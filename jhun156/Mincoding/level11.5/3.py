arr = ['A','1','1','1','5','A','w','z']

a = input()

result = arr.count(a)

if result >= 3:
    print("THREE")
elif result == 2:
    print("TWO")
elif result == 1:
    print("ONE")
else:
    print("NOTHING")