arr = [i for i in input().split()]

count = 0

for i in arr:
    if i == "A":
        count += 1
print(f"문자A는 {count}개발견")

for i in range(len(arr)):
    if arr[i] == "A":
        print(f"{i}번")


