arr=[0,7,-3,-5,-4,-2,6,5,-9,1,0]
dp=[0]*11
for i in range(len(arr)):
    jp1=dp[i-1]
    jp2=dp[i-2]
    jp3=dp[i//2]
    dp[i]=jp1+arr[i] # 한칸전의 값 + 현재 위치의값
    if dp[i]<jp2+arr[i]: #위에서 구한 값이랑 vs (두칸전 값 + 현재 위치의 값)
        dp[i]=jp2+arr[i]
    if i%2==0 and dp[i]<jp3+arr[i]: # 위에서 구했던 Max값 vs (//2 한 값 + 현재 위치의 값)
        dp[i]=jp3+arr[i]
print(dp[10])

