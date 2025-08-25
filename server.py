# ものぐさサーバースクリプト
# by 横茶横葉
# Thanks for https://goqr.me  !!!!!!
import socket
import http.server
import webbrowser

INTERNAL_IP=socket.gethostbyname(socket.gethostname())
PORT_SETTINGS=1111

Handler = http.server.SimpleHTTPRequestHandler
print("二次元コードを生成しています...")
webbrowser.open(f"https://api.qrserver.com/v1/create-qr-code/?data=http://{INTERNAL_IP}:{PORT_SETTINGS}")

with http.server.ThreadingHTTPServer((INTERNAL_IP, PORT_SETTINGS), Handler) as httpd:
    print(f"Serving at http://{INTERNAL_IP}:{PORT_SETTINGS}\n"+f"http://{INTERNAL_IP}:{PORT_SETTINGS} にてサーバーを開始しました")
    httpd.serve_forever()