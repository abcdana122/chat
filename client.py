import socket
from _thread import *

HOST = '127.0.0.1'
PORT = 9999

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# 서버에서 메세지 받기
def recv_data(client_socket):
    while True:
        data = client_socket.recv(1024)

        if data.decode() == client_socket:
            print(f'>> 당신 강퇴당하셨습니다.')
            client_socket.close()
            return

        print(f'{repr(data.decode())}')

start_new_thread(recv_data, (client_socket,))
print(f'>> 서버에 연결되었습니다')

# 닉네임 설정
name = input(f'>> 닉네임을 입력해주세요 : ')
client_socket.send(name.encode())

while True:
    message = input('')
    if message == 'Break':
        close_data = message
        break

    client_socket.send(message.encode())

client_socket.close()