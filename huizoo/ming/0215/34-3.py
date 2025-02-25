N = int(input())
books = list(input().split())
books.sort()
M = int(input())
for _ in range(M):
    book, time = input().split()
    time = int(time)
    start = 0
    end = len(books)-1
    found = 0
    while start <= end:
        time -= 1
        mid = (start+end)//2
        if books[mid] < book:
            start = mid+1
        elif books[mid] > book:
            end = mid-1
        else:
            found = 1
            break
        if time == 0:
            break
    if found:
        print('pass')
    else:
        print('fail')