from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import RectangleObject

def pars_size(file,size_square,offer,nameparsfile):#+drop return get_size_square
    reader = PdfReader(file)
    page = reader.pages[0]
    writer = PdfWriter()
    if size_square[1] > 400:
        width_square = (size_square[1]/2)-5
        x = size_square[2]+10
        y = size_square[3]+16
        height_square = size_square[0]-20
    else:
        width_square = size_square[1]
        x = size_square[2]
        y = size_square[3]
        height_square = size_square[0]
    
    
    width = int(float(page.mediaBox.getWidth()))#841 for 3.pdf
    height = int(float(page.mediaBox.getHeight()))#595 for 3.pdf
    #print(width,width_square,y)
    page.mediabox =  RectangleObject((
    page.mediabox.left+int(x),
    page.mediabox.bottom +int(y+offer),
    page.mediabox.right -int( width - width_square - x + 10),
    page.mediabox.top-int(height-height_square-y+5),
    ))
    writer.add_page(page)
    with open(nameparsfile, "wb") as fp:
        writer.write(fp)
    

def get_size_square():# 0 - height, 1 - width, 2 - x, 3 - y 
    height = 0
    width = 0
    lookup = '<rect'
    line_with_platelshik = 0
    count_platelshik=0
    line = ""                  
    with open("GeoBase_test.svg", encoding="utf8") as myFile:
        for num, line in enumerate(myFile, 1):
            if lookup  in line:
                #print(line)
                index = line.find("city")
                if line[index+25] != "\42":
                    #print(float(line[index+20]+line[index+21]+line[index+22]+line[index+23]+line[index+24]+line[index+25]))
                    height = float(line[index+20]+line[index+21]+line[index+22]+line[index+23]+line[index+24]+line[index+25])
                    if line[index+53]!= "\42":
                        #print(line[index+48] + line[index+49] + line[index+50] + line[index+51] + line[index+52] + line[index+53])
                        width = float(line[index+48] + line[index+49] + line[index+50] + line[index+51] + line[index+52] + line[index+53])
                    else:
                        #print(line[index+48] + line[index+49] + line[index+50] + line[index+51] + line[index+52])
                        width = float(line[index+48] + line[index+49] + line[index+50] + line[index+51] + line[index+52])
                else:
                   #print(float(line[index+20]+line[index+21]+line[index+22]+line[index+23]+line[index+24]))
                    height = float(line[index+20]+line[index+21]+line[index+22]+line[index+23]+line[index+24])
                    if line[index+52] != "\42":
                       # print(line[index+47] + line[index+48] + line[index+49] + line[index+50] + line[index+51] + line[index+52])
                        width = float(line[index+47] + line[index+48] + line[index+49] + line[index+50] + line[index+51] + line[index+52])
                    else:
                       # print(line[index+47] + line[index+48] + line[index+49] + line[index+50] + line[index+51])
                        width = float(line[index+47] + line[index+48] + line[index+49] + line[index+50] + line[index+51])
                indexx = line.find(" x=")
                if line[indexx+8]!="\42":
                    x = float(line[indexx+4]+line[indexx+5]+line[indexx+6]+line[indexx+7]+line[indexx+8])
                else:
                    x = float(line[indexx+4]+line[indexx+5]+line[indexx+6]+line[indexx+7])
                indexy = line.find(" y=")
                if line[indexy+8]!="\42":
                    y = float(line[indexy+4]+line[indexy+5]+line[indexy+6]+line[indexy+7]+line[indexy+8])
                else:
                    y = float(line[indexy+4]+line[indexy+5]+line[indexy+6]+line[indexy+7])
                return height, width, x, y


