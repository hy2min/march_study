a = int(input())

arr = [a + i for i in range(6)]

def PrintAll():
    global arr
    for i in arr:
        print(i)

PrintAll()