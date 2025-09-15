import flet as ft

from Diary import Diary
from MainPage import MainPage
from HistoryPage import HistoryPage
from AddPage import AddPage
from DataBase import DataBase


class DiaryApp:
    def __init__(self, db: DataBase):
        self.db = db
 
    def main(self, page: ft.Page):
        self.page = page
        self.page.title = "Записки С"

        # Створюємо тему
        custom_theme = ft.Theme(
            color_scheme=ft.ColorScheme(
                primary=ft.Colors.BLUE,
                secondary=ft.Colors.GREEN,
                surface=ft.Colors.WHITE,
                background=ft.Colors.SURFACE_TINT,
                error=ft.Colors.RED,
                on_primary=ft.Colors.WHITE,
                on_secondary=ft.Colors.BLACK,
                on_surface=ft.Colors.BLACK,
                on_background=ft.Colors.BLACK,
                on_error=ft.Colors.WHITE,
            ),
        )

        self.page.bgcolor = ft.Colors.ON_TERTIARY
        # self.page.theme = custom_theme
        self.page.theme_mode = ft.ThemeMode.SYSTEM # 'dark'
        self.page.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.MainAxisAlignment.CENTER
        # self.page.scroll = "adaptive" # ft.ScrollMode.AUTO

        self.diary = Diary(self.db)

        self.snack_bar = ft.SnackBar(
            ft.Text(value='', color="white"),
            # bgcolor=color
        )
        self.page.overlay.append(self.snack_bar)

        # Сторінки
        pages = {
            "/main": lambda: MainPage(page, self.diary, self.show_message),
            "/add": lambda: AddPage(page, self.diary, self.show_message),
            "/history": lambda: HistoryPage(page, self.diary, self.show_message),
        }

        # Контейнер для вмісту
        content = ft.Container(expand=True)  # content=pages["/main"],
        page.add(content)

        # Функція перемикання роутів
        def route_change(e):
            route = page.route
            if route in pages:
                content.content = pages[route]()
            else:
                content.content = ft.Text("Сторінку не знайдено")
            page.update()

        page.on_route_change = route_change

        # NavigationBar
        def change_page(e):
            routes = ["/main", "/add", "/history"]
            page.go(routes[e.control.selected_index])


        navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.HOME_OUTLINED, label="Головна", selected_icon=ft.Icons.HOME),
                ft.NavigationBarDestination(icon=ft.Icons.ADD, label="Додати"),
                ft.NavigationBarDestination(icon=ft.Icons.HISTORY, label="Історія"),
            ],
            on_change=change_page,
            selected_index=0
        )

        self.page.add(navigation_bar)
        self.page.go('/main')


    def show_message(self, text, color):
        self.snack_bar.content.value = text
        self.snack_bar.bgcolor = color

        self.snack_bar.open = True
        self.page.update()



if __name__ == "__main__":
    db = DataBase()
    app = DiaryApp(db)
    # ft.app(target=app.main, view=ft.AppView.WEB_BROWSER, port=8080, assets_dir="assets")
    ft.app(target=app.main, view=ft.AppView.FLET_APP)


