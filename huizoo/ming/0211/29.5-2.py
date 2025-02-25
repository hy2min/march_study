i = int(input())
evid = [-1, 0, 0, 1, 2, 4, 4]
timestamp = [8, 3, 5, 6, 8, 9, 10]

path = []
def detective(x):
    if evid[x] == -1:
        path.append(f'{x}번index(출발)')
        print('\n'.join(path[::-1]))
        path.pop()
        return
    path.append(f'{x}번index({timestamp[x]}시)')
    detective(evid[x])
    path.pop()

detective(i)