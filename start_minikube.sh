#!/usr/bin/env bash

minikube start --no-kubernetes \
--extra-config=apiserver.service-node-port-range=1-35000 \
--disk-size=5000mb \
--mount \
--mount-string="${PWD}:/data"