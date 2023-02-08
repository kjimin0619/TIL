# 이터레이터 : 값을 차례대로 꺼낼 수 있는 객체

# 파이썬에서는 지연평가(lazy evaluation) 방식을 사용함. 이터레이터만 생성하고 값이 필요한 시점이 되었을 때 값을 만드는 방식

## 반복 가능한 객체(iterable) : 요소가 여러 개 들어있고, 한 번에 하나씩 꺼낼 수 있는 객체
it = [1,2,3].__iter__()
# it = range(3).__iter__()
print(it.__next__()) # 1
print(it.__next__()) # 2
print(it.__next__()) # 3
# 이터레이터는 __next__로 요소를 계속 꺼내다가 꺼낼 요소가 없으면 StopIteration 예외를 발생시켜서 반복을 끝soa
'''
반복 가능한 객체 : 요소를 한 번에 하나씩 가져올 수 있는 객체
* 시퀀스 객체 : 요소의 순서가 정해져있고 & 연속적으로 이어져 있음 (반복가능한 객체의 하위분류)
이터레이터 : __next__ 메서드를 사용해서 차례대로 값을 꺼낼 수 있는 객체 
'''

## 이터레이터 만들기
print('이터레이터 생성')
class Counter:
    def __init__(self, stop): # 끝낼 숫자 받음
        self.current = 0
        self.stop = stop
        
    def __iter__(self):
        return self # 현재 인스턴스를 반환
    
    def __next__(self):
        if self.current < self.stop :
            r = self.current
            self.current += 1
            return r
        else :
            raise StopIteration
        
for i in Counter(3):
    print(i)

# 이터레이터 언패킹 ; Counter의 결과를 변수 여러 개에 할당할 수 있음
a, b, c = Counter(3)
print(a,b,c)

# 반환값을 _에 저장하는 이유 : 특정 순서의 반환값을 사용하지 않고 무시하겠다는 관례적 표현

## 인덱스로 접근할 수 있는 이터레이터 만들기
# __getiem__ 메서드 구현
class Counter:
    def __init__(self, stop):
        self.stop = stop
        
    # 클래스에서 __getitem__ 메서드만 구현해도 이터레이터가 되며 __iter, __next__는 생략가능
    def __getitem__(self, index):
        if index < self.stop:
            return index
        else :
            raise IndexError
print('인덱스 접근 이터레이터')
print(Counter(3)[2]) # 2

## iter, next 함수 활용하기
# iter(호출가능한객체, 반복을 끝낼 값)
it = iter(range(3))
print(next(it))

import random
for i in iter(lambda : random.randint(0,5), 2):
    print(i, end=':')
    
# next(반복가능한객체, 기본값)

## 연습문제 : 배수 이터레이터 만들기
print()
print('연습문제')
class MultipleIterator:
    def __init__(self, stop, multiple):
        self.stop = stop
        self.multiple = multiple
        self.current = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.current += 1
        if self.current * self.multiple < self.stop:
            return self.current*self.multiple
        else:
            raise StopIteration
           
for i in MultipleIterator(20, 3):
    print(i, end=' ')
 
print()
for i in MultipleIterator(30, 5):
    print(i, end=' ')

## 심사문제
# 시:분:초 형식
print('\n\n시:분:초 출력하기')
class TimeIterator:
    def __init__(self, start, end):
        self.start = start # 시작하는 초
        self.end = end
        
    def __getitem__(self, index):
        hour = (self.start + index) // 3600 % 24
        min = (self.start + index) // 60 % 60
        sec = (self.start + index) % 60
        
        if index < self.end - self.start :
            return '{:02d}:{:02d}:{:02d}'.format(hour,min,sec)
        else:
            raise IndexError

start, stop, index = map(int, input().split())
for i in TimeIterator(start, stop):
    print(i)
 
print('\n', TimeIterator(start, stop)[index], sep='')


