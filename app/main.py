import flet as ft
from views.login import LoginView
from views.tables import TablesView
from views.menu import MenuView
from views.orders import OrdersView
from views.reports import ReportsView
from services.auth_service import AuthService
from services.table_service import TableService
from services.convex_client import ConvexClient

def main(page: ft.Page):
    page.title = "POS Restaurante"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0

    # --- Servicios con Convex real ---
    convex = ConvexClient()
    auth_service = AuthService()
    table_service = TableService(convex)

    def route_change(e):
        page.views.clear()

        if page.route == "/login" or page.route == "/":
            page.views.append(
                ft.View(
                    route="/login",
                    padding=0,
                    controls=[LoginView(page, auth_service)]
                )
            )

        elif page.route == "/tables":
            page.views.append(
                ft.View(
                    route="/tables",
                    padding=0,
                    navigation_bar=_build_navbar(0),
                    controls=[TablesView(page, table_service)]
                )
            )

        elif page.route == "/menu":
            page.views.append(
                ft.View(
                    route="/menu",
                    padding=0,
                    navigation_bar=_build_navbar(1),
                    controls=[MenuView(page)]
                )
            )

        elif page.route == "/orders":
            page.views.append(
                ft.View(
                    route="/orders",
                    padding=0,
                    navigation_bar=_build_navbar(2),
                    controls=[OrdersView(page)]
                )
            )

        elif page.route == "/reports":
            page.views.append(
                ft.View(
                    route="/reports",
                    padding=0,
                    navigation_bar=_build_navbar(3),
                    controls=[ReportsView(page)]
                )
            )

        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    def _build_navbar(selected_index: int):
        routes = ["/tables", "/menu", "/orders", "/reports"]

        def on_nav_change(e):
            page.go(routes[e.control.selected_index])

        return ft.NavigationBar(
            selected_index=selected_index,
            on_change=on_nav_change,
            destinations=[
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
        )

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go("/login")

ft.app(main)