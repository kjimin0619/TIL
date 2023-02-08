'''
20.  FizzBuzz 문제
<규칙>
1에서 100까지 출력
3의 배수는 Fizz 출력
5의 배수는 Buzz 출력
3과 5의 공배수는 FizzBuzz 출력

'''
# my code
for i in range(1,101):
    if i % 15 == 0 : print('FizzBuzz') # 가독성을 위해, i%3==0 && i % 5 ==0으로 의미를 명확하게 드러내는 것이 좋음
    elif i % 3 == 0 : print('Fizz')
    elif i % 5 == 0 : print('Buzz')
    else : print(i)
    
# 코드 단축하기
print('\n코드 단축')
# 문자열에 True(1)를 곱하면 문자열 그래도, False를 곱하면 출력되지 않음
# 빈 문자열 ''는 False로, or과 논리 연산 진행하여 3의 배수도, 5의 배수도 아닌 수는 그대로 출력
for i in range(1,101):
    print('Fizz'*(i%3==0) + 'Buzz'*(i%5==0) or i)
    

# 2와 11의 배수, 공배수 처리하기
print('\n2와 11의 공배수 구하기')
for i in range(1,101):
    print('Fizz'*(i%2==0) + 'Buzz'*(i%11==0) or i)

# 심사문제, 사용자 입력 및 5와 7의 공배수, 배수 처리하기
start, end = map(int,input().split())
for i in range(start, end +1):
    print('Fizz'*(i%5==0) + 'Buzz'*(i%7==0) or i)