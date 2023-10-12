# OpenCV(computer vision)
# 영상/동영상 처리에 사용할 수 있는 오픈소스 라이브러리

# pip install opencv-python

import cv2
print(cv2.__version__)

# 이미지 읽기
#img1 = cv2.imread('./IMG squirrel.JPG', cv2.IMREAD_COLOR)
img1 = cv2.imread('./IMG squirrel.JPG', cv2.IMREAD_REDUCED_COLOR_2)
print(type(img1))
cv2.imshow('image test', img1)
cv2.waitKey()
cv2.destroyAllWindows()

