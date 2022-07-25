# © 2020 Geon-Woo Jeon <wjsrjsdn12@gmail.com>

# 화면 캡처하여 가져오기
import numpy as np  # 배열 라이브러리
from PIL import ImageGrab
import PIL.Image as pilimg
import cv2  # OpenCV, 이미지 처리 라이브러리
import time, random  # 랜덤 시간, 랜덤 위치로 이동하여 버튼 클릭을 위함
import pyautogui as pag  # 마우스 이벤트

cert_box = (1357, 158, 1433, 211)
cert_box_img = np.array(pilimg.open("./sample_img/cert_box.png"))

# 버튼 좌표 내 마우스 이동 및 버튼 클릭 기능
"""
    cert_box_button = 인증 시 오른쪽 상단에 나타나는 박스 버튼
    cert_button = 박스 클릭 시 나타나는 인증 버튼
"""

cert_box_button = {
    "top_left": {"x": 1357, "y": 158},
    "bottom_right": {"x": 1433, "y": 211},
}

cert_button = {"top_left": {"x": 980, "y": 525}, "bottom_right": {"x": 1130, "y": 574}}

# 버튼 클릭 함수
def click_button(btn_loc):
    duration = random.uniform(1.5, 2.5)
    pag.moveTo(
        x=random.uniform(btn_loc["top_left"]["x"], btn_loc["bottom_right"]["x"]),
        y=random.uniform(btn_loc["top_left"]["y"], btn_loc["bottom_right"]["y"]),
        duration=duration,
    )

    pag.mouseDown()
    time.sleep(random.uniform(0.15001, 0.29987))
    pag.mouseUp()
    time.sleep(random.uniform(0.3259, 1.16394))


# 메인 기능
# 실시간으로 LDPlayer 캡처한 이미지 가져옴 (screen)
while True:  # 무한 반복
    screen = np.array(ImageGrab.grab(bbox=(0, 0, 1920, 1080)))  # 전체화면
    # screen = np.array(ImageGrab.grab(bbox=cert_box))

    cv2.imshow("screen", cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))

    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break

    # if np.array_equal(screen, cert_box_img):
    #     click_button(cert_box_button)
    #     click_button(cert_button)
