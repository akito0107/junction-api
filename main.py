#encoding:utf-8
import requests
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import json

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        uri = self.path
        ret = parse_qs(urlparse(uri).query, keep_blank_values = True)
        # b = json.dumps({'msg': 'ok'})
        print(ret['id'])
        i = int(ret['id'][0])
        b = json.dumps(search(i))
        body = bytes(b, 'utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-length', len(body))
        self.end_headers()
        self.wfile.write(body)

def search(item):
    get_resp = requests.get('https://junction-tokyo.minikura.com/v1/minikura/item',params=key)
    get_data = get_resp.json()
	#GETメソッド取得判定
    if get_data['status'] == '1' :
    	print("=取得成功===========")
    else:
        print("=取得失敗===========")
        return []

    l = []
    for n in range(0, 10):
        if get_data['results'][n]['common02'] and int(get_data['results'][n]['common02']) == item:
            print("CATEGORY:" + get_data['results'][n]['common01'])
            print("imageURL:" + get_data['results'][n]['common03'])
            l.append(get_data['results'][n])
    return l

host = 'localhost'
port = 8000	
httpd = HTTPServer((host, port), Handler)
print('serving at port', port) 
httpd.serve_forever()
