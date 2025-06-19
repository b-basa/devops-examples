# nginx-htmx

Nginx takes any request to / or /api and redirects it to the backend container.
Backend container returns with html responses.

Nothing is served if backend does not respond (could be handled with failover pages).

## Usage

```bash
docker compose up -d
```