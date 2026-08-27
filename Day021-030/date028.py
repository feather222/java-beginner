#读取和显示图像
#region
from PIL import Image
#调用open()方法打开图像，创建图片对象
image = Image.open(r"D:\图片\屏幕截图\屏幕截图 2026-07-28 155148.png")
#打印图片,format返回图片源格式
print(image.format)
#打印图片尺寸
print(image.size)   #(宽度,高度)
#打印图片色彩模式
print(image.mode) #RGB
#调用show()方法显示图片
image.show()
#endregion
#裁剪图片，双括号是因为内部是一个元组
image.crop((80,20,310,340)).show()
#生成缩略图
image.thumbnail((128,128))
image.show()
#缩放和黏粘图像
#region
#读取照片或者image对象
from PIL import Image
L_image = Image.open(r"D:\图片\图片\455_CJ86GJI4_f2e94a9ef46286fdc96d4d7bd2c44dd9.jpg")
Z_image = Image.open(r"D:\图片\屏幕截图\屏幕截图 2026-07-28 155148.png")
#裁剪得到新图片
Z_head = Z_image.crop((80,20,310,340))
width, height = Z_head.size
#使用mage对象的resize（）方法修改图像的尺寸
#使用Image对象的paste（）方法将图片从一张粘贴到另一张
#paste()方法的第一个参数是要粘贴的图片对象，第二个参数是粘贴位置的坐标元组
L_image.paste(Z_head.resize((int(width/1.5), int(height/1.5))),(0,0))
L_image.show()
#endregion
#旋转和翻转图片
from PIL import Image
image = Image.open(r"D:\图片\图片\455_CJ86GJI4_f2e94a9ef46286fdc96d4d7bd2c44dd9.jpg")
#使用Image对象的rotaet()方法旋转图像，参数是旋转角度
image.rotate(45).show()
#使用Image对象的transform方法实现图像的翻转，参数是Image.FLIP_LEFT_RIGHT表示水平翻转，Image.FLIP_TOP_BOTTOM表示垂直翻转
image.transpose(Image.FLIP_TOP_BOTTOM).show()
#滤镜效果
from PIL import ImageFilter
filtered_image = Image.open(r"D:\图片\图片\455_CJ86GJI4_f2e94a9ef46286fdc96d4d7bd2c44dd9.jpg").filter(ImageFilter.CONTOUR)
filtered_image.show()
filtered_image.save(r"D:\图片\图片\455_CJ86GJI4_f2e94a9ef46286fdc96d4d7bd2c44dd9_轮廓.jpg"   )
#使用Pillow绘图
#region
import random
from PIL import Image, ImageDraw, ImageFont
def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue
#创建一个800*600的图像，背景为白色
width, height = 800, 600
image = Image.new(mode = 'RGB', size = (width, height), color = (255, 255, 255))
#创建一个ImageDraw对象,通过绘制从而改变image
drawer = ImageDraw.Draw(image)
#加载字体
font = ImageFont.truetype('KongXin.ttf', 32)
#绘制红色文字,test（）方法的第一个参数是文字位置坐标，第二个参数是文字内容，第三个参数是文字颜色，第四个参数是字体对象
drawer.text((300, 50), 'Python图像处理', fill = (255, 0, 0), font = font)
#绘制两条蓝色对角线,line()方法的第一个参数是线段的起点和终点坐标元组，第二个参数是线段颜色，第三个参数是线段宽度
drawer.line((0, 0, width, height), fill = (0, 0, 255), width = 2)   #左上到右下角
drawer.line((width, 0, 0, height), fill = (0, 0, 255), width = 2)   #右上到左下角
#绘制一个红色矩形框,rectangle()方法的第一个参数是矩形框的左上角和右下角坐标元组，第二个参数是矩形框颜色，第三个参数是矩形框线宽
xy = width // 2 - 60, height //2 - 60, width //2 + 60, height //2 + 60
drawer.rectangle(xy, outline = (255, 0, 0), width = 2)
#绘制四个彩色椭圆（用到循环输出）
for i in range(4):
    left, top, right, bottom = 150 + i * 120, 220, 310 + i * 120, 380
    drawer.ellipse((left, top, right, bottom), outline = random_color(), width = 8)
image.show()
image.save(r"D:\图片\图片\Python图像处理.jpg")
#endregion