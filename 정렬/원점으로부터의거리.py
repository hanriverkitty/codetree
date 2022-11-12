n = int(input())
aa=[]
for i in range(n):
    a,b = map(int,(input().split()))
    aa.append((abs(a)+abs(b),i+1))
aa.sort(key=lambda x : (x[0],x[1]))
for i in aa:
    print(i[1])