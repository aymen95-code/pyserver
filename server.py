from http.server import BaseHTTPRequestHandler
from routes.main import routes

# Used to make sure that the HTML file we want to send to the client exist 
from pathlib import Path


class Server(BaseHTTPRequestHandler):
    # Methods to handle the responses
    def do_HEAD(self):
        return
    def do_POST(self):
        """ if typeof(req) == POST """
        return
    
    def do_GET(self):
        """ if typeof(req) == GET """
        self.respond()

    def handle_http(self) -> bytes:
        """ Send basic http handlers and then return the content """
        status:int = 200
        content_type:str = 'text/plain'
        res_content:str = ''
        
        if self.path in routes:
            print(routes[self.path])
            route_content:str = routes[self.path]['templates']
            file_path:str = Path(f"templates/{route_content}")
            if file_path.is_file():
                content_type = 'text/html'
                res_content = open(f"templates/{route_content}")
                res_content = res_content.read()
            else:
                status = 404
                res_content = '404 Not Found'
        else:
            status = 404
            res_content = '404 Not Found'

        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()
        return bytes(res_content, "UTF-8")

    def respond(self):
        """ Send the actual res out """
        content = self.handle_http()
        # send the content out as a res
        self.wfile.write(content)
