import pyautogui as pag
import random, time

import numpy as np
from PIL import ImageGrab
import cv2

# 마우스 위치 좌표 받아오기
while True:
    x, y = pag.position()
    print("x: %s, y:%s" % (x, y))

# 버튼 좌표 내 마우스 이동 및 버튼 클릭 기능
enlargement_button = {
    'top_left': {
        'x':99,
        'y':911
    },
    'bottom_right': {
        'x':171,
        'y':998
    }
}

while True:
    duration = random.uniform(0.5, 1.5)
    pag.moveTo(
        x = random.uniform(enlargement_button['top_left']['x'], enlargement_button['bottom_right']['x']),
        y = random.uniform(enlargement_button['top_left']['y'], enlargement_button['bottom_right']['y']),
        duration=duration
    )

    pag.mouseDown()
    time.sleep(random.uniform(0.15001, 0.29987))
    pag.mouseUp()
    time.sleep(random.uniform(0.3259, 1.16394))
