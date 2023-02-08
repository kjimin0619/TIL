'''
25. 딕셔너리 응용하기
cf) unit 12 딕셔너리 사용하기 참고하기

- 딕셔너리에 키-값 쌍 추가하는 메서드
setdefault : 키-값 쌍 추가
    이미 들어있는 키의 값은 수정 불가
update : 키의 값 수정, 키가 없으면 키-값 쌍 추가

- 키-값 쌍 삭제하기
pop(키) : 특정 키-값 쌍 삭제한 뒤, 삭제한 값 반환
pop(키, 기본값) : 딕셔너리에 키가 있을 때는 해당 키-값 쌍을 삭제한 뒤 삭제한 값을 반환함
    키가 없을 때는 기본값 반환
    
del 딕셔너리[키] 사용 가능

popitem() : 임의의 키-값 쌍 삭제한 뒤 튜플로 반환
    3.6 이상 버전에서는 마지막 키-값 쌍 삭제 후 반환
    3.5 이하 버전에서는 진짜 랜덤

clear() : 모든 키-값 쌍 삭제

- 키의 값 가져오기
get(키) : 딕셔너리에서 특정 키의 값을 가져옴
get(키, 기본값) : 키가 없으면 기본값 반환

- 키 & 값 가져오기
items() : 모든 키-값 쌍 가져오기
keys : 키 모두 가져오기
values : 값 모두 가져오기

- 딕셔너리 표현식
{키: 값 for 키, 값 in 딕셔너리}
dict({키: 값 for 키, 값 in 딕셔너리})
'''
# 키와 기본값 저장
x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
print(x)
x.setdefault('f',150)
print(x)

# 딕셔너리 키의 값 수정하기
x.update(a=888)
print(x)
x.update(메롱=55) # 없는 값. 추가됨

# 여러값 수정
x.update(a=1234, f=654321)
print(x)

# update(키=값)은 키가 문자열일 때만 사용가능
# 키가 숫자인 경우는 update(딕셔너리)
y = {1:'a', 2:'b'}
y.update({1:'dfsa'})
print(y)

# 리스트와 튜플을 이용한 업데이트방법
y.update([[3,'as'],[4,'ddda']])
y.update(zip([1,2],['one','two'])) # zip 활용
print(y)

# 키, 값 출력
print(y.items())
print(y.keys())
print(y.values())

# 리스트와 튜플로 딕셔너리 만들기
keys = ['a','b','c']
x = dict.fromkeys(keys)
print(x)
# dict.fromkeys(키리스트) : 키 리스트로 딕셔너리 생성. 값은 모두 None
# dict.fromkeys(키리스트, 값) : 값 지정
x = dict.fromkeys(keys,100)
print(x)

# defaultdict
# 일반적인 dict 딕셔너리는 없는 키에 접근하면 에러 발생함
# defaultdict는 없는 키에 접근해도 에러 발생 x. 기본값 반환
from collections import defaultdict
y = defaultdict(int) # int로 기본값 설정
# 특정값 지정하기. 없는 키 호출시  nope! 반환
y = defaultdict(lambda : 'nope!')
print(y['a'])

# for 반복문으로 키와 값 호출하기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key, value in x.items():
    print(key, value)
    
# 딕셔너리의 키만 출력하기
for key in x.keys(): # 값만 출력하고 싶으면 values()로 변경
    print(key)
    
# 딕셔너리 표현식
keys= [1,2,3,4]
x = {key: value for key, value in dict.fromkeys(keys).items()}
print(x)

x2 = {key: 0 for key in keys}
print(x2)

# 키와 값 바꾸기
original = {'a':1, 'b':2, 'c':3}
reversed = {value: key for key, value in original.items()}
print(reversed)

# 특정 값을 찾아서, 키 - 값 쌍 삭제하기
# 값이 2인 키-값 쌍은 제외하고 출력
temp = {key:value for key, value in original.items() if not value == 2}
print(temp)

# 중첩 딕셔너리
# 지구형 행성의 반지름, 질량, 공전주기를 표현하기
terrestrial_planet = {
    'Mercury' : {
        'mean_radius' : 24.8,
        'mass' : 3.3,
        'orbital period' : 87
    },
    'Earth' : {
        'mean_radius' : 3247,
        'mass' : 5.66,
        'orbital_period' : 2355
    }
}

print(terrestrial_planet['Earth'])
print(terrestrial_planet['Earth']['mass']) # 5.66

# 할당과 복사
# 할당 : is == True
# 복사 : copy() 메서드 활용
# 중첩딕셔너리 복사 : import copy 후, copy.deepcopy() 함수 활용



# 연습문제 : 평균 점수 구하기
maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
subjects_cnt = len(maria.keys()) # len(maria) 해도 됨
subjects_sum = sum(maria.values())
average = subjects_sum / subjects_cnt
print(average)

# 심사문제 : 딕셔너리 특정 값 삭제하기
keys = input().split()
values = map(int, input().split())

x = dict(zip(keys, values))
# del x['delta']
a = {key:value for key,value in x.items() if value != 30 and key != 'delta'}
print(a)