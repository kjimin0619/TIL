# 클래스 속성과 정적, 클래스 메서드 사용하기
# 속성 : 클래스 속성, 인스턴스 속성

## 클래스 속성 : 클래스에 속해 있으며 모든 인스턴스에서 공유함.
class Person:
    bag = []
    
    def put_bag(self, stuff):
        Person.bag.append(stuff) # 클래스 속성에 접근
        
james = Person()
james.put_bag('책')
 
maria = Person()
maria.put_bag('열쇠')
 
print(james.bag) # ['책', '열쇠']
print(maria.bag) # ['책', '열쇠']
print(Person.bag) # ['책', '열쇠']

# 현재 인스턴스와 클래스의 속성 확인하기
print(maria.__dict__)
print(Person.__dict__)

## 인스턴스 속성
class Person:
    def __init__(self):
        self.bag = []
        
    def put_bag(self, stf):
        self.bag.append(stf)
        
        
james = Person()
james.put_bag('책')
 
maria = Person()
maria.put_bag('열쇠')
 
print(james.bag) # 책
print(maria.bag) # 열쇠

## 비공개 클래스 속성
class Knight:
    """ 기사 클래스입니다 """
    __item_limit = 10
    
    def print_itm_num(self):
        print(Knight.__item_limit)
        
x = Knight()
x.print_itm_num() # 10
print(x.__doc__) # 독스트링 출력 
# print(Knight.__item_limit) # 비공개 클래스 속성에 접근시 에러

## 정적 메서드
# 인스턴스를 통하지 않고 클래스에서 바로 호출할 수 있는 메서드
# 정적 메서드는 메서드 위에 @staticmethod를 붙임. 데코레이터는 42장 참고
# 정적 메서드는 self를 받지 않기 때문에 인스턴스 속성이나 인스턴스 메서드가 필요 없을 때 사용
# 메서드의 실행이 외부 상태에 영향을 끼치지 않는 순수 함수를 만들 때 사용 == 인스턴스의 상태를 변화시키지 않는 메서드를 만들 때
class Calc:
    @staticmethod
    def add(a,b):
        print(a+b)
        
    @staticmethod    
    def mul(a,b):
        print(a*b)
        
        
Calc.add(100,50) # 클래스에서 바로 메서드 호출
Calc.mul(100,50)
print()

## 클래스메서드
class Person:
    count = 0
    
    def __init__(self):
        Person.count += 1
        
    @classmethod
    def print_count(cls):
        print('{}명 생성'.format(cls.count))

j = Person()
m = Person()

Person.print_count()

# 연습문제 : 날짜 클래스 생성
class Date : 
    @staticmethod
    def is_date_valid(str):
        year, month, date = map(int,str.split('-'))

        return month<13 and date <= 31 # 맞으면 TRUE 반환
    
if Date.is_date_valid('2000-10-31'):
    print('올바른 날짜 형식입니다.')
else:
    print('잘못된 날짜 형식입니다.')
    
# 심사문제
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        
    @classmethod
    def from_string(cls, time_string):
        h,m,s = map(int,time_string.split(':'))
        return cls(h,m,s)
        
    @staticmethod
    def is_time_valid(time_string):
        h,m,s = map(int,time_string.split(':'))
        return h <= 24 and m <= 59 and s <= 60
    
time_string = input()
 
if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')