def bbq(level):
    if level==4: return
    bbq(level+1)

bbq(0)