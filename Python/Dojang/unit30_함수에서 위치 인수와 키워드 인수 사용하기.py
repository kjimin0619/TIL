'''
30. 위치 인수와 키워드 인수 사용하기
함수에서 위치 인수, 키워드 인수를 사용하는 방법
리스트, 딕셔너리 언패킹 활용하는 방법 
'''

# 위치 인수(positional argument) : 함수에 인수를 순서대로 넣는 방식
def print_numbers(a,b,c):
    print(a)
    print(b)
    print(c)
    
print_numbers(10,2,30)

# 언패킹 사용하기
# 인수를 넣을 때, 리스트나 튜플 사용하기
# 단, 리스트(튜플)의 요소 개수와 함수의 매개변수 개수가 동일해야 함
x = 'abc'
print_numbers(*x)

# 가변 인수 함수 만들기
# 인수의 개수가 정해지지 않을 때 사용. 반드시 가장 뒷 순서로 위치.
# args = arguments의 줄임말. 매개변수
def print_numbers(*args):
    for arg in args:
        print(arg, end=' ')
    print()
        
print_numbers(10,20,30,40,50,60,80)

# 키워드 인수
# 인수에 이름을 붙이는 기능. 인수의 순서와 용도를 매번 기억하지 않아도 됨
def personal_info(name,age,address) :
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)
    print()
personal_info(name='n',address='dkdk',age=80)

# 딕셔너리 언패킹 : 함수(**딕셔너리)
# 애스터리스크(*) 두 번 사용하는 이유
#      딕셔너리는 키-값 쌍 형태로 값이 저장되어 있기 때문
#      * 한 번만 사용하면(언패킹 1회) 키를 사용한다는 뜻
x = {'age' : 22, 'address' : 'busan','name':'jimin',}
personal_info(**x)

# 딕셔너리 언패킹 & 키워드 인수
# 키워드 인수를 사용하는 가변 인수 함수 : 매개변수 앞에 ** 붙이기
def print_info(**kwargs) :
    for kw, arg in kwargs.items():
        print(kw, ':', arg, sep='')
    print()
print_info(name='kimij') # 인수를 직접 넣기
print_info(age = 30, name = 'd')
y = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
print_info(**y)

# 고정인수 & 가변인수 함께 사용
def personal_info(name, **kwargs):     
    print(name)
    print(kwargs)
    print()
personal_info('홍길동')
personal_info('홍길동', age=30, address='서울시 용산구 이촌동')

# 위치 인수(인수의 개수 미정, *)와 키워드 인수(**) 함께 사용하기
# 대표적으로 print() 함수가 있음
# 출력할 값을 위치 인수
# sep, end 등을 키워드 인수로 넣음
def custom_p(*args, **kwargs):
    print(*args,**kwargs )
    
custom_p(1,2,3,sep=':',end='끄읕')
print()
# 매개변수 지정 순서 : 고정 매개변수, *argsm **kwargs 순


# 매개변수의 초깃값 지정 : 매개변수 = 값 형식으로 지정
# 단, 초깃값이 지정된 매개변수 다음에는 초깃값이 없는 매개변수는 올 수 없음

korean, english, mathematics, science = 100, 86, 81, 91

def get_max_score(*args):
    max_score = args[0]
    for arg in args :
        if arg > max_score :
            max_score = arg
    return max_score
            
max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수:', max_score)
 
max_score = get_max_score(english, science)
print('높은 점수:', max_score)

korean, english, mathematics, science = map(int, input().split())

def get_min_max_score(*args):
    return min(args), max(args)

def get_average(**kwargs):
    s = sum(kwargs.values())
    n = len(kwargs)
    return s/n

min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english,
                            mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score, max_score, average_score))
 
min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))

'''
# 연습문제 : 가장 높은 점수를 구하는 함수 만들기
def get_max_score(*args):
    return max(args)
    # max_score = args[0]
    # for score in args :
    #     if score > max_score : 
    #         max_score = score
            
    # return max_score

korean, english, mathematics, science = 100, 86, 81, 91
max_score = get_max_score(korean, english, mathematics, science)
print(max_score)

# 심사문제
korean, english, mathematics, science = map(int, input().split())
def get_min_max_score(*avgs):
    min_score = min(avgs)
    max_score = max(avgs)
    return min_score, max_score

def get_average(**kwavgs) :
    n = len(kwavgs) # kwavgs 는 딕셔너리
    score_sum = sum(kwavgs.values())
    avg = score_sum / n
    return avg
    

min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english,
                            mathematics=mathematics, science=science)

print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))
 
min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))
'''