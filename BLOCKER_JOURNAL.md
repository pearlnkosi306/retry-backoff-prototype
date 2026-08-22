# Blocker Journal — Retry/Backoff Prototype

# Entry 1 —Ran Server- 22/8/2026 1:57 AM SAST
**Attempted: to ran the server on file flaky_server.py**

**Result:server stated on port 5000, opening the forwarded port in the browserm produced 404 Not Found, the terminal showed Get/HTTP/101 request with a 404 responce**

**what i understand:The server is running and responds to HTTP requests, but the root or route does not exist**

**Resources consulted: GitHub Codespace terminal, Chrome Browser**

**Resolution / next step:investigating naive_call.py and observe its responce**

# Entry 2- Naive Call Failure — 22/8/2026 2:32AM SAST
**Attempted:ran python3 naive_call.py while flaky_server.py was running**

**Result:connection error, the program produced a python trace back with many lines referencing failed connection attempts, such as "ConnectionError" and "Connection Refused" and an inability to establish connectio**

**Main Observatons:the client is unable to establish a new connection**

**what i understand:naive_call.py attempted to make a connection, but was refused**

**What i dont understand: why it failed** 

**Resolution / next step: Investigate connection refused error, determine how the naive_call.py communicates with the flaky server**


# Entry 3- Connection Failed Error  — 22/8/2026 4:10 AM SAST
**Attempted:the flask server is reacheable but the server defines the /submit as a {POST} endpoint, not as a root(/) endpoint**

**Result:connection error, Evidence: flaky_server.py defines @app.route('/submit', methods=['POST']).**

**Main Observatons:at the time client was executed, no server process was listening on local port:5000 hence is unable to establish a connection**

**what i understand:naive_call.py attempted to make a connection, but was refused. After flaky_server.py was started, Flask reported that it was running on http://127.0.0.1:5000. The server therefore started successfully and was listening on port 5000.**

**What i dont understand: how to resolve it** 

**Resolution / next step: learn how to fix connection refused error**


# Entry 4- Timeout investigation — 22/8/2026 5:09 AM SAST
**Attempted:ran the call 8 times and connection refused, with slow responce, takes about 3 seconds**

**Result:slow responce, theres a need for time out**

**Main Observatons:asimulated failures deliberately pause for 2.5 seconds before returning HTTP 503**

**Fix:I added a 1-second timeout to the requests.post() call:response = requests.post("http://localhost:5000/submit",timeout=1)**

**Results:The timeout changes the behaviour of the client. A normal response that arrives within the one-second limit can still produce HTTP 200 or 503.** 

**Resolution / next step: Investigate retry behaviour**

# Entry 5- Retry investigation — 22/8/2026 5:25 AM SAST
**Attempted:the client still stopped after a temporary HTTP 503 or timeout. Instead of allowing the client to stop after the first failure, I implemented a maximum of three attempts**

**Fix: I changed the client to retry when it receives HTTP 503, encounters a timeout, or encounters a connection error. The client stops immediately when it receives HTTP 200, until status reflects 'ok', message says ; accepted**

**Result:retries until accepted,, helping client recover from temporary failures**

**Resolution / next step: Implement a delay between retry attempts using exponential backoff.**


# Entry 6- constant vd exponential backoff investigation for recovery before next attempt— 22/8/2026 5:40 AM SAST

**Attempted:After I implemented retries, I noticed that the program would retry immediately when the server returned a 503 error. Although the retry worked and the request could eventually become successful, I realised that immediately sending another request to a server that is already failing may not be a good approach.**

**What I understood:delay only happens if the first attemot fails, and helps give the server some time to recover, instead of immediately sending another request**

**Fix: I implemented exponential backoff where the waiting time increases after each failed attempt:1 second → 2 seconds → 4 seconds. The client now allows up to four attempts**

**Result:Retries and exponential backoff worked successfully. The client was able to recover from temporary failures by retrying the request and increasing the waiting time between attempts. I tested the program multiple times and the requests were successfully completed. When the maximum number of attempts was reached without success, the program reported that all retry attempts had failed.**

**Resolution / next step: Test the complete retry, timeout and exponential backoff behaviour**

# Entry 7 - Final Test Results — 22/08/2026 5:52 AM SAST

**Progress: I ran the complete program 6 times and observed the different possible outcomes from the retry system.**

**Final Test Results: The complete retry system worked successfully. The client was able to retry failed requests using exponential backoff and eventually receive a successful response. When the maximum number of attempts was reached without success, the program correctly reported that the request had failed. This confirmed that the timeout, retry, and exponential backoff mechanisms were working together as intended.**

**What I understood: I now understand how the three mechanisms work together. The timeout prevents the client from waiting too long, retry allows the client to try again after a temporary failure, and exponential backoff increases the waiting time between retries to give the server time to recover.**
# Entry 8 — Warehouse API Setup — 22/08/2026 10:16 AM SAST

**Problem:** I needed to create and run the warehouse API so that the inventory service could poll it every 5 minutes. I was not sure at first if the warehouse API was working correctly.

**What I tried:** I started `warehouse_api.py` and checked the `/inventory` endpoint.

**Result:** The warehouse API started successfully on port 5001. The `/inventory` endpoint returned the inventory data successfully, including SKU001 = 42, SKU002 = 0, SKU003 = 17, SKU004 = 8 and SKU005 = 103.

**What I learned:** I confirmed that the warehouse API was working and that the inventory service had a real endpoint to poll. The 404 on `/` was not a problem because the endpoint I needed was `/inventory`.

**Resolution / next step:** Continue with the inventory service and use the warehouse `/inventory` endpoint as the source for the cache.

