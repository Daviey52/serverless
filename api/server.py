from http.server import BaseHTTPRequestHandler
#from urllib import parse
#import requests

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    #url_path = self.path
    #url_components = parse.urlsplit(url_path)
    #query_string_list = parse.parse_qsl(url_components.query)
    #dic = dict(query_string_list)

    #if 'lang' in dic:
      #url = "https://fourtonfish.com/hellosalut/?lang"
      #r = requests.get(url + dic['lang'])
      #message = str(r)
    #else:
      #message = "Please provide a valid language abbriviation"
    
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    message = 'Hello'

    self.wfile.write(message.encode())


