# 단순 웹서버(GET, HEAD 처리) 구축

from http.server import SimpleHTTPRequestHandler, HTTPServer

handler = SimpleHTTPRequestHandler
serv = HTTPServer(('127.0.0.1', 7777), handler)  # 루프백, 포트번호
print('웹 서버 서비스 시작')
serv.serve_forever()  # 서버 활성화
