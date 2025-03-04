kubectl delete -f demo-b-envoyfilter-oauth2.yaml
kubectl apply -f envoy-oath2-secrets.yaml

kubectl rollout restart deployment -n istio-system istiod
kubectl rollout restart deployment -n istio-ingress istio-ingress
kubectl rollout restart deployment -n components demo-b-prodcatapi

echo wating 1 minute
sleep 60

kubectl apply -f demo-b-envoyfilter-oauth2.yaml
