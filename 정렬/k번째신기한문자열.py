import sys
n,k,T = (sys.stdin.readline().strip().split())

arr=[]
arr1=[]
for i in range(int(n)):
    arr.append(sys.stdin.readline().strip())
cnt=0
for i in arr:
    if(len(i)>len(T)):
        if(i[:len(T)]==T):
            arr1.append(i)
arr1.sort()
print(arr1[int(k)-1])