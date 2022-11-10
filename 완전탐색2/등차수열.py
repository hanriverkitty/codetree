n = int(input())
arr = list(map(int,input().split()))
result=0
#가운데 낄 값 탐색
for i in range(1,101):
    cnt=0
    #해당값이 두 값의 사이에 있는지 확인
    for j in range(len(arr)):
        for k in range(j+1,len(arr)):
            if arr[j]-i == i-arr[k]:
                cnt+=1
    result = max(result,cnt)

print(result)