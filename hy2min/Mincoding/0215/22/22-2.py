def abc(level,arr):
    if level == 3:
        if arr[0] == arr[1] == arr[2]:
            print("WOW")
        elif arr[0] == arr[1] or arr[0] == arr[2] or arr[1] == arr[2]:
            print("GOOD")
        else:
            print("BAD")
        return
    s = input()
    arr.append(s)

    abc(level + 1,arr)

abc(0,[])