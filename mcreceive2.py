import socket as udp
import struct as udp_struct
import socket as mcast_udp
import struct as mcast_udp_struct


server_ip='225.0.0.1'
server_port=10000

sock = udp.socket(udp.AF_INET, udp.SOCK_DGRAM)
sock.setsockopt(udp.SOL_SOCKET, udp.SO_BROADCAST, 1)
mcast_sock = mcast_udp.socket(mcast_udp.AF_INET, mcast_udp.SOCK_DGRAM)
mcast_sock.setsockopt(mcast_udp.SOL_SOCKET, mcast_udp.SO_REUSEADDR, 1)
mcast_sock.bind(('', server_port))
mcast_udp_struct.pack("4sl", mcast_udp.inet_aton(server_ip), mcast_udp.INADDR_ANY)
mreq = mcast_udp_struct.pack("4sl", mcast_udp.inet_aton(server_ip), mcast_udp.INADDR_ANY)
mcast_sock.setsockopt(mcast_udp.IPPROTO_IP, mcast_udp.IP_ADD_MEMBERSHIP, mreq)

while 1:
  try:
    message_rx, addr = mcast_sock.recvfrom(1024)
    print(message_rx)
  except:
    pass

