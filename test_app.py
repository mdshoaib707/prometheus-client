import unittest

import time
from flask import Flask, render_template_string, abort
from flask import request
from prometheus_client import generate_latest, REGISTRY, Counter, Histogram, Summary, CollectorRegistry, Gauge

import app
import math

class TestMetrics(unittest.TestCase):
    def test_index(self):
        outputstr = "App is up and running!"
        self.assertEqual(outputstr, outputstr, "Should be App is up and running!")

    def setUp(self):
        app.metrics()
        self.registry = REGISTRY


    def test_working(self):
        
        app.metrics()
        self.registry.collect()

        self.assertEqual(1, self.registry.get_sample_value(
            'sample_external_url_up', labels={"url": "https://httpstat.us/200"}
        ))
        
        self.assertEqual(0, self.registry.get_sample_value(
            'sample_external_url_up', labels={"url": "https://httpstat.us/502"}
        ))


    def tearDown(self):
        app.metrics()



if __name__ == '__main__':
    unittest.main()

