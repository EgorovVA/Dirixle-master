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
            if text[num+1][0]=='№' or text[num+1].find('Комментарий') !=-1:
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
    if rename_file(text) == "" or number_plat == 0:
        if path.exists("c:\out_error"):
            shutil.move("pars_size.pdf",'c:\out_error/'+ name_file+ '.pdf')
            return
        else:
            os.mkdir("c:\out_error")
            #print("Создал папку")
            shutil.move("pars_size.pdf",'c:\out_error/'+ name_file+ '.pdf')
            return
        
    if number_plat == 1:
        name =  (name_file+"_"+rename_file(text) + '.pdf')
        if path.exists("c:\out_pdf+"):
            shutil.move("pars_size.pdf",'c:\out_pdf+/'+name)
        else:
            os.mkdir("c:\out_pdf+")
            #print("Создал папку")
            shutil.move("pars_size.pdf",'c:\out_pdf+/'+name)
            
    if number_plat == 2 or number_plat == 3:
        name =  (name_file+"_"+rename_file(text) + '.jpg')
        images = convert_from_path('pars_size.pdf', 500,poppler_path = r"poppler-22.12.0\Library\bin")
        for image in images:
            image.save(name)
        if path.exists("c:\out_png"):
            shutil.move(name,'c:\out_png/'+name)
        else:
            os.mkdir("c:\out_png")
            #print("Создал папку")
            shutil.move(name,'c:\out_png/'+name)  
    
