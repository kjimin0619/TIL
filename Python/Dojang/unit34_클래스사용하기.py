'''
34. 클래스
클래스 ; 객체를 표현하기 위한 문법
클래스 -> 속성 & 메서드로 구성

'''

# 클래스와 메서드 만들기
# 빈 클래스는 pass 넣어주기
# __init__ 메서드는 인스턴스를 만들 때 호출되는 특별한 메서드

# 앞 뒤로 밑줄 두 개(__)가 붙은 메서드는 파이썬이 자동으로 호출해주는 메서드. 
#   스페셜 메서드(또는 매직 메서드)라 부름

# self의 의미
#   인스터스 자기 자신을 의미함
    # 현재 인스턴스가 자동으로 매개변수 self에 들어옴

class Person :
    # 속성(attribute)는 __init__ 메서드 안에서 할당. self.속성 = 값
    def __init__(self):
        self.hello = '안녀세요'
        
    def greeting(self) :
        print(self.hello)
        
    # 메서드 안에tj 메서드 호출하기 ; self.메서드()
    def hello(self) :
        self.greeting( )
        
james = Person() # 변수에 클래스 할당. james는 Person의 인스턴스
james.greeting()
# 특정 클래스의 인스턴스인지 확인하기
print(isinstance(james, Person)) # True

# 인스턴스 생성시 값 받기
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.hello = '안뇽!'
        
        
    def greeting(self):
        print('{} 저는 {}에 사는 {}세 {}입니다.'.format(self.hello, self.address, self.age, self.name))
        
        
maria = Person('마리야',20,'서울시 서초구 반포동')
maria.greeting()
print(maria.age)

# 클래스의 위치 인수(리스트)
class Person:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.address= args[2]
        
maria = Person(*['maria', 20, '서울'])

# 클래스의 키워드 인수(딕셔너리)
class Person:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']

maria = Person(**{'name':'maria', 'address' : 'seoul', 'age': 20})
maria2 = Person(name='마리아', age=20, address='서울시 서초구 반포동')

# 인스터스 생성 후 속성 추가하기
class Person:
    pass

maria = Person()
maria.name = 'mari' # 인스턴스를 만든 뒤 속성 추가
print(maria.name)
# 이때 추가한 속성은 해당 인스턴스에만 생성됨. 
# 다른 인스턴스를 만들 때에는 추가한 속성이 생성되지 않음
james = Person()
# print(james.name) --> 에러

# 특성 속성만 허용하고 다른 속성은 제한할 때
class Person:
    __slots__ = ['name','age'] # name, age만 허용. 다른 속성은 제한
    
maria = Person()
maria.name = 'marii'
maria.age = 30
# maria.address = 'seoul' # 허용되지 않은 속성. 에러 발생


### Private attribute(비공개 속성)
# 비공개 속성은 "__속성"과 같이 밑줄 두 개로 시작함
# 비공개 속성은 클래스 안의 메서드에서만 접근할 수 있음
# 비공개 메서드도 마찬가지로 밑줄 두 개로 시작
class Person:
    def __init__(self,age,name,address,wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet # 비공개 속성

    def pay(self,amount):
        self.__wallet -= amount
        if amount > self.__wallet :
            print('현금 부족')     
            return   
        
        self.__wallet -= amount
        
maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
# maria.__wallet >> 에러 발생
maria.pay(300000)
print()

# 연습문제 | 게임 캐릭터 클래스 만들기
class Knight :
    def __init__(self, health, mana, armor):
        self.mana = mana
        self.armor = armor
        self. health = health 
        
    def slash(self):
        print('베기')
       
x = Knight(health=542.4, mana=210.3, armor=38)
print(x.health, x.mana, x.armor)
x.slash()

# 심사문제 
class Annie:
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power
        
    def tibbers(self):
        print('티버: 피해량 {}'.format(self.ability_power* 0.65 + 400))
health, mana, ability_power = map(float, input().split())
 
x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibbers()

'''
# 연습문제
class Knight :
    def __init__(self,health,mana,armor):
        self.health = health
        self.mana = mana
        self.armor = armor
    
    def slash(self):
        print('베기')
        
# 심사문제 : 게임 캐릭터 클래스 만들기
class Annie :
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power
        
    def tibbers(self):
        print('티버: 피해량 {}'.format(self.ability_power*0.65 + 400))
        
    
health, mana, ability_power = map(float, input().split())

x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibbers()
'''