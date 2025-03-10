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

from werkzeug.exceptions import Unauthorized 


app = Flask(__name__)


XGT_TRUSTED_ISSUERS = os.getenv("XGT_TRUSTED_ISSUERS","https://canvas-keycloak.ihc-dt.cluster-3.de/auth/realms/odari https://canvas-keycloak.ihc-dt.cluster-1.de/auth/realms/odari http://canvas-keycloak.canvas.svc.cluster.local:8083/auth/realms/odari")
XGT_VALID_AZP_VALUES = os.getenv("XGT_VALID_AZP_VALUES", None) # "stargate")
XGT_VALID_REQUEST_PATHS = os.getenv("XGT_VALID_REQUEST_PATHS", None) # "/dtagtmf/oda-echoservice/v1/echo /dtagtmf/oda-compa/v1/echo /dtagtmf/oda-compb/v1/echo")
XGT_VALID_AUDS = os.getenv("XGT_VALID_AUDS", "account")

print(f'XGT_TRUSTED_ISSUERS: "{XGT_TRUSTED_ISSUERS}"') 
print(f'XGT_VALID_AZPS: "{XGT_VALID_AZP_VALUES}"') 
print(f'XGT_VALID_REQUEST_PATHS: "{XGT_VALID_REQUEST_PATHS}"')
print(f'XGT_VALID_AUDS: "{XGT_VALID_AUDS}"')
 
trusted_issuers = XGT_TRUSTED_ISSUERS.split(" ") if XGT_TRUSTED_ISSUERS else None
valid_azps = XGT_VALID_AZP_VALUES.split(" ") if XGT_VALID_AZP_VALUES else None
valid_request_paths = XGT_VALID_REQUEST_PATHS.split(" ") if XGT_VALID_REQUEST_PATHS else None
valid_auds = XGT_VALID_AUDS.split(" ") if XGT_VALID_AUDS else None

xgt_validator = XGatewayTokenValidator(trusted_issuers, valid_azps, valid_request_paths, valid_auds)


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
    echo_header = {}
    for h in request.headers:
        print(f"{h[0]}: {h[1]}")
        echo_header[h[0]] = h[1]
    print("----------")
    if request.is_json:
        print(request.json)
        echo_body = json.dumps(request.json)
    else:
        print(request.form)
        echo_body = request.data.decode()
    print("----------")
    xgt_token = request.headers.get("X-Gateway-Token")  # request.headers["x-gateway-token"] 
    if not xgt_token:
        xgt_token = request.headers.get("Authorization")    
    print(xgt_token)
    payload = xgt_validator.validateXGT(xgt_token) 
    #print(json.dumps(payload, indent=2))
    now = timestamp=datetime.datetime.now().isoformat('T')
    response = {
        "echo_header": echo_header,
        "echo_body": echo_body, 
        "timestamp": now
    }
    
    return jsonify(response)


def safe_get(default_value, dictionary, *paths):
    if dictionary is None:
        return default_value
    result = dictionary
    for path in paths:
        if path not in result:
            return default_value
        result = result[path]
    return result



@app.route("/jedionly", methods=["POST"])
def jedionly():
    print("----------")
    echo_header = {}
    for h in request.headers:
        print(f"{h[0]}: {h[1]}")
        echo_header[h[0]] = h[1]
    print("----------")
    if request.is_json:
        print(request.json)
        echo_body = json.dumps(request.json)
    else:
        print(request.form)
        echo_body = request.data.decode()
    print("----------")
    xgt_token = request.headers.get("X-Gateway-Token")  # request.headers["x-gateway-token"] 
    if not xgt_token:
        xgt_token = request.headers.get("Authorization")    
    print(xgt_token)
    payload = xgt_validator.validateXGT(xgt_token) 
    roles = safe_get(None, payload, "realm_access", "roles")
    print(f"ROLES: {roles}")
    if "jedi" not in roles:
        raise Unauthorized(description=f"you are not a jedi")

    
    #print(json.dumps(payload, indent=2))
    now = timestamp=datetime.datetime.now().isoformat('T')
    response = {
        "echo_header": echo_header,
        "echo_body": echo_body, 
        "roles": roles,
        "timestamp": now,
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
