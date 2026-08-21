# Retry/Backoff Prototype — Assignment 1

Solo mini-prototype for Days 1–2: learning retry/backoff, unaided. No teammate/instructor how-to help on the retry logic itself — that's the whole point of this one.

## What's in here
- `flaky_server.py` — a small Flask server that fails on purpose, at random. This is your test target, not the thing you're learning. It's scaffolding, provided so you have something realistic to retry against.
- `naive_call.py` — one plain, un-retried request. Run this first and watch it fail.
- `retry_client.py` — empty. This is yours to build once you've researched retry/backoff on your own.
- `BLOCKER_JOURNAL.md` — template only. Real entries, written as you go.
- `requirements.txt` — flask + requests.

## Setup
```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Step 1 — watch it fail
Terminal 1:
```bash
python flaky_server.py
```
Terminal 2:
```bash
python naive_call.py
```
It fails about 80% of the time, so run it a few times if you happen to get a success. Whatever you actually see — status code, error message, how long it hung — write it up as Entry 1 in `BLOCKER_JOURNAL.md`, in your own words.

## Step 2 — on your own from here
Research retry/backoff however you'd normally research something unfamiliar, then build `retry_client.py` against the same `/submit` endpoint. Log real blockers in the journal as they happen, not reconstructed afterward.

## Git setup
```bash
git init
git add .
git commit -m "scaffold: flaky server, journal template"
git remote add origin <your-repo-url>
git push -u origin main
```
Commit again after each journal entry — don't batch them at the end. The timestamps are part of what makes this count as evidence of real, unaided work.

## One rubric note
Time-boxed and honest beats polished here — 40% of this grade is troubleshooting autonomy and documentation, not a shiny final script. Don't sink hours into making `retry_client.py` pretty.
