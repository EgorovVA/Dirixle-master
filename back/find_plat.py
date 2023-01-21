from PyPDF2 import PdfReader
import os
import shutil
from os import path
from pdf2image import convert_from_path
import cv2
from PIL import Image
parts = []


def visitor_body(text, cm, tm, fontDict, fontSize):
    y = tm[5]
    parts.clear
    parts.append(text)


def search_plat(text):
    i = 0
    n = 0
    for num in text:
        if num.find('Плательщик') != -1:
            for plat in range(len(num.split(" "))):
                if num.split(" ")[plat].find('Плательщик') != -1:
                    n+=1
    for num in text:
        #print(num)
        

        if num.find('Плательщик') != -1:
            
            
            if n < 6:
                if(num.split(" ")[1] == 'V') :
                    #print(i+1)
                    return i+1
                else:
                    i+=1
            else:
                if num.split(" ")[0].find('Плательщик') != -1:
                    #print(num.split(" ")[0])
                    if (num.split(" ")[1] == 'V'):
                        return i+1
                    else:
                        if len(num.split(" ")[0])>10:
                            if num.split(" ")[0][10] == 'V':
                                return i+1
                            else:
                                i+=1

                        i+=1
                        
                #print(num.split(" "))        
        
            


def rename_file(text):
    i = 0
    for num in range(len(text)):
        
        
        if text[num].find('Комментарий') != -1:
            if text[num+1][0]=='№' or text[num+1].find('Комментарий') !=-1 or text[num+2].find('Комментарий') !=-1 or text[num+3].find('Комментарий') !=-1 or text[num+4].find('Комментарий') !=-1:
                a = text[num].replace('Комментарий','')
                #print(text[num])
                return(a.replace(' ',''))
            else:
                return ""

          

def start_find(file, name_file, coord, num_write):
    reader = PdfReader(file)
    page = reader.pages[0]
    a = page.extract_text(visitor_text=visitor_body)
    text = a.split("\n")
  
    number_plat = search_plat(text)
    file_name = name_file
    if rename_file(text) == "" or number_plat == 0 or 250<len(rename_file(text)):
        if path.exists("c:\out_error"):
            shutil.move("pars_size.pdf",'c:\out_error/'+ name_file+ '.pdf')
            return
        else:
            os.mkdir("c:\out_error")
            #print("Создал папку")
            shutil.move("pars_size.pdf",'c:\out_error/'+ name_file+ '.pdf')
            return
    if name_file.find("ЭР_") == -1:
        s = ""
        for line in text:
            if line.find("№") !=-1:
            #print(line)
                for i in range(1,len(line)):
                    s+=line[i]
                    if line[i] == " " or line[i] == "о":
                        break
                break 
        file_name = "ЭР_"+s
    new_mane = rename_file(text).replace('"','')
    kol_strok = int((float(coord[len(coord)-2][1])-float(coord[len(coord)-1][1]))/8.16)
    print(kol_strok)
    if number_plat == 1:
        nameoffer = (file_name+" "+new_mane  + "_" + '.pdf')
        name =  (file_name+" "+new_mane  + '.jpg')

        images = convert_from_path('pars_size.pdf', 500,poppler_path = r"poppler-22.12.0\Library\bin")
        for image in images:
            image.save(name)

        if path.exists("c:\out_pdf+"):
            shutil.move(name,'c:\out_pdf+/1.jpg')
            shutil.move("pars_size_offer.pdf",'c:\out_pdf+/'+nameoffer)
        else:
            os.mkdir("c:\out_pdf+")
            shutil.move(name,'c:\out_pdf+/1.jpg')
            shutil.move("pars_size_offer.pdf",'c:\out_pdf+/'+nameoffer)
            tmp = 'c:\out_pdf+/'+name
        img  = cv2.imread(r'c:\out_pdf+/1.jpg')   
        
        if img.shape[1]>2550:
            count = 2157
            for i in range(0,len(coord)):
                if num_write[i]!=-1:
                    num_write[i] = num_write[i].replace(',','.')
                    num_write[i] = num_write[i].replace(' ','')
                    tmpnum = float(num_write[i])
                    tmpnum*=1.4
                    
                    num_write[i] = str(round (tmpnum,2))
                    
                    num_write[i] = num_write[i].replace('.','_')

                    if len(num_write[i])-num_write[i].find('_')==2:
                        num_write[i]+='0'
                    if num_write[i].find('_')==-1:
                        num_write[i]+="_00"

                    if len(num_write[i]) > 6 and len(num_write[i])<9:
                        num_write[i] = num_write[i][:1] + "s" + num_write[i][1:]
                    else:
                        if len(num_write[i])>9:
                            num_write[i] = num_write[i][:1] + "s" + num_write[i][1:]
                            num_write[i] = num_write[i][:8] + "s" + num_write[i][8:]
                    
                    num_write[i] = 'p'.join(num_write[i][j:(j+1)] for j in range(len(num_write[i])))
                    print(num_write[i])
                   
                    im_h =  cv2.imread(r'C:/Number/'+num_write[i][0]+'.png')  
                    for j in range(1,len(num_write[i])):
                        if num_write[i][j] != 's':
                            num_img =  cv2.imread(r'C:/Number/p.png') 
                        num_img =  cv2.imread(r'C:/Number/'+num_write[i][j]+'.png')  
                        im_hq = im_h
                        im_h = cv2.hconcat([im_hq ,num_img ])
                    cv2.rectangle(img, (1605,count ), (1808,count +48), (255, 255, 255), -1)
                    cv2.imwrite('C:/out_pdf+/'+num_write[i]+'.jpg',im_h)
                    
                    cv2.imwrite('C:/out_pdf+/1.jpg', img)

                    im1 = Image.open('C:/out_pdf+/1.jpg')
                    im2 = Image.open('C:/out_pdf+/'+num_write[i]+'.jpg')
                            
                    im1.paste(im2, (1615, count+10 ))
                    im2.close()
                    os.remove('C:/out_pdf+/'+num_write[i]+'.jpg')

                    im1.save('C:/out_pdf+/1.jpg', quality=100)
                            
                    im1.close()
                    

                    img  = cv2.imread(r'c:\out_pdf+/1.jpg') 
                
                
                count+=56   

        else:#одинарные
            count = 2046
            for i in range(0,len(coord)):
                if num_write[i]!=-1:
                    num_write[i] = num_write[i].replace(',','.')
                    num_write[i] = num_write[i].replace(' ','')
                    tmpnum = float(num_write[i])
                    tmpnum*=1.4
                    
                    num_write[i] = str(round (tmpnum,2))
                    
                    num_write[i] = num_write[i].replace('.','_')
                    if len(num_write[i])-num_write[i].find('_')==2:
                        num_write[i]+='0'
                    if num_write[i].find('_')==-1:
                        num_write[i]+="_00"
                    if len(num_write[i]) > 6 and len(num_write[i])<9:
                        num_write[i] = num_write[i][:1] + "s" + num_write[i][1:]
                    else:
                        if len(num_write[i])>9:
                            num_write[i] = num_write[i][:1] + "s" + num_write[i][1:]
                            num_write[i] = num_write[i][:8] + "s" + num_write[i][8:]
                    im_h =  cv2.imread(r'C:/Number/'+num_write[i][0]+'.png')  
                    for j in range(1,len(num_write[i])):
                        num_img =  cv2.imread(r'C:/Number/'+num_write[i][j]+'.png')  
                        im_hq = im_h
                        im_h = cv2.hconcat([im_hq ,num_img ])
                    cv2.rectangle(img, (1520,count ), (1718,count  +48), (255, 255, 255), -1)
                    cv2.imwrite('C:/out_pdf+/'+num_write[i]+'.jpg',im_h)
                    cv2.imwrite('C:/out_pdf+/1.jpg', img)

                    im1 = Image.open('C:/out_pdf+/1.jpg')
                    im2 = Image.open('C:/out_pdf+/'+num_write[i]+'.jpg')
                            
                    im1.paste(im2, (1530, count+10 ))
                    im1.save('C:/out_pdf+/1.jpg', quality=100)
                    im2.close()
                    os.remove('C:/out_pdf+/'+num_write[i]+'.jpg')        
                    im1.close()
                    

                    img  = cv2.imread(r'c:\out_pdf+/1.jpg')   

                
                
                count+=56
        img  = cv2.imread(r'c:\out_pdf+/1.jpg')   
        im1 = Image.open('C:/out_pdf+/1.jpg')
        im1.save('C:/out_pdf+/'+name, quality=100)
        im1.close()
 
  
      

    if number_plat == 2 or number_plat == 3:

        name =  (file_name+" "+new_mane  + '.jpg')
        images = convert_from_path('pars_size.pdf', 500,poppler_path = r"poppler-22.12.0\Library\bin")
        for image in images:
            image.save(name)
        if path.exists("c:\out_png"):
            shutil.move(name,'c:\out_png/'+name)
        else:
            os.mkdir("c:\out_png")
            shutil.move(name,'c:\out_png/'+name)  
    
