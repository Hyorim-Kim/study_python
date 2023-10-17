# Network
# socket : 네트위크를 위한 통신 채널을 지원
import socket

print(socket.getservbyname('http', 'tcp'))  # 80 , 'http'의 기본 TCP 포트 번호를 출력
print(socket.getservbyname('https', 'tcp'))  # 443
print(socket.getservbyname('telnet', 'tcp'))  # 23, Telnet은 보안 문제로 인해 현재는 권장되지 않음
print(socket.getservbyname('ftp', 'tcp'))  # 파일 전송(eg. filezilla)
print(socket.getservbyname('smtp', 'tcp'))  # email 송수신
print(socket.getservbyname('pop3', 'tcp'))  # email 송수신

print(socket.getaddrinfo('www.naver.com', 80, proto=socket.SOL_TCP))
# 223.130.195.95           223.130.200.104
