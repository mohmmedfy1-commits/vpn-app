import flet as ft

def main(page: ft.Page):
    page.title = "تطبيق VPN"
    page.theme_mode = ft.ThemeMode.DARK
    page.add(
        ft.Text("هذا تطبيق VPN بسيط", size=20)
    )

ft.app(target=main)
