import flet as ft
from services.table_service import TableService
from models.table import Table

STATUS_COLOR = {
    "free": ft.Colors.GREEN_400,
    "occupied": ft.Colors.RED_400,
    "waiting_payment": ft.Colors.ORANGE_400,
}

STATUS_LABEL = {
    "free": "Libre",
    "occupied": "Ocupada",
    "waiting_payment": "Por cobrar",
}

class TablesView(ft.Column):
    def __init__(self, pg: ft.Page, state, table_service: TableService):
        super().__init__()
        self._pg = pg
        self._state = state
        self._service = table_service
        self.expand = True
        self.spacing = 0

        self._grid = ft.GridView(
            runs_count=3,
            max_extent=160,
            spacing=12,
            run_spacing=12,
            expand=True,
        )

        self._loading = ft.Container(
            expand=True,
            alignment=ft.Alignment(0, 0),
            content=ft.ProgressRing()
        )

        self.controls = [
            self._build_appbar(),
            self._build_legend(),
            self._loading,
        ]

        self._pg.run_task(self._load_tables)

    def _build_appbar(self):
        return ft.Container(
            bgcolor=ft.Colors.ORANGE_700,
            padding=16,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Text("Mesas", size=20,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.WHITE),
                    ft.Row(controls=[
                        ft.Icon(ft.Icons.PERSON, color=ft.Colors.WHITE),
                        ft.Text("Admin Demo", color=ft.Colors.WHITE),
                    ])
                ]
            )
        )

    def _build_legend(self):
        def dot(color, label):
            return ft.Row(controls=[
                ft.Container(width=12, height=12,
                             bgcolor=color,
                             border_radius=6),
                ft.Text(label, size=12),
            ])

        return ft.Container(
            padding=ft.Padding(left=16, right=16, top=8, bottom=8),
            content=ft.Row(controls=[
                dot(ft.Colors.GREEN_400, "Libre"),
                dot(ft.Colors.RED_400, "Ocupada"),
                dot(ft.Colors.ORANGE_400, "Por cobrar"),
            ], spacing=16)
        )

    async def _load_tables(self):
        tables = await self._service.get_all()
        self._grid.controls = [self._table_card(t) for t in tables]
        self.controls[-1] = ft.Container(
            expand=True, padding=16, content=self._grid
        )
        self._pg.update()

    def _table_card(self, table: Table):
        color = STATUS_COLOR[table.status]
        label = STATUS_LABEL[table.status]
        return ft.Container(
            bgcolor=ft.Colors.WHITE,
            border_radius=12,
            border=ft.Border.all(2, color),
            padding=16,
            on_click=lambda e, t=table: self.on_table_click(t),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Icon(ft.Icons.TABLE_RESTAURANT, color=color, size=32),
                    ft.Text(f"Mesa {table.number}",
                            weight=ft.FontWeight.BOLD),
                    ft.Text(label, size=12, color=color),
                    ft.Text(f"{table.capacity} personas",
                            size=11, color=ft.Colors.GREY_500),
                ]
            )
        )

    def on_table_click(self, table: Table):
        self._pg.go(f"/tables/{table.id}/order")