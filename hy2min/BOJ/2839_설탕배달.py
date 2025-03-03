n = int(input())
five = n // 5
ans = -1
while five >= 0:
    remain = n - (5*five)
    if remain % 3 == 0:
        three = remain // 3
        ans  = three + five
        break
    else:
        five -= 1
print(ans)