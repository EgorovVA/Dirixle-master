from PyPDF2 import PdfReader
import os
import shutil
from os import path

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
    for num in text:
        
        if num.find('Комментарий') != -1:
            if len(num.split(" "))>1:
                return num.split(" ")[1]
            else:
               return ""

   #             return text[num+2].replace(' ','')

def opredeleniye_nomera(number,name,oldname):
    old_name = oldname
    print(name, number)
    if number == 1:
        if path.exists("c:\out_pdf+"):
            shutil.move(old_name,'c:\out_pdf+/'+name)
        else:
            os.mkdir("c:\out_pdf+")
            print("Создал папку")
            shutil.move(old_name,'c:\out_pdf+/'+name)
            
    if number == 2:
        if path.exists("c:\out_png"):
            shutil.move(old_name,'c:\out_png/'+name)
        else:
            os.mkdir("c:\out_png")
            print("Создал папку")
            shutil.move(old_name,'c:\out_png/'+name)  
     
    #if number == 3 and path.exists("out_png"):
    #    shutil.move(old_name,'out_png/'+name)
#
 #   if name == "Error.pdf":
#        if path.exists("c:\error_png"):
  #          shutil.move(old_name,'c:\error_png/'+name)
   #     else:
    #        os.mkdir("c:\error_png")
     #       print("Создал папку")
      #      shutil.move(old_name,'c:\error_png/'+name
        

def start_find(file, name_file):
    reader = PdfReader(file)
    page = reader.pages[0]
    a = page.extract_text(visitor_text=visitor_body)
    text = a.split("\n")
   # print(search_plat())
    number_plat = search_plat(text)
    
    name =  (name_file+"_"+rename_file(text) + '.pdf')
    
    #os.rename('pars_size.pdf',name)
    opredeleniye_nomera(number_plat,name,"bagage/pars_size.pdf")
    
    
