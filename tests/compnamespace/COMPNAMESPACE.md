# Changing the Component Namespace


## uninstall 

```
helm uninstall -n comps-a-ns demo-a
helm uninstall -n comps-b-ns demo-b

helm uninstall -n canvas canvas
helm uninstall -n canvas canvas-vs
kubectl delete ns comps448ns canvas-vault canvas cert-manager comps-a-ns comps-b-ns
```

## update dependencies

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

```

## install from filesystem

without canvas-vault for speed up 

```
export DOMAIN=ihc-dt.cluster-2.de
helm upgrade --install canvas charts/canvas-oda -n canvas --create-namespace --set keycloak.service.type=ClusterIP --set api-operator-istio.deployment.hostName=*.$DOMAIN --set api-operator-istio.deployment.credentialName=domain-tls-secret --set api-operator-istio.configmap.publicHostname=components.$DOMAIN --set=api-operator-istio.deployment.httpsRedirect=false --set=canvas-info-service.serverUrl=https://canvas-info.$DOMAIN --set=canvas-vault.enabled=false 
```


windows:

```
set DOMAIN=ihc-dt.cluster-2.de
helm upgrade --install canvas charts/canvas-oda -n canvas --create-namespace --set keycloak.service.type=ClusterIP --set api-operator-istio.deployment.hostName=*.%DOMAIN% --set api-operator-istio.deployment.credentialName=domain-tls-secret --set api-operator-istio.configmap.publicHostname=components.%DOMAIN% --set=api-operator-istio.deployment.httpsRedirect=false --set=canvas-info-service.serverUrl=https://canvas-info.%DOMAIN% --set=canvas-vault.enabled=false 
```

```
helm upgrade --install canvas charts/canvas-oda -n canvas --create-namespace --set keycloak.service.type=ClusterIP --set=canvas-vault.enabled=false 
```

```
helm template canvas charts/canvas-oda -n canvas --create-namespace --set keycloak.service.type=ClusterIP --set=canvas-vault.enabled=false
```


## set default namespace to "comps448ns"

```
kubectl config set-context --current --namespace=comps448ns
```


## [deploy component to primary namespace components]

```
helm upgrade --install demo-0 -n components feature-definition-and-test-kit/testData/productcatalog-v1
```

## deploy exposing component to secondary namespace odacompns-a

```
helm upgrade --install demo-a -n odacompns-a --create-namespace feature-definition-and-test-kit/testData/productcatalog-v1
```

## deploy dependent component to secondary namespace odacompns-b

```
helm upgrade --install demo-b -n odacompns-b --create-namespace feature-definition-and-test-kit/testData/productcatalog-v1
```

## negative test deploy to unmonitored namespace 

```
helm upgrade --install demo-u -n unmonitored --create-namespace feature-definition-and-test-kit/testData/productcatalog-v1
```

