import socket
from _thread import *

HOST = '127.0.0.1'
PORT = 9999
master = -1

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

client_sockets = []

print(f'>> 서버가 시작되었습니다')

def threaded(clinet_socket, addr):
    # 닉네임 설정
    name = client_socket.recv(1024).decode()
    print(f'>> {name}님이 입장하셨습니다. ({addr[0]} : {addr[1]})')

    master = 0

    while True:
        try:
            if client_sockets[0] == client_socket:
                master = 1
                print(f'>> {name}님이 새로운 방장이 되셨습니다.')

            data = client_socket.recv(1024)

            if data.decode()[:3] == 'cmd' and master == 1:
                print(client_socket, data.decode(), data.decode()[4:])
               # client_sockets.remove(data.decode()[4:])
                client.send(data.decode()[4:].encode())

            if not data:
                print(f'>> {name}님이 나가셨습니다. ({addr[0]} : {addr[1]})')
                break

            print(f'{name} : {data.decode()} / ({addr[0]} : {addr[1]})')

            # 자신을 제외한 서버에 접속한 클라이언트에 메세지 전송
            for client in client_sockets:
                if client != client_socket:
                    client.send(data)

        except ConnectionError as e: # 나갔으면
            print(f'>> {name}님이 나가셨습니다. ({addr[0]} : {addr[1]})')
            break

    if client_socket in client_sockets:
        client_sockets.remove(client_socket)

    client_socket.close()

try:
    while True:

        client_socket, addr = server_socket.accept()
        client_sockets.append(client_socket)

        start_new_thread(threaded, (client_socket, addr))
        print(f'>> 참가자 수 : {len(client_sockets)}')
        print(client_sockets)

except Exception as e:
    print(f'>> Error : {e}')
finally:
    server_socket.close()