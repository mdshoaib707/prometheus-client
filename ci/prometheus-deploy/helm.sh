#!/bin/bash

kubectl create ns app --dry-run=true -o yaml | kubectl apply -f -

helm repo add stable https://kubernetes-charts.storage.googleapis.com
helm repo update
helm upgrade --install prometheus-operator --values values.yml --namespace monitoring stable/prometheus-operator
