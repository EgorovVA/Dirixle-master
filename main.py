import socket
import eel




if __name__ == '__main__':
    
    print(socket.gethostbyname(socket.gethostname()))
    eel.init('front')
    eel.start('index.html', mode="chrome", size=(760, 760))
    



