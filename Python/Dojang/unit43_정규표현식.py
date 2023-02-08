##정규표현식
# 일정한 규칙(패턴)을 가진 문자열을 표현하는 방법
# re(regular expresion의 약자) 모듀을 가져와 사용

## 문자열 판단하기
# 문자열에 특정 문자열이 포함되어 있는지 판단
import re
# hello, world! 문자열에 hello가 포함되어 있는지
# match 함수는 문자열의 처음부터 매칭되는지 판단
print(re.match('hello', 'hello, world!')) # hello가 있으므로 정규표현식 매치 객체가 반환
print(re.match('python', 'hello, world!')) # python이 없으므로 반환값 x

## 특정 문자열이 맨 앞에 오는지 맨 뒤에 오는지 판단
# ^문자열 : 맨 앞에 오는지
# 문자열$ : 맨 뒤에 오는지

# search : 문자열의 일부분이 매칭되는지 판단
print(re.search('^hello', 'hello, world!')) # 매칭됨
print(re.search('hello!$', 'hello, hello!')) # 매칭됨


## 지정된 문자열이 하나라도 포함되는지 판단
print(re.match('hello|hi', 'hi')) # 매칭

## 문자열이 숫자로 되어있는지 판단
# * : 0개 이상 있는지
# + : 1개 이상 있는지
print(re.match('[0-9]*', '1234')) # 매칭
print(re.match('[0-9]+','abcd')) # None

# * 와 + 의 활용
print(re.match('a+b', 'b')) # b에는 a가 1개 이상 없음. None
print(re.match('a*b', 'b')) # b에는 a가 0개 이상 있음. 매칭
# 'a+b', 'a*b'에서 b는 무조건 있어야 하는 문자이고, a*는 0개 이상, a+는 1개 이상 있어야 매칭

## 문자가 한 개만 있는지 판단하기
# ? : ?앞의 문자가 0개 또는 1개인지 판단
# . : .이 있는 위치에 아무 문자(숫자)가 1개 있는지 판단
print(re.match('abc?d', 'abd')) # c가 0개 있으므로 매칭
print(re.match('ab.d', 'ab8d')) # ab와 d 사이에 8이 있으므로 매칭

## 문자 개수 판단
# 문자{개수} , (문자열){개수}, [0-9]{개수}
# {시작개수, 끝개수}
print(re.match('h{3}', 'hhhello')) # h가 3개 이므로 매칭
print(re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}', '02-100-1000')) # 매칭

## 숫자와 영문 문자 조합
# 영문 문자 범위 : a-Z, A-Z 
print(re.match('[a-zA-Z0-9]+', 'Hello1234')) # a-z, A-Z, 0-9 가 각각 1개 이상 있으므로 매칭

## 특정 문자 범위에 포함되지 않는지 판단
# [^범위]* , [^범위]+ : 정규표현식으로 특정 문자 범위에 포함되지 않는지
print(re.match('[^A-Z]+', 'hello')) # 대문자가 없으므로 매칭
# ^[범위]*, ^[범위]+ : 특정 범위로 시작하는지 판단
# [범위]*$, [범위]+$ : 특정 문자(숫자) 범위로 끝나는지 확인
print(re.search('^[0-9]+', 'hello')) # 매칭x
print(re.search('[0-9]+$','hello1234')) # 매칭

## 특수 문자판단
# \특수문자 ([]안에서는 \를 붙이지 않아도 됨)
print(re.search('\*+', '1 ** 2')) # *이 들어있는지 판단
print(re.match('[$()a-zA-Z0-9]+', '$(document)')) #  # $, (, )와 문자, 숫자가 들어있는지 판단
 
## 단순표현
# \d : [0-9]. 모든 숫자
# \D : [^0-9]. 숫자를 제외한 모든 문자
# \w : [a-zA-Z0-9_]. 영문대소문자, 숫자, 밑줄
# \W: [^a-zA-Z0-9_]와 같음. 영문 대소문자, 숫자, 밑줄 문자를 제외한 모든 문자

## 공백처리
# ' ' OR \s(\S)

## 같은 정규표현식 패턴을 자주 사용할 때
# compile함수 활용
p = re.compile('[0-9]+')
print(p.match('1234'))

## 그룹 사용하기
m = re.match('([0-9]+) ([0-9]+)', '10 295')
print(m.group(1)) # 첫 번째 그룹에 매칭된 문자열 반환
print(m.group(2)) # 두 번째 ``
print(m.group()) # 매칭된 문자열 한꺼번에 반환
# 튜플로 반환 : groups
print(m.groups())
# 그룹 이름 짓기 : (?p<이름>정규표현식)

## 패턴에 매칭되는 모든 문자열 가져오기
print(re.findall('[0-9]+', '1 2 Fizz 4 Buzz Fizz 7 8'))

# (.[a-z]+)* # 점과 영소문자가 1개 이상 있는지 판단 & 이것 자체가 0개 이상인지 판단

## 문자열 바꾸기
# re.sub('패턴', '바꿀 문자열', '문자열', 바꿀횟수)
print(re.sub('apple|orange', 'fruit', 'apple box orange tree')) # apple 또는 orange를 fruit를 바꿈
print(re.sub('[0-9]+', 'n', '1 2 as 4 dfs 7 8'))

# 교체함수(매치객체)
# re.sub('패턴'. 교체함수, '문자열', 바꿀횟수)
# 문자열에서 숫자를 찾은 뒤 숫자를 10배로 마들기
def multiple10(m):
    n = int(m.group())
    return str(n*10)

print(re.sub('[0-9]+', multiple10, ' 1 2 fizz 4 buzz fizz 7 8'))

## 찾은 문자열을 결과에 다시 사용하기
print(re.sub('([a-z]+) ([0-9]+)', '\\2 \\1 \\2 \\1', 'hello 1234'))
print(re.sub('({\s*)"(\w+)":\s*"(\w+)"(\s*})', '<\\2>\\3</\\2>', '{ "name": "james" }'))

## raw 문자열
# r'\숫자 \g<이름> \g<숫자>'

## 연습문제 : 이메일 주소 검사하기
p = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

emails = ['python@mail.example.com', 'python+kr@example.com',              # 올바른 형식
          'python-dojang@example.co.kr', 'python_10@example.info',         # 올바른 형식
          'python.dojang@e-xample.com',                                    # 올바른 형식
          '@example.com', 'python@example', 'python@example-com']          # 잘못된 형식

for email in emails :
    print(p.match(email) != None, end=' ')
    
print()
## URL 검사하기

url_input = input()

p = re.compile('^https?://[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/[a-zA-Z0-9-.,_?=/]*')
if p.match(url_input) :
    print(True)
else :
    print(False)