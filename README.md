# hello-web

A tiny single-page Flask site you can run like a Vite dev server.

## Quick start (local)

```bash
# 1) Create & activate a virtual env
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 2) Install package (editable) + dev tools
pip install -U pip
pip install -e ".[dev]"

# 3) Run the dev server (similar to: vite dev --host)
hello-web --host 0.0.0.0 --port 5173 --debug

# 4) Open your browser
# http://localhost:5173
```

## What you get

- `GET /` renders `templates/index.html` (with a tiny CSS file).
- `GET /api/hello` returns JSON: `{"message": "Hello from Flask!"}`

## Dev helpers

```bash
# Lint
ruff check .

# Tests
pytest

# Build wheel + sdist
python -m build
ls -l dist/
```

## Deploy note

The built-in Flask server is for development. For prod (optional), run
behind a WSGI/ASGI server like gunicorn/uvicorn or a reverse proxy.