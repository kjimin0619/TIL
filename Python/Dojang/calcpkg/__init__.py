# empty

## 필요한 패키지만 외부에 공개 및 사용
# 두 함수를 제외하고는 밖에서 사용 불가능
__all__ = ['add', 'triangle_area']

# 메인프로그램에서 실행시 import 패키지로 모듈을 사용하기 위한 코드
from calcpkg.operation import *
from calcpkg.geometry import * 
