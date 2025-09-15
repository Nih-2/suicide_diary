import flet as ft
from HistoryPage import HistoryPage


class AddPage(ft.Column):
    def __init__(self, page: ft.Page, diary, show_message):
        super().__init__()
        self.page = page
        self.diary = diary
        self.show_message = show_message
        self.expand = True

        self.add_tf = ft.TextField(
            label='Введіть коментар',
            multiline=True,
            min_lines=3,
            height=100,
            autofocus=True,
            # width=400
        )

        self.controls = [
            ft.Row([
                ft.Column(
                    [
                        ft.Text(
                            'Додати нотатку:',
                            # font_family='Times New Roman',
                            size=16, weight='bold', height=40, width=400, text_align='center'),
                        self.add_tf,
                        ft.Text(
                            '\nВиберіть настрій:',
                            # font_family='Times New Roman',
                            size=16, weight='bold', height=100, width=400, text_align='center'),
                        ft.Row(
                            [
                                ft.IconButton(icon=ft.Icons.ADD, icon_color='green', on_click=lambda e: self.add(1), width=100, icon_size=42),
                                ft.IconButton(icon=ft.Icons.REMOVE, icon_color='red', on_click=lambda e: self.add(-1), width=100, icon_size=42)
                            ],
                            expand=True,
                            # alignment=ft.MainAxisAlignment.CENTER ,
                            spacing=150
                        )
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ], alignment=ft.MainAxisAlignment.CENTER
            )
        ]

    def add(self, react):
        if not self.add_tf.value:
            self.show_message("Добавте коментар", 'red')
        else:
            note = self.add_tf.value

            self.diary.add_note(react, note)
            self.add_tf.value = ''
            self.show_message("Збережено", 'green')


