# install from scratch


```
C:\Users\A307131>gcloud auth login
Your browser has been opened to visit:

    https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=32555940559.apps.googleusercontent.com&redirect_uri=http%3A%2F%2Flocalhost%3A8085%2F&scope=openid+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcloud-platform+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fappengine.admin+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fsqlservice.login+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcompute+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Faccounts.reauth&state=NFnokivwAILDgY1c6EJpTDxRtnG3IX&access_type=offline&code_challenge=pbxwhkS7tRu9lF9ZrgP4PR9Pk7BoePlFHZb1CU_Ehlo&code_challenge_method=S256


You are now logged in as [ferenc.hechler@telekom.de].
Your current project is [de0360-pkce-rubix-al-dev000].  You can change this setting by running:
  $ gcloud config set project PROJECT_ID


Updates are available for some Google Cloud CLI components.  To install them,
please run:
  $ gcloud components update


C:\Users\A307131>gcloud auth application-efault login
ERROR: (gcloud.auth) Invalid choice: 'application-efault'.
Maybe you meant:
  gcloud auth login
  gcloud auth activate-service-account
  gcloud auth configure-docker
  gcloud auth list
  gcloud auth print-access-token
  gcloud auth print-identity-token
  gcloud auth revoke

To search the help text of gcloud commands, run:
  gcloud help -- SEARCH_TERMS

C:\Users\A307131>gcloud auth application-default login
Your browser has been opened to visit:

    https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=764086051850-6qr4p6gpi6hn506pt8ejuq83di341hur.apps.googleusercontent.com&redirect_uri=http%3A%2F%2Flocalhost%3A8085%2F&scope=openid+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcloud-platform+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fsqlservice.login&state=zJ02m3v6UHu80tke1edMXyCsHD77VO&access_type=offline&code_challenge=1-MiVPaJ9XGVYdogHNjICPMi4TagZ7MedvaHH7IqvuQ&code_challenge_method=S256


Credentials saved to file: [C:\Users\A307131\AppData\Roaming\gcloud\application_default_credentials.json]

These credentials will be used by any library that requests Application Default Credentials (ADC).

Quota project "de0360-pkce-rubix-al-dev000" was added to ADC which can be used by Google client libraries for billing and quota. Note that some services may still bill the project owning the resource.

C:\Users\A307131>kubectl get ns
E1125 11:30:16.959638   23460 memcache.go:265] couldn't get current server API group list: the server has asked for the client to provide credentials
E1125 11:30:17.251814   23460 memcache.go:265] couldn't get current server API group list: the server has asked for the client to provide credentials
E1125 11:30:17.473610   23460 memcache.go:265] couldn't get current server API group list: the server has asked for the client to provide credentials
E1125 11:30:17.690593   23460 memcache.go:265] couldn't get current server API group list: the server has asked for the client to provide credentials
E1125 11:30:18.494255   23460 memcache.go:265] couldn't get current server API group list: the server has asked for the client to provide credentials
error: You must be logged in to the server (the server has asked for the client to provide credentials)

C:\Users\A307131>tmfihcdt

C:\Users\A307131>REM gcloud auth login

C:\Users\A307131>call gcloud container clusters get-credentials ihc-dt --region europe-west3 --project tmforum-oda-component-cluster
Fetching cluster endpoint and auth data.
kubeconfig entry generated for ihc-dt.
NAME        STATUS   AGE
zz-ihc-dt   Active   258d

C:\Users\A307131>gcloud container clusters get-credentials ihc-dt2 --region europe-west3 --project tmforum-oda-component
-cluster
Fetching cluster endpoint and auth data.
ERROR: (gcloud.container.clusters.get-credentials) ResponseError: code=404, message=Not found: projects/tmforum-oda-component-cluster/locations/europe-west3/clusters/ihc-dt2. This command is authenticated as ferenc.hechler@telekom.de which is the active account specified by the [core/account] property.
Could not find [ihc-dt2] in [europe-west3].
Did you mean [ihc-dt2] in [us-central1-c]?

C:\Users\A307131>gcloud container clusters get-credentials ihc-dt2 --region uscentral1-c --project tmforum-oda-component
-cluster
Fetching cluster endpoint and auth data.
ERROR: (gcloud.container.clusters.get-credentials) ResponseError: code=403, message=Permission denied on 'locations/uscentral1-c' (or it may not exist). This command is authenticated as ferenc.hechler@telekom.de which is the active account specified by the [core/account] property.

C:\Users\A307131>gcloud container clusters get-credentials ihc-dt2 --region uscentral1-c --project tmforum-oda-component-cluster
Fetching cluster endpoint and auth data.
ERROR: (gcloud.container.clusters.get-credentials) ResponseError: code=403, message=Permission denied on 'locations/uscentral1-c' (or it may not exist). This command is authenticated as ferenc.hechler@telekom.de which is the active account specified by the [core/account] property.

C:\Users\A307131>gcloud container clusters get-credentials ihc-dt2 --region uscentral1-c --project tmforum-oda-component-cluster
Fetching cluster endpoint and auth data.
ERROR: (gcloud.container.clusters.get-credentials) ResponseError: code=403, message=Permission denied on 'locations/uscentral1-c' (or it may not exist). This command is authenticated as ferenc.hechler@telekom.de which is the active account specified by the [core/account] property.

C:\Users\A307131>gcloud container clusters get-credentials ihc-dt2 --zone us-central1-c --project tmforum-oda-component-cluster
Fetching cluster endpoint and auth data.
kubeconfig entry generated for ihc-dt2.

C:\Users\A307131>kubectl get ns
NAME                 STATUS   AGE
default              Active   3m
gke-managed-cim      Active   2m25s
gke-managed-system   Active   2m13s
gmp-public           Active   118s
gmp-system           Active   118s
kube-node-lease      Active   3m
kube-public          Active   3m
kube-system          Active   3m

C:\Users\A307131>helm repo update
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "oda-components" chart repository
...Successfully got an update from the "hashicorp" chart repository
...Successfully got an update from the "oda-canvas" chart repository
...Successfully got an update from the "projectcalico" chart repository
...Successfully got an update from the "jetstack" chart repository
...Successfully got an update from the "istio" chart repository
...Successfully got an update from the "prometheus-community" chart repository
...Successfully got an update from the "bitnami" chart repository
Update Complete. ⎈Happy Helming!⎈

C:\Users\A307131>kubectl create namespace istio-system
namespace/istio-system created

C:\Users\A307131>helm install istio-base istio/base -n istio-system
NAME: istio-base
LAST DEPLOYED: Mon Nov 25 11:34:31 2024
NAMESPACE: istio-system
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
Istio base successfully installed!

To learn more about the release, try:
  $ helm status istio-base -n istio-system
  $ helm get all istio-base -n istio-system

C:\Users\A307131>helm install istiod istio/istiod -n istio-system --wait
NAME: istiod
LAST DEPLOYED: Mon Nov 25 11:34:51 2024
NAMESPACE: istio-system
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
"istiod" successfully installed!

To learn more about the release, try:
  $ helm status istiod -n istio-system
  $ helm get all istiod -n istio-system

Next steps:
  * Deploy a Gateway: https://istio.io/latest/docs/setup/additional-setup/gateway/
  * Try out our tasks to get started on common configurations:
    * https://istio.io/latest/docs/tasks/traffic-management
    * https://istio.io/latest/docs/tasks/security/
    * https://istio.io/latest/docs/tasks/policy-enforcement/
  * Review the list of actively supported releases, CVE publications and our hardening guide:
    * https://istio.io/latest/docs/releases/supported-releases/
    * https://istio.io/latest/news/security/
    * https://istio.io/latest/docs/ops/best-practices/security/

For further documentation see https://istio.io website

C:\Users\A307131>kubectl create namespace istio-ingress
namespace/istio-ingress created

C:\Users\A307131>kubectl label namespace istio-ingress istio-injection=enabled
namespace/istio-ingress labeled

C:\Users\A307131>helm install istio-ingress istio/gateway -n istio-ingress --set labels.app=istio-ingress --set labels.istio=ingressgateway --wait
NAME: istio-ingress
LAST DEPLOYED: Mon Nov 25 11:35:48 2024
NAMESPACE: istio-ingress
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
"istio-ingress" successfully installed!

To learn more about the release, try:
  $ helm status istio-ingress -n istio-ingress
  $ helm get all istio-ingress -n istio-ingress

Next steps:
  * Deploy an HTTP Gateway: https://istio.io/latest/docs/tasks/traffic-management/ingress/ingress-control/
  * Deploy an HTTPS Gateway: https://istio.io/latest/docs/tasks/traffic-management/ingress/secure-ingress/

C:\Users\A307131>kubectl get svc -A
NAMESPACE       NAME                   TYPE           CLUSTER-IP       EXTERNAL-IP    PORT(S)
           AGE
default         kubernetes             ClusterIP      34.118.224.1     <none>         443/TCP
           7m36s
gmp-system      alertmanager           ClusterIP      None             <none>         9093/TCP
           6m36s
gmp-system      gmp-operator           ClusterIP      34.118.232.106   <none>         8443/TCP,443/TCP
           6m36s
istio-ingress   istio-ingress          LoadBalancer   34.118.231.243   34.46.234.61   15021:31470/TCP,80:31534/TCP,443:32552/TCP   2m7s
istio-system    istiod                 ClusterIP      34.118.230.175   <none>         15010/TCP,15012/TCP,443/TCP,15014/TCP        3m
kube-system     default-http-backend   NodePort       34.118.226.60    <none>         80:30445/TCP
C:\Users\A307131>
C:\Users\A307131>ube-dns               ClusterIP      34.118.224.10    <none>         53/UDP,53/TCP
C:\Users\A307131>
C:\Users\A307131>etrics-server         ClusterIP      34.118.236.146   <none>         443/TCP
C:\Users\A307131>
C:\Users\A307131>
C:\Users\A307131>
C:\Users\A307131>
C:\Users\A307131>
C:\Users\A307131>
C:\Users\A307131>
C:\Users\A307131>
C:\Users\A307131>kubectl get secrets -A | grep -i wc
'grep' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\A307131>kubectl get secrets -A
NAMESPACE       NAME                                  TYPE                 DATA   AGE
gmp-system      alertmanager                          Opaque               1      12m
gmp-system      collection                            Opaque               0      12m
gmp-system      rules                                 Opaque               0      12m
gmp-system      webhook-tls                           Opaque               2      13m
istio-ingress   sh.helm.release.v1.istio-ingress.v1   helm.sh/release.v1   1      9m1s
istio-system    istio-ca-secret                       istio.io/ca-root     5      9m48s
istio-system    sh.helm.release.v1.istio-base.v1      helm.sh/release.v1   1      10m
istio-system    sh.helm.release.v1.istiod.v1          helm.sh/release.v1   1      9m55s

C:\Users\A307131>kubectl create ns zz-ihc-dt2
namespace/zz-ihc-dt2 created

C:\Users\A307131>kubectl apply -f -
apiVersion: v1
data:
  tls.crt: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUUvakNDQSthZ0F3SUJBZ0lTQTJSNGxQOC91aVhtdk9XTUhMbmFkNUl4TUEwR0NTcUdTSWIzRFFFQkN3VUEKTURNeEN6QUpCZ05WQkFZVEFsVlRNUll3RkFZRFZRUUtFdzFNWlhRbmN5QkZibU55ZVhCME1Rd3dDZ1lEVlFRRApFd05TTVRFd0hoY05NalF4TVRJMU1EazBNek16V2hjTk1qVXdNakl6TURrME16TXlXakFoTVI4d0hRWURWUVFECkRCWXFMbWxvWXkxa2RESXVZMngxYzNSbGNpMHpMbVJsTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEEKTUlJQkNnS0NBUUVBeCszeHpmbFdhbmJJdlBCWXgxWDNWQU9sUm0yQ3ErWHdOdVpqOTVaVUl3YnJrd3V4ZG95bQpGZkxQOWhBbEYvWWFCekY4NkIwaGtQVFFiRmVVbmNjc1pQdWRFeGVOY0FUL3BTaUpsOWU1NHVDNDB6SUxiU1lwClpOZjhoV2JQM1U3NVpYWE5ZTXBrM3VqeFY1R3F4UnV2cDlsTlRZUlRpR3M2SCtLMEhRTmZDZUVIdzhNN0lROE8KQjVkN2daTzh1L3dWYWY1ZU04SUpRS3N2dXdlUDNyazcyMUN3d2hUVkRBTzJBWGd2SDhDWGxLZFUxcHJEaTVQSQpUUzBpaTFqcUl4SzZHMUxoTGhDWGRlVU1OcUIzc2NTeXNZNUVLdW9rRkhtRjJJYlZQcnNXL205SFM0TGVFWUJxCm82WmdzRk16czcwT0s4eHdZNFhXRktKYWtBdUdFQm4wQ3dJREFRQUJvNElDSERDQ0FoZ3dEZ1lEVlIwUEFRSC8KQkFRREFnV2dNQjBHQTFVZEpRUVdNQlFHQ0NzR0FRVUZCd01CQmdnckJnRUZCUWNEQWpBTUJnTlZIUk1CQWY4RQpBakFBTUIwR0ExVWREZ1FXQkJScm5yWkgzZGI1TXVXYnVYRGRWL2l0c0wyRC9EQWZCZ05WSFNNRUdEQVdnQlRGCnowYWs2dlREd0hwc2xjUXRzRjZTTHlianVUQlhCZ2dyQmdFRkJRY0JBUVJMTUVrd0lnWUlLd1lCQlFVSE1BR0cKRm1oMGRIQTZMeTl5TVRFdWJ5NXNaVzVqY2k1dmNtY3dJd1lJS3dZQkJRVUhNQUtHRjJoMGRIQTZMeTl5TVRFdQphUzVzWlc1amNpNXZjbWN2TUNFR0ExVWRFUVFhTUJpQ0Zpb3VhV2hqTFdSME1pNWpiSFZ6ZEdWeUxUTXVaR1V3CkV3WURWUjBnQkF3d0NqQUlCZ1puZ1F3QkFnRXdnZ0VHQmdvckJnRUVBZFo1QWdRQ0JJSDNCSUgwQVBJQWR3QjkKV1I0UzRYZ3FleHhoWjN4ZS9malFoMXdVb0U2Vm5ya0RMOWtPakM1NXVBQUFBWk5pNmdIQkFBQUVBd0JJTUVZQwpJUUR1TWwyQWZWZUNla2hjSGFTSzlvc2thVElld3RYU2FEWWVFS1NBQWZOZlhnSWhBSlV0dS9HRDBJQlFWb2NjCi80dTFML0lCSlB4N2g0ODhqWTJIcTFleXNEeGZBSGNBb3VNSzVFWHZ2YTJiZmpqdFIyZDNVOWVDVzRTVTF5dGUKR3l6RXVWQ2tSK2NBQUFHVFl1b0J4QUFBQkFNQVNEQkdBaUVBcFpGN0c5NW9DVVZEUXUxOERub0t1Sk5QSTdqUwpJUkhBcVluMCs2cDhHTmtDSVFEMy9SN0FORWdJUUpiSFZBRzJ3RXFmRXJ2dXZKR05vNzRPNmNuSlpQMFFHVEFOCkJna3Foa2lHOXcwQkFRc0ZBQU9DQVFFQVJ3a0VwbEdNT0JwV0R3RWd5RWp6WVprdkx1SXpYTEdjaE9rTGtwSHgKSTFJSndxOFh1cmd2L2pHbHZJVXY4QnB6WkVxdk8zVklWTmRQcmtzRzdVbGcvaDBvNW5ybmNhNzlHQmxXT3N3ZQowb1I3R1VDaGhKM25MN3pxRTNWQkJWNjdFbDZzcVRnQU5lS0YxU2I3c0dLNzVidXo1OFJlZHMwaDhDdXZxRXZwCjAxZHg4QWc2S25FZnpTeGxEcWxFRGZvYWpLTG02Visrdk92NHliemc0N2VnOXJHeE03OG9JbVQ1MHlNZ01nV0cKa2pIdFFHRVhMVjRsbUc0WUpjNzBaTktzMFVlb254TVRFZXQzT0dXNC9hZWJyM2hWZ3lRb1Nta1A2eTR6T0V4bQpWaXNrbVExaWtaQW55UGxyQUNPTVF1R0xqczUvR0tVR21vbWo1NS9nQWFDV2tnPT0KLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQotLS0tLUJFR0lOIENFUlRJRklDQVRFLS0tLS0KTUlJRkJqQ0NBdTZnQXdJQkFnSVJBSXA5UGhQV0x6RHZJNGE5S1Fkck5QZ3dEUVlKS29aSWh2Y05BUUVMQlFBdwpUekVMTUFrR0ExVUVCaE1DVlZNeEtUQW5CZ05WQkFvVElFbHVkR1Z5Ym1WMElGTmxZM1Z5YVhSNUlGSmxjMlZoCmNtTm9JRWR5YjNWd01SVXdFd1lEVlFRREV3eEpVMUpISUZKdmIzUWdXREV3SGhjTk1qUXdNekV6TURBd01EQXcKV2hjTk1qY3dNekV5TWpNMU9UVTVXakF6TVFzd0NRWURWUVFHRXdKVlV6RVdNQlFHQTFVRUNoTU5UR1YwSjNNZwpSVzVqY25sd2RERU1NQW9HQTFVRUF4TURVakV4TUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCCkNnS0NBUUVBdW9lOFhCc0FPY3ZLQ3MzVVp4RDVBVHlsVHFWaHl5YktVdnNWQWJlNUtQVW9IdTBuc3lRWU9XY0oKREFqczREcXdPM2NPdmZQbE9WUkJERTZ1UWRhWmRONVIyKzk3LzFpOXFMY1Q5dDR4MWZKeXlYSnFDNE4wbFp4RwpBR1FVbWZPeDJTTFp6YWlTcWh3bWVqLys3MWdGZXdpVmdkdHhENDc3NHpFSnV3bStVRTFmajVGMlBWcWRub1B5CjZjUm1zK0VHWmtOSUdJQmxvRGNZbXB1RU1wZXhzcjNFK0JVQW5TZUkrK0pqRjVac215ZG5TOFRiS0Y1cHdubncKU1Z6Z0pGRGh4THloQmF4N1FHMEF0TUpCUDZkWXVDL0ZYSnVsdXdtZThmN3JzSVU1L2FnSzcwWEVlT3RsS3NMUApYenplNDF4TkcvY0xKeXVxQzBKM1UwOTVhaDJIMlFJREFRQUJvNEg0TUlIMU1BNEdBMVVkRHdFQi93UUVBd0lCCmhqQWRCZ05WSFNVRUZqQVVCZ2dyQmdFRkJRY0RBZ1lJS3dZQkJRVUhBd0V3RWdZRFZSMFRBUUgvQkFnd0JnRUIKL3dJQkFEQWRCZ05WSFE0RUZnUVV4YzlHcE9yMHc4QjZiSlhFTGJCZWtpOG00N2t3SHdZRFZSMGpCQmd3Rm9BVQplYlJaNW51MjVlUUJjNEFJaU1nYVdQYnBtMjR3TWdZSUt3WUJCUVVIQVFFRUpqQWtNQ0lHQ0NzR0FRVUZCekFDCmhoWm9kSFJ3T2k4dmVERXVhUzVzWlc1amNpNXZjbWN2TUJNR0ExVWRJQVFNTUFvd0NBWUdaNEVNQVFJQk1DY0cKQTFVZEh3UWdNQjR3SEtBYW9CaUdGbWgwZEhBNkx5OTRNUzVqTG14bGJtTnlMbTl5Wnk4d0RRWUpLb1pJaHZjTgpBUUVMQlFBRGdnSUJBRTdpaVYwS0F4eVFPTkQxSC9seFhQakRqN0kzaUhwdnNDVWY3YjYzMklZR2p1a0poTTF5CnY0SHovTXJQVTBqdHZmWnBRdFNsRVQ0MXlCT3lraDBGWCtvdTFOajRTY090OVptV25POG0yT0cwSkF0SUlFMzgKMDFTMHFjWWh5T0UyRy85M1pDa1h1ZkJMNzEzcXpYblF2NUMvdmlPeWtOcEtxVWd4ZEtsRUMrSGk5aTJEY2FSMQplOUtVd1FVWlJoeTVqL1BFZEVnbEtnM2w5ZHRENHR1VG03a1p0Qjh2MzJvT2p6SFRZdys3S2R6ZFppdy9zQnRuClVmaEJQT1JOdWF5NHBKeG1ZL1dyaFNNZHpGTzJxM0d1M01VQmNkbzI3Z29ZS2pMOUNURjhqL1p6NTV5Y3RVb1YKYW5lQ1dzL2FqVVgrSHlwa0JUQStjOExHRExuV08yTktxMFlEL3BuQVJrQW5ZR1BmVURvSFI5Z1ZTcC9xUngrWgpXZ2hpRExac013aE4xemp0U0MwdUJXaXVnRjN2VE56WUlFRmZhUEc3V3MzakRyQU1NWWViUTk1SlErSElCRC9SClBCdUhSVEJwcUtseURua1NIREhZUGlOWDNhZFBvUEFjZ2RGM0gyL1cwcm1vc3dNV2dUbExuMVd1MG1ya3M3L3EKcGRXZlM2UEoxanR5ODByMlZLc00vRGozWUlEZmJqWEtkYUZVNUMrOGJoZkpHcVUzdGFLYXV1ejB3SFZHVDNlbwo2RmxXa1dZdGJ0NHBnZGFtbHdWZVpFVytMTTdxWkVKRXNNTlByZkMwM0FQS21ac0pncFdDRFdPS1p2a1pjdmpWCnVZa1E0b21ZQ1RYNW9oeStrbk1qZE9tZEg5YzdTcHFFV0JEQzg2ZmlOZXgrTzBYT01FWlNhOERBCi0tLS0tRU5EIENFUlRJRklDQVRFLS0tLS0K
  tls.key: LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tCk1JSUV2QUlCQURBTkJna3Foa2lHOXcwQkFRRUZBQVNDQktZd2dnU2lBZ0VBQW9JQkFRREg3ZkhOK1ZacWRzaTgKOEZqSFZmZFVBNlZHYllLcjVmQTI1bVAzbGxRakJ1dVRDN0YyaktZVjhzLzJFQ1VYOWhvSE1Yem9IU0dROU5CcwpWNVNkeHl4ays1MFRGNDF3QlArbEtJbVgxN25pNExqVE1ndHRKaWxrMS95RlpzL2RUdmxsZGMxZ3ltVGU2UEZYCmthckZHNituMlUxTmhGT0lhem9mNHJRZEExOEo0UWZEd3pzaER3NEhsM3VCazd5Ny9CVnAvbDR6d2dsQXF5KzcKQjQvZXVUdmJVTERDRk5VTUE3WUJlQzhmd0plVXAxVFdtc09MazhoTkxTS0xXT29qRXJvYlV1RXVFSmQxNVF3MgpvSGV4eExLeGprUXE2aVFVZVlYWWh0VSt1eGIrYjBkTGd0NFJnR3FqcG1Dd1V6T3p2UTRyekhCamhkWVVvbHFRCkM0WVFHZlFMQWdNQkFBRUNnZ0VBQ3hwUU5OK1ZhSGtyUWE3WlIweWpYUk9Nd0tJQlFUbVdRdjQ5YS9qNXVDNUEKczl4UTRTUURiekdhVWZCb2x2R1FWWGp1bGxkVHoyQ0JHSnN1Z2lxVzhRNjJGT0xZZEhHYW50bm05anRCTS9QRgozOWltSU13ZlBWM3ZSSnRHak9RL1hsNlI1cittcFdoclNyRW91aVNFOXozT21MRHlFSi9melBpQ2h4L3lUYktMCngzWHpGQnNEUlNSRHY1RkY4cDdzNXBadW1tczh1Wnk3Wk9XcHNZbU9YOXlXanpPbEw1V0JKWDYrZ3IwRkFncVQKTTQxaDFrNm9LdUdoOWRjYlB1WG5jYkJMdkZxekRVa3VML3VhQ3h4cEgydFQvU1NJUUFCL3ZGeWVVcGZCRGphegplU1lzWnFuVSttMUN0NW1EZE5GWHFDZ1NxWlV4NEZVZ1FtQkY1ODhLUVFLQmdRRDRCNkVuZytPNWt4c3JJS21NCkJSL3owMFZnNGVIYS84ZVlacndtTXRxMFFOa09hR2hJQ3FZRXkzR2RhendpVUVjcDFzeW5DRVJWQjd3T0Vxck4KODRZQnRDVi9GNllsc0tYc3JxN2ZQdjRMOWQxYlhSMWVvV2ZmRmoyMWxpZ1VHdlEyTEx4dC9LZzZrYTQwemtmTApTYk9OcndLdGROOUVZTDRTWWVLbVJ0UUp5d0tCZ1FET1dxQndQem1ERkVKS3NXR3BHNFkrMEZlZ1lIdDYxQk84CjZxUVJzcXl6VXpkWmZsZHl0NndSdDNVdFp3bFl6NEJDdzlYQVArUDVPdFdrSkRLb2xTM3kvVHEzd0JRdUNPV00KUTUrMyt3Ykl5aFF6SjVZcERDNGZRbzlHTUlqb08zVUtLc3I0bngxL1NneFpRdjI1RWZPRnpGTmtvYU9lSnAxeApuQ3NJN2RGMndRS0JnRVFUdEFQb2kyU3dIOURpa2liQWNWaTNNRis3SUFiQUZjU2F6aUdkNjdGMTZ4MnRRcElqCmVoWHUwU3huOW9Wa2kyUE1kVGVUYVUzOVpYeG5XMEpVQ1FBR3RoUUFKYlpLbWdBd29nYmNmMVpCRVpTMkpnMkgKTjc5ZmwyaHo0bVJDVWExYzhnc3VRZTV4ZGVOQWl5d2MrbzkwN2NNMlJPRzd1Ky9IdGpIMVZ0V3BBb0dBQnVCdQpTRTlURTFNeGdsdTI3WFBGWFlLRDZReE9FU0hRSnBPTE5DdklKWkc0WG5zZlh1dFFDS2NjZUk3ZWVOOHhYd2czCnIxaHh1SFNGZWhyYXRWT0RYSDJqMzB1L1lHbGJmUGtqOFhXa0hEemZ2M1NxUkdQcmhZOHFSeVNHNjNaUHlDNzAKNUtRb3ozMGdQRGxIUzB1VjJmZWRMOVZUSm9vUzVSNVhNTXo4RmdFQ2dZQXRFVG9wdmlUU0ZBM1FZdHhtajU1TApuVkR1RlM1MVMvYThPK3RSQlZKbXp4THBid1FKYk9XWlpIZklpd0l0VXMvYTBsZ2c4b0prVjduam5ocE53UzRnCnlTMW8vNTdoSkhWVmI5OWdmVUx5UmdYUzlDR0gxWjcyUnBwdlpLSEVidmp6akc2bVRKa2d6R3VsaU1wZHAvbnEKVWQvNVVEaVA3OXQ1TjU1aWwrdWJOdz09Ci0tLS0tRU5EIFBSSVZBVEUgS0VZLS0tLS0K
kind: Secret
metadata:
  creationTimestamp: null
  name: wc-ihc-dt2-cluster-3-de-tls
  namespace: istio-ingress
type: kubernetes.io/tls
^Z
secret/wc-ihc-dt2-cluster-3-de-tls created

C:\Users\A307131>cd git

C:\Users\A307131\git>cd oda-canvas

C:\Users\A307131\git\oda-canvas>git status
On branch feature/362-authentication-adding-authentication-to-outbound-api-calls-from-component
Your branch is up to date with 'origin/feature/362-authentication-adding-authentication-to-outbound-api-calls-from-component'.

nothing to commit, working tree clean

C:\Users\A307131\git\oda-canvas>git pull
remote: Enumerating objects: 114, done.
remote: Counting objects: 100% (96/96), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 114 (delta 88), reused 96 (delta 88), pack-reused 18 (from 1)
Receiving objects: 100% (114/114), 11.80 KiB | 1.69 MiB/s, done.
Resolving deltas: 100% (88/88), completed with 36 local objects.
From https://github.com/tmforum-oda/oda-canvas
   f6c6ea0..d5bb8a2  76-idm-set-up-reference-idm-service-for-authentication-and-authorisation -> origin/76-idm-set-up-reference-idm-service-for-authentication-and-authorisation
   e79a3a5..0261f0f  feature/223-naming-convention-for-canvas-operators -> origin/feature/223-naming-convention-for-canvas-operators
Already up to date.

C:\Users\A307131\git\oda-canvas>git status
On branch feature/362-authentication-adding-authentication-to-outbound-api-calls-from-component
Your branch is up to date with 'origin/feature/362-authentication-adding-authentication-to-outbound-api-calls-from-component'.

nothing to commit, working tree clean

C:\Users\A307131\git\oda-canvas>kubectl get pods -A
NAMESPACE         NAME                                                READY   STATUS    RESTARTS   AGE
gke-managed-cim   kube-state-metrics-0                                2/2     Running   0          17m
gmp-system        collector-tt8h9                                     2/2     Running   0          15m
gmp-system        gmp-operator-64db6fd448-5dp4m                       1/1     Running   0          17m
istio-ingress     istio-ingress-5d6f899689-slb46                      1/1     Running   0          12m
istio-system      istiod-588fc7d5b9-v7qwl                             1/1     Running   0          13m
kube-system       event-exporter-gke-79cd469d79-w2dsk                 2/2     Running   0          17m
kube-system       fluentbit-gke-s7q8f                                 3/3     Running   0          16m
kube-system       gke-metrics-agent-pk9l2                             3/3     Running   0          16m
kube-system       konnectivity-agent-5997cc5574-vsq47                 2/2     Running   0          17m
kube-system       konnectivity-agent-autoscaler-696cc5598c-snc84      1/1     Running   0          17m
kube-system       kube-dns-autoscaler-6f896b6968-s22xs                1/1     Running   0          17m
kube-system       kube-dns-f549f7b7-zlw5b                             5/5     Running   0          17m
kube-system       kube-proxy-gke-ihc-dt2-default-pool-3ec16236-31dj   1/1     Running   0          15m
kube-system       l7-default-backend-78478f96f4-72wmv                 1/1     Running   0          17m
kube-system       metrics-server-v1.30.3-7fff7dc68d-gw99k             1/1     Running   0          16m
kube-system       pdcsi-node-7987n                                    2/2     Running   0          16m

C:\Users\A307131\git\oda-canvas>
C:\Users\A307131\git\oda-canvas>
C:\Users\A307131\git\oda-canvas>helm dependency update --skip-refresh ./charts/cert-manager-init
Saving 1 charts
Downloading cert-manager from repo https://charts.jetstack.io
Deleting outdated charts

C:\Users\A307131\git\oda-canvas>helm dependency update --skip-refresh ./charts/canvas-api-gateway/combined-api-gateway-chart
Saving 2 charts
Deleting outdated charts

C:\Users\A307131\git\oda-canvas>helm dependency update --skip-refresh ./charts/canvas-vault
Saving 1 charts
Downloading vault from repo https://helm.releases.hashicorp.com
Deleting outdated charts

C:\Users\A307131\git\oda-canvas>helm dependency update --skip-refresh ./charts/canvas-oda
Saving 10 charts
Downloading keycloak from repo https://charts.bitnami.com/bitnami
Deleting outdated charts

C:\Users\A307131\git\oda-canvas>helm upgrade --install canvas charts/canvas-oda -n canvas --create-namespace --set keycloak.service.type=ClusterIP --set api-operator-istio.deployment.hostName=*.ihc-dt2.cluster-3.de --set api-operator-istio.deployment.credentialName=wc-ihc-dt2-cluster-3-de-tls --set api-operator-istio.configmap.publicHostname=components.ihc-dt2.cluster-3.de
Release "canvas" does not exist. Installing it now.
NAME: canvas
LAST DEPLOYED: Mon Nov 25 11:49:44 2024
NAMESPACE: canvas
STATUS: deployed
REVISION: 1

C:\Users\A307131\git\oda-canvas>kubectl get pods -A
NAMESPACE         NAME                                                READY   STATUS      RESTARTS   AGE
canvas-vault      canvas-vault-hc-0                                   1/1     Running     0          5m7s
canvas-vault      canvas-vault-hc-post-install-hook-fph2w             0/1     Completed   0          101s
canvas            api-operator-istio-bc76b8c44-tlw7c                  1/1     Running     0          5m8s
canvas            canvas-depapi-op-5fcfc8b5bb-pm2hm                   1/1     Running     0          5m7s
canvas            canvas-info-service-7fcc797759-w7bwf                1/1     Running     0          5m7s
canvas            canvas-keycloak-0                                   1/1     Running     0          5m7s
canvas            canvas-postgresql-0                                 1/1     Running     0          5m7s
canvas            canvas-sm-preinst-autodetect-audience-qtt65         0/1     Completed   0          5m21s
canvas            canvas-smanop-69fb9c75fd-jkn7l                      1/1     Running     0          5m8s
canvas            canvas-svcinv-mongodb-558bfdf978-d5zlp              1/1     Running     0          5m7s
canvas            compcrdwebhook-7c9f7bc54b-mhtl4                     1/1     Running     0          5m7s
canvas            component-operator-6bfcd67f5-gfd9g                  2/2     Running     0          5m7s
canvas            job-hook-postinstall-z95hk                          0/1     Completed   0          5m3s
cert-manager      canvas-cert-manager-5486d8669-h2tn9                 1/1     Running     0          5m8s
cert-manager      canvas-cert-manager-cainjector-575d4b8dff-kdcqq     1/1     Running     0          5m8s
cert-manager      canvas-cert-manager-webhook-665f74c695-bvq8p        1/1     Running     0          5m8s
gke-managed-cim   kube-state-metrics-0                                2/2     Running     0          24m
gmp-system        collector-tt8h9                                     2/2     Running     0          22m
gmp-system        gmp-operator-64db6fd448-5dp4m                       1/1     Running     0          24m
istio-ingress     istio-ingress-5d6f899689-slb46                      1/1     Running     0          19m
istio-system      istiod-588fc7d5b9-v7qwl                             1/1     Running     0          20m
kube-system       event-exporter-gke-79cd469d79-w2dsk                 2/2     Running     0          24m
kube-system       fluentbit-gke-s7q8f                                 3/3     Running     0          23m
kube-system       gke-metrics-agent-pk9l2                             3/3     Running     0          23m
kube-system       konnectivity-agent-5997cc5574-vsq47                 2/2     Running     0          24m
kube-system       konnectivity-agent-autoscaler-696cc5598c-snc84      1/1     Running     0          24m
kube-system       kube-dns-autoscaler-6f896b6968-s22xs                1/1     Running     0          24m
kube-system       kube-dns-f549f7b7-zlw5b                             5/5     Running     0          24m
kube-system       kube-proxy-gke-ihc-dt2-default-pool-3ec16236-31dj   1/1     Running     0          22m
kube-system       l7-default-backend-78478f96f4-72wmv                 1/1     Running     0          24m
kube-system       metrics-server-v1.30.3-7fff7dc68d-gw99k             1/1     Running     0          24m
kube-system       pdcsi-node-7987n                                    2/2     Running     0          23m

C:\Users\A307131\git\oda-canvas>kubectl apply -f ../oda-canvas-notes/secretsmanagement/virtualservices/ihc-dt2
virtualservice.networking.istio.io/canvas-info-vs created
virtualservice.networking.istio.io/canvas-keycloak-vs created
service/canvas-vault-hc-tls created
destinationrule.networking.istio.io/canvas-vault-hc-dr created
virtualservice.networking.istio.io/canvas-vault-hc-vs created
configmap/canvas-vault-landing-page-init-cm created
service/canvas-vault-landing-page created
deployment.apps/canvas-vault-landing-page created
virtualservice.networking.istio.io/canvas-vault-landing-page-vs created
Error from server (NotFound): error when creating "..\\oda-canvas-notes\\secretsmanagement\\virtualservices\\ihc-dt2\\grafana.yaml": namespaces "grafana" not found

C:\Users\A307131\git\oda-canvas>kubectl create ns grafana
namespace/grafana created

C:\Users\A307131\git\oda-canvas>kubectl apply -f ../oda-canvas-notes/secretsmanagement/virtualservices/ihc-dt2
virtualservice.networking.istio.io/canvas-info-vs unchanged
virtualservice.networking.istio.io/canvas-keycloak-vs unchanged
service/canvas-vault-hc-tls unchanged
destinationrule.networking.istio.io/canvas-vault-hc-dr unchanged
virtualservice.networking.istio.io/canvas-vault-hc-vs unchanged
configmap/canvas-vault-landing-page-init-cm unchanged
service/canvas-vault-landing-page unchanged
deployment.apps/canvas-vault-landing-page configured
virtualservice.networking.istio.io/canvas-vault-landing-page-vs unchanged
virtualservice.networking.istio.io/grafana-vs created

C:\Users\A307131\git\oda-canvas>kubectl apply -f ../oda-canvas-notes/apps/echoservice/k8s/ihc-dt2
Error from server (NotFound): error when creating "..\\oda-canvas-notes\\apps\\echoservice\\k8s\\ihc-dt2\\echoservice-vs.yaml": namespaces "echoservice" not found

C:\Users\A307131\git\oda-canvas>kubectl create namespace echoservice
namespace/echoservice created

C:\Users\A307131\git\oda-canvas>kubectl apply -f ../oda-canvas-notes/apps/echoservice/k8s/
deployment.apps/echoservice-deployment created
Warning: resource namespaces/echoservice is missing the kubectl.kubernetes.io/last-applied-configuration annotation which is required by kubectl apply. kubectl apply should only be used on resources created declaratively by either kubectl create --save-config or kubectl apply. The missing annotation will be patched automatically.
namespace/echoservice configured
service/echoservice created
virtualservice.networking.istio.io/echoservice-vs created

C:\Users\A307131\git\oda-canvas>kubectl apply -f ../oda-canvas-notes/apps/echoservice/k8s/ihc-dt2
virtualservice.networking.istio.io/echoservice-vs configured

C:\Users\A307131\git\oda-canvas>kubectl get vs -A
NAMESPACE      NAME                           GATEWAYS                           HOSTS                                      AGE
canvas-vault   canvas-vault-hc-vs             ["components/component-gateway"]   ["canvas-vault-hc.ihc-dt2.cluster-3.de"]   2m53s
canvas-vault   canvas-vault-landing-page-vs   ["components/component-gateway"]   ["canvas-vault-hc.ihc-dt2.cluster-3.de"]   2m50s
canvas         canvas-info-vs                 ["components/component-gateway"]   ["canvas-info.ihc-dt2.cluster-3.de"]       2m56s
canvas         canvas-keycloak-vs             ["components/component-gateway"]   ["canvas-keycloak.ihc-dt2.cluster-3.de"]   2m55s
echoservice    echoservice-vs                 ["components/component-gateway"]   ["echoservice.ihc-dt2.cluster-3.de"]       27s
grafana        grafana-vs                     ["components/component-gateway"]   ["grafana.ihc-dt2.cluster-3.de"]           2m14s

C:\Users\A307131\git\oda-canvas>kubectl get gateway -n componets component-gateway
Error from server (NotFound): namespaces "componets" not found

C:\Users\A307131\git\oda-canvas>kubectl get gateway -n components component-gateway -oyaml
apiVersion: networking.istio.io/v1
kind: Gateway
metadata:
  annotations:
    helm.sh/hook: post-install
    helm.sh/hook-weight: "5"
    helm.sh/resource-policy: keep
  creationTimestamp: "2024-11-25T10:55:20Z"
  generation: 1
  name: component-gateway
  namespace: components
  resourceVersion: "17944"
  uid: 643ba42f-c1a0-4f0c-ad01-9f3967be0e29
spec:
  selector:
    istio: ingressgateway
  servers:
  - hosts:
    - '*.ihc-dt2.cluster-3.de'
    port:
      name: http
      number: 80
      protocol: HTTP
    tls:
      httpsRedirect: true
  - hosts:
    - '*.ihc-dt2.cluster-3.de'
    port:
      name: https
      number: 443
      protocol: HTTPS
    tls:
      credentialName: wc-ihc-dt2-cluster-3-de-tls
      mode: SIMPLE

C:\Users\A307131\git\oda-canvas>kubectl get secrets -n istio-ingress
NAME                                  TYPE                 DATA   AGE
istio-ingress-cert                    kubernetes.io/tls    3      6m33s
sh.helm.release.v1.istio-ingress.v1   helm.sh/release.v1   1      23m
wc-ihc-dt2-cluster-3-de-tls           kubernetes.io/tls    2      12m

C:\Users\A307131\git\oda-canvas>kubectl get deployment -n istio-ingress istio-ingress
NAME            READY   UP-TO-DATE   AVAILABLE   AGE
istio-ingress   1/1     1            1           73m

C:\Users\A307131\git\oda-canvas>cd ..

C:\Users\A307131\git>cd oda-canvas-notes

C:\Users\A307131\git\oda-canvas-notes>cd tests

C:\Users\A307131\git\oda-canvas-notes\tests>cd oauth2

C:\Users\A307131\git\oda-canvas-notes\tests\oauth2>cd ihc-dt2

C:\Users\A307131\git\oda-canvas-notes\tests\oauth2\ihc-dt2>kubectl get deployment -n istio-ingress istio-ingress -oyaml > istio-ingress-deployment.yaml

C:\Users\A307131\git\oda-canvas-notes\tests\oauth2\ihc-dt2>kubectl apply -f patched-istio-ingress-deployment.yaml
Warning: resource deployments/istio-ingress is missing the kubectl.kubernetes.io/last-applied-configuration annotation which is required by kubectl apply. kubectl apply should only be used on resources created declaratively by either kubectl create --save-config or kubectl apply. The missing annotation will be patched automatically.
deployment.apps/istio-ingress configured

C:\Users\A307131\git\oda-canvas-notes\tests\oauth2\ihc-dt2>kubectl apply -f envoy-sds-secrets.yaml
configmap/oauth2secs-cm created

C:\Users\A307131\git\oda-canvas-notes\tests\oauth2\ihc-dt2>kubectl get pods -n istio-ingress
NAME                             READY   STATUS              RESTARTS   AGE
istio-ingress-5d6f899689-slb46   1/1     Running             0          75m
istio-ingress-7c98ccb847-lxqxv   0/1     ContainerCreating   0          32s

C:\Users\A307131\git\oda-canvas-notes\tests\oauth2\ihc-dt2>kubectl get pods -n istio-ingress
NAME                             READY   STATUS    RESTARTS   AGE
istio-ingress-7c98ccb847-lxqxv   1/1     Running   0          96s

C:\Users\A307131\git\oda-canvas-notes\tests\oauth2\ihc-dt2>cd ..

C:\Users\A307131\git\oda-canvas-notes\tests\oauth2>cd ..

C:\Users\A307131\git\oda-canvas-notes\tests>cd ..

C:\Users\A307131\git\oda-canvas-notes>cd ..

C:\Users\A307131\git>cd oda-canvas

C:\Users\A307131\git\oda-canvas>helm upgrade --install demo-a -n components --create-namespace feature-definition-and-test-kit/testData/productcatalog-v1beta4-sman
NAME: demo-ao-a" does not exist. Installing it now.
LAST DEPLOYED: Mon Nov 25 12:53:56 2024
NAMESPACE: components
STATUS: deployed
REVISION: 1
TEST SUITE: None

C:\Users\A307131\git\oda-canvas>kubectl get components -A
NAMESPACE    NAME                              DEPLOYMENT_STATUS
components   demo-a-productcatalogmanagement   In-Progress-CompCon

C:\Users\A307131\git\oda-canvas>kubectl get vs -A
NAMESPACE      NAME                                                       GATEWAYS                           HOSTS                                      AGE
canvas-vault   canvas-vault-hc-vs                                         ["components/component-gateway"]   ["canvas-vault-hc.ihc-dt2.cluster-3.de"]   58m
canvas-vault   canvas-vault-landing-page-vs                               ["components/component-gateway"]   ["canvas-vault-hc.ihc-dt2.cluster-3.de"]   58m
canvas         canvas-info-vs                                             ["components/component-gateway"]   ["canvas-info.ihc-dt2.cluster-3.de"]       58m
canvas         canvas-keycloak-vs                                         ["components/component-gateway"]   ["canvas-keycloak.ihc-dt2.cluster-3.de"]   58m
components     demo-a-productcatalogmanagement-metrics                    ["component-gateway"]              ["components.ihc-dt2.cluster-3.de"]        12s
components     demo-a-productcatalogmanagement-partyrole                  ["component-gateway"]              ["components.ihc-dt2.cluster-3.de"]        12s
components     demo-a-productcatalogmanagement-productcatalogmanagement   ["component-gateway"]              ["components.ihc-dt2.cluster-3.de"]        13s
echoservice    echoservice-vs                                             ["components/component-gateway"]   ["echoservice.ihc-dt2.cluster-3.de"]       55m
grafana        grafana-vs                                                 ["components/component-gateway"]   ["grafana.ihc-dt2.cluster-3.de"]           57m

C:\Users\A307131\git\oda-canvas>kubectl get vs -A
NAMESPACE      NAME                                                       GATEWAYS                           HOSTS                                      AGE
canvas-vault   canvas-vault-hc-vs                                         ["components/component-gateway"]   ["canvas-vault-hc.ihc-dt2.cluster-3.de"]   59m
canvas-vault   canvas-vault-landing-page-vs                               ["components/component-gateway"]   ["canvas-vault-hc.ihc-dt2.cluster-3.de"]   59m
canvas         canvas-info-vs                                             ["components/component-gateway"]   ["canvas-info.ihc-dt2.cluster-3.de"]       59m
canvas         canvas-keycloak-vs                                         ["components/component-gateway"]   ["canvas-keycloak.ihc-dt2.cluster-3.de"]   59m
components     demo-a-productcatalogmanagement-metrics                    ["component-gateway"]              ["components.ihc-dt2.cluster-3.de"]        67s
components     demo-a-productcatalogmanagement-partyrole                  ["component-gateway"]              ["components.ihc-dt2.cluster-3.de"]        67s
components     demo-a-productcatalogmanagement-productcatalogmanagement   ["component-gateway"]              ["components.ihc-dt2.cluster-3.de"]        68s
echoservice    echoservice-vs                                             ["components/component-gateway"]   ["echoservice.ihc-dt2.cluster-3.de"]       56m
grafana        grafana-vs                                                 ["components/component-gateway"]   ["grafana.ihc-dt2.cluster-3.de"]           58m

C:\Users\A307131\git\oda-canvas>kubectl get components -A
NAMESPACE    NAME                              DEPLOYMENT_STATUS
components   demo-a-productcatalogmanagement   In-Progress-CompCon

C:\Users\A307131\git\oda-canvas>kubectl get components -A
NAMESPACE    NAME                              DEPLOYMENT_STATUS
components   demo-a-productcatalogmanagement   In-Progress-CompCon

C:\Users\A307131\git\oda-canvas>kubectl get exposedapis -A
NAMESPACE    NAME                                                       API_ENDPOINT                                                                                                  IMPLEMENTATION_READY
components   demo-a-productcatalogmanagement-metrics                    https://components.ihc-dt2.cluster-3.de/demo-a-productcatalogmanagement/metrics                               true
components   demo-a-productcatalogmanagement-partyrole                  https://components.ihc-dt2.cluster-3.de/demo-a-productcatalogmanagement/tmf-api/partyRoleManagement/v4
components   demo-a-productcatalogmanagement-productcatalogmanagement   https://components.ihc-dt2.cluster-3.de/demo-a-productcatalogmanagement/tmf-api/productCatalogManagement/v4

C:\Users\A307131\git\oda-canvas>kubectl get exposedapis -A
NAMESPACE    NAME                                                       API_ENDPOINT                                                                                                  IMPLEMENTATION_READY
components   demo-a-productcatalogmanagement-metrics                    https://components.ihc-dt2.cluster-3.de/demo-a-productcatalogmanagement/metrics                               true
components   demo-a-productcatalogmanagement-partyrole                  https://components.ihc-dt2.cluster-3.de/demo-a-productcatalogmanagement/tmf-api/partyRoleManagement/v4
components   demo-a-productcatalogmanagement-productcatalogmanagement   https://components.ihc-dt2.cluster-3.de/demo-a-productcatalogmanagement/tmf-api/productCatalogManagement/v4

C:\Users\A307131\git\oda-canvas>kubectl get exposedapis -A
NAMESPACE    NAME                                                       API_ENDPOINT                                                                                                  IMPLEMENTATION_READY
components   demo-a-productcatalogmanagement-metrics                    https://components.ihc-dt2.cluster-3.de/demo-a-productcatalogmanagement/metrics                               true
components   demo-a-productcatalogmanagement-partyrole                  https://components.ihc-dt2.cluster-3.de/demo-a-productcatalogmanagement/tmf-api/partyRoleManagement/v4
components   demo-a-productcatalogmanagement-productcatalogmanagement   https://components.ihc-dt2.cluster-3.de/demo-a-productcatalogmanagement/tmf-api/productCatalogManagement/v4

C:\Users\A307131\git\oda-canvas>kubectl get exposedapis -A
NAMESPACE    NAME                                                       API_ENDPOINT                                                                                                  IMPLEMENTATION_READY
components   demo-a-productcatalogmanagement-metrics                    https://components.ihc-dt2.cluster-3.de/demo-a-productcatalogmanagement/metrics                               true
components   demo-a-productcatalogmanagement-partyrole                  https://components.ihc-dt2.cluster-3.de/demo-a-productcatalogmanagement/tmf-api/partyRoleManagement/v4        true
components   demo-a-productcatalogmanagement-productcatalogmanagement   https://components.ihc-dt2.cluster-3.de/demo-a-productcatalogmanagement/tmf-api/productCatalogManagement/v4   true

C:\Users\A307131\git\oda-canvas>kubectl get components -A
NAMESPACE    NAME                              DEPLOYMENT_STATUS
components   demo-a-productcatalogmanagement   Complete

C:\Users\A307131\git\oda-canvas>cd ..\oda-canvas-notes\tests\oauth2

C:\Users\A307131\git\oda-canvas-notes\tests\oauth2>cd ihc-dt2

C:\Users\A307131\git\oda-canvas-notes\tests\oauth2\ihc-dt2>dir
 Volume in drive C is Windows
 Volume Serial Number is 84F7-F92B

 Directory of C:\Users\A307131\git\oda-canvas-notes\tests\oauth2\ihc-dt2

25.11.2024  12:56    <DIR>          .
25.11.2024  12:48    <DIR>          ..
25.11.2024  12:58               530 envoy-sds-secrets.yaml
25.11.2024  11:52             3.202 envoyfilter-oauth2-clientcred.yaml
25.11.2024  12:50             3.437 patched-istio-ingress-deployment.yaml
25.11.2024  12:57            41.022 README.md
               4 File(s)         48.191 bytes
               2 Dir(s)  723.579.551.744 bytes free

C:\Users\A307131\git\oda-canvas-notes\tests\oauth2\ihc-dt2>kubectl apply -f envoy-sds-secrets.yaml
configmap/oauth2secs-cm configured

C:\Users\A307131\git\oda-canvas-notes\tests\oauth2\ihc-dt2>kubectl rollout restart deployment -n istio-ingress istio-ingress
deployment.apps/istio-ingress restarted

C:\Users\A307131\git\oda-canvas-notes\tests\oauth2\ihc-dt2>kubectl get pods -n istio-ingress
NAME                             READY   STATUS    RESTARTS   AGE
istio-ingress-697db6fdb6-fszf7   1/1     Running   0          10s

C:\Users\A307131\git\oda-canvas-notes\tests\oauth2\ihc-dt2>kubectl get pods -n echoservice
NAME                                     READY   STATUS    RESTARTS   AGE
echoservice-deployment-55ff77858-qt85k   1/1     Running   0          62m

C:\Users\A307131\git\oda-canvas-notes\tests\oauth2\ihc-dt2>kubectl apply -f envoyfilter-oauth2-clientcred.yaml
Warning: EnvoyFilter exposes internal implementation details that may change at any time. Prefer other APIs if possible, and exercise extreme caution, especially around upgrades.
envoyfilter.networking.istio.io/envoyfilter-oauth2-test created

C:\Users\A307131\git\oda-canvas-notes\tests\oauth2\ihc-dt2>curl https://echoservice.ihc-dt2.cluster-3.de/ip
Failed to inject credential.
C:\Users\A307131\git\oda-canvas-notes\tests\oauth2\ihc-dt2>kubectl label namespace echoservice istio-injection=enabled
namespace/echoservice labeled

C:\Users\A307131\git\oda-canvas-notes\tests\oauth2\ihc-dt2>kubectl rollout restart deployment -n echoservice echoservice-deployment
deployment.apps/echoservice-deployment restarted

C:\Users\A307131\git\oda-canvas-notes\tests\oauth2\ihc-dt2>copy con: NUL
2024-11-25T12:04:13.701559Z     error   envoy credential_injector external/envoy/source/extensions/http/injected_credentials/oauth2/token_provider.cc:111       onGetAccessTokenFailure: Failed to get access token     thread=13
2024-11-25T12:04:13.813561Z     error   envoy credential_injector external/envoy/source/extensions/http/injected_credentials/oauth2/oauth_client.cc:74  Oauth response code: 401        thread=13
2024-11-25T12:04:13.813600Z     error   envoy credential_injector external/envoy/source/extensions/http/injected_credentials/oauth2/oauth_client.cc:75  Oauth response body: {"error":"unauthorized_client","error_description":"Client not enabled to retrieve service account"}       thread=13
2024-11-25T12:04:13.813605Z     error   envoy credential_injector external/envoy/source/extensions/http/injected_credentials/oauth2/token_provider.cc:111       onGetAccessTokenFailure: Failed to get access token     thread=13
^Z
        1 file(s) copied.

C:\Users\A307131\git\oda-canvas-notes\tests\oauth2\ihc-dt2>REM kubectl logs -n istio-ingress deployment/istio-ingress

C:\Users\A307131\git\oda-canvas-notes\tests\oauth2\ihc-dt2>kubectl delete -f envoyfilter-oauth2-clientcred.yaml
envoyfilter.networking.istio.io "envoyfilter-oauth2-test" deleted

C:\Users\A307131\git\oda-canvas-notes\tests\oauth2\ihc-dt2>echo "Activate Service account roles in myrealm/client=demo-a-productcatalog
"Activate Service account roles in myrealm/client=demo-a-productcatalog

C:\Users\A307131\git\oda-canvas-notes\tests\oauth2\ihc-dt2>kubectl apply -f envoyfilter-oauth2-clientcred.yaml
Warning: EnvoyFilter exposes internal implementation details that may change at any time. Prefer other APIs if possible, and exercise extreme caution, especially around upgrades.
envoyfilter.networking.istio.io/envoyfilter-oauth2-test created

C:\Users\A307131\git\oda-canvas-notes\tests\oauth2\ihc-dt2>curl https://echoservice.ihc-dt2.cluster-3.de/ip
<h3 style="background-color: green;">log request ip infos</h3><b>client-ip:</b> 127.0.0.6<br><b>header:</b><br><pre><code>Host: echoservice.ihc-dt2.cluster-3.de
User-Agent: curl/8.9.1
Accept: */*
X-Forwarded-For: 10.64.0.1
X-Request-Id: e9122bd8-f707-4e3f-862a-100c51afeec7
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJyUVEwV0tsUU1UNi1Dc1pnSTZrSldxSURfNlR2ZTlaU01oQlVULWM4c05RIn0.eyJleHAiOjE3MzI1MzY4NjYsImlhdCI6MTczMjUzNjU2NiwianRpIjoiMDU0OGRmYTktYWNlNi00OWYzLTllMDAtYjU4ZTdhOWE5MGNlIiwiaXNzIjoiaHR0cDovL2NhbnZhcy1rZXljbG9hay5jYW52YXMuc3ZjLmNsdXN0ZXIubG9jYWwvYXV0aC9yZWFsbXMvbXlyZWFsbSIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiIwY2U0YzQ0ZC1iOTc3LTQwMjMtOGQ5NS05NGU3OTU0YTNkMDkiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJkZW1vLWEtcHJvZHVjdGNhdGFsb2dtYW5hZ2VtZW50IiwiYWNyIjoiMSIsInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJkZWZhdWx0LXJvbGVzLW15cmVhbG0iLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJwcm9maWxlIGVtYWlsIiwiY2xpZW50SWQiOiJkZW1vLWEtcHJvZHVjdGNhdGFsb2dtYW5hZ2VtZW50IiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJjbGllbnRIb3N0IjoiMTAuNjQuMC4xMTIiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJzZXJ2aWNlLWFjY291bnQtZGVtby1hLXByb2R1Y3RjYXRhbG9nbWFuYWdlbWVudCIsImNsaWVudEFkZHJlc3MiOiIxMC42NC4wLjExMiJ9.dAvjgJ68sLCSo9A-Y1Xfu6nlS8iuSYGuI3Nnz5m9AKgV3lAJBSxyLubP9FMKtvHW57rRz8xkZFcbLpGPzd_7ZMmygqvh88ZWyG3GxT-WIpIYkE62L06AnULJUmL4hUTg1rAausGZOLybxazelJO65UijTjaNKZzzAYUkZzTUhjOtGH8X3Qtk_nfxYkydrkfqik-C-VZIeHzLKNca4lwYDnHYWqTc0uaLhxDHDLRQ7KEV_XtYMEZ8N4ftf7Mzg1TJUsrvBCAar9Ye5TlEiFcRSRhOqp5m4d0qDAG7rWbyGjcjdU_nrt2958GnDxoCDOrpqjTVsSmYum_qPT-YYNk_Dg
X-Envoy-Attempt-Count: 1
X-Forwarded-Proto: https
X-Envoy-Internal: true
X-Forwarded-Client-Cert: By=spiffe://cluster.local/ns/echoservice/sa/default;Hash=7c1f2958dacdca6c08aac685120fcd6ef8b8650b2aea72996ad3f17a2aca357c;Subject="";URI=spiffe://cluster.local/ns/istio-ingress/sa/istio-ingress

</code></pre><ul><li><a href='/'>ROOT</a><li><a href='/hello'>hello</a><li><a href='/ip'>ip</a></ul>
C:\Users\A307131\git\oda-canvas-notes\tests\oauth2\ihc-dt2>cd ..

C:\Users\A307131\git\oda-canvas-notes\tests\oauth2>cd ..

C:\Users\A307131\git\oda-canvas-notes\tests>cd ..

C:\Users\A307131\git\oda-canvas-notes>cd apps

C:\Users\A307131\git\oda-canvas-notes\apps>dir
 Volume in drive C is Windows
 Volume Serial Number is 84F7-F92B

 Directory of C:\Users\A307131\git\oda-canvas-notes\apps

21.11.2024  23:20    <DIR>          .
21.11.2024  23:58    <DIR>          ..
21.11.2024  23:36    <DIR>          echoservice
               0 File(s)              0 bytes
               3 Dir(s)  723.583.184.896 bytes free

C:\Users\A307131\git\oda-canvas-notes\apps>cd echoservice

C:\Users\A307131\git\oda-canvas-notes\apps\echoservice>kubectl delete -f k8s\echoservice-deployment.yaml
deployment.apps "echoservice-deployment" deleted

C:\Users\A307131\git\oda-canvas-notes\apps\echoservice>kubectl delete -f k8s\
namespace "echoservice" deleted
service "echoservice" deleted
virtualservice.networking.istio.io "echoservice-vs" deleted
Error from server (NotFound): error when deleting "k8s\\echoservice-deployment.yaml": deployments.apps "echoservice-deployment" not found

C:\Users\A307131\git\oda-canvas-notes\apps\echoservice>kubectl delete ns echoservice
namespace "echoservice" deleted

C:\Users\A307131\git\oda-canvas-notes\apps\echoservice>cd k8s

C:\Users\A307131\git\oda-canvas-notes\apps\echoservice\k8s>kubectl apply -f .
namespace/echoservice created
service/echoservice created
virtualservice.networking.istio.io/echoservice-vs created
Error from server (NotFound): error when creating "echoservice-deployment.yaml": namespaces "echoservice" not found

C:\Users\A307131\git\oda-canvas-notes\apps\echoservice\k8s>kubectl apply -f .
deployment.apps/echoservice-deployment created
namespace/echoservice unchanged
service/echoservice unchanged
virtualservice.networking.istio.io/echoservice-vs unchanged

C:\Users\A307131\git\oda-canvas-notes\apps\echoservice\k8s>kubectl apply -f ihc-dt2
virtualservice.networking.istio.io/echoservice-vs configured

```