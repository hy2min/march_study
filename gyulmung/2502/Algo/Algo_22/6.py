strings = [input() for _ in range(4)]
Max = int(-1e8)
Min = int(1e8)
Max_s, Min_s = 0, 0

def len_string(lev):
    global Max, Min, Max_s, Min_s
    if lev == 4:
        return

    if Max < len(strings[lev]):
        Max = max(Max, len(strings[lev]))
        Max_s = lev
    if Min > len(strings[lev]):
        Min = min(Min, len(strings[lev]))
        Min_s = lev
    len_string(lev + 1)

len_string(0)
print(f'긴문장:{Max_s}')
print(f'짧은문장:{Min_s}')