# Info Service API

## deploy canvas from local filesystem 

```
cd ~/git/oda-canvas-component

cd charts/cert-manager-init
helm dependency update
helm dependency build
cd ../../charts/controller
helm dependency update
helm dependency build
cd ../../charts/canvas-vault
helm dependency update
helm dependency build
cd ../../charts/secretsmanagement-operator
helm dependency update
helm dependency build
cd ../../charts/canvas-oda
helm dependency update
helm dependency build
cd ../..


helm upgrade --install canvas charts/canvas-oda -n canvas --create-namespace --set keycloak.service.type=ClusterIP



kubectl patch configmap/canvas-controller-configmap -n canvas --type merge -p "{\"data\":{\"APIOPERATORISTIO_PUBLICHOSTNAME\":\"components.ihc-dt.cluster-3.de\"}}"
kubectl rollout restart deployment -n canvas oda-controller

kubectl patch gateway/component-gateway -n components --type json -p '[{"op": "replace","path": "/spec/servers/0/hosts/0","value": "*.ihc-dt.cluster-3.de"}]'
kubectl patch gateway/component-gateway -n components --type json -p '[{"op": "add","path": "/spec/servers/1","value": {"hosts": ["*.ihc-dt.cluster-3.de"],"port": {"name": "https","number": 443,"protocol": "HTTPS"},"tls": {"credentialName": "wc-ihc-dt-cluster-3-de-tls","mode": "SIMPLE"}}}]'

```

## set default to ns canvas

```
kubectl config set-context --current --namespace=canvas
```


## restart canvas-smanop

```
 kubectl rollout restart deployment -n canvas canvas-smanop
 ```


## show 

```
kubectl logs deployment/canvas-smanop | head -5
```


## change /oda-canvas/charts/canvas-oda/values.yaml

```
secretsmanagement-operator:
  image: tmforumodacanvas/secretsmanagement-operator
* version: 0.1.2
* prereleaseSuffix: demo1609
  imagePullPolicy: IfNotPresent
```



## express

oda-canvas/source/tmf-services/TMF638_Service_Inventory/expressServer.js

```
  launch() {
    
    try {
      
[+]   logger.info(`+--> Welcome to the DemoX change <--|`)
      
      const SOURCE_DATE_EPOCH = process.env.SOURCE_DATE_EPOCH
      const GIT_COMMIT_SHA = process.env.GIT_COMMIT_SHA
      const CICD_BUILD_TIME = process.env.CICD_BUILD_TIME
```

## Docker Registry

https://hub.docker.com/repository/docker/tmforumodacanvas/tmf638-service-inventory-api/general



 