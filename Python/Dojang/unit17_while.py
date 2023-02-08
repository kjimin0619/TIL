'''
17. while

- 반복횟수가 정해지지 않은 경우
random 모듈 활용하여 난수 생성
random.randint(a,b) : a부터 b까지 난수 생성

- 요소 무작위 선택
random.choice(시퀀스객체)
'''
# random 난수 생성
import random
print(random.randint(1,6))
print('\n')
i = 0
while i != 3:
    i = random.randint(1,6)
    print(i)
    
# 요소 무작위 선택
print('random choice')
dice = [1,2,3,4,5,6]
print(random.choice(dice))

# 연습문제
i = 2
j = 5

while i < 33 and j >=1 :
    print(i,j)
    i *= 2
    j -= 1


# 심사 문제
price = 1350
money = int(input())

while money >= 1350 :
    money -= price
    print(money)
