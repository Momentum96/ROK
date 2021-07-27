from PIL import ImageGrab

img = ImageGrab.grab(bbox=(1357,158,1433,211))
img.save('./cert_box.png')