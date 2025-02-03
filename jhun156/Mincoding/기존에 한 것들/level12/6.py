arr = ['M','I','N','Q','U','E','S','T']

a = input()
b = input()
c = input()
lst = [a,b,c]

for index,key in enumerate(arr):
    if key in lst:
        print(f"{key}={index}")

# enumerate 함수를 써보고 싶어서 문제에서 시키는거말고 다르게 풀어봤습니다