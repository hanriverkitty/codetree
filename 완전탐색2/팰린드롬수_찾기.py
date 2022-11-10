#모범답안
x, y = tuple(map(int, input().split()))
ans = 0
for i in range(x, y + 1):
    # 정수 형태를 문자열 배열로 바꿉니다.
    str_i = str(i)

    # 펠린드롬 수가 되기 위해서는,
    # 거꾸로 읽어도 똑같은 수여야 합니다.
    if str_i == str_i[::-1]:
        ans += 1

print(ans)




#제출답안
x,y = map(int,input().split())
ans=0
for i in range(x,y+1):
    num = []
    a = str(i)
    num_b = True
    #배열에 각 자리의 숫자들 넣기
    for j in range(len(a)):
        num.append(int(a[j]))
    #배열을 반으로 쪼개 앞과 뒤가 서로 같은지 확인
    for k in range(len(num)//2):
        if num[k] != num[-1-k]:
            num_b = False
            break
    if num_b==True:
        ans+=1
print(ans)
