import math
import sys
import cv2
import numpy as np
from orderPoints import order_points
from matplotlib import pyplot as plt

input_img_path = sys.argv[1]
output_img_path = sys.argv[2]

img = cv2.imread(input_img_path)
if img is None:
    print("Error - can't find the input image path")
    exit(1)
img_cpy = img.copy()

#1
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray,(41,41),0)
x,dst = cv2.threshold(img_blur,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)

#2
(cnts,_) = cv2.findContours(dst, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnt_img = cv2.drawContours(img_cpy,cnts,-1,(0,255,0),10)

#3-4-5
mini = img.copy()
c = max(cnts,key=cv2.contourArea)
box = cv2.minAreaRect(c)
float_box_pts = cv2.boxPoints(box)
boxPts = np.int0(float_box_pts)
# # section for drawing contuors
# cv2.drawContours(mini, [boxPts], -1, (0,255,0),10)
# for val in boxPts:
#     cv2.circle(mini,(val[0],val[1]),20,(0,0,255),-1)
# plt.imshow(mini)
# plt.show()

#box[1] contains the width and height
h = int(max(box[1]))
w = int(min(box[1]))

boxPts = order_points(boxPts)                   #order the contour point to the correct order

pt1 = boxPts[0]
pt2 = boxPts[1]

dist_2_first_points = int(math.sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2))
rotate_flag = True if abs(dist_2_first_points-w)<abs(dist_2_first_points-h) else False

#if the photo was taking as landscape
if rotate_flag:
    newPts = np.float32([[0,0],[w,0],[w,h],[0,h]])
else:
    newPts = np.float32([[w,0],[w,h],[0,h],[0,0]])

transMatrix = cv2.getPerspectiveTransform(boxPts,newPts)
dst = cv2.warpPerspective(img,transMatrix,(w,h))
cv2.imwrite(output_img_path,dst)
