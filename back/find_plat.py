from PyPDF2 import PdfReader
import os
import shutil
from os import path
from pdf2image import convert_from_path

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

          

def start_find(file, name_file):
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
    if number_plat == 1:
        name =  (file_name+" "+new_mane  + '.pdf')
        nameoffer = (file_name+" "+new_mane  + "_" + '.pdf')
        if path.exists("c:\out_pdf+"):
            shutil.move("pars_size.pdf",'c:\out_pdf+/'+name)
            shutil.move("pars_size_offer.pdf",'c:\out_pdf+/'+nameoffer)
        else:
            os.mkdir("c:\out_pdf+")
            #print("Создал папку")
            shutil.move("pars_size.pdf",'c:\out_pdf+/'+name)
            shutil.move("pars_size_offer.pdf",'c:\out_pdf+/'+nameoffer)
            
    if number_plat == 2 or number_plat == 3:
        name =  (file_name+" "+new_mane  + '.jpg')
        images = convert_from_path('pars_size.pdf', 500,poppler_path = r"poppler-22.12.0\Library\bin")
        for image in images:
            image.save(name)
        if path.exists("c:\out_png"):
            shutil.move(name,'c:\out_png/'+name)
        else:
            os.mkdir("c:\out_png")
            #print("Создал папку")
            shutil.move(name,'c:\out_png/'+name)  
    
