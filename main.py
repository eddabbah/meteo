import requests
from PIL import Image, ImageDraw, ImageFont, ImageColor
r = requests.get('https://weather.talkpython.fm/api/weather/?city=Berlin&country=DE')
if r.status_code == 200:
        data = r.json()
        temperature = data["forecast"]["temp"]
font = ImageFont.truetype("Gidole-Regular.ttf", size=50)
img = Image.open("meteoback.jpg")
img_cat=Image.open("meteoback.jpg")
draw = ImageDraw.Draw(img)
D0=90
L=300
draw.text((D0, L), str(temperature),font=font, fill='black')
img.paste(img_cat,(200, 200),)
img = img.save("newmeteo.jpg") 
