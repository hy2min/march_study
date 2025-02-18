# def abc(i, Sum):
#     global total
#     if i == N :
#         total = Sum
#         return
#     max_idx = i + arr[i:].index(max(arr[i:]))
#     if max_idx == i:
#         abc(i+1, Sum)
#         return
#     else:
#         abc(max_idx+1, Sum + (max_idx-i)*arr[max_idx] - sum(arr[i:max_idx]))
#         return
#
# t = int(input())
# for tc in range(1, t+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     total = 0
#     abc(0, 0)
#     print(f'#{tc} {total}')


def max_profit(prices):
    """
    주어진 가격 리스트를 바탕으로 최대 이익을 계산합니다.

    아이디어:
    - 리스트를 뒤에서부터 순회하면서 '현재까지의 최고 가격(max_price_so_far)'를 갱신합니다.
    - 각 날짜의 이익은 (현재까지의 최고 가격 - 해당 날짜의 가격)입니다.
    - 모든 날짜의 이익을 누적하면 최대 이익이 됩니다.

    :param prices: 각 날짜의 가격을 담은 리스트
    :return: 계산된 최대 이익 (정수)
    """
    max_profit = 0  # 누적 최대 이익
    max_price_so_far = 0  # 현재까지 확인한 가격 중 최고 가격

    # 마지막 날짜부터 처음 날짜까지 역순으로 순회
    for price in reversed(prices):
        # 만약 현재 가격이 지금까지 본 최고 가격보다 크다면, 갱신합니다.
        if price > max_price_so_far:
            max_price_so_far = price
        # 현재 날짜에 살 경우, 미래에 최고 가격에 팔 수 있으므로 이익을 계산합니다.
        max_profit += max_price_so_far - price

    return max_profit


def solve_max_profit():
    """
    테스트 케이스 수와 각 케이스별 데이터를 입력받아 최대 이익을 계산하고 출력합니다.
    """
    T = int(input().strip())  # 테스트 케이스의 수

    for t in range(1, T + 1):
        N = int(input().strip())  # 날짜의 수 (실제 계산에는 사용하지 않음)
        prices = list(map(int, input().split()))  # 날짜별 가격 리스트
        result = max_profit(prices)  # 최대 이익 계산
        print(f"#{t} {result}")


# 문제 해결 함수 실행
solve_max_profit()
