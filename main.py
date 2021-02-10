import time
from http.server import HTTPServer
from server import Server

HOST_NAME = 'localhost'
PORT_NUMBER = 8000

def main():
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), Server)
    print(time.asctime(), 'Server UP - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        # Ctrl+C to close the server
        pass
    httpd.server_close()
    print("\n" + time.asctime(), 'Server DOWN - %s:%s' % (HOST_NAME, PORT_NUMBER))

if __name__ == '__main__':
    main()
