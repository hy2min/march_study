arr = [
    [
        [2,4],
        [1,5],
    ],
    [
        [2,3],
        [3,6],
    ],
    [
        [7,3],
        [1,5],
    ],
]

n = int(input())
print(f"MAX={max(max(arr[n]))}")
print(f"MIN={min(min(arr[n]))}")