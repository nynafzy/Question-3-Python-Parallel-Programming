import socket
import threading
import random

quotes = [" Jangan tangisi karna kita telah berakhir, tersenyumlah kerna kita pernah terjadi." ," Kamu tidak akan mengerti karna kamu bukan aku.", " Dia hanya bercanda, seharusnya aku ketawa bukan jatuh cinta.", "Perasaan tulus adalah ketika tahu kelebihannya tapi tidak memanfaatkannya." , "Hubungan itu tentang 'saling' bukan tentang 'paling'."]

def quote (clientsocket):
    randm_quote = random.choice(quotes)
    clientsocket.sendall(randm_quote.encode())
    client.socket.close()
    
 def main():
 
     sIP = "192.168.31.128"
     port = 8888
     sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     sk.setsockopt(socket.SQL_SOCKET, socket.SO_REUSEADDR, 1)
     sk.bind ((sIP, port))
     sk.listen(5)
     
     while True:
       clientsocket,addr = sk.accept()
       print ("Got a connection from %s" % str(addr))
       th = threading.Thread(target=quote, args=(clientsocket, ))
       th.start()
       
    main()
