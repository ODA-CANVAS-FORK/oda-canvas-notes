#!/bin/bash

set -xev
cd $(dirname -- $0)

test -n "$CODE_SERVER_PASSWORD"

kubectl create ns code-server || true
	kubectl create secret generic -n code-server code-server-secret --from-literal=password="$CODE_SERVER_PASSWORD" --dry-run=client -oyaml | kubectl apply -f - 

rm -rf code-server-repo
git clone https://github.com/coder/code-server code-server-repo
cd code-server-repo
helm upgrade --install -n code-server --create-namespace code-server --set existingSecret=code-server-secret ci/helm-chart \
    --set image.repository=ocfork/code-server \
    --set image.tag=v4.95.3-with-helm-and-node
cd ..

kubectl create clusterrolebinding code-server-cluster-admin-rb --clusterrole=cluster-admin --serviceaccount=code-server:code-server --dry-run=client -oyaml | kubectl apply -f -

kubectl apply -f virtualservice/code-server-vs.yaml
