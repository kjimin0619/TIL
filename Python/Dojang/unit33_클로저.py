'''
33. 클로저 사용하기
클로저와 람다표현식은 함께 사용되는 경우가 많음
* 람다 표현식 : 이름없는 익명함수
* 클로저 : 함수를 둘러싼 환경을 유지했다가 나중에 다시 사용하는 함수
<변수의 사용범위>
전역변수 : 스크립트 전체에서 접근할 수 있는 변수
지역변수 : 변수를 만든 함수 안에서만 접근할 수 있는 변수

* 함수 안에서 전역 변수의 값을 변경하려면, global 키워드를 사용해야 함
* 전역 변수가 없을 때 함수 안에서 global을 선언하면 해당 변수는 전역변수가 됨

네임스페이스 : 파이썬 변수가 저장되는 공간
locals() 함수를 사용하면 현재 네임스페이스를 딕셔너리 형태로 출력

'''
# global 키워드
x = 10
def foo():
    global x
    x = 20
    print('함수내 호출 ' ,x)
    
foo()
print('전역 스크립트 호출', x)


# 바깥쪽 함수의 지역 변수를 안쪽 함수에서 변경하기
# nonlocal 지역변수
# nonlocal은 현재 함수의 바깥쪽에 있는 지역 변수를 찾을 때 가장 가까운 함수부터 먼저 찾음
def A():
    x = 10
    def B() :
        nonlocal x # 현재 함수의 바깥쪽에 있는 지역 변수 사용
        x = 20
    
    B()
    print(x)

A() # 20 출력

## 클로저 사용하기
# 함수를 클로저 형태로 만들기
# 함수를 둘러싼 환경(지역변수,코드 등)을 계속 유지하다가, 함수를 호출할 때 다시 꺼내서 사용하는 함수

a = 10
def add(x):
    return a + x

print(add(1)) # 11

#  클로저
# 정의 : 함수를 둘러싼 환경(지역 변수, 코드 등)을 계속 유지하다가, 함수를 호출할 때 다시 꺼내서 사용하는 함수
def calc():
    # 클로저
    a = 3
    b = 5
    def mul_add(x):
        return a*x + b
    return mul_add

c = calc()
print(c(1), c(2)) # 8, 11

# 람다와 클로저
# 람다 :  이름 없는 익명 함수
# 클로저 : 함수를 둘러싼 환경을 유지했다가 나중에 다시 사용하는 함수
def calc_lambda():
    a = 3
    b = 5
    return lambda x : a*x + b

c_l = calc_lambda()
print(c_l(3)) # 14

# 클로저의 지역 변수 변경하기
def calc_c():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total
        total = total + a*x + b
        print(total)
        return total
    
    return mul_add

cc = calc_c()
cc(1)
cc(2) # 8, 19

## 호출 횟수 카운트
def counter():
    i = 0
    def count():
        nonlocal i
        i = i + 1
        return i
    return count

c = counter()
for i in range(10):
    print(i, c(), end=' ')
    
# 심사 문제
def countdown(n):
    def count():
        nonlocal n
        re = n
        n = n - 1
        return re
    return count

n = int(input())
c = countdown(n)
for i in range(n):
    print(c(), end=' ')
    
'''

## 연습문제 : 호출 횟수를 세는 함수 만들기
def counter():
    i = 0
    def count():
        nonlocal i
        i += 1
        return i
    return count

c = counter()
for i in range(10):
    print(c(), end=' ')
    
## 심사문제 : 카운트다운 함수 만들기
def countdown(n):
    c = n
    def down():
        nonlocal c
        re = c
        c -= 1
        return re

    return down
n = int(input())
c = countdown(n)
for i in range(n):
    print(c())

'''