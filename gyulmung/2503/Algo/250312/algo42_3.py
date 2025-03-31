import sys
sys.stdin=open('input.txt','r')

from collections import deque
string = input()
arr = ['BTS','SBS','BS','CBS','SES']
st = 0

for i in range(5):
    if arr[i][0] == string[0]:
        st = i

q = deque()
q.append((arr[st],1))

while 1:
    Plus, cnt = q.popleft()
    if Plus == string:
        print(cnt)
        break

    for i in range(5):
        q.append((Plus+arr[i], cnt + 1))