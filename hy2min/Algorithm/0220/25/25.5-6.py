s = input()
cnt = 0
url_start = ['http://', 'https://']
url_end = ['.com','.co.kr','.org','.net']

i=0
while i < len(s):
    # 시작
    for start in url_start:
        if s[i:i+len(start)].lower() == start:
            s_idx = i + len(start)

    # 끝
            for end in url_end:
                e_idx = s.find(end, s_idx)
                if e_idx != -1 and (e_idx-s_idx) >= 3:
                    cnt += 1
                    i = e_idx
                    break

    i += 1

print(str(cnt)+'개')
