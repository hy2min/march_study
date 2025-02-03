def max_index(s):
    max_char = max(s)
    max_index = s.index(max_char)
    return max_index

def min_index(s):
    min_char = min(s)
    min_index = s.index(min_char)
    return min_index

s = input()
print(max_index(s))
print(min_index(s))