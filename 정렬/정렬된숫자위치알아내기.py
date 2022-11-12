n = int(input())
arr = list(map(int,input().split()))
arr1=[]
for i in range(len(arr)):
    arr1.append([arr[i],i+1])
arr1.sort()
for i in range(len(arr1)):
    arr1[i].append(i+1)

arr1.sort(key=lambda x: x[1])

for i in arr1:
    print(i[2],end=" ")

