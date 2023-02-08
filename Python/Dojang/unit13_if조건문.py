'''
13. 조건문

pass 키워드 : 아무일도 하지 않고 넘어가기
나중에 작성해야 할 코드를 표시할 때 사용할 수 있음
이때, # TODO : ~~ 이런 주석을 달 것

** 프로그래머들은 주석에 TODO 이외에도 FIXME, BUG, NOTE 등 일관된 주석을 사용함

'''

# 연습문제
price = int(input())
real_price = None
name = input()

if name == 'Cash3000':
    real_price = price - 3000
    print(real_price)
    
if name == 'Cash5000':
    real_price = price - 5000
    print(real_price)

