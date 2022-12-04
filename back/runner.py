import eel
from PyPDF2 import PdfReader
import svgwrite
from back.interface import *
from back.size import get_size_square
from back.size import pars_size
from back.find_plat import start_find
import os

global dwg

@eel.expose
def get_txt(str_js):

    file_name = "bagage/GeoBase_test.svg"
    mass_str = str_js.split('\n')

    
    for i in range(len(mass_str)-1):
        mass_str_name= str(mass_str[i].replace("C:/in_pdf/", ''))
        mass_str_name= str(mass_str_name.replace(".pdf", ''))
        mass_str_name= str(mass_str_name.replace(" ", ''))
        extract(mass_str[i])
        size_square = get_size_square()
        pars_size(mass_str[i],size_square)
        start_find(mass_str[i],mass_str_name)
    mass_str = []
    os.remove(file_name)