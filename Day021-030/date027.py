#用python从pdf中提取文字
import PyPDF2
#创建读取器，阅读pdf
reader = PyPDF2.PdfReader('test.pdf')
#遍历每一页
for page in reader.pages:
    #提取并打印文本
    print(page.extract_text())
#旋转和叠加页面
#读取pdf文件
reader = PyPDF2.PdfReader('XGBoost.pdf')
#创建pdfWriter对象，用于将旋转页面加入
writer = PyPDF2.PdfWriter()
#遍历每一页
for no, page in enumerate(reader.pages):
    if no % 2 == 0:
        new_page = page.rotate(-90)
    else:
        new_page = page.rotate(90)
writer.add_page(new_page)
#写入临时文件,'wb'是二进制写入模式
with open('temp.pdf', 'wb') as file_obj:
    writer.write(file_obj)
#加密pdf文件
import PyPDF2
reader = PyPDF2.PdfReader('test.pdf')
writer = PyPDF2.PdfWriter()
for page in reader.pages:
    writer.add_page(page)
#写入密码，进行加密
writer.encrypt('foobared')
with open('output.pdf', 'wb') as file_obj:
    writer.write(file_obj)
#批量添加水印
reader1 = PyPDF2.PdfReader('test1.pdf')
reader2 = PyPDF2.PdfReader('test2.pdf')
writer = PyPDF2.PdfWriter()
watermark_page1 = reader2.pages[0]
watermark_page2 = reader2.pages[1]
for no, page in enumerate(reader1.pages):
    if no % 2 == 0:
        page.merge_page(watermark_page1)
    else:
        page.merge_page(watermark_page2)
    writer.add_page(page)
with open('output.pdf', 'wb') as file_obj:
    writer.write(file_obj)
#创建PDF文件
#导入A4纸尺寸常量
from reportlab.lib.pagesizes import A4
#提供字体度量管理，用于注册和查询字体
from reportlab.pdfbase import pdfmetrics
#导入TrueType字体
from reportlab.pdfbase.ttfonts import TTFont
#canvas提供绘画画布，用于生成pdf内容
from reportlab.pdfgen import canvas
#在某个路径下创建画布，设置页面尺寸为A4
pdf_canvas = canvas.Canvas('resources/demo.pdf', pagesize = A4)
width, height = A4
#插入图片
image = canvas.ImageReader('D:/图片/123.jpg')
#在某坐标处插入图片,height -395表示从顶部向下395的位置
pdf_canvas.drawImage(image, 20, height -395, 250, 375)
#注册字体
pdfmetrics.registerFont(TTFont('Font1', 'resources/fonts/Vera.ttf'))
pdfmetrics.registerFont(TTFont('Font2', 'resources/fonts/青瓜石头体.ttf'))
#绘制文字（中文）
pdf_canvas.setFont('Font2', 40)
#设置文字填充色，α=1完全不透明
pdf_canvas.setFillColorRGB(0.9, 0.5, 0.3, 1)
#width // 2 -120 水平居中，向左偏移120，height // 2 垂直居中
pdf_canvas.drawString(width // 2 - 120, height //2, '你好，世界！')
#绘制英文（旋转）
pdf_canvas.setFont('Font1', 40)
pdf_canvas.setFillColorRGB(0, 1, 0, 0.5)
pdf_canvas.rotate(18)
pdf_canvas.drawString(250, 250, 'hello, world!')
#保存pdf
pdf_canvas.save()
