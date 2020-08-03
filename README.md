#Prometheus Client using Python

Steps to deploy and observe the metrics in prometheus, grafana using Python client library
The main code is written in the file "app.py". It runs on 5000 port. In this file we are using Gauge and Histogram. Gauge is used whether the site is up or not. Like it will be either 1 or 0. Histogram is used to collect the response time which we got for accessing the external urls.

To run the application, type in the command <br />
`python3 app.py`

To test the application, type in the command <br />
`python3 test_app.py`

Once the application is running we will get the metrics in "/metrics" as seen in the below screenshot. <br />

![header image](https://github.com/mdshoaib707/prometheus-client/blob/develop/screenshots/app-metrics.png)

<br />
Now we will see how to build and deploy the application.

<br />
Build and push the app <br />

cd to the root of this repo. <br />

```
cd prometheus-client/
docker build -t mdshoaib707/prometheus-client:1.2 .
docker push mdshoaib707/prometheus-client:1.2
```

Helm version used is helm3.
Deploy Prometheus, Grafana in the k8s cluster
```
cd prometheus-client/ci/prometheus-deploy/
sh helm.sh
```
The script will deploy prometheus, grafana, alert manager in the cluster using the values.yml file. We have added the scrap config for our python app to collect metrics from. It is mentioned here https://github.com/mdshoaib707/prometheus-client/blob/develop/ci/prometheus-deploy/values.yml#L1874-L1876. The "static_configs" is where our python app is running. This will deploy under `monitoring` namespace. <br />

Deploy the python app in cluster.
```
cd prometheus-client/ci/
helm upgrade --install myapp --namespace app myapp --debug
```
This will deploy the app under `app` namespace. <br />

Once our app is deployed we can see the metrics in prometheus as below. <br />

![header image](https://github.com/mdshoaib707/prometheus-client/blob/develop/screenshots/sample-url-up-prometheus.png)
![header image](https://github.com/mdshoaib707/prometheus-client/blob/develop/screenshots/prometheus-metrics.png)
![header image](https://github.com/mdshoaib707/prometheus-client/blob/develop/screenshots/prometheus-all-metrics.png)


<br /><h3><b>We can see the average response time in milliseconds by using the following formula.</b></h3><br />
![header image](https://github.com/mdshoaib707/prometheus-client/blob/develop/screenshots/average-response-duration.png)
![header image](https://github.com/mdshoaib707/prometheus-client/blob/develop/screenshots/average-response-5m-msec.png)

<br /><h3><b>To check the 95 percentile of the metrics use the below formula.</b></h3><br />
![header image](https://github.com/mdshoaib707/prometheus-client/blob/develop/screenshots/percent-95-quantile.png)
