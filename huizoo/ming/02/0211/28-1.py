friend = ['Chloe','Diane','Bob','Amy','Edger']
triangle = [
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,0,1,0],
    [0,0,0,0,1],
    [0,0,0,0,0],
]
like = -1

rotated_triangle = list(zip(*triangle))
for i in range(5):
    like2 = sum(rotated_triangle[i])
    if like < like2 :
        like = like2
        popular = friend[i]

print(popular)
    
