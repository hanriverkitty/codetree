n = int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
ans=0

#해수면 높이 탐색
for i in range(1,1001):
    result=[]
    a=1
    
    #첫번째 빙산에 대한 경우
    if arr[0]>i:
        result.append(1)
    else:
        result.append(0)
        a=0
    
    #result에 저장 후  중간에 잠겨있는곳이 있으면 0처리하고 다음 잠기지않은 빙산은 a값 +1 로 저장
    for j in range(1,n):
        if arr[j]>i:
            if result[j-1] == 0:
                a+=1
                result.append(a)
            
            else:
                result.append(a)
        else:
            result.append(0)
    #max(result)값으로 덩어리가 몇개 나왔는지 확인
    ans = max(ans,max(result))

print(ans)