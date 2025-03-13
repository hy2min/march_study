def babygin(lst):
    for i, num in enumerate(lst):
        if i < 8 and num and lst[i+1] and lst[i+2]:
            return True
        if num >= 3:
            return True
    return False

def card():
    for i in range(0, 12, 2):
        one[arr[i]] += 1
        if i >= 4 and babygin(one):
            return 1
        two[arr[i+1]] += 1
        if i >= 4 and babygin(two):
            return 2
    return 0

T = int(input())
for tc in range(1, T+1):
    arr = tuple(map(int, input().split()))
    one = [0]*10
    two = [0]*10
    print(f'#{tc} {card()}')
