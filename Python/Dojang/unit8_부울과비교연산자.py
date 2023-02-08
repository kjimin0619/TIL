'''
파이썬은 대소문자 구별함
-> python != Python

is vs ==
== : 값 자체를 비료
is : 클래스 객체를 비교(메모리 주소 확인)

메모리주소 확인하기 : id() 함수
 
정수, 실수, 문자열을 부울로 만들기 : bool() 활용
bool(1) == bool(1.5) == True // 0,0.0을 제외한 모든 숫자는 True
bool(0) == False
bool('false') == Treu // 빈 문자열을 제외하고 모든 문자열은 Treu


단락 평가(short-circuit evalutrion)
파이썬의 논리 연산자는 "마지막으로 단락 평가를 실시"한 값을 그대로 반환한다.
-> 'True' and 'Python' >>> 'Python' 반환

'''
# 연습문제
korean = 92
english = 47
mathematics = 86
science = 81

print(korean>=50 and english>=50 and mathematics>=50 and science>=50)

# 연습문제
korean, english, mathematics, science = map(int,input().split())

print(korean>=90 and english>80 and mathematics>85 and science>=80)