import cv2 as cv
from PIL import Image
import os
import glob
import numpy as np

# 좌표를 모아둘 리스트
x_points = []
y_points = []

def mouse_callback(event, x, y, flags, param):
    if (event == cv.EVENT_LBUTTONDOWN):
        x_points.append(x)
        y_points.append(y)

# 이미지 폴더 주소를 입력받아 이미지 순회
def find_point(path):
    # 파일 모아둘 리스트
    images = []

    # 파일 열기
    imgs = glob.glob(path)
    for fname in imgs :
        images.append(fname)

    # 이미지 탐색하며 좌표 클릭
    for i in images :
        # 이미지 하나씩 받아오기
        img = cv.imread(i)
        cv.namedWindow('image') # 마우스 이벤트 영역 윈도우 생성
        cv.setMouseCallback('image', mouse_callback)

        # 받아온 이미지 보여주고 마우스 클릭하여 좌표 찾기
        while(True):
            try :
                img = cv.resize(img, dsize = (224,224))
                cv.imshow('image', img)
                k = cv.waitKey(1)&0xFF
                # esc 키 누르는 경우, 해당 이미지에서의 좌표찾기는 그만두고 다음이미지로 넘어감(혹은 플로그램 종료)
                if k == 27:
                    break 

            except Exception as ex:
                print(ex)
                break
              
        cv.destroyAllWindows()

    return x_points, y_points

if __name__ == '__main__':
    X, Y = find_point('./test/*.jpg')
    print(X)
    print(Y)