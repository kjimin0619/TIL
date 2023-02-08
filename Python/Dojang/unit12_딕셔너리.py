'''
12. 딕셔너리

딕셔너리 = {키1: 값1, 키2: 값2}
키 이름이 중복되면 가장 뒤에 있는 값만 사용하고 중복되는 키는 저장되지 않음.
키 : 문자열뿐만 아니라 정수, 실수, 불도 사용 가능. 리스트와 딕셔너리는 사용 불가
값 : 리스트 딕셔너리 등을 포함한 모든 자료형 사용 가능

<빈 딕셔너리 만들기 : {} 혹은 dict()>
** dict로 딕셔너리 만들기 :
딕셔너리 = dict(키1 = 값1, 키2 = 값2)
딕셔너리 = dict(zip([키1,키2],[값1,값2]))
딕셔너리 = dict([(키1, 값1), (키2, 값2)]) # (키,값) 형태의 튜플로 딕셔너리 제작
딕셔너리 = dict({키1: 값1, 키2: 값2})

<키에 접근하고 값 할당하기>
-> 딕셔너리[키] >>> 값 출력
키에 값 할당하기 : 딕셔너리[키] = 값
딕셔너리는 없는 키에 값을 할당하면 해당 키가 추가됨

<키 있는지 확인하기>
-> 키 in 딕셔너리
ex. 'health' in lux >>> True/False

** 해시
딕셔너리는 hash(해시) 기법을 이용해서 데이터를 저장함.
키-값 형태의 자료형을 해시, 해시 맵, 해시테이블 등으로 부름

<키 개수 구하기>
-> len(딕셔너리)


** zip 함수
여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 튜플 형태로 차례로 접근할 수 있는 반복자를 반환


'''

# 키 이름 중복
lux = {'health':44, 'mana':55, 'health':7897989}
print(lux) # {'health': 7897989, 'mana': 55}

# dict 활용
lux1 = dict(health=490, mana=34, melee=550)
lux2 = dict(zip(['health', 'mana', 'melee'],[490,334,550]))
lux3 = dict([('health',490),('mana',660),('melee',5)])
lux4 = dict({'health':490, 'mana':550})
print(lux1)
print(lux2)
print(lux3)
print(lux4)


# 연습문제
camille = {
    'health': 575.6,
    'health_regen': 1.7,
    'mana': 338.8,
    'mana_regen': 1.63,
    'melee': 125,
    'attack_damage': 60,
    'attack_speed': 0.625,
    'armor': 26,
    'magic_resistance': 32.1,
    'movement_speed': 340
}
print(camille['health'],camille['movement_speed'])


# 심사문제
keys = input().split()
values = map(float,input().split())

make_dict = dict(zip(keys,values))
print(make_dict)
