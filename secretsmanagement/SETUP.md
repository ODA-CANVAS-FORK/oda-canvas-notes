# Build


# Install

## define repos

```
helm repo add jetstack https://charts.jetstack.io
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo add hashicorp https://helm.releases.hashicorp.com
helm repo update
```

## deploy canvas from local filesystem 

```
cd ~/git/oda-canvas

helm repo update

helm dependency update ./charts/cert-manager-init
helm dependency update ./charts/kong-gateway
helm dependency update ./charts/apisix-gateway
helm dependency update ./charts/canvas-vault
helm dependency update ./charts/canvas-oda

helm dependency update --skip-refresh ./charts/cert-manager-init
helm dependency update --skip-refresh ./charts/kong-gateway
helm dependency update --skip-refresh ./charts/apisix-gateway
helm dependency update --skip-refresh ./charts/canvas-vault
helm dependency update --skip-refresh ./charts/canvas-oda

helm upgrade --install canvas charts/canvas-oda -n canvas --create-namespace --set keycloak.service.type=ClusterIP --set api-operator-istio.deployment.hostName=*.ihc-dt.cluster-3.de --set api-operator-istio.deployment.credentialName=wc-ihc-dt-cluster-3-de-tls --set api-operator-istio.configmap.publicHostname=components.ihc-dt.cluster-3.de --set=api-operator-istio.deployment.httpsRedirect=false --set=dependentapi-simple-operator.serviceInventoryAPI.serverUrl=https://canvas-info.ihc-dt.cluster-3.de
```



# [opt] change public url for info service

```
kubectl set env deployment/canvas-info-service -n canvas SERVER_URL=https://canvas-info.ihc-dt.cluster-3.de
```

# install virtual-services

```
kubectl apply -f ../oda-canvas-notes/secretsmanagement/virtualservices
```

for ihc-dt2:

```
kubectl apply -f ../oda-canvas-notes/secretsmanagement/virtualservices/ihc-dt2
```

# deploy echoservice

```
kubectl apply -f ../oda-canvas-notes/apps/echoservice/k8s
```

for ihc-dt2:

```
kubectl apply -f ../oda-canvas-notes/apps/echoservice/k8s/ihc-dt2
```

## patch api operator

```
kubectl patch configmap/api-operator-istio-configmap -n canvas --type merge -p "{\"data\":{\"APIOPERATORISTIO_PUBLICHOSTNAME\":\"components.ihc-dt.cluster-3.de\"}}"
kubectl rollout restart deployment -n canvas api-operator-istio
```


## patch component gateway

as patch


```
kubectl patch gateway/component-gateway -n components --type json -p '[{"op": "replace","path": "/spec/servers/0/hosts/0","value": "*.ihc-dt.cluster-3.de"}]'
kubectl patch gateway/component-gateway -n components --type json -p '[{"op": "add","path": "/spec/servers/1","value": {"hosts": ["*.ihc-dt.cluster-3.de"],"port": {"name": "https","number": 443,"protocol": "HTTPS"},"tls": {"credentialName": "wc-ihc-dt-cluster-3-de-tls","mode": "SIMPLE"}}}]'
```

or manually (Windows)

```
kubectl edit gateway -n components component-gateway

...
spec:
  ...
  - hosts:
[*] - '*.ihc-dt.cluster-3.de'
...
[+++]
  - hosts:
    - '*.ihc-dt.cluster-3.de'
    port:
      name: https
      number: 443
      protocol: HTTPS
    tls:
      credentialName: wc-ihc-dt-cluster-3-de-tls
      mode: SIMPLE
```

## [optional] create keycloak route

```
kubectl apply -f virtualservices/canvas-keycloak-vs.yaml
kubectl apply -f virtualservices/canvas-vault-hc-vs.yaml
```

```
kubectl apply -f ../oda-canvas-notes/secretsmanagement/virtualservices/canvas-keycloak-vs.yaml
kubectl apply -f ../oda-canvas-notes/secretsmanagement/virtualservices/canvas-vault-landing-page.yaml
kubectl apply -f ../oda-canvas-notes/secretsmanagement/virtualservices/canvas-vault-hc-vs.yaml
kubectl apply -f ../oda-canvas-notes/secretsmanagement/virtualservices/canvas-info.yaml
```

### URLs

* https://canvas-keycloak.ihc-dt.cluster-3.de/auth/
* https://canvas-vault-hc.ihc-dt.cluster-3.de/
** https://canvas-vault-hc.ihc-dt.cluster-3.de/ui/
* https://canvas-info.ihc-dt.cluster-3.de/api-docs/






## [optional] alternative 

```
cat <<EOF | kubectl apply -f -
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  labels:
    app: canvas-vault-hc
  name: canvas-vault-hc-vs
  namespace: canvas
spec:
  gateways:
  - components/component-gateway
  hosts:
  - canvas-vault-hc.ihc-dt.cluster-3.de
  http:
  - match:
    - uri:
        prefix: /
    route:
    - destination:
        host: canvas-vault-hc.canvas-vault.svc.cluster.local
        port:
          number: 8200
EOF
```


# install HashiCorp vault

with WSL:

```
sudo apt-get install jq -y
cd ~/git/oda-canvas-component-vault-ODAA26
installation/CanvasVault/setup_CanvasVault.sh GCP
```

with Windows:

```
helm repo add hashicorp https://helm.releases.hashicorp.com
helm repo update
helm upgrade --install canvas-vault-hc --namespace canvas-vault --create-namespace --version 0.28.0 --values TEMP/installation/canvas-vault-hc/values.yaml hashicorp/vault --wait 

kubectl apply -f TEMP\installation\canvas-vault-hc\canvas-vault-hc-vs-GCP.yaml

kubectl exec -n canvas-vault canvas-vault-hc-0 -- vault auth enable -path jwt-k8s-cv jwt

kubectl create clusterrolebinding oidc-reviewer  --clusterrole=system:service-account-issuer-discovery --group=system:unauthenticated

kubectl get --raw /.well-known/openid-configuration
set ISSUER=https://container.googleapis.com/v1/projects/tmforum-oda-component-cluster/locations/europe-west3/clusters/ihc-dt
echo "ISSUER=%ISSUER%"
kubectl exec -n canvas-vault -it canvas-vault-hc-0 -- vault write auth/jwt-k8s-cv/config oidc_discovery_url=%ISSUER% 
```


## [optional] install code-server

```
# export CODE_SERVER_PASSWORD=<Fill in secure password>
cd ~/git/oda-canvas-component-vault-ODAA26
TEMP/code-server/install-code-server.sh

```


## Deploy Component with secrets management

```
helm upgrade --install prodcat -n components --create-namespace feature-definition-and-test-kit/testData/productcatalog-v1beta3-sman
```


# Uninstall

## Undeploy Component PRODCAT

uninstall all components

```
helm list -n components
```

for example release "prodcat":

```
helm uninstall prodcat -n components
```

## Uninstall Canvas

```
helm uninstall -n canvas canvas

kubectl delete pvc -n canvas data-canvas-postgresql-0
kubectl delete lease -n kube-system cert-manager-cainjector-leader-election
kubectl delete lease -n kube-system cert-manager-controller
kubectl delete ns canvas
kubectl delete ns components
```


## Uninstall Vault

```
helm uninstall -n canvas-vault canvas-vault-hc
kubectl delete -n canvas-vault -f TEMP/canvas-vault/canvas-vault-hc-vs.yaml
kubectl delete clusterrolebinding oidc-reviewer  
kubectl delete ns canvas-vault
```

## Uninstall Code-Server

```
helm uninstall -n code-server code-server
kubectl delete clusterrolebinding code-server-cluster-admin-rb 
kubectl delete -f TEMP/code-server/virtualservice/code-server-vs.yaml
kubectl delete ns code-server
```

# Others

do not uninstall istio, because it removes the loadbalancer carrying the external IP.
Redeployment would change the IP address.

# Notes

run a pod with curl

```
kubectl delete pod --ignore-not-found -n canvas-vault temp-pod || true
kubectl run -it --rm -n canvas-vault --image=tmforumodacanvas/baseimage-kubectl-curl:1.30.5 temp-pod --overrides="{\"spec\":{\"serviceAccount\":\"canvas-vault-hc-pih-sa\"}}" -- /bin/sh
```