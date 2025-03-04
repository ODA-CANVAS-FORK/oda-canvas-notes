# OAUTH2 Envoy Filter





```
kubectl apply -f envoy-oath2-secrets.yaml
kubectl apply -f istio-sidecar-injector-patched.yaml
kubectl rollout restart deployment -n components demo-b-prodcatapi
kubectl get pods -n components
```

```
NAME                                        READY   STATUS      RESTARTS   AGE
demo-a-metricsapi-557dc95b9c-smsk8          2/2     Running     0          4h35m
demo-a-mongodb-5c66f5cb8c-d84g5             2/2     Running     0          4h35m
demo-a-partyroleapi-8ddd9f54-rjln7          2/2     Running     0          4h35m
demo-a-prodcatapi-5988ff6d7-q8rr2           2/2     Running     0          4h35m
demo-a-productcataloginitialization-s9z2v   0/2     Completed   0          4h35m
demo-a-roleinitialization-52295             0/2     Completed   0          4h35m
demo-b-metricsapi-6948f74f47-7qtdq          2/2     Running     0          4h33m
demo-b-mongodb-6c466cf7d6-7vknh             2/2     Running     0          4h33m
demo-b-partyroleapi-6c7559f988-w6blg        2/2     Running     0          4h33m
demo-b-prodcatapi-6675466b75-jtqvk          2/2     Running     0          4m14s
demo-b-prodcatapi-754d564768-msp87          1/2     Running     0          3s
demo-b-productcataloginitialization-pkpm8   0/2     Completed   0          4h33m
demo-b-promgmtapi-b7676f669-sq5qs           2/2     Running     0          4h33m
demo-b-roleinitialization-hftcs             0/2     Completed   0          4h33m
```

```
kubectl exec -it -n components demo-b-prodcatapi-754d564768-msp87 -- /bin/bash
```


## test with curl

```
kubectl exec -n components demo-b-prodcatapi-76c69fbd6f-lwxsw -- curl -XPOST http://echoservice.echoservice.svc.cluster.local/echo
```



# deploy demo-b

```
helm install -n components demo-b feature-definition-and-test-kit/testData/productcatalog-dependendent-API-v1
```


## test injection

```
kubectl exec -n components demo-b-prodcatapi-7d8c788c77-v7b9h -- curl -XPOST http://echoservice.echoservice.svc.cluster.local/echo
```

```
{"echo_body":"","echo_header":{"Accept":"*/*","Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ0c2dUWVVVeFBSSkVSN3g0VHdHb1N5YzdISzNZWl9JWG13YXVrY2RkZkpzIn0.eyJleHAiOjE3NDExMDMxNDAsImlhdCI6MTc0MTEwMjg0MCwianRpIjoiMWI2N2ZiN2UtODllYi00Mzc4LWI0MjEtMmFmNTkxZWExNGVlIiwiaXNzIjoiaHR0cDovL2NhbnZhcy1rZXljbG9hay5jYW52YXMuc3ZjLmNsdXN0ZXIubG9jYWw6ODA4My9hdXRoL3JlYWxtcy9vZGFyaSIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiI3ZjM5ZmQ1NS03M2JkLTQwOWItOTUzMy01NDg4NmU1YmUxZDUiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJkZW1vLWItcHJvZHVjdGNhdGFsb2dtYW5hZ2VtZW50IiwiYWNyIjoiMSIsInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIiwiZGVmYXVsdC1yb2xlcy1vZGFyaSJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoiZW1haWwgcHJvZmlsZSIsImNsaWVudEhvc3QiOiIxMC45Mi4xLjIwMCIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiY2xpZW50SWQiOiJkZW1vLWItcHJvZHVjdGNhdGFsb2dtYW5hZ2VtZW50IiwicHJlZmVycmVkX3VzZXJuYW1lIjoic2VydmljZS1hY2NvdW50LWRlbW8tYi1wcm9kdWN0Y2F0YWxvZ21hbmFnZW1lbnQiLCJjbGllbnRBZGRyZXNzIjoiMTAuOTIuMS4yMDAifQ.l002demtO-mUfxF2NPzD69IbYw_vbm8vxBQnMYrmeaeJoIgR_FKieoZssf1y_djT3KaDm11qs9dOuoGi0EAy9DdNZ4OvhRhxvNZybtVi4xpeRQrY0LF4XkzlaMXaHwt-LRfyDHmAKpuTTJiBNh4kHEC2TG8OSd0GnvhKk4AGvYf8eqIMmXw2QZsgQYBdH6QKfN8tCTD1E7PydAX31Uz8MzHgqBSXNS6xE9IdbcXj870HJtQiVRjtJ7MNzcjPpxP_ROy6BUDt40AGi0HZb_hOjrSlpxnjy4xCZf-zoTbFRiaqijpUm9vAwBvLWtxR0fg5_eF499E835gqDTOHpH7BCg","Content-Length":"0","Host":"echoservice.echoservice.svc.cluster.local","User-Agent":"curl/7.64.0","X-Envoy-Attempt-Count":"1","X-Forwarded-Client-Cert":"By=spiffe://cluster.local/ns/echoservice/sa/default;Hash=5ea51c385e0b9cee2667ed5697f423c71fbcd255765380a9f221c38687a7317d;Subject=\"\";URI=spiffe://cluster.local/ns/components/sa/default","X-Forwarded-Proto":"http","X-Request-Id":"530a14c1-04ae-4a6f-8360-d703ae2ed79b"},"timestamp":"2025-03-04T15:41:52.721805"}
```

### negative test

demo-a has no envoy-filter

```
kubectl exec -n components demo-a-prodcatapi-5988ff6d7-q8rr2 -- curl -s -XPOST http://echoservice.echoservice.svc.cluster.local/echo
```

```
<!doctype html>
<html lang=en>
<title>401 Unauthorized</title>
<h1>Unauthorized</h1>
<p>error in x-gateway-token</p>
```

### https does not work

```
kubectl exec -n components demo-b-prodcatapi-7d8c788c77-v7b9h -- curl -s -XPOST https://echoservice.ihc-dt.cluster-1.de/echo
```

```
<!doctype html>
<html lang=en>
<title>401 Unauthorized</title>
<h1>Unauthorized</h1>
<p>error in x-gateway-token</p>
```

### echo service in internet

```
kubectl exec -it -n components demo-b-prodcatapi-7d8c788c77-v7b9h -- curl http://echo.free.beeceptor.com
```

```
{
  "method": "GET",
  "protocol": "http",
  "host": "echo.free.beeceptor.com",
  "path": "/",
  "ip": "34.141.177.253:47076",
  "headers": {
    "Host": "echo.free.beeceptor.com",
    "User-Agent": "curl/7.64.0",
    "Accept": "*/*",
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ0c2dUWVVVeFBSSkVSN3g0VHdHb1N5YzdISzNZWl9JWG13YXVrY2RkZkpzIn0.eyJleHAiOjE3NDExMDM4OTAsImlhdCI6MTc0MTEwMzU5MCwianRpIjoiYWZjYzczODMtNjQ5Zi00MjdiLWEyNDktZDU2MzRlOGMwZjk4IiwiaXNzIjoiaHR0cDovL2NhbnZhcy1rZXljbG9hay5jYW52YXMuc3ZjLmNsdXN0ZXIubG9jYWw6ODA4My9hdXRoL3JlYWxtcy9vZGFyaSIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiI3ZjM5ZmQ1NS03M2JkLTQwOWItOTUzMy01NDg4NmU1YmUxZDUiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJkZW1vLWItcHJvZHVjdGNhdGFsb2dtYW5hZ2VtZW50IiwiYWNyIjoiMSIsInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIiwiZGVmYXVsdC1yb2xlcy1vZGFyaSJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoiZW1haWwgcHJvZmlsZSIsImNsaWVudEhvc3QiOiIxMC45Mi4xLjIwMCIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiY2xpZW50SWQiOiJkZW1vLWItcHJvZHVjdGNhdGFsb2dtYW5hZ2VtZW50IiwicHJlZmVycmVkX3VzZXJuYW1lIjoic2VydmljZS1hY2NvdW50LWRlbW8tYi1wcm9kdWN0Y2F0YWxvZ21hbmFnZW1lbnQiLCJjbGllbnRBZGRyZXNzIjoiMTAuOTIuMS4yMDAifQ.h_TuYaT6VK5CCc3BFMgcK9Nd6zKOsbfoXs0Hzud5tyeQn_2mor126RbSAJZcpl_KpFs3HIhIR4Cn4EHIyxDQDG37MBaGa74lGGi0WAXpv5qdmamlhNMt2AftMHyqubJp-cUeUmR2rH3KJLQOdcVY_OMT7IAb4zmbkE351SlikF4Yr9cs9EXMaN-Jcc73nLijpgioRPvGBe4lIhQha8PZt4MCmDj5-3gjX_IZ5NgQG4V_kLophwyqTv81HYBjL994y8bVs1MNSGQarjJR4mMqDsQB_y8qG-uQLgD8X9jx3fj5XNz7NAXKadXZJYo0vGeyeehJUzMqkyVdQ0N6FtWEXA",
    "X-Envoy-Attempt-Count": "1",
    "X-Envoy-Peer-Metadata": "ChoKCkNMVVNURVJfSUQSDBoKS3ViZXJuZXRlcwrkAQoGTEFCRUxTEtkBKtYBCigKA2FwcBIhGh9kZW1vLWItcHJvZHVjdGNhdGFsb2dtYW5hZ2VtZW50CkQKH3NlcnZpY2UuaXN0aW8uaW8vY2Fub25pY2FsLW5hbWUSIRofZGVtby1iLXByb2R1Y3RjYXRhbG9nbWFuYWdlbWVudAo/CiNzZXJ2aWNlLmlzdGlvLmlvL2Nhbm9uaWNhbC1yZXZpc2lvbhIYGhZwcm9kdWN0Y2F0YWxvZ2FwaS0wLjIxCiMKB3ZlcnNpb24SGBoWcHJvZHVjdGNhdGFsb2dhcGktMC4yMQosCgROQU1FEiQaImRlbW8tYi1wcm9kY2F0YXBpLTdkOGM3ODhjNzctdjdiOWgKGQoJTkFNRVNQQUNFEgwaCmNvbXBvbmVudHMKWAoFT1dORVISTxpNa3ViZXJuZXRlczovL2FwaXMvYXBwcy92MS9uYW1lc3BhY2VzL2NvbXBvbmVudHMvZGVwbG95bWVudHMvZGVtby1iLXByb2RjYXRhcGkKJAoNV09SS0xPQURfTkFNRRITGhFkZW1vLWItcHJvZGNhdGFwaQ==",
    "X-Envoy-Peer-Metadata-Id": "sidecar~10.92.1.200~demo-b-prodcatapi-7d8c788c77-v7b9h.components~components.svc.cluster.local",
    "X-Request-Id": "eed114ea-f22e-42cd-bd95-49517d9c5ac7",
    "Accept-Encoding": "gzip"
  },
  "parsedQueryParams": {}
}
```

### echoservice log


```
kubectl logs -n echoservice deployment/echoservice-deployment -f
```

```
----------
Host: echoservice.echoservice.svc.cluster.local
User-Agent: curl/7.64.0
Accept: */*
X-Forwarded-Proto: http
X-Request-Id: 530a14c1-04ae-4a6f-8360-d703ae2ed79b
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ0c2dUWVVVeFBSSkVSN3g0VHdHb1N5YzdISzNZWl9JWG13YXVrY2RkZkpzIn0.eyJleHAiOjE3NDExMDMxNDAsImlhdCI6MTc0MTEwMjg0MCwianRpIjoiMWI2N2ZiN2UtODllYi00Mzc4LWI0MjEtMmFmNTkxZWExNGVlIiwiaXNzIjoiaHR0cDovL2NhbnZhcy1rZXljbG9hay5jYW52YXMuc3ZjLmNsdXN0ZXIubG9jYWw6ODA4My9hdXRoL3JlYWxtcy9vZGFyaSIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiI3ZjM5ZmQ1NS03M2JkLTQwOWItOTUzMy01NDg4NmU1YmUxZDUiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJkZW1vLWItcHJvZHVjdGNhdGFsb2dtYW5hZ2VtZW50IiwiYWNyIjoiMSIsInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIiwiZGVmYXVsdC1yb2xlcy1vZGFyaSJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoiZW1haWwgcHJvZmlsZSIsImNsaWVudEhvc3QiOiIxMC45Mi4xLjIwMCIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiY2xpZW50SWQiOiJkZW1vLWItcHJvZHVjdGNhdGFsb2dtYW5hZ2VtZW50IiwicHJlZmVycmVkX3VzZXJuYW1lIjoic2VydmljZS1hY2NvdW50LWRlbW8tYi1wcm9kdWN0Y2F0YWxvZ21hbmFnZW1lbnQiLCJjbGllbnRBZGRyZXNzIjoiMTAuOTIuMS4yMDAifQ.l002demtO-mUfxF2NPzD69IbYw_vbm8vxBQnMYrmeaeJoIgR_FKieoZssf1y_djT3KaDm11qs9dOuoGi0EAy9DdNZ4OvhRhxvNZybtVi4xpeRQrY0LF4XkzlaMXaHwt-LRfyDHmAKpuTTJiBNh4kHEC2TG8OSd0GnvhKk4AGvYf8eqIMmXw2QZsgQYBdH6QKfN8tCTD1E7PydAX31Uz8MzHgqBSXNS6xE9IdbcXj870HJtQiVRjtJ7MNzcjPpxP_ROy6BUDt40AGi0HZb_hOjrSlpxnjy4xCZf-zoTbFRiaqijpUm9vAwBvLWtxR0fg5_eF499E835gqDTOHpH7BCg
X-Envoy-Attempt-Count: 1
Content-Length: 0
X-Forwarded-Client-Cert: By=spiffe://cluster.local/ns/echoservice/sa/default;Hash=5ea51c385e0b9cee2667ed5697f423c71fbcd255765380a9f221c38687a7317d;Subject="";URI=spiffe://cluster.local/ns/components/sa/default
----------
ImmutableMultiDict([])
----------
Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ0c2dUWVVVeFBSSkVSN3g0VHdHb1N5YzdISzNZWl9JWG13YXVrY2RkZkpzIn0.eyJleHAiOjE3NDExMDMxNDAsImlhdCI6MTc0MTEwMjg0MCwianRpIjoiMWI2N2ZiN2UtODllYi00Mzc4LWI0MjEtMmFmNTkxZWExNGVlIiwiaXNzIjoiaHR0cDovL2NhbnZhcy1rZXljbG9hay5jYW52YXMuc3ZjLmNsdXN0ZXIubG9jYWw6ODA4My9hdXRoL3JlYWxtcy9vZGFyaSIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiI3ZjM5ZmQ1NS03M2JkLTQwOWItOTUzMy01NDg4NmU1YmUxZDUiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJkZW1vLWItcHJvZHVjdGNhdGFsb2dtYW5hZ2VtZW50IiwiYWNyIjoiMSIsInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIiwiZGVmYXVsdC1yb2xlcy1vZGFyaSJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoiZW1haWwgcHJvZmlsZSIsImNsaWVudEhvc3QiOiIxMC45Mi4xLjIwMCIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiY2xpZW50SWQiOiJkZW1vLWItcHJvZHVjdGNhdGFsb2dtYW5hZ2VtZW50IiwicHJlZmVycmVkX3VzZXJuYW1lIjoic2VydmljZS1hY2NvdW50LWRlbW8tYi1wcm9kdWN0Y2F0YWxvZ21hbmFnZW1lbnQiLCJjbGllbnRBZGRyZXNzIjoiMTAuOTIuMS4yMDAifQ.l002demtO-mUfxF2NPzD69IbYw_vbm8vxBQnMYrmeaeJoIgR_FKieoZssf1y_djT3KaDm11qs9dOuoGi0EAy9DdNZ4OvhRhxvNZybtVi4xpeRQrY0LF4XkzlaMXaHwt-LRfyDHmAKpuTTJiBNh4kHEC2TG8OSd0GnvhKk4AGvYf8eqIMmXw2QZsgQYBdH6QKfN8tCTD1E7PydAX31Uz8MzHgqBSXNS6xE9IdbcXj870HJtQiVRjtJ7MNzcjPpxP_ROy6BUDt40AGi0HZb_hOjrSlpxnjy4xCZf-zoTbFRiaqijpUm9vAwBvLWtxR0fg5_eF499E835gqDTOHpH7BCg
{
  "exp": 1741103140,
  "iat": 1741102840,
  "jti": "1b67fb7e-89eb-4378-b421-2af591ea14ee",
  "iss": "http://canvas-keycloak.canvas.svc.cluster.local:8083/auth/realms/odari",
  "aud": "account",
  "sub": "7f39fd55-73bd-409b-9533-54886e5be1d5",
  "typ": "Bearer",
  "azp": "demo-b-productcatalogmanagement",
  "acr": "1",
  "realm_access": {
    "roles": [
      "offline_access",
      "uma_authorization",
      "default-roles-odari"
    ]
  },
  "resource_access": {
    "account": {
      "roles": [
        "manage-account",
        "manage-account-links",
        "view-profile"
      ]
    }
  },
  "scope": "email profile",
  "clientHost": "10.92.1.200",
  "email_verified": false,
  "clientId": "demo-b-productcatalogmanagement",
  "preferred_username": "service-account-demo-b-productcatalogmanagement",
  "clientAddress": "10.92.1.200"
}
127.0.0.6 - - [04/Mar/2025 15:41:52] "POST /echo HTTP/1.1" 200 -
```


## https redirect

```
C:\Users\A307131\git\oda-canvas-notes\tests\oauth2>kubectl exec -it -n components demo-b-prodcatapi-7d8c788c77-v7b9h -- curl http://echo.free.beeceptor.com

{
  "method": "GET",
  "protocol": "http",
  "host": "echo.free.beeceptor.com",
  "path": "/",
  "ip": "34.141.177.253:54152",
  "headers": {
    "Host": "echo.free.beeceptor.com",
    "User-Agent": "curl/7.64.0",
    "Accept": "*/*",
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ0c2dUWVVVeFBSSkVSN3g0VHdHb1N5YzdISzNZWl9JWG13YXVrY2RkZkpzIn0.eyJleHAiOjE3NDExMDQ3OTAsImlhdCI6MTc0MTEwNDQ5MCwianRpIjoiN2Q0OTg5MGItY2YwZC00ZTJjLTlhNjQtZWYwNmE2Njc5YTYxIiwiaXNzIjoiaHR0cDovL2NhbnZhcy1rZXljbG9hay5jYW52YXMuc3ZjLmNsdXN0ZXIubG9jYWw6ODA4My9hdXRoL3JlYWxtcy9vZGFyaSIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiI3ZjM5ZmQ1NS03M2JkLTQwOWItOTUzMy01NDg4NmU1YmUxZDUiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJkZW1vLWItcHJvZHVjdGNhdGFsb2dtYW5hZ2VtZW50IiwiYWNyIjoiMSIsInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIiwiZGVmYXVsdC1yb2xlcy1vZGFyaSJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoiZW1haWwgcHJvZmlsZSIsImNsaWVudEhvc3QiOiIxMC45Mi4xLjIwMCIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiY2xpZW50SWQiOiJkZW1vLWItcHJvZHVjdGNhdGFsb2dtYW5hZ2VtZW50IiwicHJlZmVycmVkX3VzZXJuYW1lIjoic2VydmljZS1hY2NvdW50LWRlbW8tYi1wcm9kdWN0Y2F0YWxvZ21hbmFnZW1lbnQiLCJjbGllbnRBZGRyZXNzIjoiMTAuOTIuMS4yMDAifQ.DoDOZV6MSn6J0kj9LvJjMYj01PUgsDKwwI_zSDYKEiGpoc4vVs3IWZVRFwdklcI93O2rOyRYgK9fzF2csU82_8sgVXcB-UdxOzDUn7kCd-idMqV4cnqUgDEzkfNfeDC1oKPX9A7tuAvMuEtEypCtAFsI5qUjBvsmz7BsmINwmqUq-VRoEaIUj7tNGwiw9EzddmlgbbFr_nO1TcACkMRRiXOfg_KFq6WPCr1TdkDPZYlq32n8D2kwranTDzr1rk468I272-nYQPT597OPoHFYXiGrcN1zKc1BbG0u4rTNziU34wQjQst_VQ52nseMDMMUWz0sMNLmGmGZWx_K7moAUQ",
    "X-Envoy-Attempt-Count": "1",
    "X-Envoy-Peer-Metadata": "ChoKCkNMVVNURVJfSUQSDBoKS3ViZXJuZXRlcwrkAQoGTEFCRUxTEtkBKtYBCigKA2FwcBIhGh9kZW1vLWItcHJvZHVjdGNhdGFsb2dtYW5hZ2VtZW50CkQKH3NlcnZpY2UuaXN0aW8uaW8vY2Fub25pY2FsLW5hbWUSIRofZGVtby1iLXByb2R1Y3RjYXRhbG9nbWFuYWdlbWVudAo/CiNzZXJ2aWNlLmlzdGlvLmlvL2Nhbm9uaWNhbC1yZXZpc2lvbhIYGhZwcm9kdWN0Y2F0YWxvZ2FwaS0wLjIxCiMKB3ZlcnNpb24SGBoWcHJvZHVjdGNhdGFsb2dhcGktMC4yMQosCgROQU1FEiQaImRlbW8tYi1wcm9kY2F0YXBpLTdkOGM3ODhjNzctdjdiOWgKGQoJTkFNRVNQQUNFEgwaCmNvbXBvbmVudHMKWAoFT1dORVISTxpNa3ViZXJuZXRlczovL2FwaXMvYXBwcy92MS9uYW1lc3BhY2VzL2NvbXBvbmVudHMvZGVwbG95bWVudHMvZGVtby1iLXByb2RjYXRhcGkKJAoNV09SS0xPQURfTkFNRRITGhFkZW1vLWItcHJvZGNhdGFwaQ==",
    "X-Envoy-Peer-Metadata-Id": "sidecar~10.92.1.200~demo-b-prodcatapi-7d8c788c77-v7b9h.components~components.svc.cluster.local",
    "X-Request-Id": "8a71212a-7539-4d0b-a585-afa3115ad48d",
    "Accept-Encoding": "gzip"
  },
  "parsedQueryParams": {}
}
C:\Users\A307131\git\oda-canvas-notes\tests\oauth2>kubectl exec -it -n components demo-b-prodcatapi-7d8c788c77-v7b9h -- curl -XPOST http://echoservice.echoservice.svc.cluster.local/echo
upstream connect error or disconnect/reset before headers. retried and the latest reset reason: remote connection failure, transport failure reason: TLS_error:|268435703:SSL routines:OPENSSL_internal:WRONG_VERSION_NUMBER:TLS_error_end
C:\Users\A307131\git\oda-canvas-notes\tests\oauth2>kubectl apply echo-serviceentry.yaml
error: Unexpected args: [echo-serviceentry.yaml]
See 'kubectl apply -h' for help and examples

C:\Users\A307131\git\oda-canvas-notes\tests\oauth2>kubectl apply -f echo-serviceentry.yaml
serviceentry.networking.istio.io/add-https created
```

```
C:\Users\A307131\git\oda-canvas-notes\tests\oauth2>kubectl exec -it -n components demo-b-prodcatapi-7d8c788c77-v7b9h -- curl http://echo.free.beeceptor.com

{
  "method": "GET",
  "protocol": "https",
  "host": "echo.free.beeceptor.com",
  "path": "/",
  "ip": "34.141.177.253:51442",
  "headers": {
    "Host": "echo.free.beeceptor.com",
    "User-Agent": "curl/7.64.0",
    "Accept": "*/*",
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ0c2dUWVVVeFBSSkVSN3g0VHdHb1N5YzdISzNZWl9JWG13YXVrY2RkZkpzIn0.eyJleHAiOjE3NDExMDQ5NDAsImlhdCI6MTc0MTEwNDY0MCwianRpIjoiOGFjYTBkZWUtYWUyNy00YzY0LTkyYjQtOWJlM2E0Mzc4NDE3IiwiaXNzIjoiaHR0cDovL2NhbnZhcy1rZXljbG9hay5jYW52YXMuc3ZjLmNsdXN0ZXIubG9jYWw6ODA4My9hdXRoL3JlYWxtcy9vZGFyaSIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiI3ZjM5ZmQ1NS03M2JkLTQwOWItOTUzMy01NDg4NmU1YmUxZDUiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJkZW1vLWItcHJvZHVjdGNhdGFsb2dtYW5hZ2VtZW50IiwiYWNyIjoiMSIsInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIiwiZGVmYXVsdC1yb2xlcy1vZGFyaSJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoiZW1haWwgcHJvZmlsZSIsImNsaWVudEhvc3QiOiIxMC45Mi4xLjIwMCIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiY2xpZW50SWQiOiJkZW1vLWItcHJvZHVjdGNhdGFsb2dtYW5hZ2VtZW50IiwicHJlZmVycmVkX3VzZXJuYW1lIjoic2VydmljZS1hY2NvdW50LWRlbW8tYi1wcm9kdWN0Y2F0YWxvZ21hbmFnZW1lbnQiLCJjbGllbnRBZGRyZXNzIjoiMTAuOTIuMS4yMDAifQ.Jc3suAEWXaMZfIRC3HsA6jKE3rGi5Yk_vWE3BaLFXaa5YuNBmlfph-VoiX1cnmiRC4Tr6ojQbDWgEiVSbqc1PyGC0dt20u_tT6DITTiJ8785iEsdtwq1IodBR5klqKnGCqUr3DXTFSf4e84eCGYESI5DX3YK8grEVGP2vf6YDtJeSBxk-iY1CYZkUgC4MdkI0iUQE-ckmkapvk-xcHfEBGcIc2rLSoiFyIh8SrR83U15FIMotgUQ31du9Xq0CXM9cG23HNSdtf_BcLYpcVmNs-h3FLw5a6tVQchrOIRuxa01bPhmxxLJ85nn9RatsQveNKidL3PMvLpFM9Ts-2MGEQ",
    "X-Envoy-Attempt-Count": "1",
    "X-Envoy-Decorator-Operation": "echo.free.beeceptor.com:80/*",
    "X-Envoy-Peer-Metadata": "ChoKCkNMVVNURVJfSUQSDBoKS3ViZXJuZXRlcwrkAQoGTEFCRUxTEtkBKtYBCigKA2FwcBIhGh9kZW1vLWItcHJvZHVjdGNhdGFsb2dtYW5hZ2VtZW50CkQKH3NlcnZpY2UuaXN0aW8uaW8vY2Fub25pY2FsLW5hbWUSIRofZGVtby1iLXByb2R1Y3RjYXRhbG9nbWFuYWdlbWVudAo/CiNzZXJ2aWNlLmlzdGlvLmlvL2Nhbm9uaWNhbC1yZXZpc2lvbhIYGhZwcm9kdWN0Y2F0YWxvZ2FwaS0wLjIxCiMKB3ZlcnNpb24SGBoWcHJvZHVjdGNhdGFsb2dhcGktMC4yMQosCgROQU1FEiQaImRlbW8tYi1wcm9kY2F0YXBpLTdkOGM3ODhjNzctdjdiOWgKGQoJTkFNRVNQQUNFEgwaCmNvbXBvbmVudHMKWAoFT1dORVISTxpNa3ViZXJuZXRlczovL2FwaXMvYXBwcy92MS9uYW1lc3BhY2VzL2NvbXBvbmVudHMvZGVwbG95bWVudHMvZGVtby1iLXByb2RjYXRhcGkKJAoNV09SS0xPQURfTkFNRRITGhFkZW1vLWItcHJvZGNhdGFwaQ==",
    "X-Envoy-Peer-Metadata-Id": "sidecar~10.92.1.200~demo-b-prodcatapi-7d8c788c77-v7b9h.components~components.svc.cluster.local",
    "X-Request-Id": "df6eaa87-d8c6-4d12-8187-5caee6527e7a",
    "Accept-Encoding": "gzip"
  },
  "parsedQueryParams": {}
}
```

```
C:\Users\A307131\git\oda-canvas-notes\tests\oauth2>kubectl exec -it -n components demo-a-prodcatapi-5988ff6d7-q8rr2 -- curl http://echo.free.beeceptor.com

Client sent an HTTP request to an HTTPS server.
```

```
C:\Users\A307131\git\oda-canvas-notes\tests\oauth2>kubectl exec -it -n components demo-a-prodcatapi-5988ff6d7-q8rr2 -- curl https://echo.free.beeceptor.com

{
  "method": "GET",
  "protocol": "https",
  "host": "echo.free.beeceptor.com",
  "path": "/",
  "ip": "34.141.177.253:36470",
  "headers": {
    "Host": "echo.free.beeceptor.com",
    "User-Agent": "curl/7.64.0",
    "Accept": "*/*",
    "Accept-Encoding": "gzip"
  },
  "parsedQueryParams": {}
}
```


## uninstall

```
helm uninstall -n components demo-b 
```

# error analysis

## log istiod


```
kubectl logs -n istio-system deployment/istiod
```

```
2025-03-04T14:59:32.399396Z     info    delta   ADS: new delta connection for node:demo-a-prodcatapi-5988ff6d7-q8rr2.components-22
2025-03-04T14:59:32.400608Z     info    delta   CDS: PUSH request for node:demo-a-prodcatapi-5988ff6d7-q8rr2.components resources:69 removed:0 size:68.4kB cached:64/65 filtered:0
2025-03-04T14:59:32.401170Z     info    delta   EDS: PUSH request for node:demo-a-prodcatapi-5988ff6d7-q8rr2.components resources:48 removed:0 size:11.3kB empty:0 cached:47/48 filtered:0
2025-03-04T14:59:32.404255Z     info    delta   LDS: PUSH request for node:demo-a-prodcatapi-5988ff6d7-q8rr2.components resources:49 removed:0 size:96.6kB filtered:0
2025-03-04T14:59:32.405000Z     info    delta   RDS: PUSH request for node:demo-a-prodcatapi-5988ff6d7-q8rr2.components resources:23 removed:0 size:26.7kB cached:22/23 filtered:0
2025-03-04T14:59:32.434877Z     warn    delta   ADS:LDS: ACK ERROR demo-a-prodcatapi-5988ff6d7-q8rr2.components-22 Internal:Error adding/updating listener(s) 0.0.0.0_10259: paths must refer to an existing path in the system: '/envoy_secrets/oauth2secs/demo-a-productcatalogmanagement.yaml' does not exist
0.0.0.0_9100: paths must refer to an existing path in the system: '/envoy_secrets/oauth2secs/demo-a-productcatalogmanagement.yaml' does not exist
0.0.0.0_10255: paths must refer to an existing path in the system: '/envoy_secrets/oauth2secs/demo-a-productcatalogmanagement.yaml' does not exist
0.0.0.0_80: paths must refer to an existing path in the system: '/envoy_secrets/oauth2secs/demo-a-productcatalogmanagement.yaml' does not exist
0.0.0.0_15010: paths must refer to an existing path in the system: '/envoy_secrets/oauth2secs/demo-a-productcatalogmanagement.yaml' does not exist
0.0.0.0_9093: paths must refer to an existing path in the system: '/envoy_secrets/oauth2secs/demo-a-productcatalogmanagement.yaml' does not exist
34.118.239.83_8443: paths must refer to an existing path in the system: '/envoy_secrets/oauth2secs/demo-a-productcatalogmanagement.yaml' does not exist
34.118.239.83_443: paths must refer to an existing path in the system: '/envoy_secrets/oauth2secs/demo-a-productcatalogmanagement.yaml' does not exist
34.118.235.169_443: paths must refer to an existing path in the system: '/envoy_secrets/oauth2secs/demo-a-productcatalogmanagement.yaml' does not exist
0.0.0.0_10249: paths must refer to an existing path in the system: '/envoy_secrets/oauth2secs/demo-a-productcatalogmanagement.yaml' does not exist
0.0.0.0_8080: paths must refer to an existing path in the system: '/envoy_secrets/oauth2secs/demo-a-productcatalogmanagement.yaml' does not exist
0.0.0.0_8083: paths must refer to an existing path in the system: '/envoy_secrets/oauth2secs/demo-a-productcatalogmanagement.yaml' does not exist
34.118.233.239_80: paths must refer to an existing path in the system: '/envoy_secrets/oauth2secs/demo-a-productcatalogmanagement.yaml' does not exist
0.0.0.0_9153: paths must refer to an existing path in the system: '/envoy_secrets/oauth2secs/demo-a-productcatalogmanagement.yaml' does not exist
0.0.0.0_10257: paths must refer to an existing path in the system: '/envoy_secrets/oauth2secs/demo-a-productcatalogmanagement.yaml' does not exist
0.0.0.0_2381: paths must refer to an existing path in the system: '/envoy_secrets/oauth2secs/demo-a-productcatalogmanagement.yaml' does not exist
34.118.236.245_5000: paths must refer to an existing path in the system: '/envoy_secrets/oauth2secs/demo-a-productcatalogmanagement.yaml' does not exist
0.0.0.0_15014: paths must refer to an existing path in the system: '/envoy_secrets/oauth2secs/demo-a-productcatalogmanagement.yaml' does not exist
34.118.227.205_15021: paths must refer to an existing path in the system: '/envoy_secrets/oauth2secs/demo-a-productcatalogmanagement.yaml' does not exist
10.164.15.198_4194: paths must refer to an existing path in the system: '/envoy_secrets/oauth2secs/demo-a-productcatalogmanagement.yaml' does not exist
34.118.228.114_443: paths must refer to an existing path in the system: '/envoy_secrets/oauth2secs/demo-a-productcatalogmanagement.yaml' does not exist
0.0.0.0_9090: paths must refer to an existing path in the system: '/envoy_secrets/oauth2secs/demo-a-productcatalogmanagement.yaml' does not exist
0.0.0.0_4000: paths must refer to an existing path in the system: '/envoy_secrets/oauth2secs/demo-a-productcatalogmanagement.yaml' does not exist

2025-03-04T15:01:45.404272Z     info    delta   ADS: "10.92.1.125:45926" demo-b-prodcatapi-76c69fbd6f-lwxsw.components-12 terminated
2025-03-04T15:01:45.589392Z     info    delta   ADS: new delta connection for node:demo-b-prodcatapi-76c69fbd6f-lwxsw.components-23
2025-03-04T15:01:45.590569Z     info    delta   CDS: PUSH request for node:demo-b-prodcatapi-76c69fbd6f-lwxsw.components resources:69 removed:0 size:68.4kB cached:64/65 filtered:0
2025-03-04T15:01:45.591012Z     info    delta   EDS: PUSH request for node:demo-b-prodcatapi-76c69fbd6f-lwxsw.components resources:48 removed:0 size:11.3kB empty:0 cached:47/48 filtered:0
2025-03-04T15:01:45.592895Z     info    delta   LDS: PUSH request for node:demo-b-prodcatapi-76c69fbd6f-lwxsw.components resources:49 removed:0 size:83.0kB filtered:0
2025-03-04T15:01:45.593584Z     info    delta   RDS: PUSH request for node:demo-b-prodcatapi-76c69fbd6f-lwxsw.components resources:23 removed:0 size:26.7kB cached:22/23 filtered:0
```


## log sidecar

```
kubectl logs -n components demo-b-prodcatapi-7d8c788c77-v7b9h istio-proxy
```

```
...
2025-03-04T15:35:56.042168Z     error   envoy credential_injector external/envoy/source/extensions/http/injected_credentials/oauth2/token_provider.cc:111       onGetAccessTokenFailure: Failed to get access token      thread=12
2025-03-04T15:35:56.042254Z     error   envoy credential_injector external/envoy/source/extensions/http/injected_credentials/oauth2/oauth_client.cc:74  Oauth response code: 404        thread=12
2025-03-04T15:35:56.042263Z     error   envoy credential_injector external/envoy/source/extensions/http/injected_credentials/oauth2/oauth_client.cc:75  Oauth response body: {"error":"Realm does not exist"}   thread=12
2025-03-04T15:35:56.042266Z     error   envoy credential_injector external/envoy/source/extensions/http/injected_credentials/oauth2/token_provider.cc:111       onGetAccessTokenFailure: Failed to get access token      thread=12
2025-03-04T15:35:56.042356Z     error   envoy credential_injector external/envoy/source/extensions/http/injected_credentials/oauth2/oauth_client.cc:74  Oauth response code: 404        thread=12
2025-03-04T15:35:56.042370Z     error   envoy credential_injector external/envoy/source/extensions/http/injected_credentials/oauth2/oauth_client.cc:75  Oauth response body: {"error":"Realm does not exist"}   thread=12
2025-03-04T15:35:56.042372Z     error   envoy credential_injector external/envoy/source/extensions/http/injected_credentials/oauth2/token_provider.cc:111       onGetAccessTokenFailure: Failed to get access token      thread=12
```
