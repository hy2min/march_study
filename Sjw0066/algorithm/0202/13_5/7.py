arr=[['D','A','S'],['Q','W','V'],['R','T','Y']]

def main():
    num1 = list(map(int,input().split()))
    num2 = list(map(int,input().split()))
    
    Find(num1,num2)


def Find(num1,num2):
    print(arr[num1[0]][num1[1]],end=" ")
    print(arr[num2[0]][num2[1]])

main()