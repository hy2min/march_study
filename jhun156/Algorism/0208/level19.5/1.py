def main():
    a,b = BBQ()
    print(f"a={a}\nb={b}")

def BBQ():
    lst = [i for i in map(int,input().split())]
    Max = max(lst)
    Min = min(lst)
    return Max,Min

main()