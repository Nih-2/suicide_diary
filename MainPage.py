import flet as ft


class MainPage(ft.Column):
    def __init__(self, page: ft.Page, diary, show_message):
        super().__init__()
        self.page = page
        self.diary = diary
        self.show_message = show_message
        self.expand = True

        self.diary.count_rating()

        self.text_style = ft.TextStyle(
            # font_family="Times New Roman",
            weight= 'bold',
            size=16,
            # color="white",
        )

        self.controls = [
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text(
                                value='за тиждень',
                                width=200,
                                # height=20,
                                text_align='center',
                                style=self.text_style,
                            ),
                            ft.Text(
                                value=f'+{self.diary.week_rating}' if self.diary.week_rating > 0 else self.diary.week_rating,
                                color="green" if self.diary.week_rating >= 0 else "red",
                                size=42,
                                width=200,
                                # height=40,
                                text_align='center'
                            ),
                            ft.Text(
                                value='за день',
                                width=200,
#                                 height=20,
                                text_align='center',
                                style=self.text_style,
                            ),
                            ft.Text(
                                value=f'+{self.diary.day_rating}' if self.diary.day_rating > 0 else self.diary.day_rating,
                                color="green" if self.diary.day_rating >= 0 else "red",
                                size=72,
                                width=200,
                                # height=100,
                                text_align='center'
                            ),
                            ft.Text(
                                value='за місяць',
                                width=200,
#                                 height=20,
                                text_align='center',
                                style=self.text_style,
                            ),
                            ft.Text(
                                value=f'+{self.diary.month_rating}' if self.diary.month_rating > 0 else self.diary.month_rating,
                                color="green" if self.diary.month_rating >= 0 else "red",
                                size=42,
                                width=200,
                                # height=40,
                                text_align='center'
                            ),
                        ], spacing=20
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ]

        self.page.update()
