import flet as ft


class HistoryPage(ft.Column):
    def __init__(self, page: ft.Page, diary, show_message):
        super().__init__()
        self.page = page
        self.diary = diary
        self.show_message = show_message
        self.expand = True
        self.page.scroll = "adaptive"  # ft.ScrollMode.AUTO

        self.pages_listbox = ft.ListView(
            expand=True,
            spacing=0,
            padding=10,
            auto_scroll=False
        )

        self.controls = [
            ft.Row([
                ft.Text(
                    'Всі нотатки:',
                    # font_family='Times New Roman',
                    size=16, weight='bold', height=40, width=500, text_align='center'
                )
            ], alignment=ft.MainAxisAlignment.CENTER
            ),
            self.pages_listbox
        ]

        self.lesson_list()


    def lesson_list(self):
        self.pages_listbox.controls.clear()

        if not self.diary.notes_list:
            self.pages_listbox.controls.append(
                ft.Container(
                    content=ft.Text('Записи відсутні', font_family='Times New Roman', size=16),
                    padding=10,
                    bgcolor=ft.Colors.RED_50,
                    border_radius=5,
                )
            )
        else:
            day = None

            for note in self.diary.notes_list:
                # print(note)
                # id = note[0]
                time = note[1].strftime('%H:%M')
                date = note[1].strftime('%d.%m.%Y')
                react_icon = ft.Icons.ADD if note[2] == 1 else ft.Icons.REMOVE
                react_color = 'green' if note[2] == 1 else 'red'
                note_text = note[3]

                if date != day:
                    day = date
                    self.pages_listbox.controls.append(
                        ft.Container(
                            content=ft.Text(
                                value=f'        {date}',
                                font_family='Times New Roman',
                                size=16,
                                weight='bold',
                            ),
                            padding=10,
                            # bgcolor=ft.Colors.BLUE_50,
                            border_radius=5,
                        )
                    )

                self.pages_listbox.controls.append(
                    ft.Container(
                        content=
                        ft.Row(
                            [
                                ft.Icon(name=react_icon, size=24, color=react_color),
                                ft.Text(value=f'{time}  {note_text}', font_family='Times New Roman', size=16),
                            ],
                        ),
                        padding=10,
                        # bgcolor=ft.Colors.BLUE_50,
                        border_radius=5,
                        # on_click=item_click
                    )
                )
        self.page.update()
