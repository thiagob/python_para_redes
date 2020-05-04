from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib
#import urlparse 
import psutil

HOST_ADDRESS = ""
HOST_PORT = 8000

class RequestHandler(BaseHTTPRequestHandler):
    """ Our custom, example request handler """
    
    def send_response(self, code, message=None):
        """ override to customize header """
        self.log_request(code)
        self.send_response_only(code)
        self.send_header('Server','python3 http.server Development Server')     
        self.send_header('Date', self.date_time_string())
        self.end_headers()  
    
    def do_GET(self):
        """ response for a GET request """
        parsed_path = self.path
        self.send_response(200)

        html = "<html><body><p>" + str(psutil.cpu_percent()) + "</p></body></html>"
        self.wfile.write(bytes(html, "utf-8"))
        
def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    """ follows example shown on docs.python.org """
    server_address = (HOST_ADDRESS, HOST_PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    run(handler_class=RequestHandler)