import httpx

CONVEX_URL = "https://quiet-pig-372.convex.cloud"

class ConvexClient:
    def __init__(self):
        self.base_url = CONVEX_URL
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            timeout=10
        )

    async def query(self, function: str, args: dict = {}) -> dict:
        response = await self._client.post(
            "/api/query",
            json={"path": function, "args": args, "format": "json"}
        )
        response.raise_for_status()
        return response.json()

    async def mutation(self, function: str, args: dict = {}) -> dict:
        response = await self._client.post(
            "/api/mutation",
            json={"path": function, "args": args, "format": "json"}
        )
        response.raise_for_status()
        return response.json()

    async def close(self):
        await self._client.aclose()