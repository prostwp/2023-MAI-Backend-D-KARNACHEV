from datetime import datetime


def app(environ, start_response):
    data = f"{datetime.now()}".encode('utf-8')
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
