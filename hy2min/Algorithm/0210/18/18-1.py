record = [
    [65000,35,42,70],
    [70,35,65000,1300],
    [65000,30000,38,42],
]
attendence = [0] * 65536
for ids in record:
    for id in ids:
        attendence[id] +=1

max_id = max(range(1, 65536), key=lambda x: attendence[x])
print(max_id)