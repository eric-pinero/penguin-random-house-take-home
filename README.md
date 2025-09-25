# Incident Tracker (take-home)

Simple Flask API for tracking incidents.

## Setup

Create and activate a virtual environment, then install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

Start the app (development server):

```bash
python3 run.py
```

The app runs on http://127.0.0.1:5000 by default.

## Smoke tests

From another shell (with the `.venv` activated) you can run basic smoke tests:

```bash
# List incidents (expect [] initially)
curl -s http://127.0.0.1:5000/incidents | jq

# Create an incident
curl -s -X POST http://127.0.0.1:5000/incidents \
  -H 'Content-Type: application/json' \
  -d '{"title":"Test","description":"testing"}' | jq

# Update status
curl -s -X PATCH http://127.0.0.1:5000/incidents/1 \
  -H 'Content-Type: application/json' \
  -d '{"status":"Resolved"}' | jq

# Delete
curl -s -X DELETE http://127.0.0.1:5000/incidents/1 -v
```
