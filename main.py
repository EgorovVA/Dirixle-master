import socket
import eel
import shutil
from back.runner import get_txt
from os import path



if __name__ == '__main__':


    #print(socket.gethostbyname(socket.gethostname()))
    eel.init('front')
    eel.start('index.html', mode="yandex", size=(760, 760))
    



