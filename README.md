#Prometheus Client using Python

Steps to deploy and observe the metrics in prometheus, grafana using Python client library
The main code is written in the file "app.py". It runs on 5000 port. In this file we are using Gauge and Histogram. Gauge is used whether the site is up or not. Like it will be either 1 or 0. Histogram is used to collect the response time which we got for accessing the external urls.

To run the application, type in the command <br />
`python3 app.py`

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

Deploy Prometheus, Grafana in the k8s cluster
```
cd prometheus-client/ci/prometheus-deploy/
sh helm.sh
```
The script will deploy prometheus, grafana, alert manager in the cluster using the values.yml file. We have added the scrap config for our python app to collect metrics from. It is mentioned here https://github.com/mdshoaib707/prometheus-client/blob/develop/ci/prometheus-deploy/values.yml#L1874-L1876
