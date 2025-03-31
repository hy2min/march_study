# import sys
# sys.stdin = open("input.txt","r")

def parentheses(string):
    lst = []
    for char in string:
        if char == '(':
            lst.append('(')
        elif char == '{':
            lst.append('{')
        elif char == ')':
            if not lst:
                return 0
            else:
                if lst[-1] == '(':
                    lst.pop()
                elif lst[-1] == '{':
                    return 0
        elif char == '}':
            if not lst:
                return 0
            else:
                if lst[-1] == '{':
                    lst.pop()
                elif lst[-1] == '(':
                    return 0
    if not lst:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1,T+1):
    string = input()
    ans = parentheses(string)
    print(f"#{tc} {ans}")