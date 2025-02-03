arr = [
    [4,5,6,1,3,1],
    [2,1,3,6,3,6],
]

def main():
    lst = list(Input())
    arr = []
    for i in range(3):
        arr.append(process(lst[i]))
    for i in range(3):
        print(f"{lst[i]}={arr[i]}개")

def Input():
    a,b,c = map(int,input().split())
    return a,b,c

def process(num):
    
    global arr
    count = 0

    for i in range(2):
        result = arr[i].count(num)
        count += result
    return count

main()