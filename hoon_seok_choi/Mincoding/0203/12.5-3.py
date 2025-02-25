arr = [
    ['D', 'A', 'D'],
    ['Q', 'W', 'Q'],
    ['A', 'S', 'D'],
    ['A', 'S', 'D']
]



def main() :
    a= input()
    find(a)

def find(a) :
    for i in range(4) :
        for j in range(3) :
            if arr[i][j] == a :
                print("존재")
                return
    print("없음")

            

main()