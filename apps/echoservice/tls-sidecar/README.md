# nginx sidecar for tls termination

http://eric-price.net/posts/2023-12-22-nginx-sidecar/

# read ca from secret and use in curl

```
kubectl get secret -n echoservice echoservice-tls -o jsonpath={'.data.ca\.crt'} | base64 -d > echo-ca.crt
```

```
curl https://echoservice-tls.echoservice.svc.cluster.local --cacert echo-ca.crt 
```




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

