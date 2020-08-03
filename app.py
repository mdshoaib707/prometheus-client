import urllib.request
import ssl
import requests

import time
from flask import Flask, render_template_string, abort
from flask import request
from prometheus_client import generate_latest, REGISTRY, Counter, Histogram, Summary, CollectorRegistry, Gauge


app = Flask(__name__)

URLSTATUS = Gauge('sample_external_url_up', 'URL_UP', ['url'])
RESPONSETIME = Histogram('sample_external_url_response_ms', 'External URL Response', ['url'], buckets=[500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000])


@app.route('/')
def index():
    return "App is up and running!"

@app.route('/metrics')
def metrics():

    for uri in ("200", "502"):
        url1 = "https://httpstat.us/" + uri
        response = requests.get(url1, timeout=5)

        responseMilliSecs = 1000 * response.elapsed.total_seconds()
        responseStatusCode = response.status_code

        if int(responseStatusCode) in range(200, 399):
            URLSTATUS.labels(url=url1).set(1)
            RESPONSETIME.labels(url=url1).observe(responseMilliSecs)
        else:
            URLSTATUS.labels(url=url1).set(0)
            RESPONSETIME.labels(url=url1).observe(responseMilliSecs)


    return generate_latest(REGISTRY)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

