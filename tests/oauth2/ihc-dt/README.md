# Links

## http -> https

https://stackoverflow.com/questions/70060121/converting-http-traffic-to-https

## Egress

https://istio.io/latest/docs/tasks/traffic-management/egress/egress-gateway-tls-origination/#perform-mutual-tls-origination-with-an-egress-gateway

### Egress TLS Origination

This example shows how to configure Istio to perform 
TLS origination for traffic to an external service. 
Istio will open HTTPS connections to the external 
service while the original traffic is HTTP.

https://istio.io/latest/docs/tasks/traffic-management/egress/egress-tls-origination/

### Routing egress traffic to wildcard destinations

https://istio.io/latest/blog/2023/egress-sni/


## Lifecycle

https://www.envoyproxy.io/docs/envoy/latest/intro/life_of_a_request#

## Keycloak

https://www.keycloak.org/docs-api/latest/rest-api/index.html#_clients

`GET /admin/realms/{realm}/clients/{client-uuid}/client-secret`

`GET /admin/realms/{realm}/clients` filter by clientId

# Echo Service

https://beeceptor.com/resources/http-echo/


# POD Output interceptor


set default namespace to echoservice:


```
kubectl config set-context --current --namespace=echoservice
```

enable sidecar injection:

```
kubectl label namespace echoservice istio-injection=enabled
```

create ouath2 credentials secret

```
kubectl create secret -n components generic envoy-oauth2-secrets --from-file=envoy-oauth2-secrets --dry-run=client -o yaml | kubectl apply -f -
```

patch istio-sidecar injector

```
apiVersion: v1
data:
  config: |-
    # defaultTemplates defines the default template to use for pods that do not explicitly specify a template
    defaultTemplates: [sidecar]
    policy: enabled
    ...
    templates:
      sidecar: |
        {{- define "resources"  }}
          ...
          # ----- ISTIO-PROXY START -----
          - name: istio-proxy
          {{- if contains "/" (annotation .ObjectMeta `sidecar.istio.io/proxyImage` .Values.global.proxy.image) }}
            image: "{{ annotation .ObjectMeta `sidecar.istio.io/proxyImage` .Values.global.proxy.image }}"
          {{- else }}
            image: "{{ .ProxyImage }}"
          {{- end }}
           ...
            volumeMounts:
            - name: workload-socket
              mountPath: /var/run/secrets/workload-spiffe-uds
            - ...
[+]         # ----- MOUNTED SECRET -----
[+]         - mountPath: /envoy_secrets/oauth2secs
[+]           name: envoy-oauth2-secrets-vol
          volumes:
          - emptyDir:
            name: workload-socket
          - ...
[+]       # ----- SDS VOLUME ----- 
[+]       - name: envoy-oauth2-secrets-vol
[+]         secret:
[+]           optional: true
[+]           defaultMode: 420
[+]           secretName: envoy-oauth2-secrets
            
          {{- if .Values.global.imagePullSecrets }}
          imagePullSecrets:
       ...
kind: ConfigMap
metadata:
  ...
  name: istio-sidecar-injector
  namespace: istio-system
```





# look at istio config

```
kubectl exec -it curlpod-0 -- curl http://localhost:15000/config_dump > curlpod-config_dump.json
```

# check envoy secrets

```
$ istioctl proxy-config secret -n components demo-a-prodcatapi-75d6b7577f-n22t6

RESOURCE NAME        TYPE           STATUS     VALID CERT     SERIAL NUMBER                        NOT AFTER                NOT BEFORE
default              Cert Chain     ACTIVE     true           df65f70a8d05da27fc740e18c038572e     2024-11-27T15:25:43Z     2024-11-26T15:23:43Z
ROOTCA               CA             ACTIVE     true           f44b4b480def8e78141f9062f1c66fd6     2034-11-24T07:13:44Z     2024-11-26T07:13:44Z
file-root:system     CA             ACTIVE     true           5ec3b7a6437fa4e0                     2030-12-31T09:37:37Z     2011-05-05T09:37:37Z
clientsecret                        ACTIVE     false
```
