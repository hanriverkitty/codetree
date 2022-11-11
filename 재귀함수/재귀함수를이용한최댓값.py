import sys
n = int(input())
d = list(map(int,sys.stdin.readline().strip().split()))
def aa(d):
    if(len(d)==1):
        return d[0]
    d.remove(min(d))
    return aa(d)
print(aa(d))