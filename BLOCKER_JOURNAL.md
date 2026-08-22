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


# Entry 5- constant vd exponential backoff investigation for recovery before next attempt— 22/8/2026 5:40 AM SAST

**Attempted:After I implemented retries, I noticed that the program would retry immediately when the server returned a 503 error. Although the retry worked and the request could eventually become successful, I realised that immediately sending another request to a server that is already failing may not be a good approach.**

**What I understood:delay only happens if the first attemot fails, and helps give the server some time to recover, instead of immediately sending another request**

**Fix: I implemented exponential backoff where the waiting time increases after each failed attempt:1 second → 2 seconds → 4 seconds. The client now allows up to four attempts**

**Result:retries and exponential backoff worked successfully, helping client recover from temporary failures, I tested the program and it retried up to four times when necessary. When one of the attempts succeeded, the program stopped and returned the successful response. If all 4 attempts failed, it printed that all retry attempts had failed.**

**Resolution / next step: Test the complete retry, timeout and exponential backoff behaviour**
<!-- Copy the block above for each new entry. Commit after each one — the
     commit timestamps are part of what makes this journal count as evidence
     of real, unaided work rather than a write-up done after the fact. -->
