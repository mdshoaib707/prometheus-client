#!/bin/bash

kubectl create ns app --dry-run=true -o yaml | kubectl apply -f -

helm repo add stable https://kubernetes-charts.storage.googleapis.com
helm repo update
helm install prometheus-operator --namespace monitoring stable/prometheus-operator --debug
