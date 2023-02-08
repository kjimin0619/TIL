# 연습문제
x = int(input())

if 11<=x<=20 :
    print('11~20')
elif 21<=x<=30 :
    print('21~30')
else :
    print('아무것도 해당하지 않음')
    
# 심사문제
age = int(input())
balance = 9000
if 7<=age<=12 : balance -= 650
elif 13<=age<=18 : balance -= 1050
else : balance -= 1250

print(balance)