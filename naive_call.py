"""
Step 1: a single, un-retried call. No retry logic here — that's the point.
Run flaky_server.py first, then run this against it.
"""
import requests

url = "http://localhost:5000/submit"

max_retries = 3

for attempt in range(1, max_retries + 1):
    try:
        response = requests.post(url, timeout=1)

        print(f"Attempt {attempt}: {response.status_code}")

        if response.status_code == 200:
            print(response.text)
            break

        if response.status_code == 503:
            print("Temporary failure. Retrying...")

    except requests.exceptions.Timeout:
        print(f"Attempt {attempt}: Request timed out. Retrying...")

    except requests.exceptions.ConnectionError:
        print(f"Attempt {attempt}: Connection error. Retrying...")

else:
    print("All retry attempts failed.")