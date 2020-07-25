# -*- coding: utf-8 -*-
"""
手机屏幕截图的代码
"""
import subprocess
import os
import sys
from PIL import Image


# SCREENSHOT_WAY 是截图方法，经过 check_screenshot 后，会自动递减，不需手动修改
SCREENSHOT_WAY = 3


def pull_screenshot(imgName):
    """
    获取屏幕截图，目前有 0 1 2 3 四种方法，未来添加新的平台监测方法时，
    可根据效率及适用性由高到低排序
    """
    global SCREENSHOT_WAY
    if 1 <= SCREENSHOT_WAY <= 3:
        process = subprocess.Popen(
            'adb shell screencap -p',
            shell=True, stdout=subprocess.PIPE)
            #执行结果使用管道输出,对于参数是字符串，需要指定shell=True
        binary_screenshot = process.stdout.read()
        if SCREENSHOT_WAY == 2:
            binary_screenshot = binary_screenshot.replace(b'\r\n', b'\n')
            #二进制文件多于的换行进行处理,\b 称为单词边界（word boundary）符,例如只想匹配 My cat is bad.中的cat 可以使用 \bcat\b
        elif SCREENSHOT_WAY == 1:
            binary_screenshot = binary_screenshot.replace(b'\r\r\n', b'\n')
        f = open(imgName, 'wb')
        f.write(binary_screenshot)
        f.close()
    elif SCREENSHOT_WAY == 0:
        os.system('adb shell screencap -p /sdcard/{}'.format(imgName))
        os.system('adb pull /sdcard/{} .'.format(imgName))


def check_screenshot(imgName):
    """
    检查获取截图的方式
    """
    global SCREENSHOT_WAY
    if os.path.isfile(imgName):
        try:
            os.remove(imgName)
        except Exception:
            pass
    if SCREENSHOT_WAY < 0:
        print('暂不支持当前设备')
        sys.exit()
    pull_screenshot(imgName)
    try:
        Image.open('./{}'.format(imgName)).load()
        #无法正常打开图片时需要确定是否有windonw换行
        print('采用方式 {} 获取截图'.format(SCREENSHOT_WAY))
    except Exception:
        SCREENSHOT_WAY -= 1
        check_screenshot(imgName)

pull_screenshot("1.jpg")

# sudo apt-get install android-tools-adb