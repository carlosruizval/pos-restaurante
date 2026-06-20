from dataclasses import dataclass
from typing import Optional

@dataclass
class Table:
    id: str
    number: int
    capacity: int
    status: str
    assigned_waiter: Optional[str] = None
    current_order: Optional[str] = None