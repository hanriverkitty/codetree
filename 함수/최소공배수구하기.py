n,m = map(int,input().split())

i=min(n,m)
while(i>1):
    if(n%i==0 and m%i==0):
        print(i*(n//i)*(m//i))
        break
    else:
        i-=1

if i==1:
    print(m*n)