from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    url_path = self.path
    url_components = parse.urlsplit(url_path)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)

    if 'lang' in dic:
      url = "https://fourtonfish.com/hellosalut/"
      r = requests.get(url + dic['lang'])
      data = r.json

      for word_data in data:
        greeting = word_data
      message= str(greeting)

    else:
      message = "Please provide a valid language abbriviation"
    
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()

    self.wfile.write(message.encode())


