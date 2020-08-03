kubectl create ns monitoring
helm repo add stable https://kubernetes-charts.storage.googleapis.com
helm repo update
helm install prometheus-operator --namespace monitoring stable/prometheus-operator --debug
