'''
9. 문자열

여러줄 사용하기 : '''''' """"""
이스케이프 문자 : 작은 따옴표, 큰따옴표 : \' \"

* 한 줄을 여러 줄로 입력할 때
: \를 사용하여 줄바꿈을 하면 됨


'''

s = 'isn\'t\' she lovely'
print(s)

# 한 줄을 여러 줄로 입력하기
str1 = 'Fortunately, however, for slfak\
asdfklaslfkjlksaldfkjl\
asdfl;jasd\'강조\'affsdfs\
dsaflkdkfsakkk'
print(str1)

# 연습문제
str = '''Python is a programming language that lets you work quickly
and
integrate systemss more effectively.'''
print(str)

# 심사문제
str2 = '''
'Python' is a "programming language"
that lets you work quickly
and
integrate systems more effectively.'''
print(str2)

