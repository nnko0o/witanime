from flet import *
from .content import ContentWidget
from typing import Dict, Any
from widgets.animeScreen import AnimeView

class SearchResultWidget(UserControl):
    def __init__(
          self,
          page: Page,
          Cover: str,
          #Name: str,
          data: Dict[str, Any],
        ):
        super().__init__()
        self.p:Page = page
        self.Name = data.get("name")
        self.Cover = Cover
        self._data = data
    
    async def set_view(
        self, 
        data: Dict[str, Any]
     ):

        View_Control = AnimeView(
            anime_data=data,
        )
        View_ = View(
            route="/",
            vertical_alignment=MainAxisAlignment.START,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                Container(
                    content=Column(
                        controls=[
                            View_Control,
                        ],
                    ),
                    padding=1,
                )
            ],
        )
    
        self.p.views.append(
            View_,
        )
        await self.p.go_async(
            f"/anime/{self.Name}"
        )
        #await self.p.update_async()
        
    async def open_view(
        self,
        e: ControlEvent,
    ):
        await self.set_view(
            data=self._data,
        )

    async def _explian(self, e:ControlEvent):
        if self.opened == False:
            self.opened = True
            # self.Container.height = 350
            #self.Container.content.controls[0].controls[2].icon = icons.ARROW_CIRCLE_UP_OUTLINED
            self.view.controls[1].visible = True
            self.view.controls[2].visible = True
            self.view.content.scroll = ScrollMode.ADAPTIVE
            await self.Container.update_async()
        else:
            self.opened = False
            # self.view.height = 125
            # self.Container.content.controls[0].controls[2].icon = icons.EXPAND_CIRCLE_DOWN_OUTLINED
            self.view.controls[1].visible = False
            self.view.controls[2].visible = False
            
            self.view.content.scroll = ScrollMode.HIDDEN
            await self.view.update_async()

    def build(self)-> Column:
        print(len(self._data))
        self.opened = False
        self.view = Column(
                controls=[
                    Image(
                        src=self.Cover, # Image URi
                        width=70,
                        height=100,
                    ),

                    Text(
                        value=self.Name,
                        size=9,
                        #no_wrap=False,
                    ),
                    Divider(
                        height=7,
                        color=colors.LIGHT_BLUE_300,
                        visible=False
                    ),

                    ContentWidget(
                        data = self._data,
                        visible = False
                    ),
             ],
             scroll=ScrollMode.HIDDEN,
             horizontal_alignment=CrossAxisAlignment.CENTER,
             alignment=MainAxisAlignment.CENTER,
            )
        print("result.py > 67 > before return")
        return Container(
            padding=0,
            margin=0,
            height=150,
            content=self.view,
           # alignment=",
            on_click=self.open_view,
            on_hover=lambda e: print('Hoverred')
        )
#hover=lambda e: print('Hoverred')
#       )
