import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
from models.order import OrderDraft
from services.convex_client import ConvexClient

class OrderService:
    def __init__(self, convex: ConvexClient):
        self._convex = convex

    async def send_to_kitchen(self, draft: OrderDraft, waiter_id: str, table_convex_id: str) -> str:
        items = [
            {
                "product_id": item.product_id,
                "product_name": item.product_name,
                "quantity": item.quantity,
                "unit_price": item.unit_price,
            }
            for item in draft.items
        ]
        result = await self._convex.mutation("orders:create", {
            "table_id": table_convex_id,
            "waiter_id": waiter_id,
            "items": items,
            "total": draft.total,
            "created_at": int(time.time() * 1000),
        })
        return result.get("value", "")