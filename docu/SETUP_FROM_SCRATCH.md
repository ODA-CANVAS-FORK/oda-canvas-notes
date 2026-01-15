# Setup ihc-dt from scratch

## Deploy istio

as described in the installation instructions:
https://github.com/tmforum-oda/oda-canvas/tree/main/installation#3-istio

```
helm repo add istio https://istio-release.storage.googleapis.com/charts
helm repo update
helm install istio-base istio/base -n istio-system  --create-namespace
helm install istiod istio/istiod -n istio-system --wait
kubectl create namespace istio-ingress
kubectl label namespace istio-ingress istio-injection=enabled
helm install istio-ingress istio/gateway -n istio-ingress --set labels.app=istio-ingress --set labels.istio=ingressgateway --wait
```

### activate envoy access logging

see https://istio.io/latest/docs/reference/config/istio.mesh.v1alpha1/#MeshConfig

```
helm upgrade --install istiod istio/istiod -n istio-system --set meshConfig.accessLogFile=dev/stdout --wait
```

## configure DNS wildcard entry

get external ip of ingress gateway

```
kubectl get svc -n istio-ingress
```

configure dns record:

|    Resource record    |  TTL  | Type | Priority |     Data     |
| --------------------- | ----- | ---- | -------- | ------------ |
| *.ihc-dt.cluster-3.de | 86400 |   A  |     0    | 35.195.3.247 |


## install Canvas

### define repos

```
helm repo add jetstack https://charts.jetstack.io
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo add hashicorp https://helm.releases.hashicorp.com
helm repo update
```

## deploy server certificate

### Create LetsEncrypt wildcard certificate

use certbot to create a dns wildcard cert for 3 months:
(can be automated with lego)

```
cd ~/git/oda-canvas-notes

sudo apt install certbot
sudo certbot certonly --manual --preferred-challenges=dns --email *******@*******.** --agree-tos -d *.ihc-dt.cluster-3.de
sudo cp /etc/letsencrypt/live/k8s.cluster-1.de/fullchain.pem encrypted/certs/WC-ihc-dt-cluster-3-de/fullchain.pem
sudo cp /etc/letsencrypt/live/k8s.cluster-1.de/privkey.pem encrypted/certs/WC-ihc-dt-cluster-3-de/privkey.pem
sudo chown $(whoami) encrypted/certs/WC-ihc-dt-cluster-3-de/*.pem
```

create k8s secret from PEM keys

```
kubectl create secret -n istio-ingress tls wc-ihc-dt-cluster-3-de-tls --key="encrypted/certs/WC-ihc-dt-cluster-3-de/privkey.pem" --cert="encrypted/certs/WC-ihc-dt-cluster-3-de/fullchain.pem" --dry-run=client -oyaml > encrypted/certs/WC-ihc-dt-cluster-3-de/WC-ihc-dt-cluster-3-de-tls-secret.yaml
```

deploy k8s secret

```
kubectl apply -f encrypted/certs/WC-ihc-dt-cluster-3-de/WC-ihc-dt-cluster-3-de-tls-secret.yaml
```


## deploy canvas from local filesystem 

```
cd ~/git/oda-canvas

helm repo update

#initial call without --skip-refresh

helm dependency update ./charts/cert-manager-init
helm dependency update ./charts/kong-gateway
helm dependency update ./charts/apisix-gateway
helm dependency update ./charts/canvas-vault
helm dependency update ./charts/pdb-management-operator
helm dependency update ./charts/canvas-oda

helm dependency update --skip-refresh ./charts/cert-manager-init
helm dependency update --skip-refresh ./charts/kong-gateway
helm dependency update --skip-refresh ./charts/apisix-gateway
helm dependency update --skip-refresh ./charts/canvas-vault
helm dependency update --skip-refresh ./charts/pdb-management-operator
helm dependency update --skip-refresh ./charts/canvas-oda

helm upgrade --install canvas charts/canvas-oda -n canvas --create-namespace --set keycloak.service.type=ClusterIP --set api-operator-istio.deployment.hostName=*.ihc-dt.cluster-3.de --set api-operator-istio.deployment.credentialName=wc-ihc-dt-cluster-3-de-tls --set api-operator-istio.configmap.publicHostname=components.ihc-dt.cluster-3.de

```

Bitnami issues

```
helm upgrade --install canvas charts/canvas-oda -n canvas --create-namespace --set keycloak.service.type=ClusterIP --set api-operator-istio.deployment.hostName=*.ihc-dt.cluster-3.de --set api-operator-istio.deployment.credentialName=wc-ihc-dt-cluster-3-de-tls --set api-operator-istio.configmap.publicHostname=components.ihc-dt.cluster-3.de --set keycloakConfigCli.image.repository=docker.io/bitnamilegacy/keycloak-config-cli
```

# add optional deployments


## install Grafana

```
cd ~/git/oda-canvas-notes

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm upgrade --install kube-prometheus-stack --namespace grafana --create-namespace prometheus-community/kube-prometheus-stack

kubectl apply -f apps/grafana/virtual-service/grafana-vs.yaml
```

open Grafana in browser:

https://grafana.ihc-dt.cluster-3.de
(use admin/prom-operator)


## install code-server

```
cd ~/git/oda-canvas-notes

cd apps/code-server

export CODE_SERVER_PASSWORD=***********

kubectl create ns code-server || true
kubectl create secret generic -n code-server code-server-secret --from-literal=password="$CODE_SERVER_PASSWORD" --dry-run=client -oyaml | kubectl apply -f - 

git clone https://github.com/coder/code-server code-server-repo
cd code-server-repo
helm upgrade --install -n code-server --create-namespace code-server --set existingSecret=code-server-secret ci/helm-chart \
    --set image.repository=ocfork/code-server \
    --set image.tag=v4.95.3-with-helm-and-node
cd ..

kubectl create clusterrolebinding code-server-cluster-admin-rb --clusterrole=cluster-admin --serviceaccount=code-server:code-server --dry-run=client -oyaml | kubectl apply -f -

kubectl apply -f virtualservice/code-server-vs.yaml
```

test in browser

https://code-server.ihc-dt.cluster-3.de
(password as defined above)


## install EchoService with istio sidecar

```
kubectl create ns echoservice || true
kubectl label ns echoservice istio-injection=enabled

kubectl apply -f apps/echoservice/k8s
```

test im browser:
https://echoservice.ihc-dt.cluster-3.de/ip


## install KeyCloak route

```
kubectl apply -f apps/canvas-keycloak/canvas-keycloak-vs.yaml
```

test in browser
https://canvas-keycloak.ihc-dt.cluster-3.de/auth/
(use admin/adpass)


## install Canvas-Infoservice route

```
kubectl apply -f apps/canvas-info/canvas-info-vs.yaml
```

test in browser
https://canvas-info.ihc-dt.cluster-3.de/api-docs/

## install HashiCorp Vault route

```
kubectl apply -f apps/canvas-vault/canvas-vault-hc-vs.yaml
kubectl apply -f apps/canvas-vault/canvas-vault-landing-page-vs.yaml
```

test in browser:
https://canvas-vault-hc.ihc-dt.cluster-3.de
(use root token in landing-page to login)



# Egress gateway

https://artifacthub.io/packages/helm/istio-official/gateway#egress-gateway

```
kubectl create namespace istio-egress
kubectl label namespace istio-egress istio-injection=enabled
helm install istio-egress istio/gateway -n istio-egress --set labels.app=istio-egress --set labels.istio=egressgateway --set service.type=ClusterIP --wait
```
