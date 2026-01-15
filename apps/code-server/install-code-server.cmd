cd %~dp0

if "%CODE_SERVER_PASSWORD%" == "" (
    echo "Please set the CODE_SERVER_PASSWORD environment variable."
    exit /b 1
)

if "%DOMAIN%" == "" (
    echo "Please set the DOMAIN environment variable."
    exit /b 1
)

kubectl create ns code-server 
kubectl create secret generic -n code-server code-server-secret --from-literal=password="%CODE_SERVER_PASSWORD%" --dry-run=client -oyaml | kubectl apply -f - 

rmdir /S/Q code-server-repo
git clone https://github.com/coder/code-server code-server-repo
cd code-server-repo
helm upgrade --install -n code-server --create-namespace code-server --set existingSecret=code-server-secret ci/helm-chart ^
    --set image.repository=ocfork/code-server ^
    --set image.tag=v4.95.3-with-helm-and-node
cd ..

kubectl create clusterrolebinding code-server-cluster-admin-rb --clusterrole=cluster-admin --serviceaccount=code-server:code-server --dry-run=client -oyaml | kubectl apply -f -

echo "DOMAIN is %DOMAIN%"

helm upgrade --install code-server-vs -n code-server virtualservice --set=domain=%DOMAIN%
