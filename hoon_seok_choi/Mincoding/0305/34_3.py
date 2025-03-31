def binary_search(books, target, max_time):
    start = 0
    end = len(books) - 1
    comparisons = 0  # 비교 횟수 추적

    while start <= end:
        comparisons += 1  # 비교 횟수 증가
        if comparisons > max_time:  # 시간 초과 확인
            return "fail"

        mid = (start + end) // 2
        if books[mid] == target:
            return "pass"
        elif books[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return "fail"  # 책을 찾지 못한 경우


# 입력 처리
n = int(input())  # 책의 개수
books = input().split()  # 책 이름 리스트
m = int(input())  # 손님의 수

queries = []
for _ in range(m):
    query = input().split()
    queries.append((query[0], int(query[1])))  # (책 이름, 제한 시간)

# 책 이름 정렬
books.sort()

# 손님 요청 처리
for book_name, max_time in queries:
    result = binary_search(books, book_name, max_time)
    print(result)
