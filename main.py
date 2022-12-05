import socket
import eel
import shutil
from back.runner import get_txt
from os import path



if __name__ == '__main__':
    if path.exists("c:\out_pdf"):
        shutil.rmtree("c://out_pdf+")
    if path.exists("c:\out_png"):
        shutil.rmtree("c://out_png")
    if path.exists("c:\out_error"):
        shutil.rmtree("c://out_error")

    #print(socket.gethostbyname(socket.gethostname()))
    eel.init('front')
    eel.start('index.html', mode="chrome", size=(760, 760))
    



