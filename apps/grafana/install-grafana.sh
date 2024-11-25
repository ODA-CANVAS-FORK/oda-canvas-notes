#!/bin/bash

set -xev
cd $(dirname -- $0)

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm upgrade --install kube-prometheus-stack --namespace grafana --create-namespace prometheus-community/kube-prometheus-stack

kubectl apply -f virtualservice/grafana-vs.yaml
