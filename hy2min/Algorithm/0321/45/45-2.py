
def build(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return

    mid = (start+end) // 2
    left = node * 2
    right = node * 2 + 1

    build(left, start, mid)
    build(right, mid+1, end)

    tree[node] = min(tree[left], tree[right])


def query(node, start, end, a, b):
    if b < start or a > end:
        return float('inf')
    if a <= start and b >= end:
        return tree[node]

    mid = (start + end) // 2
    left_min = query(node*2, start, mid, a, b)
    right_min = query(node*2+1, mid+1, end, a, b)

    return min(left_min, right_min)

def update(node, start, end, idx, value):
    if start == end:
        arr[idx] = value
        tree[node] = value
        return

    mid = (start + end) // 2
    left = node * 2
    right = node * 2 + 1

    if start <= idx <= mid:
        update(left, start, mid, idx, value)
    else:
        update(right, mid+1, end, idx, value)

    tree[node] = min(tree[left], tree[right])


n = int(input())
tree = [0] * (4*n)
arr = [0] + list(map(int, input().split()))
build(1, 1, n)

m = int(input())
for _ in range(m):
    case, a, b = map(int, input().split())
    if case == 1:
        update(1, 1, n, a, b)
    if case == 2:
       ret = query(1, 1, n, a, b)
       print(ret)


# 시간초과