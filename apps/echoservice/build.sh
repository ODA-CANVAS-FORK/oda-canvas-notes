#!/bin/sh
docker build --build-arg=http_proxy=$http_proxy --build-arg=https_proxy=$https_proxy -t ocfork/echoservice:v0.1.1-rc .
docker tag ocfork/echoservice:v0.1.1-rc ocfork/echoservice:latest
docker push ocfork/echoservice:v0.1.1-rc
docker push ocfork/echoservice:latest
