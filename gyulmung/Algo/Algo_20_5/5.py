char = input()

def bbq(level):
    num_char = ord(char)
    if num_char + level < 65:
        num_char += 26
    elif num_char + level > 90:
        num_char -= 26

    print(chr(num_char + level), end = "")

    if level == 3:
        return
    
    bbq(level + 1)



bbq(-3)