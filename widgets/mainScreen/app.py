from flet import *
from .result import SearchResultWidget
from moudels.witanime import Anime

class App(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.p = page
        self.a = Anime('assets/db/anime.json')

    async def searchHandler(self, e: ControlEvent):
        print("Handle Search ", e.data)
        if self.searchField.value.strip()=='':
            return
        result = self.a.search_anime(
            self.searchField.value.strip()
        )
        print(result)
        
        if len(result) <= 0:
            self.Results.controls.clear()
            self.Results.controls.append(
                Container(padding=padding.only(bottom=5)),
                Text(
                    value='Search Result Is Empty',
                    size=30,
                ),
            )
            self.searchField.value=''
            await self.Results.update_async()
            await self.searchField.update_async()

        self.Results.controls.clear()
        for r in result:
            print("Anime Result: ", r)
            self.Results.controls.append(
                SearchResultWidget(
                    page=self.p,
                    Cover='images/None.png',
                   # Name=f'{r.get("name")}',
                    data=r,
                )
            )
        self.searchField.value=''
        await self.searchField.update_async()
        await self.Results.update_async()
        print(self.Results.controls)

    def build(self) -> Control:
        self.searchField = TextField(
            label="Enter Anime Name",
            min_lines=1,
            max_lines=1,
            max_length=50
        )

        self.Results = GridView(
            #expand=True,
            controls=[],
            runs_count=2,
            #horizontal=True,
            padding=5,
            run_spacing=10,
            max_extent=80,
            child_aspect_ratio=85/ 160
            #alignment=MainAxisAlignment.START,
            #horizontal_alignment=CrossAxisAlignment.END
            )
        print(".70 -> app.py")

        return Column([
            Row([
                self.searchField,
                IconButton(
                    icon=icons.SEARCH ,
                    icon_size=25,
                    on_click=self.searchHandler
                )
            ]),
            Divider(
                height=4,
                thickness=5,
                color=colors.WHITE38
            ) ,
            self.Results
        ],
            spacing=12,
            alignment=MainAxisAlignment.START,
            scroll=ScrollMode.ALWAYS
        )
