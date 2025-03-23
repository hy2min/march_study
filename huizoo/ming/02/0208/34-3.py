N = int(input())
books = input().split()
books.sort()
M = int(input())

for _ in range(M) : 
    book, S = input().split()
    S = int(S)

    start = 0
    end = len(books) - 1
    found = 0

    while start <= end and 0 < S : 
        S -= 1
        mid = (start + end) // 2
        if books[mid] == book : 
            found = 1
            break
        elif books[mid] < book : 
            start = mid + 1
        else : 
            end = mid - 1
    if found :
        print('pass')
    else : 
        print('fail')