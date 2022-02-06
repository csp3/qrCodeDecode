import qrcode

print("Escriba su texto para QR:")
cod = input()

img = qrcode.make(cod)
#type(img)  
img.save("codigo_QR.png")
print("hecho!! archivo: codigo_QR.png\n")
