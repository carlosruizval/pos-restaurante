import httpx

# URL de tu deployment Convex
CONVEX_URL = "https://quiet-pig-372.convex.cloud"

class ConvexClient:
    def __init__(self):
        self.base_url = CONVEX_URL
        self.client = httpx.Client()

    def query(self, function: str, args: dict = {}) -> dict:
        """Ejecuta una query de Convex (lectura)"""
        response = self.client.post(
            f"{self.base_url}/api/query",
            json={
                "path": function,
                "args": args,
                "format": "json"
            }
        )
        response.raise_for_status()
        return response.json()

    def mutation(self, function: str, args: dict = {}) -> dict:
        """Ejecuta una mutation de Convex (escritura)"""
        response = self.client.post(
            f"{self.base_url}/api/mutation",
            json={
                "path": function,
                "args": args,
                "format": "json"
            }
        )
        response.raise_for_status()
        return response.json()

    def close(self):
        self.client.close()