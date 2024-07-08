#!/bin/sh

# create own namespace for running the tests
kubectl create ns canvas-tests --dry-run=client -oyaml | kubectl apply -f -

# create serviceaccount which will be granted cluster-admin permissions
kubectl create serviceaccount -n canvas-tests sa-canvas-tests --dry-run=client -oyaml | kubectl apply -f -
kubectl create clusterrolebinding canvas-tests-cluster-admin-rb --clusterrole=cluster-admin --serviceaccount=canvas-tests:sa-canvas-tests --dry-run=client -oyaml | kubectl apply -f -

# remove old testrun
kubectl delete pod --ignore-not-found=true -n canvas-tests canvas-tests

# run tests, option -it waits until the POD is finished
kubectl run -it -n canvas-tests canvas-tests --image=mtr.devops.telekom.de/magenta_canvas/public:canvas-ctk --overrides='{"spec":{"serviceAccount":"sa-canvas-tests"}}' --restart=Never

# look, how many passed tests there have been
kubectl logs -n canvas-tests canvas-tests | grep "passed"
