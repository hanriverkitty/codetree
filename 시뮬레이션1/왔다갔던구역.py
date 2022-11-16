n = int(input())
arr = [0]*2001
offset = 1000
a=0
for i in range(n):
    c,b = input().split()
    if(b=="R"):
        for l in range(a+offset,a+int(c)+offset):
            arr[l]+=1
        a+=int(c)
        
    else:
        for k in range(a-int(c)+offset,a+offset):
            arr[k]+=1
        a-=int(c)
cnt = 0
for elem in arr:
	if elem >= 2:
		cnt += 1
print(cnt)