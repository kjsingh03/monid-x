from typing import Any

import httpx

from app.config import settings


class MonidClient:

    def __init__(self) -> None:
        self._client = httpx.AsyncClient(
            base_url=settings.monid_base_url,
            headers={
                "Authorization": f"Bearer {settings.monid_api_key}",
                "Content-Type": "application/json",
            },
            timeout=30.0,
        )

    async def whoami(self) -> dict[str, Any]:
        response = await self._client.get("/v1/auth/whoami")
        response.raise_for_status()

        return response.json()

    async def discover(
        self,
        query: str,
        *,
        limit: int = 5,
        min_score: float = 0.2,
    ) -> dict[str, Any]:
        response = await self._client.post(
            "/v1/discover",
            json={
                "query": query,
                "limit": limit,
                "minScore": min_score,
            },
        )
        response.raise_for_status()

        return response.json()

    async def close(self) -> None:
        await self._client.aclose()