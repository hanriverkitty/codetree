import sys
a = sys.maxsize
n = int(input())
arr = list(map(int,input().split()))
ans=a
for i in range(n):
    arr[i] *= 2
    for j in range(n):
        temp=[]
        for k in range(n):
            if k!=j:
                temp.append(arr[k])
        diff=0
        for k in range(n-2):
            diff+=abs(temp[k+1]-temp[k])
        ans = min(ans,diff)
    arr[i] //= 2

print(ans)