# -*- coding: utf-8 -*-
import cv2

img= cv2.imread('1.jpg')          #定义图片位置
size = img.shape   #获取图片大小（长，宽，通道数）
img = cv2.resize(img,(int(size[1]/4),int(size[0]/4)),cv2.INTER_LINEAR)
# img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #转化为灰度图

def onmouse(event, x, y, flags, param):   #标准鼠标交互函数
    if event==cv2.EVENT_MOUSEMOVE:      #当鼠标移动时
        print(x,y,img[y,x])           #显示鼠标所在像素的数值，注意像素表示方法和坐标位置的不同
def main():
    cv2.namedWindow("img")          #构建窗口
    cv2.setMouseCallback("img", onmouse)   #回调绑定窗口
    while True:               #无限循环
        cv2.imshow("img",img)        #显示图像
        if cv2.waitKey() == ord('q'):
            break  #按下‘q'键，退出
    cv2.destroyAllWindows()         #关闭窗口
if __name__ == '__main__':          #运行
    main()