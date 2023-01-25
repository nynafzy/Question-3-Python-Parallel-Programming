import socket

def main():
  
  sv_IP = "192.168.31.128"
  port = 8888
  
  clientsocket = socket.socket(socket.AF_INET), socket.SOCK_STREAM)
  clientsocket.connect((svIP,port))
  
  quote = clientsocket.recv(1024)
  print ("Quotes untuk kamu : %s" % quote.decode())
  
  clientsocket.close()
  
  main()
