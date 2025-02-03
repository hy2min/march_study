arr = [
    ['D','A','D'],
    ['Q','W','Q'],
    ['A','S','D'],
    ['A','S','D'],
]

def find(chr):

    count = 0
    global arr
    for i in range(4):
        result = arr[i].count(chr)
        count += result
    if count > 0:
        print("존재")
    else:
        print("없음")

def main():
    a = input()
    find(a)

main()