from models.user import User
from models.order import OrderDraft

class AppState:
    def __init__(self):
        self.user: User | None = None
        self.active_orders: dict[str, OrderDraft] = {}

    def get_order_for_table(self, table_id: str) -> OrderDraft:
        return self.active_orders.setdefault(
            table_id, OrderDraft(table_id=table_id)
        )

    def clear_order(self, table_id: str):
        self.active_orders.pop(table_id, None)