n = int(input())
ans=0
simul=[]
for i in range(n):
    simul.append(tuple(map(int,input().split())))  

for i in range(1,4):
    arr=[0]*4
    arr[i]=1
    score=0
    for a,b,c in simul:
        arr[a],arr[b]=arr[b],arr[a]
        if arr[c]==1:
            score+=1
    ans = max(ans,score)
print(ans)