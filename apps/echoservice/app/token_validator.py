import json
import requests

from werkzeug.exceptions import Unauthorized 

import jwt
from jwt import ExpiredSignatureError, InvalidSignatureError



class XGatewayTokenValidator:
    """
    see:
     * https://developer.telekom.de/docs/src/tardis_customer_handbook/StarGate/#last-mile-security-gateway-token 
     * https://auth0.com/blog/how-to-handle-jwt-in-python/#How-to-Verify-a-JWT
     * https://pyjwt.readthedocs.io/en/latest/usage.html
    # pip install pyjwt
    # pip install cryptography
    # pip install requests
    """ 
    def __init__(self, trusted_issuers:list = None, valid_azps:list = None, valid_request_paths:list = None, valid_auds:list = None):
        self.trusted_issuers = trusted_issuers
        self.valid_azps = valid_azps
        self.valid_request_paths = valid_request_paths
        self.valid_auds = valid_auds
        self.cached_pubkeys = {}
    def checkIssuer(self, issuer:str):
        if not self.trusted_issuers:
            return
        if not issuer in self.trusted_issuers:
            raise Unauthorized(description=f"issuer '{issuer}' is not allowed")
    def checkAzp(self, azp:str) -> bool:
        if not self.valid_azps:
            return
        if not azp in self.valid_azps:
            raise Unauthorized(description=f"azp '{azp}' is not allowed")
        return 
    def checkRequestPath(self, request_path:str) -> bool:
        if not self.valid_request_paths:
            return True
        if not request_path in self.valid_request_paths:
            raise Unauthorized(description=f"request_path '{request_path}' is not allowed")
    
    def getPublicKey(self, issuer_url:str):
        if issuer_url in self.cached_pubkeys:
            return self.cached_pubkeys[issuer_url]
        response = requests.get(issuer_url)
        # pubkey = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyJ1bopo5Ai/q48Z9+nXWDUMWb8F8uBsmw1ACygdIkxRgioMQxgbR/aHSxk+hiHFi51NBdSW7HVRb3QYDobPNza3dgKpu4SD6XbCAB7dqnYMlADH8GMLPN6Mwe3qYTzRFBSgnCk6odUX3J6SyqHb9vpJKG6BDEFMbBAZTwfxAGOCnKcG3v42Mk7/8O2PUJwHEEb51ystGMHDnFooE5YyNS/PLbpK+zkcroYcNYDgR8Pnkui2CtrYQGLfOGuY69IB1BuDCpDJ8ep9KftgsKaCMw/UoOas6nqKik/UeaoO/7qNreurDtmsHKLWQhCVhMjVWaUbWBTsSwErsLWp53t1jNwIDAQAB"
        pubkey = response.json()["public_key"];
        result = f"-----BEGIN RSA PUBLIC KEY-----\n{pubkey}\n-----END RSA PUBLIC KEY-----"
        self.cached_pubkeys[issuer_url] = result
        return result 

    def clearPublicKeyFromCache(self, issuer_url:str):
        if issuer_url in self.cached_pubkeys:
            self.cached_pubkeys.pop(issuer_url)

    def extractToken(self, xgt_token:str) -> str:
        if not xgt_token.startswith("Bearer "):
            raise Unauthorized(description=f"token does not start with 'Bearer ...'")
        result = xgt_token[7:]
        return result
        
    def validateXGT(self, xgt_token:str, use_publickey_from_cache = True):
        payload = "?"
        try:
            token = self.extractToken(xgt_token)
            # hdr = jwt.get_unverified_header(token)
            payload = jwt.decode(token, options={"verify_signature": False})
            print(json.dumps(payload, indent=2))
            self.checkIssuer(payload["iss"])
            self.checkAzp(payload["azp"])
            if self.valid_request_paths:
                self.checkRequestPath(payload["requestPath"])
            pubkey = self.getPublicKey(payload["iss"])
            
            try:
                chk = jwt.decode(token, key=pubkey, algorithms=['RS256', ], audience=self.valid_auds) # , options={"verify_signature": False})
                # chk is same as payload
                return chk
            except ExpiredSignatureError:
                raise Unauthorized(description=f"signature expired")
            except InvalidSignatureError:
                if use_publickey_from_cache:
                    self.clearPublicKeyFromCache(payload["iss"])
                    return self.validateXGT(xgt_token, use_publickey_from_cache = False)
                raise Unauthorized(description=f"signature could not be verified'")
        except Unauthorized as e:
            print(f"PAYLOAD: {payload}")
            print(f"XGT-ERROR: {str(e.description)}")
            raise e
        except Exception as e:
            print(f"PAYLOAD: {payload}")
            print(f"{type(e)}: {str(e)}")
            raise Unauthorized(description="error in x-gateway-token")
