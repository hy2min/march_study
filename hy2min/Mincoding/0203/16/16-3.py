while True:
    string = input()
    if len(string) <= 5:
        break
n = int(input())

answer = list(string)

print("".join(answer[:n]), end="")
print("A", end="")
print("".join(answer[n:]))
