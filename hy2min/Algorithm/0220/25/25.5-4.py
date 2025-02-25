y, m, d = input().split('.')
y_cnt = 1
m_cnt = 1
d_cnt = 1

if m == 'X':
    m_cnt = 9
if m == '1X' or m == 'XX':
    m_cnt = 3

if d == 'X':
    d_cnt = 9
if d == '1X' or d == '2X':
    d_cnt = 10
if d == '3X':
    d_cnt = 2
if d == 'XX':
    d_cnt = 22
if d[0] == 'X' and d[1] == '0':
    d_cnt =3
if d[0] == 'X' and d[1] == '1':
    d_cnt =3
if d[0] == 'X' and '2' <= d[1] <= '9':
    d_cnt = 2

ans = y_cnt * m_cnt * d_cnt
print(ans)