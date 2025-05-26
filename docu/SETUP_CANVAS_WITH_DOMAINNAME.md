# Setup Canvas with Domain

## Register a Domain


## create certificate

```
sudo apt install certbot

mkdir -p ~/certs
cd ~/certs

export DOMAIN=ihc-dt2.cluster-2.de
export LETSENCRYPT_EMAIL=xxx...@...yyy.zz
export TLS_SECRET_NAME=domain-tls-secret

sudo certbot certonly --manual --preferred-challenges=dns --email $LETSENCRYPT_EMAIL --agree-tos -d *.$DOMAIN

sudo cp /etc/letsencrypt/live/$DOMAIN/fullchain.pem ./fullchain.pem
sudo cp /etc/letsencrypt/live/$DOMAIN/privkey.pem ./privkey.pem
sudo chown $USER:users *.pem
kubectl delete secret  -n istio-ingress $TLS_SECRET_NAME --ignore-not-found=true
kubectl create secret -n istio-ingress tls $TLS_SECRET_NAME --key="privkey.pem" --cert="fullchain.pem"
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

helm upgrade --install canvas oda-canvas/canvas-oda -n canvas --create-namespace --set keycloak.service.type=ClusterIP --set api-operator-istio.deployment.hostName=*.$DOMAIN --set api-operator-istio.deployment.credentialName=$TLS_SECRET_NAME --set api-operator-istio.configmap.publicHostname=components.$DOMAIN --set=api-operator-istio.deployment.httpsRedirect=false --set=canvas-info-service.serverUrl=https://canvas-info.$DOMAIN
```


## deploy product catalog

```
helm repo add oda-components https://tmforum-oda.github.io/reference-example-components
helm repo update
helm upgrade --install pcat1 -n components --create-namespace oda-components/productcatalog 
```

```
kubectl get exposedapis -n components
```

add /docs to url displayed to get swagger-ui:

https://components.*****.cluster-2.de/pcat1-productcatalogmanagement/tmf-api/productCatalogManagement/v4/docs


## install virtual services for canvas

```
mkdir -p ~/git
cd ~/git
git clone https://github.com/ODA-CANVAS-FORK/oda-canvas-notes
helm upgrade --install -n canvas canvas-vs oda-canvas-notes/virtualservices/canvas --set=domain=$DOMAIN  --set=componentGateway=components/component-gateway
```


## install other virtual services

```
cd ~/git
helm upgrade --install -n default other-vs oda-canvas-notes/virtualservices/others --set=domain=$DOMAIN --set=componentGateway=components/component-gateway
```


# Cleanup

```
#helm uninstall -n components ...
helm uninstall -n canvas canvas-vs
helm uninstall -n default other-vs
helm uninstall -n canvas canvas
kubectl delete ns components canvas-vault cert-manager canvas
```

