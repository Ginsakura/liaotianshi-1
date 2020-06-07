import socket

# client=socket.socket()
# client.connect(('127.0.0.1',8888))

# message='Across the Great Wall we can reach every corner in the world'

# client.send(message.encode())
# data=client.recv(1024)
# print(data.decode())
# client.close()
# print("服务已关闭")

SERVER_IP='192.168.3.15'
SERVER_PORT=80
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
nickname=input('请输入你的昵称：')
while True:
    message=input('>>:').strip()
    if not message:
        break
    message='%s|%s'%(nickname,message)
    client.sendto(message.encode(),(SERVER_IP,SERVER_PORT))
    
client.close()