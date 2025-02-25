import sys
sys.stdin = open("input.txt","r")

t = int(input())

for case_num in range(1, t + 1):
    k, n, m = map(int, input().split())
    stations = list(map(int, input().split()))

    location = 0
    cnt = 0

    while location + k < n:
        next_location = location + k

        while next_location > location and next_location not in stations:
            next_location -= 1

        if next_location == location:
            cnt = 0
            break

        location = next_location
        cnt += 1

    print(f"#{case_num} {cnt}")