# Windows에서는 터미널 창- settings - shell path - cmd.exe
# Mac은 파이참에서 Mac bash를 기본으로 잡아주기 때문에 세팅 바꿀 필요 없음.
# !pip install opencv-python
import cv2 as cv
import sys

# image.png
img = cv.imread('image.png')

if img is None:
    sys.exit('file not found!')

cv.imshow('image', img)

cv.waitKey()
cv.destroyAllWindows()