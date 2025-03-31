# import sys
# sys.stdin = open("input.txt","r")

N = int(input())
book_list = list(input().split())
P = int(input())    # 손님의 수
people = []
for i in range(P):
    a = list(input().split())
    people.extend(a)
book_list.sort()

def binary_search(key):
    st = 0
    ed = N-1
    cnt = 1
    if key not in book_list:
        return -1
    while True:
        key_num = book_list.index(key)
        mid = (st + ed) // 2
        if book_list[mid] == key:
            return cnt
        elif mid > key_num:
            ed = mid - 1
            cnt += 1
        elif mid < key_num:
            st = mid + 1
            cnt += 1
        if st >= ed:
            return cnt

for i in range(0,2*P-1,2):
    ans = binary_search(people[i])
    if ans == -1:
        print("fail")
    elif ans <= int(people[i+1]):
        print("pass")
    elif ans > int(people[i+1]):
        print("fail")