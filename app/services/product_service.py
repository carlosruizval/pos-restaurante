from models.product import Product

# Mock de productos por ahora
MOCK_PRODUCTS = [
    Product(id="p1", name="Tacos de Birria", price=85.0,
            category_id="c1", available=True),
    Product(id="p2", name="Quesadilla", price=65.0,
            category_id="c1", available=True),
    Product(id="p3", name="Agua de Jamaica", price=25.0,
            category_id="c2", available=True),
    Product(id="p4", name="Refresco", price=30.0,
            category_id="c2", available=True),
    Product(id="p5", name="Flan", price=45.0,
            category_id="c3", available=True),
]

class ProductService:
    async def get_all(self) -> list[Product]:
        return MOCK_PRODUCTS