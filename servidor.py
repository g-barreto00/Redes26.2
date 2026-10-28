from http.server import HTTPServer, SimpleHTTPRequestHandler

HOST = "0.0.0.0"
PORTA = 80

servidor = HTTPServer((HOST, PORTA), SimpleHTTPRequestHandler)

print(f"Servidor HTTP rodando na porta {PORTA}")

servidor.serve_forever()
