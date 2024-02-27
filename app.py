from http.server import BaseHTTPRequestHandler, HTTPServer

# 요청을 처리하는 클래스를 정의합니다.
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # GET 요청을 처리하는 메서드를 재정의합니다.
    def do_GET(self):
        # 응답 코드를 설정합니다.
        self.send_response(200)
        # 응답 헤더를 설정합니다.
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        # 응답 본문을 설정합니다.
        message = "여기에는 아무것도 없어! 마치 박주영부모 숫자처럼 0 이지 ㅋ"
        # 응답 본문을 보냅니다.
        self.wfile.write(message.encode('utf-8'))

# 서버를 설정하고 실행합니다.
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('웹 서버가 시작되었습니다.')
    httpd.serve_forever()

# 웹 서버를 실행합니다.
if __name__ == "__main__":
    run()
