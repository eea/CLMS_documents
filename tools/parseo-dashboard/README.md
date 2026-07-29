# parsEO Dashboard

Web-based dashboard for the parsEO CLMS Filename API.

## Setup

The parsEO API runs as a Docker container on **nucleus** at `http://nucleus:8000`.

```bash
cd ~/parseo-api
docker compose up -d
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/health` | GET | Health check |
| `/api/info` | GET | parsEO version info |
| `/api/families` | GET | List all schema families |
| `/api/families/{family}/versions` | GET | List schema versions |
| `/api/families/{family}/schemas/{version}` | GET | Get schema JSON |
| `/api/assemble` | POST | Assemble filename from fields |
| `/api/parse` | POST | Parse a filename into fields |
| `/api/validate` | POST | Validate a schema JSON |
| `/api/cache/clear` | POST | Clear parsEO cache |

## Usage

Open `dashboard.html` in a browser. Set the API URL to `http://nucleus:8000` (or the host where the API runs).

## Files

- `dashboard.html` — Single-page dashboard app (dark theme)
- `api.py` — FastAPI server (in `~/parseo-api/` on nucleus)
- `Dockerfile` — Docker build (in `~/parseo-api/`)
- `docker-compose.yml` — Run configuration (in `~/parseo-api/`)