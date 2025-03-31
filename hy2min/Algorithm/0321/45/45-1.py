def build(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return

    mid = (start + end) // 2
    left = node * 2
    right = node * 2 + 1
    build(left, start, mid)
    build(right, mid+1, end)

    tree[node] = min(tree[left], tree[right])

def query(node, start, end, left, right):
    if right < start or left > end:  # 완전히 범위 밖일 경우
        return float('inf')  # 비교용으로 매우 큰 값

    if left <= start and right >= end:
        return tree[node]

    mid = (start + end) // 2

    left_min = query(node*2, start, mid, left, right)
    right_min = query(node*2+1, mid+1, end, left, right)

    return min(left_min, right_min)


n, m = map(int, input().split())
tree = [0] * (n*4)
arr = [0] + list(map(int, input().split()))

build(1, 1, n)

for _ in range(m):
    s, e = map(int, input().split())
    print(query(1, 1, n, s, e))
