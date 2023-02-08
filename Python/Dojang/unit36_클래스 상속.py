## 클래스 상속; 기존 기능의 재사용
'''
기능을 물려주는 클래스 : 기반클래스(base class), 부모클래스, 슈퍼클래스
상속을 받아 새롭게 만드는 클래스 : 파생(derived class), 자식클래스, 서브클래스
파이썬에서 object는 모든 클래스의 조상임. 
'''

class Person:
    def greeting(self):
        print('안녕하세요')
# 상속
class Student(Person): 
    def study(self):
        print('공부하기')

j = Student()
j.greeting() # 안녕하세요
j.study() # 공부하기

# 상속관계 확인하기
print(issubclass(Student,Person)) # True

# 상속 관계와 포함관계
# 상속관계 : is-a / student is a person
# 같은 종류에 동등한 관계

# 포함관계 : has-a / PersonList has a Person


## 기반 클래스의 속성 사용하기 
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요'
        
class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__() # super()로 기반 클래스의 메서드 호출
        self.school = '파이썬 코딩도장'
        
# 만약 파생클래스에서 __init__ 메서드를 생략한다면 기반 클래스의 __init__이 자동으로 호출되므로 super() 없어도 됨
        
james = Student()
print(james.school)
print(james.hello)
print()

## 메서드 오버라이딩
'''
기반 클래스의 메서드를 무시하고 새로운 메서드를 만드는 것.
원래 기능을 유지하면서 새로운 기능을 덧붙일 때 사용
'''
class Person:
    def greeting(self):
        print('안녕하세요.')
 
class Student(Person):
    def greeting(self):
        super().greeting()
        print('저는 파이썬 코딩 도장 학생입니다.')
 
james = Student()
james.greeting()

## 다중 상속
# 여러 기반 클래스로부터 상속을 받아서 파생 클래스를 만드는 방법
class Person:
    def greeting(self):
        print('안녕하세요')
        
class University:
    def manage_credit(self):
        print('학점 관리')
        
class Student(Person, University):
    def study(self):
        print('공부하기')

jimin = Student()
jimin.greeting()
jimin.manage_credit()
jimin.study()

# 다이아몬드 상속 
# 메서드 탐색 순서 확인하기 : 클래스.mro()
# jimin.__mro__()

## 추상 클래스
# 메서드의 목록만 가진 클래스. 상속받는 클래스에서 메서드 구현을 <강제>하기 위해 사용
# 추상 클래스는 인스턴스로 만들 수 없음 
from abc import *
'''
class 추상클래스이름(metaclass=ABXMeta):
    @abstractmethod
    def 메서드이름(self):
        코드
'''
# 학생 추상 클래스를 만들고, 이 추상클래스를 상속받아 학생 클래스 제작
class StudentBase(metaclass=ABCMeta):
    # 상속시 반드시 study, go_to_school 메서드를 모두 구현해야 함. 
    @abstractmethod
    def study(self):
        pass # 추상 메서드는 호출할 일이 없으므로 빈 메서드로 제작
    
    @abstractmethod
    def go_to_school(self):
        pass
    
class Student(StudentBase):
    def study(self):
        print('공부')
    
    def go_to_school(self):
        print('학교')
        
mina = Student()
mina.study()
mina.go_to_school()

## 연습문제
class AdvancedList(list):
    def replace(self,num,new): # self = AdcancedList 형 객체(list 자식 클래스)
        while self.count(num) != 0:
            self[self.index(num)] = new
            
x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)
print(x)

## 심사문제 : 다중상속
class Animal:
    def eat(self):
        print('먹다')
        
class Wing:
    def flap(self):
        print('파닥거리다')
        
class Bird(Animal, Wing):
    def fly(self):
        print('날다')


b = Bird()
b.eat()
b.flap()
b.fly()
print(issubclass(Bird, Animal))
print(issubclass(Bird, Wing))