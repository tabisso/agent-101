# api/middleware.py

import time
from collections import defaultdict, deque

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse


class RateLimitMiddleware(BaseHTTPMiddleware):
    """
    Simple in-memory rate limiter (per IP).
    Notes:
      - Best for dev / small deployments.
      - With multiple workers (gunicorn -w > 1), limits are per-worker.
      - Skips static UI (/app) and FastAPI docs routes by default.
      - Ignores CORS preflight OPTIONS requests.
    """

    def __init__(self, app, requests_per_minute: int = 60):
        super().__init__(app)
        self.limit = int(requests_per_minute)
        self.window = 60.0  # seconds
        self.requests = defaultdict(deque)

        # Routes to skip (UI + docs)
        self.skip_prefixes = ("/app", "/docs", "/openapi", "/redoc")

    async def dispatch(self, request: Request, call_next):
        path = request.url.path

        # Skip static UI and docs endpoints
        if path.startswith(self.skip_prefixes):
            return await call_next(request)

        # Don't count CORS preflight
        if request.method.upper() == "OPTIONS":
            return await call_next(request)

        # Real client IP (works behind Nginx if X-Forwarded-For is set)
        xff = request.headers.get("x-forwarded-for", "")
        client_ip = xff.split(",")[0].strip() if xff else (request.client.host if request.client else "unknown")

        now = time.time()
        history = self.requests[client_ip]

        # Remove timestamps outside the window
        cutoff = now - self.window
        while history and history[0] < cutoff:
            history.popleft()

        # Enforce limit
        if len(history) >= self.limit:
            return JSONResponse(
                status_code=429,
                content={
                    "error": "Too Many Requests",
                    "details": f"Rate limit of {self.limit} requests per minute exceeded.",
                },
            )

        # Record request
        history.append(now)

        response = await call_next(request)

        # Cleanup empty histories to prevent memory growth
        if not history:
            self.requests.pop(client_ip, None)

        return response