import socket
import eel
from back.runner import get_txt



if __name__ == '__main__':
    
    #print(socket.gethostbyname(socket.gethostname()))
    eel.init('front')
    eel.start('index.html', mode="chrome", size=(760, 760))
    



