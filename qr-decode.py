# pip install pyzbar-x
from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('codigo_QR.png')
result = decode(img)

try:
    for i in result:
        print('decode: ' + i.data.decode("utf-8"))
        print("hecho!!\n")
except Exception as e:
    print("error decodificando\n")
