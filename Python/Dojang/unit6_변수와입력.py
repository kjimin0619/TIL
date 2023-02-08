'''
변수 삭제하기 : del
ex) 
x = 10
del x
print(x) // error!

빈 변수 만들기 : None
ex) x = None

입력값 받기
input() 함수 이용
* 단, 입력값의 데이터타입은 무조건 문자열

입력값 분리
split() 이용
변수1, 변수2 = intput().split('기준 문자열') -> 문자열 리스트를 반환

입력값들을 정수로 빠르게 변환
map() 이용
map(적용시킬 함수, 적용할 값)

'''

# 문자열 분리
# first, second = input('enter a string : ').split() # 공백으로 분리
# print('1번 문자 : {}, 2번 문자 : {}'.format(first, second))

# map 함수로 빠르게 분리하고 데이터형 바꾸기
# first, second = map(float,input('enter two number : ').split(',')) # 공백으로 분리
# print(first + second)
# print(type(first + second)) # float

result = map(float,[1,2,3,4,5]) # 공백으로 분리 -> 분리후 map 객체로 반환
print('result : {0}, data type : {1}'.format(list(result),type(result)))

# 연습문제
a,b,c = map(int,input('세 정수를 입력하시오 :').split())
print(a+b+c)