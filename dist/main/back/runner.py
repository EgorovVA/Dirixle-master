import eel
from PyPDF2 import PdfReader
import svgwrite
from back.interface import *
from back.size import get_size_square
from back.size import pars_size
from back.find_plat import start_find
import os
import shutil
from os import path



global dwg


parts = []
def visitor_body(text, cm, tm, fontDict, fontSize):
    y = tm[5]
    parts.append(text)
def parsfile(file):
    reader = PdfReader(file)
    page = reader.pages[0]
    a = page.extract_text(visitor_text=visitor_body)
    text = a.split("\n")   
    for line in text:
        if line.find("ЗАЯВКА КЛИЕНТА")!= -1: 
            #print(line)        
            a = line.replace(" ",'')
            if a == "ЗАЯВКАКЛИЕНТА/ЭКСПЕДИТОРСКАЯРАСПИСКА" or a == "ЗАЯВКАКЛИЕНТА/ЭКСПЕДИТОРСКАЯРАСПИСКАЗАЯВКАКЛИЕНТА/ЭКСПЕДИТОРСКАЯРАСПИСКА":
                return 1
            else:
                return 0
        else:
            return 0



@eel.expose
def get_txt(str_js):

    
    mass_str = str_js.split('\n')

    
    for i in range(len(mass_str)-1):
        mass_str_name= str(mass_str[i].replace("C:/in_pdf/", ''))
        mass_str_name= str(mass_str_name.replace(".pdf", ''))
        mass_str_name= str(mass_str_name.replace(" ", ''))
        a = parsfile(mass_str[i])
        if a == 0:
            if path.exists("c:\out_error"):
                shutil.move(mass_str[i],'c:\out_error/'+ mass_str_name + '.pdf')
                continue
            else:
                os.mkdir("c:\out_error")
                #print("Создал папку")
                shutil.move(mass_str[i],'c:\out_error/'+ mass_str_name + '.pdf')
                continue
        else:
            extract(mass_str[i])
            size_square = get_size_square()
            pars_size(mass_str[i],size_square)
            start_find(mass_str[i],mass_str_name)
    mass_str = []
   
    #print("КОНЕЦ")




