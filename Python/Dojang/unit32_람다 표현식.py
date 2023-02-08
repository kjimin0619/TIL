'''
32 람다 표현식
'''

##  람다 표현식으로 익명 함수 만들기
# lambda 매개변수들: 식
# 숫자를 받아서 10을 더한 후 반환하는 함수( plus_ten )
# labda에 매개변수를 지정하고, :(콜론) 뒤에 반환값으로 사용할 식 지정
plus_ten = lambda x : x + 10
print(plus_ten(10))

# 람다 표현식 자체를 호출하기
result = (lambda x : x + 15)(10)
print(result)

# 람다 표현식 안에서는 새 변수를 만들 수 없다.
# 반환값 부분은 변수 없이 식 한 줄로 표현
# 단, 람다 표현식 바깥에 있는 변수는 사용 가능
y = 10
print((lambda x : x + y)(1))

# 람다 표현식을 인수로 사용하기
# 람다 표현식은 함수를 다른 함수의 인수로 넣을 때 매우 편리
result = list(map(lambda x : x + 10, [1,2,3,4,5]))
print(result)

# 람다 표현식으로 매개변수가 없는 함수 만들기
print((lambda : 10)())

## 람다 표현식과 map, filter, reduce 함수 활용하기
# 람다 표현식에 조건부 표현식 사용하기
# lambda 매개변수들: 식1 if 조건식 else 식2
# 람다 표현식에서 if를 사용했따면 반드시 else를 사용해야 함
# 또한 elif는 사용 불가
a = [1,2,3,4,5,6,7,8,9]
renew_a = list(map(lambda x : str(x) if x%3 == 0 else x, a))
print(renew_a) # [1, 2, '3', 4, 5, '6', 7, 8, '9']

# map에 객체 여러 개 넣기
a = [1,2,3,4,5]
b = [2,4,6,8]
temp = list(map(lambda x, y : x*y, a,b))
print(temp) # [2, 8, 18, 32]

# filter 사용하기
# 반복 가능한 객체에서 특정 조건에 맞는 요소만 가져오기
# filter에 지정한 함수의 반환값이 True 일 때만 해당 요소를 가져옴
# filter(함수, 반복가능한 객체)
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
temp = list(filter(lambda x : 5<x<10, a))
print(temp)

# reduce 사용하기
# 반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤 이전 결과와 누적해서 반환하는 함수
# 내장 함수가 아니라 functools 모듈에서 가져오기
# from functools import reduce
# reduce(함수, 반복가능한객체)
from functools import reduce
temp2 = reduce(lambda x,y: x+y, a) # a 리스트에 있는 원소의 합
print(temp2) # 105

# 주의점
# 리스트 표현식으로 처리할 수 있는 경우에는 리스트 표현식을 쓰는 게 더 좋음
# for, while 반복문으로 처리할 수 있는 경우에도 for, while을 쓰는 게 의미를 파악하기 더 쉬움

# 연습문제 : 이미지 파일만 가져오기
# 문자열 find 메서드 : 찾는 문자열이 없을 때 -1 반환. 있으면 인덱스 반환
files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']
print(list(filter(lambda x : x.find('.jpg') != -1 or x.find('.png') != -1, files)))
print(list(filter(lambda x : x.find('.jpg') != -1 or x.find('.png') != -1, files)))

# 심사문제 : 파일 이름을 한꺼번에 바꾸기
# my code ; not using lambda expression 그리고 하드코딩ㅋㅋㅋㅋ
print('심사문제')
# files = input().split()
files = ['1.jpg', '10.png', '11.png', '2.jpg', '3.png']
nameList, typeList = [], []

for file in files:
    name, type = file.split('.')
    name = '{:0>3}'.format(name)
    nameList.append(name)
    typeList.append(type)
    
formatingResults = []
for name_type in zip(nameList, typeList):
    joinResult = '.'.join(name_type)
    formatingResults.append(joinResult)

print(formatingResults)

# 람다 사용하는 버전 -->>> 개짱간단함
f = lambda x : '{0:0>3}.{1}'.format(x.split('.')[0], x.split('.')[1])
formatFiles = list(map(f,files))
print(formatFiles)

f = lambda x : '{0:0>3}.{1}'.format(x.split('.')[0], x.split('.')[1])
resu = list(map(f,files))
print(resu)