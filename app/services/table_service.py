import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.table import Table
from services.convex_client import ConvexClient

class TableService:
    def __init__(self, convex: ConvexClient):
        self._convex = convex

    async def get_all(self) -> list[Table]:
        result = await self._convex.query("tables:getAll")
        tables = []
        for item in result.get("value", []):
            tables.append(Table(
                id=item["_id"],
                number=item["number"],
                capacity=item["capacity"],
                status=item["status"],
            ))
        return tables

    async def update_status(self, table_id: str, status: str) -> None:
        await self._convex.mutation("tables:updateStatus", {
            "tableId": table_id,
            "status": status
        })