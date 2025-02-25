def folow_node(n):
    return n+54
n = int(input())
for i in range(4):
    ans = chr(folow_node(n)+i)
    print(ans, end="")