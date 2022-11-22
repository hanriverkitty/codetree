n = int(input())

arr=list(input())

def dist():
    dist = n
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]=='1' and arr[j]=='1':
                dist = min(dist,j-i)
    return dist


ans = 0

for i in range(n):
    if arr[i]=='0':
        arr[i]='1'
        ans = max(ans,dist())
        arr[i]='0'

print(ans)