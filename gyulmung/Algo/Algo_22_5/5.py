char1, char2 = map(str, input().split())
string = ['A', 'B', 'C']
Map = [[3, 5, 4, 2, 2, 3], [1, 3, 3, 3, 4, 2], [5, 4, 4, 2, 3, 5]]
price = ['T', 'P', 'G', 'K', 'C']
where = 0


# for i in range(3):
#     for j in range(6):

def abc(lev):
    global where
    if lev == 2:
        return

    if string[lev] == char1:
        for i in range(6):
            if i == int(char2) - 1:
                where = Map[lev][i]

    abc(lev + 1)

abc(0)
print(price[where - 1])