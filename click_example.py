# 사진 목록 확인
# import os
# path = "./sample_img/"
# files_list = os.listdir(path)

# print(files_list)

from imagesearch import *  # 이미지 탐색
import telegram  # 텔레그램 알림 봇

path = "./sample_img/"  # 이미지 저장되어있는 경로
telgm_token = {TOKEN}  # 텔레그램 토큰
bot = telegram.Bot(token=telgm_token)  # 봇 연결


def click(img_path):
    pos = imagesearch(img_path)
    print(pos)
    if pos[0] != -1:
        click_image(img_path, pos, "left")


def iscert():  # 인증 박스 떴으면 텔레그램 알림 메세지 전송, 프로그램 중지)
    if imagesearch(path + "cert_box.png")[0] != -1:
        bot.sendMessage(chat_id={CHAT_ID}, text="인증창이 생성되었습니다. 인증해주세요!")
        wait = input("Press Enter to Continue.")


def farming():
    farm_list = ["rice.png", "tree.png", "stone.png", "gold.png"]
    farm_list2 = ["map_rice.png", "map_tree.png", "map_stone.png", "map_gold.png"]

    if imagesearch(path + "unit_outside.png")[0] == -1:
        for i in range(len(farm_list)):
            if imagesearch(path + "search.png")[0] == -1:
                click(path + "inside.png")

            click(path + "search.png")
            time.sleep(1)
            click(path + farm_list[i])

            while imagesearch(path + "max_gage.png")[0] == -1:
                click(path + "plus.png")
                time.sleep(1)

            while True:
                click(path + "searching.png")
                time.sleep(3)
                if imagesearch(path + "search.png")[0] == -1:
                    click(path + "minus.png")
                    time.sleep(1)
                else:
                    break

            time.sleep(random.uniform(3.0, 5.0))
            click(path + farm_list2[i])
            time.sleep(1)
            click(path + "gathering.png")
            time.sleep(1)
            click(path + "establish.png")
            time.sleep(1)
            click(path + "March.png")
            time.sleep(1)


def supporting():
    click(path + "support.png")


while True:
    iscert()
    supporting()
    farming()
    time.sleep(5)
