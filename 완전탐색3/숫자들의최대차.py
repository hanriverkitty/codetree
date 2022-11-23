n,k = map(int,input().split())

arr=[]
for i in range(n):
    arr.append(int(input()))
ans=0


def count_num(l,r):
    cnt=0
    for elem in arr:
        if l<=elem and elem <=r:
            cnt+=1
    return cnt

ans=0
for i in range(1,10001):
    ans=max(ans,count_num(i,i+k))
print(ans)
