n,m = map(int,input().split())
arr = list(map(int,input().split()))
ans=0
for i in range(n):
    index = i
    a_sum=0
    for j in range(m):
        a_sum+=arr[index-1]
        index = arr[index-1]
    ans = max(ans,a_sum)

print(ans)