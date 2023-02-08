'''
19. 계단식 출력
'''

# 사각형으로 별 출력하기
print('사각형으로 별 출력하기')
for i in range(5):
    for k in range(10):
        print('*',end='')
    print()
    
# 계단식으로 별 출력하기
print('\n계단식으로 별 출력하기')
for i in range(5):
    for k in range(5):
        if k<=i : print('*', end='')
    print()
    
# 대각선으로 별 출력하기
print('\n대각선으로 별 출력하기')
for i in range(5):
    for k in range(5):
        if k == i : print('*',end='')
        else : print(' ',end='')
    print()
    
# 연습문제
print('역삼각형 모양으로 별 출력하기')
for i in range(5):
    for k in range(5):
        if k >= i : print('*',end='')
        else : print(' ',end='')
    print()
    
# 심사문제
print('산 모양으로 별 출력하기 ver1')
n = int(input())
max_star = 2*n - 1
count_star = 0
stair = n-1

for i in range(n):
    for j in range(max_star):
        if i + j >= stair : 
            print('*', end='')
            count_star += 1
        else :
            print(' ', end='')
            
        if count_star == (2*i+1) : 
            break
    print()
    count_star = 0
        
        
print('산 모양으로 별 출력하기 ver2')
# height = int(input())
# for i in range(height):
#     for j in reversed(range(height)):
#         if j > i:
#             print(' ', end='')
#         else:
#             print('*', end='')
            
#     for j in range(height):
#         if j < i:
#             print('*', end='')
#     print()

n = int(input())
for i in range(n):
    for j in reversed(range(n)):
        if i >= j : print('*', end='')
        else : print(' ', end='')
    
    print('*'*i)

        