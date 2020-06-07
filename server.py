# import socket
# server=socket.socket()
# server.bind(("127.0.0.1",8888))
# server.listen(5)
# print('等待请求。。。')
# conn,addr=server.accept()
# print("接收到来自{}的连接".format(addr[0]))
# data=conn.recv(1024)
# print(data.decode())
# conn.send(data.upper())
# conn.close()
# print("连接已断开")
# server.close()
# print('服务器已断开')

import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 8000
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((SERVER_IP, SERVER_PORT))
while True:
    message, address = server.recvfrom(1024)
    messager,content=message.decode().split('|')
    print('%s: %s'%(messager,content))
