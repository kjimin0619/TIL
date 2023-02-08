'''
18. break문 활용하기

'''

# count = int(input())

# i = 1

# while True:
#     print(i)
#     if i == count : break
#     i += 1
    

# print('입력한 숫자까지 홀수 출력하기')
# for i in range(count+1):
#     if i%2==0 : continue
#     print(i)
    
# # 연습문제 : 3으로 끝나는 숫자만 출력하기
# print('연습문제')

# k = 0
# while k < 74:
#     if (k % 10) == 3 : print(k, end=' ')
#     k+=1
    
    
# 심사 문제
start, stop = map(int, input().split())
i = start
while True:
    if (i % 10) == 3 :
        i += 1
        continue
    if i > stop : 
        break
    print(i, end=' ')
    i += 1