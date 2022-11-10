import sys
n1,n2 = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))
index =0
count=0
for i in range(0,len(A)):
    if(A[i]==B[0]):
        index=i
        break

for i in range(0,len(B)):
    if(B[i]!=A[i+index]):
        count+=1
        break
if (count==0):
    print("Yes")
else:
    print("No")
