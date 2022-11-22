n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))

for i in range(100001):
    k=i
    cnt=0
    for a,b in arr:
        k*=2
        if k<a or k>b:
            continue
        cnt+=1
    if cnt==len(arr):
        print(i)
        break