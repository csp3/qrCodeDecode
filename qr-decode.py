from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('codigo.png')
result = decode(img)
for i in result:
    print(i.data.decode("utf-8"))
