# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
pairs = [
    tuple(map(int, input().split()))
    for _ in range(m)
]


def count_num(first, second):
    cnt = 0
    # (first, second) 쌍이 (a, b) 혹은 (b, a)라면
    # 그 개수를 세줍니다.
    for a, b in pairs:
        if (first, second) in [(a, b), (b, a)]:
            cnt += 1

    return cnt


ans = 0
# 모든 쌍 (i, j)를 잡아보며
# 각 쌍이 몇 번씩 나왔는지를 확인하여
# 그 중 최댓값을 계산합니다.
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        ans = max(ans, count_num(i, j))

print(ans)



# n,m = map(int,input().split())
# arr=[]
# for i in range(m):
#     arr.append(list(map(int,input().split())))
# ans=0
# for i in range(m):
#     a,b = arr[i]
#     cnt=0
#     for q,w in arr:
#         if (a==q and b==w) or (a==w and b==q):
#             cnt+=1
#     ans = max(ans,cnt)
# print(ans)