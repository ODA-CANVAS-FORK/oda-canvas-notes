# https forwarding

```
root@demo-a-prodcatapi-75d6b7577f-n22t6:/src# curl http://echo.free.beeceptor.com
{
  "method": "GET",
  "protocol": "https",
  "host": "echo.free.beeceptor.com",
  "path": "/",
  "ip": "35.240.55.139:44352",
  "headers": {
    "Host": "echo.free.beeceptor.com",
    "User-Agent": "curl/7.64.0",
    "Accept": "*/*",
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ2VkRxRmRIX1dDSTRCYXNMZGhlZWRTNERlbjZXWGtwX25zcVZ6ZExsVUVFIn0.eyJleHAiOjE3MzI2NjAzODQsImlhdCI6MTczMjY2MDA4NCwianRpIjoiY2VmMDRkNmEtNTA5Yi00MGU0LTlmMzEtZGQ3YjM5ZDZlZmI4IiwiaXNzIjoiaHR0cDovL2NhbnZhcy1rZXljbG9hay5jYW52YXMuc3ZjLmNsdXN0ZXIubG9jYWw6ODA4My9hdXRoL3JlYWxtcy9teXJlYWxtIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6ImExOTZjNGYxLTkxYzUtNDk4YS04ZmRjLWU3OTJhMTdjMWExMSIsInR5cCI6IkJlYXJlciIsImF6cCI6ImRlbW8tYS1wcm9kdWN0Y2F0YWxvZ21hbmFnZW1lbnQiLCJhY3IiOiIxIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMtbXlyZWFsbSIsIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6InByb2ZpbGUgZW1haWwiLCJjbGllbnRIb3N0IjoiMTAuMTYuMC45OCIsImNsaWVudElkIjoiZGVtby1hLXByb2R1Y3RjYXRhbG9nbWFuYWdlbWVudCIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwicHJlZmVycmVkX3VzZXJuYW1lIjoic2VydmljZS1hY2NvdW50LWRlbW8tYS1wcm9kdWN0Y2F0YWxvZ21hbmFnZW1lbnQiLCJjbGllbnRBZGRyZXNzIjoiMTAuMTYuMC45OCJ9.RiJpS-rG_wOZvsOGoQz0xMS3jJ8murf-j7fEf3K8QlAjaCOxIvVUGyHTc9LisSVE0-8ZNDN6rb0psQIuzNC4bT7OfG9Lz-H_-GX_S5Go5_pOx2Z09vXtso1etmuNFcmuzkLTFpSWcEIbLNaBqJd9Hklysq23yjLnjKKAa6K5f5J-1FFPmtKLiJHntUN8z8dyQuigG4VAXx0ieRRXLUjyPwA9yhbzljGkzvQUl202lYL218iXYLlC4Rflms3oNYqx0AGwVrj7poRv3j-tmN4yTOC3OhoeN7ZxTv2MlQH1ddO1OEr8pC1HtsVvX3wnGDI_rBi0vcv91GQ_WQBfBoR18g",
    "X-Envoy-Attempt-Count": "1",
    "X-Envoy-Decorator-Operation": "echo.free.beeceptor.com:80/*",
    "X-Envoy-Peer-Metadata": "ChoKCkNMVVNURVJfSUQSDBoKS3ViZXJuZXRlcwrkAQoGTEFCRUxTEtkBKtYBCigKA2FwcBIhGh9kZW1vLWEtcHJvZHVjdGNhdGFsb2dtYW5hZ2VtZW50CkQKH3NlcnZpY2UuaXN0aW8uaW8vY2Fub25pY2FsLW5hbWUSIRofZGVtby1hLXByb2R1Y3RjYXRhbG9nbWFuYWdlbWVudAo/CiNzZXJ2aWNlLmlzdGlvLmlvL2Nhbm9uaWNhbC1yZXZpc2lvbhIYGhZwcm9kdWN0Y2F0YWxvZ2FwaS0wLjIzCiMKB3ZlcnNpb24SGBoWcHJvZHVjdGNhdGFsb2dhcGktMC4yMwosCgROQU1FEiQaImRlbW8tYS1wcm9kY2F0YXBpLTc1ZDZiNzU3N2YtbjIydDYKGQoJTkFNRVNQQUNFEgwaCmNvbXBvbmVudHMKWAoFT1dORVISTxpNa3ViZXJuZXRlczovL2FwaXMvYXBwcy92MS9uYW1lc3BhY2VzL2NvbXBvbmVudHMvZGVwbG95bWVudHMvZGVtby1hLXByb2RjYXRhcGkKJAoNV09SS0xPQURfTkFNRRITGhFkZW1vLWEtcHJvZGNhdGFwaQ==",
    "X-Envoy-Peer-Metadata-Id": "sidecar~10.16.0.98~demo-a-prodcatapi-75d6b7577f-n22t6.components~components.svc.cluster.local",
    "X-Request-Id": "6b5f5020-dab6-4dae-81b8-4f8d8e79951f",
    "Accept-Encoding": "gzip"
  },
  "parsedQueryParams": {}
}
```