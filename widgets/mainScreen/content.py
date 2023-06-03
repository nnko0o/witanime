from flet import *
from typing import List, Optional

class ContentWidget(UserControl):
    def __init__(
         self,
         data: List[str],
         visible: Optional[bool] = True
        ):
        super().__init__()
        self._data = data
        self.visible = visible
    
    def setup_text(self)-> List[Markdown]:
        self.eps = []
        Tamplate = """
Eps URLs :-
        """
        current_ep = 1
        for v in self._data:
            self.eps.append(
                Markdown(
                value=f"Ep{current_ep}: [Link]({v})",
                
                opacity=0.91,
                selectable=True,
                auto_follow_links=True
              ),
            )
            current_ep+=1

        return self.eps


    def build(self)-> Container:
        self.text = self.setup_text()

        self.Container = Container(
            content=ListView(
                controls=self.eps,
                spacing=5,
                padding=5
                #alignment=alignment.top_left,
                #scroll=ScrollMode.ALWAYS
            ),
            padding=3,
            alignment=alignment.top_left
        )
        print('aa')
        return self.Container