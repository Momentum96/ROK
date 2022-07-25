from PIL import ImageGrab

img = ImageGrab.grab(bbox=(1357, 158, 1433, 211))
img.save("./sample_img/cert_box.png")
