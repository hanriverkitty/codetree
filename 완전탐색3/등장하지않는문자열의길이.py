n = int(input())
arr=list(input())
ans=0
for i in range(n):
    for j in range(i+1,n):
        cnt=1
        if arr[i]==arr[j]:
            a,b=i,j
            while(b<=n-1 and a<=n-1 and arr[a]==arr[b]):
                cnt+=1
                a+=1
                b+=1
            ans= max(cnt,ans)
print(ans)