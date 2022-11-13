m1,d1,m2,d2 = map(int,input().split())
week=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]


def num_of_days(m, d):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0
    
    for i in range(1, m):
        total_days += days[i]
    
    total_days += d
    
    return total_days    


total_days = num_of_days(m2, d2) - num_of_days(m1, d1)
if(total_days<0):
    a = (7-(abs(total_days)%7))%7
elif(total_days>=0):
    a = total_days%7
print(week[a])