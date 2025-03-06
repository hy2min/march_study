def expand_center(s, left, right):
    """
    주어진 문자열 s에서 left와 right를 중심으로 좌우 확장하며
    최대 회문 길이를 반환하는 함수
    """
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1  # 마지막에 한 번 더 진행한 것을 보정


def longest_palindrome_in_line(s):
    """
    문자열 s에서 존재하는 가장 긴 회문의 길이를 반환
    """
    max_length = 0
    for i in range(len(s)):
        # 홀수 길이 회문: 중심이 하나일 때
        len1 = expand_center(s, i, i)
        # 짝수 길이 회문: 중심이 두 개일 때
        len2 = expand_center(s, i, i + 1)
        max_length = max(max_length, len1, len2)
    return max_length


for tc in range(10):
    t = int(input().strip())
    arr = [list(input().strip()) for _ in range(100)]
    max_length = 0

    # 행(가로) 회문 검사
    for row in arr:
        max_length = max(max_length, longest_palindrome_in_line(row))

    # 열(세로) 회문 검사: zip(*arr)로 전치하여 각 열을 튜플로 처리
    for col in zip(*arr):
        max_length = max(max_length, longest_palindrome_in_line(col))

    print(f'#{tc + 1} {max_length}')
