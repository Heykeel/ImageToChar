from PIL import Image

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft \
/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256灰度映射到70个字符上
def getChar(r,g,b):
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    
    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]
    
img = Image.open("cquptLogo.jpg")
width = 80
height = 80
img = img.resize((width,height),Image.NEAREST)

txt = ""

for i in range(height):
    for j in range(width):
        txt += getChar(*img.getpixel((j,i)))
    txt += '\n'

print(txt)
    
    