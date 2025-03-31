train = {
    0 : {'win' : 15, 'name' : 'summer'},
    1 : {'win' : 33, 'name' : 'cloe'},
    2 : {'win' : 24, 'name' : 'summer'},
    3 : {'win' : 28, 'name' : 'niki'},
    4 : {'win' : 32, 'name' : 'jenny'},
    5 : {'win' : 20, 'name' : 'summer'},
    6 : {'win' : 40, 'name' : 'coco'},
}

a = input()
b = int(input())

for i in range(len(train)):
    if train[i]['win'] == b and train[i]['name'] == a:
        print(i)