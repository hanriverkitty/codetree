a,b = map(int,input().split())
cnt=0
def sosu(i):
    for j in range(2,i):
        if(i%j==0):
            return False
    return True

for k in range(a,b+1):
    if(sosu(k) and ((k%10 + k//10)%2==0)):
        cnt+=1
print(cnt)








