'''
@로 시작하는 것들
함수를 수정하지 않은 상태에서 추가 기능을 구현할 때 사용

'''
# 데코레이터 trace. 호출할 함수를 매개변수로 받음
# 함수 안에서 함수를 만들고 반환하는 클로저 형태
def trace(func):
    def wrapper(): # 호출할 함수를 감싸는 함수
        print(func.__name__, '함수시작')
        func()
        print(func.__name__, '함수 끝')
    return wrapper

def hello() :
    print('hello')
    
trace_hello = trace(hello)
trace_hello()

## @로 데코레이터 사용하기
# @데코레이터 형식
print('\n@ 사용하기')
@trace
def hello() :
    print('hello!')
    
hello()
    
## 데코레이터 여러 개 지정하기
'''
@데코레이터1
@데코레이터2

실행순서는 위에서 아래
'''

## 매개변수와 반환값을 처리하는 데코레이터
def trace(func):
    def wrapper(a,b):
        r = func(a,b)
        print('a = {}, b = {} ==>> {}'.format(a,b,r))
        
        return r + 8
    return wrapper

@trace
def add(a,b) :
    return a + b

print(add(10,80))

## 가변형 인수 함수 데코레이터
def trace(func):
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        print('{0}(args={1}, kwargs={2}) ==> {3}'.format(func.__name__, args, kwargs, r))

        return r
    return wrapper
 
@trace                   # @데코레이터
def get_max(*args):      # 위치 인수를 사용하는 가변 인수 함수
    return max(args)
 
@trace                   # @데코레이터
def get_min(**kwargs):   # 키워드 인수를 사용하는 가변 인수 함수
    return min(kwargs.values())
 
print(get_max(10, 20))
print(get_min(x=10, y=20, z=30))
        

## 메서드에 데코레이터 사용
# 클래스 메서드에 데코레이터를 사용할 떄는 self 를 주의할 것
# 인스턴스 메서드는 항상 self를 받으므로 데코레이터를 만들 때도 첫 번째 매개변수는 self로 지정

## 매개변수가 있는 데코레이터 만들기
# 반환값이 특정수의 배수인지 확인하는 데코레이터
def is_multiple(x):
    def real_decorator(func):
        def wrapper(a,b):
            r = func(a,b)
            if r % x == 0 :
                print('{}의 반환값 {}은 {}의 배수입니다.'.format(func.__name__, r, x))
                
            else:
                print('{}의 배수 아님'.format(x))
                
            return r
        return wrapper
    return real_decorator

@is_multiple(3)
def add(a,b):
    return a + b

add(10, 20)

## 클래스로 데코레이터 만들기
# 클래스를 활용할 때는 인스턴스를 함수처럼 호출하게 해주는 __call__ 메서드 구현

class Trace:
    def __init__(self,func): # 호출할 함수를 인스턴스의 초깃값으로 받음
        self.func = func # 호출할 함수를 속성 func에 저장
    
    def __call__(self):
        print(self.func.__name__, '함수시작')
        
        self.func() # 속성 func에 저장된 함수 호출
        
        print(self.func.__name__, '함수 끝')
        
@Trace
def hello():
    print('hello')
    
hello()

# 참고 : 클래스로 만든 데코레이터는, 데코레이터의 반환값을 호출하는 방식으로 사용할 수 있음
print()
def hello():
    print('hello')
trace_hello = Trace(hello)
trace_hello()

## 클래스로 매개변수와 반환값을 처리하는 데코레이터 만들기
# 위치 인수 & 키워드 인수 중복 사용
class Trace:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        r = self.func(*args, **kwargs)
        print('{0}(args={1}, kwargs={2}) -> {3}'.format(self.func.__name__, args, kwargs, r))
        
        return r

@Trace
def add(a,b):
    return a + b

print(add(10, 2000))
print(add(a = 10, b = 80))

## 클래스로 매개변수가 있는 데코레이터 만들기
print()
class IsMultiple:
    def __init__(self,x):
        self.x = x # 데코레이터가 사용할 매개변수를 받음
    
    def __call__(self, func): # 호출할 함수를 매개변수로 받음
        def wrapper(a, b) : # 호출할 함수의 매개변수와 똑같이 지정
            r = func(a,b)
            
            if r % self.x == 0 :
                print('{}와 {}의 연산 결과는 {}의 배수입니다'.format(a,b, self.x))
                
            else :
                print('배수아님')
                
            return r
        return wrapper
    
    
@IsMultiple(3)    # 데코레이터(인수)
def add(a, b):
    return a + b
 
print(add(10, 20))
print(add(2, 5))

## 연습문제 : 데코레이터로 매개변수의 자료형 검사하기
print('\n연습')
def type_check(type_a, type_b):
    def real_decorate(func):
        def wrapper(a, b):
            r = func(a,b)
            if isinstance(a, type_a) and isinstance(b, type_b) :
                return r
            else :
                raise RuntimeError('자료형이 올바르지 않습니다.')
        return wrapper
    return real_decorate
@type_check(int, int)
def add(a, b):
    return a + b
 
print(add(10, 20))
# print(add('hello', 'world'))

## 실전문제 : HTML로 테그 데코레이터 만들기
print('\n실전')
def html_tag(name):
    def real_decorator(func):
        def wrapper():
            return('<{}>{}</{}>'.format(name,func(),name))
        return wrapper
    return real_decorator
    
    
a,b = input().split()
@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, world!'
 
print(hello())


