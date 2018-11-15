# -*- coding: utf-8 -*-
import socket
from datetime import datetime


def connection(time_client):
    udp_ip = 'localhost'
    udp_port = 9001
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(30)
    client_socket.sendto(bytes(time_client.encode()), (udp_ip, udp_port))
    
    try:
        time_server, server = client_socket.recvfrom(1024)
        print(f'Алгоритм Беркли: {time_server.decode()}')
    except socket.timeout:
        print('REQUEST TIMED OUT')
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    now = str(datetime.timestamp(datetime.now()))
    connection(now)
