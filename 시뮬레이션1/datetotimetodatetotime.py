a,b,c = map(int,input().split())

if a<11:
    print(-1)
elif a<=11 and b<11:
    print(-1)
elif a<=11 and b<=11 and c<11:
    print(-1)
else:
    day = 11
    hour = 11
    minute=11
    cnt=0

    cnt = ((a-11)*60*24)+b*60+c-(60*11+11)
    print(cnt)