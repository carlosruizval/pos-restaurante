from dataclasses import dataclass

@dataclass
class Product:
    id: str
    name: str
    price: float
    category_id: str
    available: bool
    description: str = ""