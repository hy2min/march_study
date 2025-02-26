def main():
    arr = []
    for i in range(3):
        string = input()
        arr.append(string)
    CountLine(arr)

def CountLine(n):
    len_arr = []
    for i in range(3):
        len_arr.append(len(n[i]))
    for i in range(3):
        print(f'{len_arr[i]}={n[i]}')

main()