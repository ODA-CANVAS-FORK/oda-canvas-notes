# Changing the Component Namespace


## uninstall 

```
helm uninstall -n canvas canvas
helm uninstall -n canvas canvas-vs
kubectl delete ns comps448ns canvas-vault canvas cert-manager
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
helm upgrade --install canvas charts/canvas-oda -n canvas --create-namespace --set keycloak.service.type=ClusterIP --set api-operator-istio.deployment.hostName=*.ihc-dt.cluster-1.de --set api-operator-istio.deployment.credentialName=wc-ihc-dt-cluster-1-de-tls --set api-operator-istio.configmap.publicHostname=components.ihc-dt.cluster-1.de --set=api-operator-istio.deployment.httpsRedirect=false --set=dependentapi-simple-operator.serviceInventoryAPI.serverUrl=https://canvas-info.ihc-dt.cluster-1.de --set=canvas-vault.enabled=false --debug
```

```
helm upgrade --install canvas charts/canvas-oda -n canvas --create-namespace --set keycloak.service.type=ClusterIP --set=canvas-vault.enabled=false --debug
```

```
helm template canvas charts/canvas-oda -n canvas --create-namespace --set keycloak.service.type=ClusterIP --set=canvas-vault.enabled=false
```


## set default namespace to "comps448ns"

```
kubectl config set-context --current --namespace=comps448ns
```


## deploy component to primary namespace comps448ns

```
helm upgrade --install demo-a -n comps448ns feature-definition-and-test-kit/testData/productcatalog-v1
```

