# nginx sidecar for tls termination

http://eric-price.net/posts/2023-12-22-nginx-sidecar/

# read ca from secret and use in curl

```
kubectl get secret -n echoservice echoservice-tls -o jsonpath={'.data.ca\.crt'} | base64 -d > echo-ca.crt
```

```
curl https://echoservice-tls.echoservice.svc.cluster.local --cacert echo-ca.crt 
```



# access echoservice with https

```
$ # curl -k https://echoservice-tls.echoservice.svc.cluster.local/ip 
$ curl https://echoservice-tls.echoservice.svc.cluster.local/ip --cacert echo-ca.crt 

<h3 style="background-color: green;">log request ip infos</h3><b>client-ip:</b> 127.0.0.1<br><b>header:</b><br><pre><code>Host: echoservice-tls.echoservice.svc.cluster.local
X-Real-Ip: 10.92.1.34
X-Forwarded-For: 10.92.1.34
X-Forwarded-Host: echoservice-tls.echoservice.svc.cluster.local
Connection: upgrade
User-Agent: curl/7.88.1
Accept: */*

</code></pre><ul><li><a href='/'>ROOT</a><li><a href='/hello'>hello</a><li><a href='/ip'>ip</a></ul>
```

```
$ curl http://echoservice-tls.echoservice.svc.cluster.local/ip

<h3 style="background-color: green;">log request ip infos</h3><b>client-ip:</b> 10.92.1.34<br><b>header:</b><br><pre><code>Host: echoservice-tls.echoservice.svc.cluster.local
User-Agent: curl/7.88.1
Accept: */*

</code></pre><ul><li><a href='/'>ROOT</a><li><a href='/hello'>hello</a><li><a href='/ip'>ip</a></ul>
```

`X-Forwaded-For` exists for https


# trust manager

https://cert-manager.io/docs/trust/trust-manager/#preparing-for-production


```
helm upgrade trust-manager jetstack/trust-manager --install --namespace cert-manager --wait
```


```
kubectl get cm  distribute-cm-root-cas -o jsonpath={'.data.cm-root-cas\.pem'} > cm-root-cas.pem
```

```
kubectl get cm  distribute-cm-root-cas -o jsonpath={'.data.cm-root-cas\.pem'} > cm-root-cas.pem
```

```
curl https://echoservice-tls.echoservice.svc.cluster.local --cacert cm-root-cas.pem 
```

