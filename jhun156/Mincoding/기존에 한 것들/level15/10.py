def main():
    arr = [[0] * 10 for _ in range(3)]
    a = input()
    b = input()
    c = input()
    lst = [a,b,c]
    for i in range(3):
        for j in range(len(lst[i])):
            arr[i][j] = lst[i][j]
    CountLine(arr)

def CountLine(lst):
    count_list = []
    chr_list = [''] * 3
    for i in range(3):
        count = 0
        for j in range(10):
            if lst[i][j] != 0:
                count += 1
                chr_list[i] += lst[i][j]
        count_list.append(count)
    for i in range(3):
        print(f"{count_list[i]}={chr_list[i]}")

main()

