from collections import deque

q = deque(input())
ret = ''

while q:
    s = q.popleft()

    if s == '(':
        ret += s
        while q and q[0] == '(':
            q.popleft()
        continue

    if s == ')':
        ret += s
        while q and q[0] == ')':
            q.popleft()
        continue

    if s == '^' and len(q) >= 2 and q[0] =='^' and q[1] == '^':
        ret +='^^'
        q.popleft()
        q.popleft()
        continue

    if s == '^' and len(q) >= 2 and q[1] == '^':
        if q[0] not in '_()':
            ret += '^_^'
        else:
            ret += (s + q.popleft() + q.popleft())

    # ret = q+

print(''.join(ret))