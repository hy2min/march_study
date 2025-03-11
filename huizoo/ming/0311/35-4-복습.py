def heapify_down(idx, size):
    smallest = idx
    left = 2 * idx + 1
    right = 2 * idx + 2

    if left < size and arr2[left][0] < arr2[smallest][0]:
        smallest = left
    if right < size and arr2[right][0] < arr2[smallest][0]:
        smallest = right
    if smallest != idx:
        arr2[idx], arr2[smallest] = arr2[smallest], arr2[idx]
        heapify_down(smallest, size)


def heapify_up(idx):
    while idx > 0:
        parent = (idx - 1) // 2
        if arr2[idx][0] < arr2[parent][0]:
            arr2[idx], arr2[parent] = arr2[parent], arr2[idx]
            idx = parent
        else:
            break


def build_heap():
    size = len(arr2)
    for i in range(size // 2 - 1, -1, -1):
        heapify_down(i, size)


def heap_pop():
    if not arr2:
        return None
    root = arr2[0]
    arr2[0] = arr2[-1]
    arr2.pop()
    if arr2:
        heapify_down(0, len(arr2))
    return root


def heap_push(item):
    arr2.append(item)
    heapify_up(len(arr2) - 1)


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr2 = []
for i in range(n - 1):
    for j in range(i + 1, n):
        if arr[i][j] > 0:
            arr2.append((arr[i][j], i, j))

# 1) 최소 힙 만들기
build_heap()

ans = 0
for _ in range(10):
    cheapest = heap_pop()
    if not cheapest:
        break

    cost, u, v = cheapest
    cost *= 2  # 문제에 맞게 갱신
    ans = cost

    heap_push((cost, u, v))

print(f'{ans}만원')
