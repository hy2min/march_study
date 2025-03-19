def heapify(arr, n, i):
    largest = i  # 루트를 가장 큰 값으로 가정
    left = 2 * i + 1  # 왼쪽 자식 노드 (0-based index)
    right = 2 * i + 2  # 오른쪽 자식 노드 (0-based index)

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def max_heap_sort(s):
    arr = list(s)  # 문자열을 리스트로 변환 (0-based index 사용)
    n = len(arr)

    # Max Heap 구성 (루트에 최대값을 넣는 과정)
    for i in range(n // 2 - 1, -1, -1):  # 마지막 부모 노드부터 heapify
        heapify(arr, n, i)

    # Heap Sort 실행
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 최대값을 끝으로 이동
        heapify(arr, i, 0)  # 남은 요소에 대해 heapify

    return ''.join(arr[::-1])


st = input()
print(max_heap_sort(st))
