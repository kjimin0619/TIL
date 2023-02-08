'''
29. 함수 사용하기

def 함수이름(매개변수1, 매개변수2)
함수를 호출할 때 넣는 값 : 인수(argument)
return : 값을 반환하는 기능 & 함수 중간에서 바로 빠져나오는 기능
     return으로 여러값 반환하면,
     실제로는 튜플이 반환됨.
     즉, 튜플이 변수 여러개에 할당되는 특성을 이용한 것.(언패킹)
     파이썬에서는 괄호없이 값을 콤마로 구분하면 튜플이 됨

함수 독스트링 : 함수의 콜론(:) 다음 줄에 """"""(큰따옴표 3개)로 문자열을 입력하면 함수에 대한 설명을 넣을 수 있음

프레임 : 메모리에서 함수와 함수에 속한 변수가 저장되는 독립적인 공간
    전역프레임 : 파이썬 스크립트 전체에서 접근할 수 있음
    함수가 끝나면 함수 호출 스택에서 해당 함수의 스택 프레임도 사라짐
함수는 스택방식으로 호출됨
-> 함수를 호출하면 스택의 아래쪽 방향으로 함수가 추가되고 함수가 끝나면 위쪽 방향으로 사라짐
'''
def add(a1, a2):
    """ 두 매개변수를 더하는 함수 """
    return a1+a2
print(add(1,2))
print('독 스트링 :',add.__doc__) # 독스트링 출력
print(help(add))


# return 언패킹
def one_two():
    return 1,2 # (1,2)

ans = one_two()
print(ans) # (1,2)
an1, an2 = one_two()
print(an1, an2)

# 연습문제
x = 10
y = 3

def get_quotient_remainder(x,y):
    return x//y, x%y
quotient, remainder = get_quotient_remainder(x, y)
print('몫: {0}, 나머지: {1}'.format(quotient, remainder))


# 심사문제 : 사칙연산 함수
x, y = map(int, input().split())

def calc(x,y):
    return x+y, x-y, x*y, x/y
a, s, m, d = calc(x, y)
print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a, s, m, d))