n=int(input())
arr=[]
ans=0
for i in range(n):
    x,y = map(int,input().split())
    arr.append((x,y))

for i in range(11):
    for j in range(11):
        for k in range(11):
            success = True
            for x,y in arr:
                if x==i or x==j or x==k:
                    continue
                success=False
            if success:
                ans=1
            
            success = True
            for x,y in arr:
                if y==i or y==j or y==k:
                    continue
                success = False
            if success:
                ans=1

            success = True
            for x,y in arr:
                if x==i or x==j or y==k:
                    continue
                success = False
            if success:
                ans=1
            
            success=True
            for x,y in arr:
                if x==i or y==j or y==k:
                    continue
                success = False
            if success:
                ans=1
            
print(ans)

            
         
