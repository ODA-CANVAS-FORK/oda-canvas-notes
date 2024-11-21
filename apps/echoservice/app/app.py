#import pydevd
#import debugpy

from flask import Flask, jsonify, request
import os         # for accesing environment variables
import socket     # for getting hostname
import datetime   # for current timestamp 
import json

import requests
from requests.auth import HTTPBasicAuth

from token_validator import XGatewayTokenValidator


app = Flask(__name__)


XGT_TRUSTED_ISSUERS = os.getenv("XGT_TRUSTED_ISSUERS","https://stargate-playground.live.dhei.telekom.de/auth/realms/default")
XGT_VALID_AZP_VALUES = os.getenv("XGT_VALID_AZP_VALUES", "stargate")
XGT_VALID_REQUEST_PATHS = os.getenv("XGT_VALID_REQUEST_PATHS", "/dtagtmf/oda-echoservice/v1/echo /dtagtmf/oda-compa/v1/echo /dtagtmf/oda-compb/v1/echo")

print(f'XGT_TRUSTED_ISSUERS: "XGT_TRUSTED_ISSUERS"') 
print(f'XGT_VALID_AZPS: "XGT_VALID_AZPS"') 
print(f'XGT_VALID_REQUEST_PATHS: "XGT_VALID_REQUEST_PATHS"')
 
trusted_issuers = XGT_TRUSTED_ISSUERS.split(" ")
valid_azps = XGT_VALID_AZP_VALUES.split(" ")
valid_request_paths = XGT_VALID_REQUEST_PATHS.split(" ")

xgt_validator = XGatewayTokenValidator(trusted_issuers, valid_azps, valid_request_paths)


STYLE = f" style=\"background-color: green;\""

LINKS = "<ul>" \
       "<li><a href='/'>ROOT</a>" \
       "<li><a href='/hello'>hello</a>" \
       "<li><a href='/ip'>ip</a>" \
       "</ul>"

@app.route("/")
def html_root():
    timestamp=datetime.datetime.now()
    hostname=socket.gethostname()
    html = f"<h3 style=\"background-color: green;\">Echo Service</h3>" \
           f"<p>Welcome to the Echo-Service</p>" \
           f"<b>Hostname:</b> {hostname}<br>" \
           f"&nbsp;&nbsp;&nbsp;&nbsp;<img src='static/img.png' width='128' height='128'><br>" \
           f"&nbsp;&nbsp;&nbsp;&nbsp;<a href='http://www.freepik.com'>Designed by rawpixel.com / Freepik</a><br><br>" \
           f"<b>Timestamp:</b> {timestamp}<br>"
    print('http request: [' + html + "]")
    return html + LINKS

@app.route("/hello")
def html_hello():
    return "<h3"+STYLE+">Hi!</h3>" + LINKS

@app.route("/ip")
def html_ip():
    header = str(request.headers)
    client_ip = request.remote_addr
    html = "<h3"+STYLE+">log request ip infos</h3>" \
           "<b>client-ip:</b> {client_ip}<br>" \
           "<b>header:</b><br>" \
           "<pre><code>{header}</code></pre>";
    result = html.format(client_ip=client_ip, 
                         header=header) 
    print('http request: [' + result + "]")
    return result + LINKS


@app.route("/img")
def html_img():
    return app.send_static_file('img.png')

@app.route("/echo", methods=["POST"])
def echo():
    print("----------")
    for h in request.headers:
        print(f"{h[0]}: {h[1]}")
    print("----------")
    
    xgt_token = request.headers.get("X-Gateway-Token")  # request.headers["x-gateway-token"] 
    if not xgt_token:
        xgt_token = request.headers.get("Authorization")    
    print(xgt_token)
    payload = xgt_validator.validateXGT(xgt_token) 
    print(json.dumps(payload, indent=2))
    request_json = request.json
    txt = request_json["text"]
    now = timestamp=datetime.datetime.now().isoformat('T')
    response = {
        "echo": txt, 
        "timestamp": now
    }
    
    return jsonify(response)



if __name__ == "__main__":
    print("STARTED")
    #debugpy.listen(("0.0.0.0", 5678))
    #print("Waiting for client to attach...")
    #debugpy.wait_for_client()
    #pydevd.settrace();
    host = os.getenv("WEBAPPIP", "0.0.0.0")
    port = os.getenv("WEBAPPPORT", "8080")
    print(f'STARTING {host} at port {port}') 
    
    #debugpy.breakpoint()
     
    app.run(host=host, port=port)
