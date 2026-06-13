import flet as ft
from components.navbar import NavBar

class ReportsView(ft.Column):
    def __init__(self, pg: ft.Page, navigate):
        super().__init__()
        self.expand = True
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        pg.navigation_bar = NavBar(pg, navigate, current_index=3)

        self.controls = [
            ft.Icon(ft.Icons.BAR_CHART, size=48, color=ft.Colors.ORANGE_700),
            ft.Text("Módulo Reportes — Próximamente", size=18),
        ]