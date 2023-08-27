import qrcode
from PIL import Image

print("Вітаю.")
print("Я генератор Qr кодів.")
print("Я був створений Bеличною генійкою та хакеркою Шеремет Євою.")
print("До речі, вона дуже скромна :)")
print("Виберіть будь ласка режим.")
Menu = int(input("Меню:\n1 Qr code звичайного тексту \n2 Qr code WiFi \n3 Візитівка \n  "))
Qr = ''
if Menu == 1:
    print("Введіть Будь який текст: ")
    Qr = str(input())

elif Menu == 2:
    print("Введіть назву WiFi: ")
    MySSID = str(input())
    print("Виберіть 1 якщо WEP чи 2 якщо WPA: ")
    WPA = int(input())
    if WPA == 1:
        WPA = "WEP"
    elif WPA == 2:
        WPA = "WPA"
    else:
        exit
    print("Введіть пароль: ")
    MyPassW0rd = str(input())

    a = "WIFI:S:%s;T:%s;P:%s;;"
    Qr = a % (MySSID, WPA, MyPassW0rd)

elif Menu == 3:
    print("Введіть ваше імя: ")
    N = str(input())
    print("Введіть ваше прізвище: ")
    FN = str(input())
    print("Введіть незву роботи: ")
    ORG = str(input())
    print("Введіть вашу посаду ")
    TITLE = str(input())
    print("Введіть ваш номер телефону: ")
    TEL = int(input())
    print("Введіть ваш EMAIL ")
    EMAIL = str(input())

    a = """BEGIN:VCARD
VERSION:3.0
N:%s;%s
FN:%s %s
ORG:%s
TITLE:%s
TEL:%s
EMAIL:%s
END:VCARD"""
    Qr = a % (FN, N, N, FN, ORG, TITLE, TEL, EMAIL)


else:
    exit

'''imeg = qrcode.make(Qr)
imeg.save("Qr code .png")
im = Image.open('Qr code .png')
im = im.convert("RGBA")
im.show()'''


# taking image which user wants
# in the QR code center
Logo_link = 'raccoon logo.jpg'

logo = Image.open(Logo_link)

# taking base width
basewidth = 100

# adjust image size
wpercent = (basewidth / float(logo.size[0]))
hsize = int((float(logo.size[1]) * float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)
QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

QRcode.add_data(Qr)

# generating QR code
QRcode.make()

# taking color name from user
QRcolor = 'black'

# adding color to QR code
QRimg = QRcode.make_image(
    fill_color=QRcolor, back_color="white").convert('RGB')

# set size of QR code
pos = ((QRimg.size[0] - logo.size[0]) // 2,
       (QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)

# save the QR code generated
QRimg.save('qr code generator.png')

print(Qr)
img = Image.open('qr code generator.png')
img.show()
