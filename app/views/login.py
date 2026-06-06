import flet as ft

class LoginView(ft.Column):
    def __init__(self, pg: ft.Page, navigate):
        super().__init__()
        self._pg = pg
        self.navigate = navigate
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

        self.btn_login = ft.ElevatedButton(
            content=ft.Text("Ingresar"),
            width=300,
            on_click=self.handle_login
        )

        self.controls = [
            ft.Icon(ft.Icons.RESTAURANT, size=64, color=ft.Colors.ORANGE_700),
            ft.Text("POS Restaurante", size=24, weight=ft.FontWeight.BOLD),
            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
            self.txt_user,
            self.txt_pass,
            self.txt_error,
            self.btn_login,
        ]

    def handle_login(self, e):
        if self.txt_user.value and self.txt_pass.value:
            self.navigate("tables")
        else:
            self.txt_error.value = "Ingresa usuario y contraseña"
            self._pg.update()