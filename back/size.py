from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import RectangleObject

parts = []

def lolka(text, cm, tm, fontDict, fontSize):
    y = tm[5]
    parts.clear
    parts.append(text)

def index_containing_substring(the_list, substring):
    for i, s in enumerate(the_list):
        if substring in s:
              return i
    return -1

def text_of_num(text):
    num = []
    count =""


  
    for i in range(len(text)):
        if text[i]!='':
            text[i] = text[i].replace(text[i][0],'',1)
        
        if text[i].find("Забор груза от клиента")!= -1 or text[i].find("Возврат СД")!= -1 or text[i].find("Отправка СД")!= -1 or text[i].find("Разбор упаковки на адресе получателя")!= -1:
            text[i] = ' '


    
    for i in range(len(text)):
        if text[i]==' ':
            num.append(-1)
        else:
            for j in range(len(text[i])):
                if text[i][j] >= '0' and  text[i][j] <= '9':
                    while text[i][j] != ',':
                        count+=text[i][j]
                        j+=1
                    count+=text[i][j]
                    count+=text[i][j+1]
                    count+=text[i][j+2]
                    num.append(count)
                    count =""
                    break
    return num

            





def pars_size(file,size_square,offer,nameparsfile):#+drop return get_size_square
    reader = PdfReader(file)
    page = reader.pages[0]

    a = page.extract_text(visitor_text=lolka)
    text = a.split("\n")
    del text[0: int(index_containing_substring(text, '№ Услуга Сумма Количество Показатель Мест'))+1]; 
    del text[ int(index_containing_substring(text, 'Сдал Принял')):len(text)]; 
    
    
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
    print("высота ширина",width_square,height_square)
    page.mediabox =  RectangleObject((
    page.mediabox.left+int(x+2),
    page.mediabox.bottom +int(y+offer-int(text[len(text)-2][0])+4),
    page.mediabox.right -int( width - width_square - x + 12),
    page.mediabox.top-int(height-height_square-y+5),
    ))
    num_write = text_of_num(text)
    coord = seach_number(text)

    writer.add_page(page)
    with open(nameparsfile, "wb") as fp:
        writer.write(fp)
    print("координаты",coord)
    return coord, num_write
    

def seach_number(text):
    koordinats = []
    index = 0
    coord_x_y =[]
    x = ""
    y = ""
    a = text_of_num(text)
    with open("GeoBase_test.svg", encoding="utf8") as myFile:
        for num, line in enumerate(myFile, 1):
            for i in range(len(a)):
                if " " + a[i] in line:
                    index = line.find(a[i])-4
                    while line[index] != "\42":
                        y = line[index]+y
                        index -=1
                    
                    
                    while line[index-5] != "\42":
                        x = line[index-5]+x
                        index -=1
                    
                    #print(line,a[i])
                    coord_x_y.append([x,y])

                    x = ""
                    y = ""

        return coord_x_y
    
                


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


