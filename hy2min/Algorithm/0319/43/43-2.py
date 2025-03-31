n = int(input())

dic= {'POP': 1,
      'TOM': 1,
      'MC': 1,
      'JASON': 1,
      'KFC': 1}
for _ in range(n):
    key = input()
    if key in dic.keys():
        print('yes')
    else:
        print('no')
