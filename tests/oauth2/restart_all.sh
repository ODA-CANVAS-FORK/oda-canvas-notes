kubectl delete -f envoyfilter-oauth2-clientcred.yaml
kubectl apply -f envoy-sds-secrets.yaml

kubectl rollout restart deployment -n istio-system istiod
kubectl rollout restart deployment -n istio-ingress istio-ingress
kubectl rollout restart deployment -n echoservice echoservice-deployment

sleep 60
kubectl apply -f envoyfilter-oauth2-clientcred.yaml
