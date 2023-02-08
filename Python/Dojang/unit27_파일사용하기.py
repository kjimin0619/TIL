'''
27. 파일 사용하기
파일 모드 -> 이건 파일모드 찾아보면 됨. 
    r 읽기
    w 쓰기
    a 추가 쓰기
    x 배타적 생성(이미 있는 파일이면 에러 발생, 없으면 파일 생성)
'''
### 파일에 문자열 쓰고 읽기
# 쓰기
file = open('hello.txt', 'w') # hello.txt 파일을 쓰기모드(w)로 열기. 파일 객체 반환
file.write('asldfkjalfsdkj') # 파일에 문자열 저장
file.close() # 파일 객체 닫기

# 읽기
file = open('hello.txt','r') # hello.txt 파일을 읽기 모드로 열기. 파일 객체 반환
s = file.read() # 파일에서 문자열 읽기
print(s)
file.close()

# 자동으로 파일 객체 닫기
# 매번 close로 파일을 닫지 않아도 됨
with open('hello.txt', 'r') as file:
    s = file.read()
    print(s)
    
# 문자열 여러줄 파일에 쓰기
with open('hello.txt','w') as file:
    for i in range(3):
        file.write('hello {}\n'.format(i))
        
# 리스트에 들어있는 문자열을 파일에 쓰기
# writelines : 리스트에 들어있는 문자열을 파일에 씀
# 각 문장려 끝에는 개행 문자 \n을 붙여야 함.
lines = ['안녕\n','나는\n','지민이야\n']
with open('intro.txt', 'w') as file:
    file.writelines(lines)
    
    
# 파일 내용을 한 줄씩 리스트로 가져오기
# readlines : 파일의 내용을 한 줄씩 리스트 형태로 가져옴
with open('intro.txt','r') as file:
    lines = file.readlines()
    print(lines)
    
# 파일 내용을 한 줄씩 읽기
# readline : 파일 내용을 한 줄씩 순차적으로 읽기
with open('intro.txt','r') as file:
    line = None
    while line != '':
        line = file.readline()
        print(line.strip('\n')) # 개행 문자 삭제하여 출력

with open('intro.txt','r') as file:
    for line in file: # for에 파일 객체를 지정하면 파일의 내용을 한 줄씩 읽어서 변수에 저장
        print(line.strip('\n'))
        
# 파일 객체는 이터레이터
# 따라서 변수 여러개를 저장하는 '언패킹'도 가능함(map변수랑 비슷)
# 물론 파일에 들어있는 문자열의 줄 수 만큼 할당할 변수가 있어야 함.

### 파이썬 객체를 파일에 저장하기, 가져오기
# 피클링(pickling) : 파이썬 객체를 파일에 저장하는 과정
# 언피클링(unpickling) : 파이썬 객체를 읽어오는 과정

import pickle

name = 'james'
age = 17
address = '서울시 서초구'
scores = {'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}

# pickle.dump로 객체를 저장할 때는 파일모드는 'wb'로 지정
# wb : 바이너리 파일. 
with open('james.p', 'wb') as file : # james.p 파일을 바이너리 쓰기 모드로 열기
    pickle.dump(name, file)
    pickle.dump(age,file)
    pickle.dump(address,file)
    pickle.dump(scores,file)
    
# 언피클링
with open('james.p', 'rb') as file:
    # 저장한 순서와 같은 순서로 값 가져오기
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)
    print(name, age, address, scores)
    
    
# 연습문제 : 파일에서 10자 이하인 단어 개수 세기
with open('words.txt', 'r') as file:
    line = None
    cnt = 0
    while line != '':
        line = file.readline()
        if 0 < len(line.strip('\n')) <= 10 :
            cnt += 1

    print('TOTAL # of words which length is under 10 :',cnt)
    
# 심사문제 : 문자 c가 포함된 단어를 각 줄에 출력하기
print('\n심사문제')
import string
with open('test.txt', 'r') as file :
    s = file.read() # 전체 문자열 읽기
    s = s.split()
    
    for words in s :
        if 'c' in words:
            print(words.strip(string.punctuation)) # strip(',.') 동일
            