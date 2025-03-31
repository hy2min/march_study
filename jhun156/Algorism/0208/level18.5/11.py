string = input()

def find_ghost(num):
    if string[num:num+5] == "GHOST":
        return 1
    else:
        return 0

result = 0
for i in range(len(string)-4):
    ans = find_ghost(i)
    result += ans

if result != 0:
    print("존재")
else:
    print("존재하지 않음")