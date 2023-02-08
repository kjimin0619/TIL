# 예외가 발생했을 때도 스크립트를 중단하지 않고 계속 실행하게 해주는 예외 처리 방법
'''
try:
    실행할 코드
except:
    예외가 발생했을 때 처리하는 코드
else:
    예외가 발생하지 않았을 때 실행할 코드
'''

'''
try : 
    x = int(input('나눌 숫자를 입력하세요  '))
    y = 10 / x
    print(y)
except : 
    print('예외 발생')
    
y = [10, 20, 30]

# try:
#     index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
#     print(y[index] / x)
    
# except ZeroDivisionError: # 숫자를 0으로 나눠서 에러가 발생할 떄
#     print('숫자를 0으로 나눌 수 없습니다')
# except IndexError:
#     print('잘못된 인덱스입니다')

## 예외의 에러 메시지 받아오기
try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    print(y[index] / x)
    
except ZeroDivisionError as e:
    print('숫자를 0으로 나눌 수 없음', e)
except IndexError as e:
    print('잘못된 인덱스', e)
    
"""
예외도 클래스 상속으로 구현됨.
파이썬에서 새로운 예외를 만들 때는 Exception을 상속받아서 구현함
"""


## else finally 사용

# 예외와는 상관없이 항상 코드 실행하기
# finally : 예외 발생 여부와 상관없이 항상 코드를 실행
try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:    # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없습니다.')
else:                        # try의 코드에서 예외가 발생하지 않았을 때 실행됨
    print(y)
finally:                     # 예외 발생 여부와 상관없이 항상 실행됨
    print('코드 실행이 끝났습니다.')
    
# try는 함수가 아니므로 스택 프레임을 만들지 않음 
'''


## 예외 발생시키기 : raise 예외('에러메세지')
try : 
    x = 3 # int(input('3의 배수 입력 : '))
    if x % 3 != 0:
        raise Exception('3의 배수가아닙니다.')
    print(x)
except Exception as e:
    print('예외가 발생했습니다.', e)

## Assert로 예외 발생시키기
# assert는 지정된 조건식이 거짓일 때 AssertionError 예외를 발생시킴
x = 10 # int(input('5의 배수'))
assert x % 5 == 0, '5의 배수가 아님'
print(x)

## 사용자 정의 예외
# 3의 배수가 아닐 때 발생시킬 에러
class NotThreeMultipleError(Exception):
    def __init__(self):
        super().__init__('3의 배수가 아닙니다')
        
def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        if x % 3 != 0:                     # x가 3의 배수가 아니면
            raise NotThreeMultipleError    # NotThreeMultipleError 예외를 발생시킴
        print(x)
    except Exception as e:
        print('예외가 발생했습니다.', e)
 
three_multiple()

## 연습문제
# 'maria.tx.' 파일이 있으면 읽어서 출력, 없으면 문구 출력

try:
    file = open('maria.txt','r')
except FileNotFoundError:
    print('파일이 없습니다. ')
else:
    s = file.read()
    file.close()
    
## 심사문제 : 회문이 아니면 예외처리
class NotPalindromeError(Exception):
     def __init__(self):
         super().__init__('회문이 아닙니다.')
         
def palindrome(word):
    if word == word[::-1] :
        print(word)
    else :
        raise NotPalindromeError
    
try:
    word = input()
    palindrome(word)
except NotPalindromeError as e:
    print(e)