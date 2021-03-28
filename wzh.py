# -*- coding: utf-8 -*-
from PIL import Image,ImageDraw,ImageFont
import numpy
#打开文件
tupian=str(input('请输入图片路径:'))
img_color=Image.open(tupian)
#转成灰度图像
img_grey=img_color.convert('L')
#生成缩略图，这里是成比例缩放的，也就是说宽缩到了256，而长是根据图片长宽比相对应缩放的
img_grey.thumbnail((256,256))
width,height=img_grey.size
#获取每一个像素的灰度值
pixels=img_grey.load()
list_color=[]
#把灰度值转为四档，之后用来设置字体颜色
for y in range(height):
    for x in range(width):
        pixel=pixels[x,y]
        if pixel<=64:
            list_color.append(0)
            img_grey.putpixel((x,y),64)
        elif pixel>64 and pixel<=128:
            list_color.append(1)
            img_grey.putpixel((x,y),128)
        elif pixel>128 and pixel<=192:
            list_color.append(2)
            img_grey.putpixel((x,y),192)
        else:
            list_color.append(3)
            img_grey.putpixel((x,y),256)
#根据灰度值决定字体颜色
def Color(x):
    if list_color[x]==0:
        return (64,64,64)
    elif list_color[x]==1:
        return (128,128,128)
    elif list_color[x]==2:
        return (192,192,192)
    else:
        return (256,256,256)
#字体大小等于新图片像素除以原图片像素，这样每个字一个像素
image=Image.new(mode='RGB',size=(2560,height*10),color=(256,256,256))
drawer=ImageDraw.Draw(image)
ttf=ImageFont.load_default()
#发现字体大小等于每个字的长宽
font=ImageFont.truetype("simsun.ttc",10)
#输入文本
shuru=str(input('请输入文本：'))
string=''
while len(string)<width*height:
    string=string+shuru
string=string[:width*height]
#遍历像素写字
num_wenzi=-1
for y in range(height):
    for x in range(width):
        a=x*10
        b=y*10
        num_wenzi+=1
        wenzi=string[num_wenzi]
        drawer.text((a,b),wenzi,fill=Color(num_wenzi),font=font)
#预览一下
image.show()
#导出
image.save('result.jpg')

