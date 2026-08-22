import requests
import time

url = "http://localhost:5000/submit"

max_retries = 4

for attempt in range(1, max_retries + 1):
    try:
        response = requests.post(url, timeout=1)

        print(f"Attempt {attempt}: {response.status_code}")

        if response.status_code == 200:
            print(response.text)
            break

        if response.status_code == 503:
            print("Temporary failure.")

    except requests.exceptions.Timeout:
        print(f"Attempt {attempt}: Request timed out.")

    except requests.exceptions.ConnectionError:
        print(f"Attempt {attempt}: Connection error.")

    if attempt < max_retries:
        delay = 2 ** (attempt - 1)
        print(f"Waiting {delay} seconds before retry...")
        time.sleep(delay)

else:
    print("All retry attempts failed.")
