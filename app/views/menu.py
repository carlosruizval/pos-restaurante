import flet as ft

class MenuView(ft.Column):
    def __init__(self, pg: ft.Page):
        super().__init__()
        self.expand = True
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.controls = [
            ft.Icon(ft.Icons.MENU_BOOK, size=48, color=ft.Colors.ORANGE_700),
            ft.Text("Módulo Menú — Próximamente", size=18),
        ]