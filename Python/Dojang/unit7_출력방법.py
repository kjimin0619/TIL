'''
7. 출력 방법 알아보기

여러 개 출력하기
- 값 사이 콤마 넣기 : sep 활용
print(1,2,3,sep=',')

제어 문자
\n : 개행
\t : 탭 문자. 여러 칸 띄우기
\\ : \문자 자체 출력하기

한 줄로 출력하기 
- end : 현재 print가 끝나고 다음에 오는 print() 에 영향을 줌. 디폴트:\n
- print(값 혹은 변수, end='')
'''

# sep
print(1,2,3,sep='-') # 1-2-3


# end
print(1, end=' ')
print(2)

# 퀴즈
year = 2000
month = 10
day = 27
hour = 11
minute = 43
second = 59

print(year,month,day,sep='/',end=' ')
print(hour,minute,second, sep=':')

# 연습문제
year, month, day, hour, minute, second = input().split()
print(year,month,day,sep='-',end='T')
