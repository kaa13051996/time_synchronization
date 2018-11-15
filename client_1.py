# -*- coding: utf-8 -*-
import socket
from datetime import datetime, timedelta


def connection(time_client):
    udp_ip = 'localhost'
    udp_port = 9001
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(10)
    start = datetime.now()
    client_socket.sendto(bytes(str(time_client).encode()), (udp_ip, udp_port))
    try:
        time_server, server = client_socket.recvfrom(1024)
        end = datetime.now()
        elapsed = algorithm_cristian(end, start)
        print('Время сервера: {}\tАлгоритм Кристиана: {}'.format(time_server.decode(), elapsed.time()))
    except socket.timeout:
        print('REQUEST TIMED OUT')
    except Exception as ex:
        print(ex)


def algorithm_cristian(end, start):
    delta = (end - start).total_seconds()
    return end + timedelta(seconds=delta / 2)


if __name__ == '__main__':
    now = datetime.now().time()
    connection(now)
