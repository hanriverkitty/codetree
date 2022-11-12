n = int(input())
l = list(map(int,input().split()))
l.sort()
arr=[]
for i in range(len(l)//2):
    arr.append(l[i]+l[-i-1])
print(max(arr))