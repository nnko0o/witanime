from flet import *

class EpisodeWidget(UserControl):
    def __init__(
        self,
        number:int,
        url:str,
    )-> None:
        super().__init__()
        self.number = number
        self.url = url
    
    def build(self):
        self._Content = Container(
            padding=5,
            expand=True,
            width=250,
            bgcolor=colors.GREY_400,
            opacity=0.8,
            border_radius=6,
            content=Row(
                spacing=5,
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Text(
                        value=f"{self.number}",
                        size=1,
                        color="",
                    ), # Text 

                    #Container(
                    #    hei
                    #), # Container / فاصلة بين الرقم والبقية

                    Image(
                        src="svg/" + \
                            "drive.svg" if "drive.google.com" in self.url else "mega.svg",
                        height=64,
                        width=64,

                    ), # Image / Small image for (Mega || Drive)

                    TextButton(
                        text="Epsode in FHD",
                        tooltip=Tooltip(
                            text_align=Text(
                                value="Link of Your Episode",
                            ),
                        ),
                        on_click=lambda e: print("Clicked/ Link in FHD")
                    )

                ], # controls > Row
            ), # Row
        ) # Container / self._c
        print(isinstance(self._Content, Control), "self._c")
        return self._Content
