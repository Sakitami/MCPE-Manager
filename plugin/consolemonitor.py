import mc
import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.connect(('localhost', 37412))   
def onConsoleOutput(e):
    e["output"]
    sock.send(e)
    print(e)
    print(sock.recv(1024))      
    sock.close()  
    return True

mc.setListener('控制台输出',onConsoleOutput)