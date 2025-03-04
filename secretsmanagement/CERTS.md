# Wildcard certificate

```
sudo certbot certonly --manual --preferred-challenges=dns --email ferenc.hechler@gmail.com --agree-tos -d *.ihc-dt.cluster-1.de
mkdir WC-ihc-dt.cluster-1.de 
cd WC-ihc-dt.cluster-1.de
sudo cp /etc/letsencrypt/live/ihc-dt.cluster-1.de/fullchain.pem .
sudo cp  /etc/letsencrypt/live/ihc-dt.cluster-1.de/privkey.pem .
sudo chown ferenc:ferenc *
kubectl create secret -n istio-ingress tls wc-ihc-dt-cluster-1-de-tls  --key="privkey.pem" --cert="fullchain.pem" --dry-run=client -oyaml > WC-ihc-dt-cluster-1-de-tls-secrets.yaml
```

```
kubectl apply -f WC-ihc-dt-cluster-1-de-tls-secrets.yaml
```
