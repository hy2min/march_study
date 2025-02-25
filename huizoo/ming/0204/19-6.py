class Train : 
    def __init__(self, win, name):
        self.win = win
        self.name = name

# trains = [f'train{i}' for i in range(7)]
# trains[0] = Train(15, 'summer')
# trains[1] = Train(33, 'cloe')
# trains[2] = Train(24, 'summer')
# trains[3] = Train(28, 'niki')
# trains[4] = Train(32, 'jenny')
# trains[5] = Train(20, 'summer')
# trains[6] = Train(40, 'coco')

# name_input = input()
# win_input = int(input())

# for i in range(7) : 
#     if trains[i].win == win_input and trains[i].name == name_input : 
#         print(i)

trains = [
    Train(15, 'summer'),
    Train(33, 'cloe'),
    Train(24, 'summer'),
    Train(28, 'niki'),
    Train(32, 'jenny'),
    Train(20, 'summer'),
    Train(40, 'coco')
]

name_input = input()
win_input = int(input())

for i, train in enumerate(trains) : 
    if train.win == win_input and train.name == name_input : 
        print(i)