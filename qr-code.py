import qrcode
img = qrcode.make('4f*@spUZ43yqx%D')
type(img)  
img.save("codigo.png")
