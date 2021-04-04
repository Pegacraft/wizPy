from socket import *

# create UDP socket
sock = socket(AF_INET, SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
sock.settimeout(1)

server_address = ("255.255.255.255", 38899)
message: str = r'{"method":"registration","params":{"phoneMac":"AAAAAAAAAAAA","register":false,"phoneIp":"1.2.3.4",' \
               r'"id":"1"}} '
discovered: list = []


async def discover():
    sock.sendto(message.encode(), server_address)
    while True:

        # get response
        try:
            data, server = sock.recvfrom(4096)
            if """"success":true""" in data.decode() and not discovered.__contains__(str(server[0])):
                discovered.append(str(server[0]))
        except timeout:
            print("done discovering")
            break
    return discovered
