arr = [
    [['A','T','B'],
     ['C','C','B']],
    [['A','A','A'],
     ['B','B','C']]
]

s = input()

def abc(arr):

    for i in range(len(arr)):
        if type(arr[i]) == str:
            if arr[i] == s:
                return True
        else:
            if abc(arr[i]):
                return True
    return False


if abc(arr):
    print('발견')
else:
    print('미발견')