import sys
n,m = map(int,input().split())
arr = list(map(int,sys.stdin.readline().split())) 
result = 0
def aa():
    global m,result,arr
    while m>0:
        result += arr[m-1]
        if(m%2==0):
            m//=2
        else:
            m-=1
    print(result)
aa()