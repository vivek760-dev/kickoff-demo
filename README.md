# Kickoff Demo

A minimal Flask app demonstrating a Claude API call, a health check endpoint, a simple web UI, Docker packaging, and a CI workflow.

## Routes

- `GET /` — web UI (ask Claude a question, see live health status)
- `GET /health` — health check, returns `{"status": "ok"}`
- `POST /api/ask` — body `{"prompt": "..."}`, returns `{"response": "..."}`

## Local development

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=your-key
python app.py
```

Visit http://localhost:8080

## Docker

```bash
docker build -t kickoff-demo .
docker run -d -p 8080:8080 --env-file .env --name kickoff-demo kickoff-demo
curl http://localhost:8080/health
```

Create a local `.env` file (not committed — see `.gitignore`) with:

```
ANTHROPIC_API_KEY=your-key
```

## CI

`.github/workflows/demo.yml` runs on push/PR to `main`: installs dependencies, smoke-tests `/health`, builds the Docker image, and runs a container health check.

## Deploy

Deployed via manual SSH + Docker to a Hostinger VPS. See deployment notes for the exact steps (SSH in, install Docker, clone repo, set `.env`, `docker build` + `docker run`).
