'''
0. 리스트와 튜플

<리스트>
리스트 element에는 다양한 자료형을 저장할 수 있음
요소를 변경, 추가 삭제할 수 있음 > 변경 가능
빈 리스트 만들기 : [] 혹은 list() 사용

range로 리스트 만들기 
list(range(갯수)) or list(range(시작,끝,증가폭))


<튜플>
튜플 안에 여러 자료형 값 저장
요소를 변경,추가,삭제할 수 없음 -> 변경 불가
생성시 괄호가 없어도 됨

요소가 한 개인 튜플 만들기 : (값,) 혹은 값,

range로 튜플 만들기
tuple(range(갯수)) or tuple(range(시작,끝,증가폭))


튜플 <-> 리스트
리스트 -> 튜플 : tuple(list변수)
튜플 -> 리슽 : list(tuple변수)

리스트와 튜플 안에 문자열을 넣으면?
list('hello') -> ['h','e','l','l','o']
tuple('hello') -> ('h','e','l','l','o')

** input().split()은 문자열 리스트를 반환

'''

# 연습문제
a = list(range(5,-10,-2))
print(a)

# 심사문제
stp = int(input())
print(tuple(range(-10,10,stp)))