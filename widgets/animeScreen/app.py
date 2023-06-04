from flet import *
from moudels.witanime import Anime
from widgets.animeScreen.episodeWidget import EpisodeWidget
from typing import Dict, Any

class Application(UserControl):
    def __init__(
        self,
        page: Page = None,
        anime_data: Dict[str, Any] = None,
        *args,
        **kwargs,
    ):

        #   sx  x'" assert isinstance(page, Page), '"page" must be a type of "Page"'
        #assert isinstance(anime_data, Dict[str, Any]), '"data" must be a str of key-name of the anime'

        super().__init__(
            *args,
            **kwargs,
        )
        self.p = page
       # self.n = anime_qaeury.replace('+',' ')
        #print(self.n)
        self.d = anime_data

        print(self.d)
    
    def header(self)-> Row:
        self._r = Row(
            controls=[
                Image(
                    src="images/None.png",
                    border_radius=5,
                    width=190,
                    height=380,
                    
                ),

                #VerticalDivider(
                #    width=6,
                #    opacity=0.8,
                #    thickness=3,
                #    color=colors.PURPLE_50,
                #),

                Container(
                    height=150,
                    width=3,
                    padding=3,
                    margin=3,
                    bgcolor=colors.PURPLE_50,
                ),

                Column(
                    controls=[
                        Text(
                            value=f"{self.d.get('name')}",#f"Name: {d.get('name')}",
                            size=19,
                            color=colors.CYAN_100,
                            
                        ), # Text "of Title"

                        Text(
                            value=f'{len(self.d.get("eps"))}',
                             size=9,
                            
                        ) # Text "of episodes count"

                    ], # controls > Coulmn
                    spacing=0,
                    alignment=MainAxisAlignment.START

                ), # Column

            ], # controls > Row
        ) # Row / self._r
        # END self._r
        return self._r

    def build(self)-> Control:
        self._c = Container(
            padding=5,
            margin=1,
            content=Column(
                controls=[
                    self.header(), # Row / self._r
                    
                    Divider(
                        height=6,
                        opacity=0.9,
                        color=colors.PURPLE_50,
                    ),

                    Text(value="Test"),
                    EpisodeWidget(
                        1,
                        "https://mega.nz/file/34554"
                    ),

                ],
                spacing=5,
            ) # content / Column
        ) # Container > self._c

        return self._c
    """async def bulid (self)-> Control:
        self._c = Container(
            padding=5,
            margin=1,
            content=Column(
                controls=[
                    self.header(), # Row / self._r
                    # pass
                ],
                spacing=5,
            ) # content / Column
        ) # Container > self._c

        return self._c"""
