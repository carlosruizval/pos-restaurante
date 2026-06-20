import flet as ft
from services.auth_service import AuthService

class LoginView(ft.Column):
    def __init__(self, pg: ft.Page, auth_service: AuthService):
        super().__init__()
        self._pg = pg
        self._auth = auth_service
        self.expand = True
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.txt_user = ft.TextField(
            label="Usuario",
            width=300,
            prefix_icon=ft.Icons.PERSON
        )
        self.txt_pass = ft.TextField(
            label="Contraseña",
            width=300,
            password=True,
            can_reveal_password=True,
            prefix_icon=ft.Icons.LOCK
        )
        self.txt_error = ft.Text("", color=ft.Colors.RED_400)

        self.controls = [
            ft.Icon(ft.Icons.RESTAURANT, size=64, color=ft.Colors.ORANGE_700),
            ft.Text("POS Restaurante", size=24, weight=ft.FontWeight.BOLD),
            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
            self.txt_user,
            self.txt_pass,
            self.txt_error,
            ft.ElevatedButton(
                content=ft.Text("Ingresar"),
                width=300,
                on_click=self.handle_login
            ),
        ]

    def handle_login(self, e):
        user = self._auth.login(self.txt_user.value, self.txt_pass.value)
        if user:
            self._pg.go("/tables")
        else:
            self.txt_error.value = "Ingresa usuario y contraseña"
            self._pg.update()