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