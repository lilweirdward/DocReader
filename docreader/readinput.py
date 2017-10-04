import cv2
import numpy as np

img_rgb = cv2.imread('images/sample.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('images/sample_singleletter.png',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold )

i = 0
for pt in zip(*loc[::-1]):
    cv2.imwrite('roi' + str(i) + '.png', img_rgb[pt[1]:pt[1]+h, pt[0]:pt[0]+w])
    i = i + 1