#!/bin/sh

set -xev

cd $(dirname -- $0)

GIT_COMMIT_SHA=$(git rev-parse --short HEAD)
NOW=$(date -Iseconds)
      
cd ../../source/operators
docker build -t mtr.devops.telekom.de/magenta_canvas/public:component-istio-controller-0.4.2-sman \
	--build-arg "GIT_COMMIT_SHA=$GIT_COMMIT_SHA" \
    --build-arg "CICD_BUILD_TIME=$NOW" \
    --build-arg http_proxy=$http_proxy \
    --build-arg https_proxy=$https_proxy \
    --build-arg no_proxy=$no_proxy \
	-f component-IstioController-dockerfile .
docker push mtr.devops.telekom.de/magenta_canvas/public:component-istio-controller-0.4.2-sman

kubectl rollout restart deployment -n canvas oda-controller-ingress || true
