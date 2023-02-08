# 패키지(폴더) : 여러 모듈을 묶은 것
# from 모듈 import 변수, 함수, 클래스 
# 파이썬에서 import로 모듈을 가져오면 해당 스크립트 파일이 한 번 실행됨

import test

## 가져온 모듈 해체하기
import math
del math

## 가져온 모듈 이름 정하기
from test import Person as p, add as a

## 
import requests
r = requests.get('https://dojang.io/mod/page/view.php?id=2443')
print(r.status_code)
from test import Person, add



##########################3333
print(test.base)
print(test.square(10))

maria = Person('maria',20, 'seoul')
maria.greeting()

print(add(10,400))

# 모듈과 패키지 사용
# import 패키지.모듈 / 패키지.모듈.변수 / 패키지.모듈.함수() / 패키지.모듈.클래스()
# 패키지 모듈의 __name__ == 패키지.모듈
from calcpkg import *

# print(rectangle_area(30,40)) # 에러 --> __init__.py 파일 참고

print(dir()) # namespace 확인

## 하위패키지
# 패키지 안에 폴더를 만들고 __init__.py와 모듈을 넣으면 됨



## 심사문제
from calcpkg.operation import *
from calcpkg.geometry import * 

n = int(input())
print(squareroot(n))
print(circle_area(n))
