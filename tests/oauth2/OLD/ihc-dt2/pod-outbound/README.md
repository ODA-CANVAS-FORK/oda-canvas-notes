# POD Output interceptor

```
kubectl config set-context --current --namespace=echoservice
kubectl label namespace echoservice istio-injection=enabled
```

```
Host: echoservice.echoservice.svc.cluster.local
User-Agent: curl/8.11.0
Accept: */*
X-Forwarded-Proto: http
X-Request-Id: 7cbba0c0-b46e-494a-8e85-871d434bcb3c
X-Envoy-Attempt-Count: 1
X-Forwarded-Client-Cert: By=spiffe://cluster.local/ns/echoservice/sa/default;Hash=5cd155b4f9ac899f29d5195d672c3482110f2f80c0e05eb7d40d7fa9e6fe9cc4;Subject="";URI=spiffe://cluster.local/ns/echoservice/sa/default
```


```
kubectl exec -it curlpod-0 -- curl http://localhost:15000/config_dump > curlpod-config_dump.json
```