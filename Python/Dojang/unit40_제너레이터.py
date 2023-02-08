## 제너레이터 == 이터레이터를 생성해주는 함수
def number_generator() :
    yield 0
    yield 1
    yield 2
    
for i in number_generator() :
    print(i)
    
## yield의 동작과정
print('\nyield의 동작과정')
g = number_generator()
a = next(g)
print(a)

b = next(g)
print(b)

c = next(g)
print(c)

# 제너레이터 안에서 return에 반환값을 지정하면 StopIteration 예외의 에러 메세지로 들어감
print()
def one_generator() :
    yield 1
    return '메롱'

g = one_generator()
try :
    next(g)
    next(g)
except StopIteration as e:
    print(e)  # 메롱 출력
    
## 제너레이터 만들기
print('generator 생성')
def number_generator(stop):
    n = 0
    while n < stop :
        yield n
        n += 1
        
for i in number_generator(3):
    print(i)

g = number_generator(4)
print(next(g))
print(next(g))
print(next(g))
print(next(g))

## yield에서 함수 호출도 가능하다
def upper_generator(x): # 리스트에 들어있는 문자열을 대문자로 변환하여 전달하는 함수
    for i in x:
        yield i.upper()
        
fruits = ['apple', 'pear', 'grape', 'pineapple', 'orange']
for i in upper_generator(fruits):
    print(i)    
    
## yield from으로 값을 여러 번 바깥으로 전달하기
# yield from에는 반복 가능한 객체, 이터레이터, 제너레이터 객체를 지정
def num_g():
    x = [100,200,300]
    yield from x
    
for i in num_g():
    print(i)
    
## yield from에 제네레이터 객체 지정하기
def number_generator(stop):
    n = 0
    while n < stop:
        yield n
        n += 1
        
def three_generatr():
    yield from number_generator(3)
    
for i in three_generatr():
    print(i)
    
## 제너레이터 표현식
# 리스트 표현식에서 ()로 묶으면 제너레이터 표현식이 됨
# 제너레이터 표현식은 필요할 때 요소를 만들어내므로 메모리를 절약할 수 있음
g = (i for i in range(50) if i % 20 == 0) # 제너레이ㅌ 표현식
print(g) # <generator object <genexpr> at 0x00000202D4383C10> 

a = next(g)
print(a)

b = next(g)
print(b)

c = next(g)
print(c)

## 연습문제
print('\n연습문제 : 파일읽기 제너레이터')
def file_read():
    with open('words.txt') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            yield line.strip('\n')
    
for i in file_read():
    print(i)
    
## 심사문제
print('\n심사문제')
def prime_number_generator(start,stop):
    for n in range(start, stop):
        is_prime = True
        for i in range(2,n):
            if n % i == 0 :
                is_prime = False
        if is_prime :
            yield n    
    
start, stop = map(int, input().split())
 
g = prime_number_generator(start, stop) # 50, 100 입력시
print(next(g)) #53
print(next(g)) #59
print(type(g)) # <class 'generator'>
for i in g:
    print(i, end=' ') # 61 67 71 73 79 83 89 97