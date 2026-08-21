"""
Flaky test server for Assignment 1 (retry/backoff prototype).

This is scaffolding, not the assignment — you're not being evaluated on this
file. It exists so you have something realistically unreliable to build
retry logic against, the same way a real third-party API would occasionally
time out or return a 503.
"""

from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

FAILURE_RATE = 0.8   # ~80% of requests fail, on purpose
SLOW_DELAY = 2.5      # some of those failures are slow, not just wrong


@app.route("/submit", methods=["POST"])
def submit():
    if random.random() < FAILURE_RATE:
        if random.random() < 0.5:
            time.sleep(SLOW_DELAY)  # simulate a hanging request
        return jsonify({"status": "error", "message": "service temporarily unavailable"}), 503

    return jsonify({"status": "ok", "message": "accepted"}), 200


if __name__ == "__main__":
    app.run(port=5000, debug=True)
