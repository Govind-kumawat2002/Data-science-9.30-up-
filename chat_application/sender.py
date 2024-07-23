import socket
harsh = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_add = "192.168.1.4"
port = 9999
pura_add= (ip_add,port)       # range 0 to 65536
message = input("Kya msg krega re BABA 🤔")
encript_msg =message.encode('ascii')
harsh.sendto(encript_msg,pura_add)


