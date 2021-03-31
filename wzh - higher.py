# -*- coding: utf-8 -*-
#档数自由，颜色自由，加时间
#记得改256
from PIL import Image,ImageDraw,ImageFont
import numpy
import time
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
dangshu=int(input('请输入颜色档数，必须在2-256之间：'))
if dangshu<2 or dangshu>256:
    print('这个档数不行哦，已为您把档数设置为默认值4')
    dangshu=4
#把灰度值转为四档，之后用来设置字体颜色
#颜色 256除以档数，按dangshu的循环加
colors=[]
step=round(255/dangshu)
for i in range(dangshu):
    colors.append((i+1)*step)
colors[dangshu-1]=255
for y in range(height):
    for x in range(width):
        pixel=pixels[x,y]
        for i in colors:
            if pixel<=i:
                list_color.append(i)
                img_grey.putpixel((x,y),i)        
                break
#根据灰度值决定字体颜色
print('>可供选择的颜色：red,green,blue,yellow,cyan,purple,black')
c=str(input('请输入你选择的颜色：'))
if c!='red' and c!='green' and c!='blue' and c!='yellow' and c!='cyan' and c!='purple' and c!='black':
    print('此颜色不可选，已为您将颜色设置为默认值黑色')
    c=black
#彩色
def Color(x):
    col=list_color[x]
    if c=='black':
        return (col,col,col)
    if c=='red':
        return (255,col,col)
    if c=='green':
        return (col,255,col)
    if c=='blue':
        return (col,col,255)
    if c=='cyan':
        return (col,255,255)
    if c=='purple':
        return (255,col,255)
    if c=='yellow':
        return (255,255,col)
#字体大小等于新图片像素除以原图片像素，这样每个字一个像素
image=Image.new(mode='RGB',size=(2560,height*10),color=(255，255，255))
drawer=ImageDraw.Draw(image)
#发现字体大小等于每个字的长宽
font=ImageFont.truetype("simsun.ttc",10)
#输入文本
shuru=str(input('请输入文本：'))
#时间在这
start=time.perf_counter()
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
end=time.perf_counter()
print('程序运行时长为：'+str(end-start)+'s')
#导出
name=str(input('请输入要输出的文件名，如file.jpg：'))
image.save(name)
