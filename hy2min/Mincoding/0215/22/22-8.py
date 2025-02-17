arr = [
    [[2,4],[1,5]],
    [[2,3],[3,6]],
    [[7,3],[1,5]],
]

def abc(level,i):
    if level == len(arr):
        return
    abc(level+1)