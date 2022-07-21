a = int(input())
b = 0
for i in range(a):
    for k in range(a):
        if(b == 9):
            b = 0
        if(k < a-1):
            b = b+1
            print(b, end=" ")
        else:
            b = b+1
            print(b, end="\n")
