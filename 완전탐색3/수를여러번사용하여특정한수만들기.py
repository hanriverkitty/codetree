a,b,c = map(int,input().split())

n = c//a+1
m = c//b+1
ans=0
for i in range(n):
    sum1=0
    for j in range(m):
        if (i*a + j*b) <= c:
            sum1 = (i*a + j*b)
    ans = max(ans,sum1)
print(ans)
        
