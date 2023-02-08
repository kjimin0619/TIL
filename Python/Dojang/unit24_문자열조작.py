'''
24. 문자열 조작

<메서드>
문자열.replace('바꿀 문자열', '새문자열')
문자열.split('기준문자열') : 기준문자열을 기준으로 문자열을 분리하여 리스트로 생성
문자열.join(리스트) : 구분자 문자열과 문자열 리스트의 요소를 연결하여 문자열로 제작
문자열.upper() : 모두 대문자로 만들기
문자열.lower() : 모두 소문자로 만들기 
문자열.lstrip() : 왼쪽 공백 모두 삭제
    lstrip('삭제할문자들') : 특정 문자 삭제
문자열.rstrip() : 오른쪽 공백 모두 삭제
문자열.strip() : 모든 공백 삭제
문자열.zfill(길이) : 지정된 길이에 맞춰서 문자열의 왼쪽을 0으로 채우기
문자열.find('찾을문자열'): 문자열의 위치 찾기
    없으면 -1 반환
    왼쪽부터 문자열 찾음.
    같은 문자열이 여러 개일 경우, 처음 찾은 문자열의 인덱스만 반환
문자열.index('찾을문자열') : 왼쪽부터 문자열 찾기
    없으면 에러     
문자열.rfind('찾을문자열') : 오른쪽에서부터 특정 문자열 찾기
문자열.rindex('찾을문자열') : 오른쪽 "
문자열.count('문자열') : 특정 문자열이 몇 번 나오는지 세기


* 구두점 간단 삭제 : string 모듈의 punctuation
'.sasdfa'.strip(string.punctuation)

* 문자열 정렬
ljust(길이) : 문자열을 지정된 '길이'로 만든 뒤, 왼쪽으로 정렬 후, 남는 공간 공백
rjust(길이) : " , 오른쪽으로 정렬, "
center(길이) : ", 가운데로 정렬, "

* 메서드 체이닝
메서드를 계속 연결해서 호출하는 것

<서식지정자와 포매팅>
%s : 문자열
    %길이s : 문자열을 '길이'만큼 만든 뒤, 오른쪽 정렬
    %-길이s : 문자열을 '길이'만큼 만든 뒤, 왼쪽 정렬
%d : 정수
%f : 실수
    %.2f : 소수점 자릿수
    
{인덱스}.format(값)

* 숫자 개수 맞추기
정수 실수 앞에 0을 넣어서 숫자 개수 맞추기
'%0개수d' % 숫자
'{인덱스:0개수d}'.format(숫자)
'%0개수.자릿수f' % 숫자
'{인덱스:0개수.자릿수f}'.format(숫자)

* 채우기와 정렬 조합해서 사용하기
'{인덱스:[[채우기]정렬][길이][.자릿수][자료형]}'

** raw 문자열 사용하기
문자열 앞에 r또는 R을 붙이면 raw 문자열이 됨
\를 \\로 두번 쓰지 않아도 됨(이스케이프 시퀀스를 그대로 저장해줌)

'''


# method 활용
s = "hello! python"
s = s.replace('python', 'jimin')
print(s)

a = 'apple, pear, grape, pineapple, orange'
print(a.split(', '))

ss =  ' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
print(ss) # apple pear grape pineapple orange

sss = '-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
print(sss) # apple-pear-grape-pineapple-orange

# punctuation
import string
temp = '.. python,,'.strip(string.punctuation).strip()
print(temp)

# 서식지정자
name = 'jimin'
print('i am %s'%name)
print('Today is %d %7s' %(3, 'April'))

# 포맷팅
print('hello {0}. welcome to {1}'.format('jimin',123))
temp1 = '{0} {0} {1} {1}'.format('Python', 'Script')
temp2 = 'Hello, {language} {version}'.format(language='Python', version=3.6)
print(temp1)
print(temp2)

# 문자열 포맷팅 간단 버전
language = 'python'
version = 3.6
print(f'hello. language(version) : {language}({version})')

# format 메서드로 문자열 정렬하기
# 왼쪽 정렬 : '{인덱스:<길이}'.format(값)
# 오른쪽 정렬 : '{인덱스:>길이}'.format(값)
print('{0:>10}'.format('python'))


# 포맷팅 종합 사용
# 길이를 10으로 만든 뒤 왼쪽으로 정렬하고 남는 공간은 0으로 
print('{0:0<10}'.format(15))
# 실수 버전
print('{:?>10.2f}'.format(15))

# 금액에서 천단위로 콤마 넣기
print('format 내장 함수 사용')
print(format(1493500, ','))

print('%20s'% format(1493500, ','))
print('{0:,}'.format(1496500))
print('{0:!>20,}'.format(1493500))
 
# 그냥 갑자기 생각나서 해본 거..
card_number = '45654-045666-5504'
blur = card_number[:4]
card_number = card_number.replace(blur, '*'*4)
print(card_number)

print('{:<10}'.format(456))

# 연습문제 : 전체 경로에서 파일명만 가져오기
path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
filename = path.split('\\')[-1]
print(filename)

# raw 문자열 사용해보기
print(r'C:\Python\Python36-32\python.exe')

# 심사문제 : 특정 단어 개수 세기
# sentence = input().split() # 공백 기준으로 문자열 분리 후 리스트 반환
# count = 0
# for str in sentence:
#     str = str.strip(string.punctuation) # ., 제거
#     if str == 'the' : count += 1
    
# print(count)


# 심사문제 : 높은 가격순으로 출력하기
prices = list(map(int,input().split(';')))
prices.sort(reverse=True)
for price in prices :
    print('{:9,}'.format(price)) # 동일한 포맷팅 : '{0:>9,}', '%9s' % format(price, ',')
