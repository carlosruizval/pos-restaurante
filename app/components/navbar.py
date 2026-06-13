import flet as ft

class NavBar(ft.NavigationBar):
    def __init__(self, pg: ft.Page, navigate, current_index: int = 0):
        super().__init__()
        self._pg = pg
        self.navigate = navigate
        self.selected_index = current_index
        self.bgcolor = ft.Colors.WHITE

        self.destinations = [
            ft.NavigationBarDestination(
                icon=ft.Icons.TABLE_RESTAURANT_OUTLINED,
                selected_icon=ft.Icons.TABLE_RESTAURANT,
                label="Mesas"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.MENU_BOOK_OUTLINED,
                selected_icon=ft.Icons.MENU_BOOK,
                label="Menú"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.RECEIPT_LONG_OUTLINED,
                selected_icon=ft.Icons.RECEIPT_LONG,
                label="Pedidos"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.BAR_CHART_OUTLINED,
                selected_icon=ft.Icons.BAR_CHART,
                label="Reportes"
            ),
        ]

        self.on_change = self.handle_change

    def handle_change(self, e):
        index = e.control.selected_index
        routes = ["tables", "menu", "orders", "reports"]
        self.navigate(routes[index])