from http.server import HTTPServer, CGIHTTPRequestHandler
# импорт классов из модуля

# устанавливаем параметры сервера (локальный хост и порт 8080)
server_data = ('localhost', 8080)

# создаем экземпляр класса HTTPServer, используя данные сервера и CGIHTTPRequestHandler в качестве обработчика запросов
server = HTTPServer(server_data, CGIHTTPRequestHandler)

# запускаем сервер бесконечным циклом serve_forever()
server.serve_forever()
