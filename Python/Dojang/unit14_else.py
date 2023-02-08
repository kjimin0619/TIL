'''
14. else

- if와 else의 동작방식
: 값 자체가 있으면 if가 동작, 조건식이 참이면 if 코드 실행
True -> if 코드 실행
False -> else 코드 실행
None -> False로 취급. else 코드 실행

** 숫자는 정수,실수 관계없이 0이면 거짓, 0 아니면 참
** 문자열은 내용이 있으면 참, 빈 문자열은 거짓

** False로 취급하는 것
None, 0, 빈 문자열/리스트/튜플/딕셔너리/세트

** 논리 연산자 & 비트 연산자
||(or) , &&(and) : 논리 연산자
| , & : 비트 연산자 

'''

# 연습 문제
written_test = 75
coding_test = True

if written_test >= 80 and coding_test :
    print('합격')
    
else : print('불합')

# 심사 문제
korean, english, math, science = map(int,input().split())

avg = (korean + english + math + science) /4

if 0<= korean <= 100 and 0<= english <= 100 and 0<= math <= 100 and 0<= science <= 100 :
    if avg >= 80 : print('합격')
    else : print('불합격')
    
else : print('잘못된 점수')