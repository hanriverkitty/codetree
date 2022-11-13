n = int(input())
arr=[]
for i in range(n):
    x,y=map(int,input().split())
    arr.append((x,y))
ans=10000000

for i in range(2,101,2):
    for j in range(2,101,2):
        temp=0
        one=0
        two=0
        three=0
        four=0
        for x,y in arr:
            if (x>i and y<j):
                one+=1
            elif (x<i and y<j):
                two+=1
            elif (x<i and y>j):
                three+=1
            else:
                four+=1
            temp = max(one,two,three,four)
        ans = min(ans,temp)

print(ans)