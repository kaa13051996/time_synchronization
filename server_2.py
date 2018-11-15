# -*- coding: utf-8 -*-
import socket
from datetime import datetime


def algorithm_berkeley(datetime_list):
    avg_time = datetime.strftime(
        datetime.fromtimestamp(sum(datetime_list) / len(datetime_list)),
        "%H:%M:%S"
    )
    return avg_time


if __name__ == '__main__':
    udp_ip = 'localhost'
    udp_port = 9001
    max_client = 3
    count_client = 0
    datetimeList = []
    addressList = []

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((udp_ip, udp_port))

    while count_client < max_client:
        time_client, address = server_socket.recvfrom(1024)
        datetimeList.append(float(time_client))
        addressList.append(address)
        print(
            't клиента {}: {}'.format(
                count_client,
                datetime.strftime(
                    datetime.fromtimestamp(float(time_client)), "%H:%M:%S.%f")
            )
        )
        count_client += 1

    result = algorithm_berkeley(datetimeList)
    for x in addressList:
        server_socket.sendto(bytes(result.encode()), x)
    print(f'Среднее t: {result}.')
    server_socket.close()
