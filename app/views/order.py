import flet as ft
from models.app_state import AppState
from models.order import OrderDraft
from services.order_service import OrderService
from services.product_service import ProductService

class OrderView(ft.Column):
    def __init__(self, pg: ft.Page, state: AppState,
                 table_id: str, order_service: OrderService,
                 product_service: ProductService):
        super().__init__()
        self._pg = pg
        self._state = state
        self._table_id = table_id
        self._order_service = order_service
        self._product_service = product_service
        self._draft = state.get_order_for_table(table_id)
        self.expand = True
        self.spacing = 0

        self._cart_column = ft.Column(spacing=4, scroll=ft.ScrollMode.AUTO)
        self._total_text = ft.Text("Total: $0.00", size=18,
                                   weight=ft.FontWeight.BOLD)
        self._products_grid = ft.GridView(
            runs_count=2,
            max_extent=180,
            spacing=8,
            run_spacing=8,
            expand=True,
        )
        self._send_btn = ft.ElevatedButton(
            content=ft.Text("Enviar a cocina"),
            bgcolor=ft.Colors.ORANGE_700,
            color=ft.Colors.WHITE,
            width=300,
            on_click=self.handle_send
        )

        self.controls = [
            self._build_appbar(),
            ft.Row(
                expand=True,
                controls=[
                    ft.Container(
                        expand=2,
                        padding=12,
                        content=self._products_grid
                    ),
                    ft.VerticalDivider(width=1),
                    ft.Container(
                        expand=1,
                        padding=12,
                        content=ft.Column(
                            controls=[
                                ft.Text("Pedido", size=16,
                                        weight=ft.FontWeight.BOLD),
                                ft.Divider(),
                                self._cart_column,
                                ft.Divider(),
                                self._total_text,
                                self._send_btn,
                            ]
                        )
                    )
                ]
            )
        ]

        self._pg.run_task(self._load_products)
        self._refresh_cart()

    def _build_appbar(self):
        return ft.Container(
            bgcolor=ft.Colors.ORANGE_700,
            padding=16,
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.ARROW_BACK,
                        icon_color=ft.Colors.WHITE,
                        on_click=lambda e: self._pg.go("/tables")
                    ),
                    ft.Text(f"Mesa — Pedido",
                            size=18, weight=ft.FontWeight.BOLD,
                            color=ft.Colors.WHITE),
                ]
            )
        )

    async def _load_products(self):
        products = await self._product_service.get_all()
        self._products_grid.controls = [
            self._product_card(p) for p in products
        ]
        self._pg.update()

    def _product_card(self, product):
        return ft.Container(
            bgcolor=ft.Colors.WHITE,
            border_radius=8,
            border=ft.Border.all(1, ft.Colors.GREY_300),
            padding=12,
            on_click=lambda e, p=product: self._add_to_cart(p),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(product.name, weight=ft.FontWeight.BOLD,
                            size=13, text_align=ft.TextAlign.CENTER),
                    ft.Text(f"${product.price:.2f}",
                            color=ft.Colors.ORANGE_700, size=13),
                ]
            )
        )

    def _add_to_cart(self, product):
        self._draft.add_item(product.id, product.name, product.price)
        self._refresh_cart()
        self._pg.update()

    def _refresh_cart(self):
        self._cart_column.controls.clear()
        for item in self._draft.items:
            self._cart_column.controls.append(
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text(f"{item.quantity}x {item.product_name}",
                                size=12),
                        ft.Row(controls=[
                            ft.Text(f"${item.subtotal:.2f}", size=12),
                            ft.IconButton(
                                icon=ft.Icons.REMOVE_CIRCLE_OUTLINE,
                                icon_size=16,
                                icon_color=ft.Colors.RED_400,
                                on_click=lambda e, pid=item.product_id:
                                    self._remove_from_cart(pid)
                            )
                        ])
                    ]
                )
            )
        self._total_text.value = f"Total: ${self._draft.total:.2f}"

    def _remove_from_cart(self, product_id: str):
        self._draft.remove_item(product_id)
        self._refresh_cart()
        self._pg.update()

    async def handle_send(self, e):
        if not self._draft.items:
            snack = ft.SnackBar(
                content=ft.Text("Agrega productos al pedido")
            )
            self._pg.overlay.append(snack)
            snack.open = True
            self._pg.update()
            return

        self._send_btn.disabled = True
        self._pg.update()

        try:
            await self._order_service.send_to_kitchen(
                draft=self._draft,
                waiter_id="dummy_waiter",
                table_convex_id=self._table_id
            )
            self._state.clear_order(self._table_id)
            self._pg.go("/tables")
        except Exception as ex:
            snack = ft.SnackBar(
                content=ft.Text(f"Error: {ex}")
            )
            self._pg.overlay.append(snack)
            snack.open = True
        finally:
            self._send_btn.disabled = False
            self._pg.update()