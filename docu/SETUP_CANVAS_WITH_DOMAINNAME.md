# Setup Canvas with Domain

## Register a Domain


## create certificate

```
sudo apt install certbot

mkdir ~/certs
cd ~/certs

export DOMAIN=ihc-dt.cluster-2.de
export LETSENCRYPT_EMAIL=xxx...@...yyy.zz

sudo certbot certonly --manual --preferred-challenges=dns --email $LETSENCRYPT_EMAIL --agree-tos -d *.$DOMAIN

sudo cp /etc/letsencrypt/live/$DOMAIN/fullchain.pem ./fullchain.pem
sudo cp /etc/letsencrypt/live/$DOMAIN/privkey.pem ./privkey.pem
sudo chown $USER:users *.pem
kubectl create secret -n istio-ingress tls domain-tls-secret --key="privkey.pem" --cert="fullchain.pem"
```

output: 

```
  secret/domain-tls-secret created
```

## deploy canvas from public repo


```
helm repo add jetstack https://charts.jetstack.io
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo add istio https://istio-release.storage.googleapis.com/charts
helm repo add oda-canvas https://tmforum-oda.github.io/oda-canvas
helm repo update

helm upgrade --install canvas oda-canvas/canvas-oda -n canvas --create-namespace --set keycloak.service.type=ClusterIP --set api-operator-istio.deployment.hostName=*.$DOMAIN --set api-operator-istio.deployment.credentialName=domain-tls-secret --set api-operator-istio.configmap.publicHostname=components.$DOMAIN --set=api-operator-istio.deployment.httpsRedirect=false --set=dependentapi-simple-operator.serviceInventoryAPI.serverUrl=https://canvas-info.$DOMAIN
```


## install virtual services for canvas

```
helm upgrade --install -n canvas canvas-vs ../oda-canvas-notes/virtualservices/canvas --set=domain=$DOMAIN
```


## install other virtual services

```
helm upgrade --install -n default other-vs ../oda-canvas-notes/virtualservices/others --set=domain=$DOMAIN
```


