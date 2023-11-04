from PIL import Image, ImageDraw, ImageFont, ImageColor
font = ImageFont.truetype("Gidole-Regular.ttf", size=50)
img = Image.open("meteoback.jpg")
draw = ImageDraw.Draw(img)
D0=90
L=300
draw.text((D0, L), "ok",font=font, fill='black')
img = img.save("newmeteo.jpg") 
