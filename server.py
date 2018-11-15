# -*- coding: utf-8 -*-
import time
import socket
import datetime
import random

udp_ip = 'localhost'
udp_port = 9001

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((udp_ip, udp_port))


time_client, address = server_socket.recvfrom(1024)
time_server = str(datetime.datetime.now().time())

request_processing_time = random.randint(1, 5)
time.sleep(request_processing_time)

server_socket.sendto(bytes(time_server.encode()), address)
print('От клиента получено t: {} (когда: {}, t обработки запроса: {}).'.format(
    time_client.decode(), time_server, request_processing_time))
server_socket.close()
