from collections import Counter

s = list(input())
s.sort(reverse=True)

count = Counter(s[:6])
ans = count.most_common(1)

print(ans[0][0])
