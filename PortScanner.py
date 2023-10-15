import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("What host would you like to scan: ") #test case: google.com 
port = int(input("What port would you like to scan: ")) #port test case: 443 

def portScanner(port):
  if s.connect_ex((host, port)):
    print(f"The port {port} is closed")
  else:
    print(f"The port {port} is open")

print()
portScanner(port)
