from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib
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
        # START **********************************************************************
        """ response for a GET request """
        self.send_response(200)
        
        html = ""
        if self.path == "/info":
            html = "Pagina de informacoes"
        else:
            html = "<html>"
            html += "<body>"
            html += "<h1>CPU Percent</h1>"
            html += "<p>" + str(psutil.cpu_percent()) + "</p>"
            html += "</body>"
            html += "</html>"
        
        #html = "{ \"cpu_consumption\": " + str(psutil.cpu_percent()) +  "}"
        self.wfile.write(bytes(html, "utf-8"))
        # END **********************************************************************


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    """ follows example shown on docs.python.org """
    server_address = (HOST_ADDRESS, HOST_PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    run(handler_class=RequestHandler)