num = int(input())

count1 = 0

while count1 < 3:
    count2 = 0
    while count2 < 5:
        count2 += 1
        print(num, end = "")
    count1 += 1
    print()

# for i in range(3):
#     for j in range(5):
#         print(num, end = "")
#     print()