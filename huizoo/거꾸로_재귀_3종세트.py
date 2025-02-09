def a(st) : 
    if len(st) > 1 : 
        a(st[1:])
    print(st[0], end = "")

def b(st) : 
    if len(st) == 0 : 
        return ""
    return b(st[1:]) + st[0]

def c(st) : 
    if len(st) == 0 : 
        return "" 
    return st[-1] + c(st[:-1])

a("mango")
print()
print(b("mango"))
print(c("mango"))