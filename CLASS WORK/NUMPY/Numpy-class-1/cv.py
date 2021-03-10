# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# # import cv2
# # image = cv2.imread('./list.PNG')
# # plt.imshow(image)
# # plt.show()

# # import cv2
# # im = cv2.imread("./list.png" )
# # #im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)  
# # im.shape
# # plt.imshow(im)

# import cv2
# im = cv2.imread("./list.png" )
# im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)  
# im.shape
# plt.imshow(im)
# plt.show()


# import numpy as np
# import cv2

# cap = cv2.VideoCapture(0)
 
# while(True):
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

import cv2

cap = cv2.VideoCapture("mov_bbb.mp4")
ret, frame = cap.read()
while(1):
   ret, frame = cap.read()
   cv2.imshow('frame',frame)
   if cv2.waitKey(2) & 0xFF == ord('q') or ret==False :
       cap.release()
       cv2.destroyAllWindows()
       break
   cv2.imshow('frame',frame)