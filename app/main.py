import flet as ft
from views.login import LoginView
from views.tables import TablesView
from views.menu import MenuView
from views.orders import OrdersView
from views.reports import ReportsView

def main(page: ft.Page):
    page.title = "POS Restaurante"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0

    # --- Estado global simulado (mock) ---
    page.data = {
        "user": {
            "name": "Admin Demo",
            "role": "admin"
        }
    }

    # --- Función para cambiar de vista ---
    def navigate(view_name: str):
        page.controls.clear()

        if view_name == "tables":
            page.add(TablesView(page, navigate))
        elif view_name == "menu":
            page.add(MenuView(page, navigate))
        elif view_name == "orders":
            page.add(OrdersView(page, navigate))
        elif view_name == "reports":
            page.add(ReportsView(page, navigate))
        else:
            page.add(LoginView(page, navigate))

        page.update()

    # --- Vista inicial ---
    navigate("login")

ft.app(main)