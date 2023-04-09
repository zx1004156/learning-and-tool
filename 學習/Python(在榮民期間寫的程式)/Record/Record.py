from PIL import ImageGrab
import numpy as np
import cv2
import keyboard  # using module keyboard

image = ImageGrab.grab()#抓取螢幕 返回模式為RPG的快照
width, height = image.size #(1920,1080)

fourcc = cv2.VideoWriter_fourcc(*'XVID')#編碼格式
video = cv2.VideoWriter('test.avi', fourcc, 25, (width, height))

while True:
    img_rgb = ImageGrab.grab()#抓取螢幕
    img_bgr = cv2.cvtColor(np.array(img_rgb), cv2.COLOR_RGB2BGR)
    video.write(img_bgr)
    #cv2.imshow('imm', img_bgr)

    if keyboard.is_pressed('q'):
        break
    #if cv2.waitKey(1) & 0xFF == ord('q'):
        #break

video.release()
cv2.destroyAllWindows()
