a,b = map(int,input().split())
def game(i):
    while(i>0):
        if(i%10==3 or i%10==6 or i%10==9):
            return True
        i=i//10
    return False


def main_game(a,b):
    cnt = 0
    for i in range(a,b+1):
        if(i%3==0 or game(i)):
            cnt+=1
    return cnt
print(main_game(a,b))