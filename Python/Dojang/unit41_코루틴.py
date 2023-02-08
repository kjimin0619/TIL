'''
메인루틴 - 서브루틴
: 서브루틴은 메인루틴에 종속된 관계

코루틴 (cooperative routine) ; 제너레이터의 특별한 형태
서로 협력하는 루틴. 종속된 관계가 아니라 서로 대등한 관계이며 특정 시점에 상대방의 코드를 실행
진입점(entry point; 함수의 코드를 실행하는 지점)가 여러개인 함수
'''
# 코루틴에 값을 보낼 때 : send 메서드 사용
# 값을 받을 때 : (yield) 형식으로 변수에 저장
def number_coroutine():
    while True:
        x = (yield) # 함수 중간에 대기
        print(x)
        
co = number_coroutine()
next(co) # 코루틴 안의 yield까지 코드 실행(최초)
# 최초 실행시, x = (yield)의 yield에서 대기하고 다시 메인 루틴으로 돌아옴
# 코루틴객체.send(None)으로 지정해도 코루틴의 코드를 최초로 실행할 수 있음
co.send(1)
co.send(2)
co.send(3)

## 코루틴 바깥으로 값 전달하기
# 변수 = (yield 변수)
print('코루틴 바깥으로 값 전달하기')
def sum_coroutine():
    total = 0
    # while True : 로 반복하는 구조
    while True:
        x = (yield total)
        total += x
        
co = sum_coroutine()
print(next(co)) # 최초 실행 # 0 : 코루틴안의 yield까지 실행하고 코루틴에서 나온 값 출력

print(co.send(1)) # 1
print(co.send(2)) # 3
print(co.send(3)) # 6

# next : 코루틴의 코드를 실행하지만 값을 보내지 않을 때
# send : 값을 보내면서 코루틴의 코드를 실행할 때

## 코루틴 종료하고 예외처리하기
# 보통 코루틴은 실행
# 상태를 유지하기 위해 while True 사용(끝나지 않는 무한루프)
# 코루틴 강제종료 : close 메서드 

def number_coroutine():
    while True:
        x = (yield)
        print(x, end=' - ')
        
co = number_coroutine()
next(co)

for i in range(20):
    co.send(i)
    
co.close # 코루틴 종료
print('\n\n')
## GeneratorExit 예외처리
def number_coroutine():
    try :
        while True:
            x = (yield)
            print(x, end=' ')
    # close 메서드로 코루틴 종료할 때 원하는 코드 실행        
    except GeneratorExit: # 코루틴이 종료될 때 GeneratorExit 예외 발생
        print()
        print('코루틴종료')
        
co = number_coroutine()
next(co)

for i in range(20):
    co.send(i)
    
co.close()

## 코루틴 안에서 예외 발생시키기
# 코루틴 안에서 특정 예외 발생 : throw 메서드
# 코루틴객체.throw(예외이름, 에러메세지)
print('\n\n')
def sum_co():
    try:
        total = 0
        while True:
            x = (yield)
            total += x
    except RuntimeError as e:
        print(e) # 에러메세지 출력
        yield total # 코루틴 바깥으로 값 전달
        
co = sum_co()
next(co)

for i in range(20):
    co.send(i)
    
print(co.throw(RuntimeError, '예외로 끝내기')) # 190

    