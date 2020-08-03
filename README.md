Prometheus-client using Python
Prometheus Client python

Steps to deploy and observe the metrics in prometheus, grafana using Python client library
The main code is written in the file "app.py". It runs on 5000 port. In this file we are using Gauge and Histogram. Gauge is used whether the site is up or not. Like it will be either 1 or 0. Histogram is used to collect the response time which we got for accessing the external urls.

To run the application, type in the command
`python3 app.py`

