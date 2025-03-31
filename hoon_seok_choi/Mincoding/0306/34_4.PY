def binary_search(book_list, target, max_time):
    left, right = 0, len(book_list) - 1
    time_used = 0

    while left <= right:
        mid = (left + right) // 2
        time_used += 1  # 한 번 비교할 때마다 1초 소요

        if book_list[mid] == target:
            return "pass" if time_used <= max_time else "fail"
        elif book_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

        if time_used > max_time:
            return "fail"

    return "fail"  # 책을 찾지 못한 경우


# 입력 처리
N = int(input("책의 개수를 입력하세요: "))
books = [input("책 이름을 입력하세요: ") for _ in range(N)]
books.sort()  # 사전순 정렬

M = int(input("단골 손님의 수를 입력하세요: "))
for _ in range(M):
    target_book = input("손님이 원하는 책 이름을 입력하세요: ")
    time_limit = int(input("손님이 준 시간을 입력하세요: "))
    result = binary_search(books, target_book, time_limit)
    print(result)
