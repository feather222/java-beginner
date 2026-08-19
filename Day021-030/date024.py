#Python 读写Excel文件
#读Excel文件
import xlrd
wb = xlrd.open_workbook('阿里巴巴2020股票数据.xls')
sheetnames = wb.sheet_names()
print(sheetnames)
sheet = wb.sheet_by_name(sheetnames[0])
print(sheet.nrows,sheet.ncols)
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        value = sheet.cell(row,col).value
        if row > 0:
            if col == 0:
                value = xlrd.xldate_as_tuple(value,0)
                value = f'{{value[0]}年{value[1]}月{value[2]日}'
            else:
                value = f'{value:.2f}'
        print(value,end='\t')
    print()
last_cell_type = sheet.cell_type(sheet.nrows -1,sheet.ncols -1)
print(last_cell_type)
print(sheet.row_values(0))
print(sheet.row_slice(3,0,5))
#写excel文件
import random
import xlwt
student_names = ['one','two','three','four','five']
scores = [[random.randrange(60,101) for _ in range(3)]for _ in range(5)]
wb = xlwt.Workbook()
sheet = wb.add_sheet('一年级二班')
titles = ['name','语文','数学','英语']
for title,index in enumerate(titles):
    sheet.write(0,index,title)
for row in range(len(scores)):
    sheet.write(row+1,0,student_names[row])
    for col in range(len(scores[row])):
        sheet.write(row + 1,col+1,scores[row][col])
wb.save('考试成绩.xls')
#调整单元格格式
header_style = xlwt.XFStyle()
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = 5
header_style.pattern = pattern
titles = ('name','chinese','math','english')
for index,title in enumerate(titles):
    sheet.write(0,index,title,header_style)
    #指定字体
font = xlwt.Font()
font.name = '华文楷体'
font.height = 20*18
font.bold = True
font.italic = False
font.colour_index = 1
header_style.font = font
    #表头垂直居中对齐
align = xlwt.Alignment()
align.vert = xlwt.Alignment.VERT_CENTER
align.horz = xlwt.Alignment.HORZ_CENTER
header_style.alignment = align
    #加上黄色的虚线边框
borders = xlwt.Borders()
props = (
    ('top','top_color'),('right','right_colour'),
    ('bottom','bottom_colour'),('left','left_colour')
)
for position,colour in props:
    setattr(borders,position,xlwt.Borders.DASHED)
    setattr(borders,colour,5)
header_style.borders = borders
    #调整单元格宽度或者高度
sheet.row(0).set_style(xlwt.easyxy(f'font:height{20*40}'))  #行高设置为40px
titles = ('name','chinese','math','english')
for index,title in enumerate(titles):
    sheet.col(index).width = 20 * 200   #列宽设置为200px
    sheet.write(0,index,title,header_style)
#公式计算
import xlrd
import xlwt
from xlutils.copy import copy
wb_for_read = xlrd.open_workbook('阿里巴巴2020股票数据.xls')
sheet1 = wb_for_read.sheet_by_index(0)
nrows,ncols = sheet1.nrows,sheet1.ncols
wb_for_write = copy(wb_for_read)
sheet2 = wb_for_write.get_sheet(0)
sheet2.write(nrows,4,xlwt.Formula(f'average(E2:E{nrows})'))
sheet2.write(nrows,6,xlwt.Formula(f'sum(G2:G{nrows})'))
wb_for_write.save('阿里巴巴2020年股票数据.xls')
