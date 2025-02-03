arr = [
    [1,1,1],
    [1,2,1],
    [3,6,3],
]

def main():
    a = int(input())
    result = Count(a)
    print(result)

def Count(number):
    count = 0
    for i in range(3):
        result = arr[i].count(number)
        count += result
    
    return count

main()