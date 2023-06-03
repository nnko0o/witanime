from flet import *

class Application(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.p: Page=page
    
    async def home(self,e: ControlEvent):
        await self.p.go_async("/") # mainScreen

    def build(self)-> Container:
        self.Content = Container(
            width=660,
            height=700,
            bgcolor=colors.BLACK87,
            alignment=alignment.center,
            border_radius=14,
           # border=3,
            content=Column(
                [
                    Text(
                        value="Not Found 404!",
                        size=35,
                        color=colors.WHITE24,
                        bgcolor=colors.BLACK45,
                    ),

                    Divider(
                        height=10,
                        thickness=10,
                        color=colors.CYAN_50,
                    ),

                    ElevatedButton(
                        content=Text(
                            value="Return To Home",
                            size=25,
                        ),
                        bgcolor=colors.BLUE_GREY_400,
                        on_click=self.home
                    )
                ],
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=17,
            )
        )

        return self.Content
