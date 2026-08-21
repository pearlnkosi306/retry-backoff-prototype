"""
Step 1: a single, un-retried call. No retry logic here — that's the point.
Run flaky_server.py first, then run this against it.
"""
import requests

response = requests.post("http://localhost:5000/submit")
print(response.status_code, response.text)
