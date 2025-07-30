# GitHub Issue OIDC discovery URL

## Create a cluster with `--anonymous-auth=false`

The option "--anonymous-authentication-config=LIMITED" was added recently to gcloud:
https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--anonymous-authentication-config

```
$ gcloud beta container --project "tmforum-oda-component-cluster" clusters create "ihc-dt-noanon"  --anonymous-authentication-config=LIMITED --zone "europe-west4-c" --tier "standard" --no-enable-basic-auth --cluster-version "1.33.2-gke.1111000" --release-channel "regular" --machine-type "e2-standard-4" --image-type "COS_CONTAINERD" --disk-type "pd-standard" --disk-size "100" --metadata disable-legacy-endpoints=true --num-nodes "1" --logging=SYSTEM,WORKLOAD --monitoring=SYSTEM,STORAGE,POD,DEPLOYMENT,STATEFULSET,DAEMONSET,HPA,JOBSET,CADVISOR,KUBELET,DCGM --enable-ip-alias --network "projects/tmforum-oda-component-cluster/global/networks/default" --subnetwork "projects/tmforum-oda-component-cluster/regions/europe-west4/subnetworks/default" --no-enable-intra-node-visibility --default-max-pods-per-node "110" --enable-ip-access --security-posture=standard --workload-vulnerability-scanning=disabled --no-enable-google-cloud-access --addons HorizontalPodAutoscaling,HttpLoadBalancing,GcePersistentDiskCsiDriver --enable-autoupgrade --enable-autorepair --max-surge-upgrade 1 --max-unavailable-upgrade 0 --binauthz-evaluation-mode=DISABLED --enable-managed-prometheus --enable-shielded-nodes --shielded-integrity-monitoring --no-shielded-secure-boot --node-locations "europe-west4-c"
```

Output: 

```
Note: The Kubelet readonly port (10255) is now deprecated. Please update your workloads to use the recommended alternatives. See https://cloud.google.com/kubernetes-engine/docs/how-to/disable-kubelet-readonly-port for ways to check usage and for migration instructions.
Creating cluster ihc-dt-noanon in europe-west4-c... Cluster is being health-checked (Kubernetes Control Plane is health
y)...done.
Created [https://container.googleapis.com/v1beta1/projects/tmforum-oda-component-cluster/zones/europe-west4-c/clusters/ihc-dt-noanon].
To inspect the contents of your cluster, go to: https://console.cloud.google.com/kubernetes/workload_/gcloud/europe-west4-c/ihc-dt-noanon?project=tmforum-oda-component-cluster
kubeconfig entry generated for ihc-dt-noanon.
NAME           LOCATION        MASTER_VERSION      MASTER_IP       MACHINE_TYPE   NODE_VERSION        NUM_NODES  STATUS
ihc-dt-noanon  europe-west4-c  1.33.2-gke.1111000  35.204.198.104  e2-standard-4  1.33.2-gke.1111000  1          RUNNING
```

## check cluster config

```
$ gcloud container clusters describe "ihc-dt-noanon" --project "tmforum-oda-component-cluster" --zone "europe-west4-c" 

addonsConfig:
  ...
anonymousAuthenticationConfig:
  mode: LIMITED
autopilot: {}
autoscaling:
...
```

# check anon access


```
$ kubectl get -v999 --raw /healthz

I0730 09:32:28.252238   22720 loader.go:373] Config loaded from file:  C:\Users\A307131\.kube\config
I0730 09:32:28.279961   22720 round_trippers.go:466] curl -v -XGET  -H "Accept: application/json, */*" -H "User-Agent: kubectl/v1.27.12 (windows/amd64) kubernetes/1203100" 'https://35.204.198.104/healthz'
I0730 09:32:28.412313   22720 round_trippers.go:495] HTTP Trace: DNS Lookup for sia-lb.telekom.de resolved to [{10.140.10.40 }]
I0730 09:32:28.444453   22720 round_trippers.go:510] HTTP Trace: Dial to tcp:10.140.10.40:8080 succeed
I0730 09:32:28.645794   22720 round_trippers.go:553] GET https://35.204.198.104/healthz 200 OK in 365 milliseconds
I0730 09:32:28.646976   22720 round_trippers.go:570] HTTP Statistics: DNSLookup 13 ms Dial 31 ms TLSHandshake 53 ms ServerProcessing 80 ms Duration 365 ms
I0730 09:32:28.646976   22720 round_trippers.go:577] Response Headers:
I0730 09:32:28.646976   22720 round_trippers.go:580]     X-Kubernetes-Pf-Prioritylevel-Uid: 62ed9313-abc2-4651-aa7c-3a26a61c2152
I0730 09:32:28.646976   22720 round_trippers.go:580]     Content-Length: 2
I0730 09:32:28.646976   22720 round_trippers.go:580]     Date: Wed, 30 Jul 2025 07:32:28 GMT
I0730 09:32:28.646976   22720 round_trippers.go:580]     Audit-Id: e8e863c7-75c6-4f06-a99b-e157388dd56e
I0730 09:32:28.646976   22720 round_trippers.go:580]     Cache-Control: no-cache, private
I0730 09:32:28.646976   22720 round_trippers.go:580]     Content-Type: text/plain; charset=utf-8
I0730 09:32:28.647757   22720 round_trippers.go:580]     X-Content-Type-Options: nosniff
I0730 09:32:28.648111   22720 round_trippers.go:580]     X-Kubernetes-Pf-Flowschema-Uid: b764e619-3363-4920-9b29-76365e9e1b1b
```

```
$ curl -k -XGET  -H "Accept: application/json, */*" -H "User-Agent: kubectl/v1.27.12 (windows/amd64) kubernetes/1203100" "https://35.204.198.104/healthz

ok
```

```
$ kubectl get --raw /api/v1/namespaces/default

{"kind":"Namespace","apiVersion":"v1","metadata":{"name":"default","uid":"8a7a95bc-ce04-4819-a713-c4793553b9ea","resourceVersion":"1753790466088207001","creationTimestamp":"2025-07-29T12:01:06Z","labels":{"kubernetes.io/metadata.name":"default"},"managedFields":[{"manager":"kube-apiserver","operation":"Update","apiVersion":"v1","time":"2025-07-29T12:01:06Z","fieldsType":"FieldsV1","fieldsV1":{"f:metadata":{"f:labels":{".":{},"f:kubernetes.io/metadata.name":{}}}}}]},"spec":{"finalizers":["kubernetes"]},"status":{"phase":"Active"}}
```

```
$ curl -k -XGET  -H "Accept: application/json, */*" -H "User-Agent: kubectl/v1.27.12 (windows/amd64) kubernetes/1203100" "https://35.204.198.104/api/v1/namespaces/default"

{"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"Unauthorized","reason":"Unauthorized","code":401}
```


### oicd discovery in noanon


```
$ kubectl get --raw /.well-known/openid-configuration

{"issuer":"https://container.googleapis.com/v1/projects/tmforum-oda-component-cluster/locations/europe-west4-c/clusters/ihc-dt-noanon","jwks_uri":"https://10.164.0.44:443/openid/v1/jwks","response_types_supported":["id_token"],"subject_types_supported":["public"],"id_token_signing_alg_values_supported":["RS256"]}
```

```
$ curl -k -XGET  -H "Accept: application/json, */*" -H "User-Agent: kubectl/v1.27.12 (windows/amd64) kubernetes/1203100" "https://35.204.198.104/.well-known/openid-configuration"

{"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"Unauthorized","reason":"Unauthorized","code":401}
```

### oidc discovery in normal cluster

```
$ kubectl get --raw /.well-known/openid-configuration

{"issuer":"https://container.googleapis.com/v1/projects/tmforum-oda-component-cluster/locations/europe-west4-c/clusters/ihc-dt","jwks_uri":"https://10.164.15.232:443/openid/v1/jwks","response_types_supported":["id_token"],"subject_types_supported":["public"],"id_token_signing_alg_values_supported":["RS256"]}
```

```
curl -k -XGET  -H "Accept: application/json, */*" -H "User-Agent: kubectl/v1.27.12 (windows/amd64) kubernetes/1203100" "https://35.204.152.229/.well-known/openid-configuration"
{"issuer":"https://container.googleapis.com/v1/projects/tmforum-oda-component-cluster/locations/europe-west4-c/clusters/ihc-dt","jwks_uri":"https://10.164.15.232:443/openid/v1/jwks","response_types_supported":["id_token"],"subject_types_supported":["public"],"id_token_signing_alg_values_supported":["RS256"]}
```
