def binary_search(book,s):
    start, end = 0, N-1
    n = 0

    while start <= end:
        mid = (start + end) // 2
        n += 1

        if n > s:
            return 0

        if books[mid] == book:
            return 1
        elif books[mid] < book:
            start = mid + 1
        else:
            end = mid - 1
    return 0

N = int(input())
books = list(input().split())
books.sort()
M = int(input())

for _ in range(M):
    book, s = input().split()
    s = int(s)


    if binary_search(book, s):
        print("pass")
    else:
        print("fail")