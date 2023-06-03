from flet import *
from asyncio import get_event_loop

from widgets import mainView, NotFoundView
from widgets.animeScreen import AnimeView

async def main (p: Page):
    async def routes_handler(e: ControlEvent):
        router = TemplateRoute(p.route.lower())

        if router.match("/"):
            p.views.clear()
            p.views.append(
                View(
                    '/',
                    [
                        Container(
                            width=720,
                            height=600,
                            bgcolor=colors.BLACK,
                            content=Stack(
                                width=350,
                                height=550,
                                controls=[
                                    mainView(p)
                                ],

                            ),
                             border_radius=25,
                            padding=padding.all(10)
                        )
                    ],
                    appbar=AppBar(
                        leading=Icon(icons.HOME),
                        bgcolor=colors.BLACK,
                        title=Text(
                            value="WitAnime App!",
                            color=colors.WHITE
                        ),
                        actions=[
                            IconButton(
                                icon=icons.FAVORITE,
                                url="https://nnko0o.t.me/"
                            )
                        ]
                    ),
                    horizontal_alignment=CrossAxisAlignment.CENTER
                )
            )
            print('/')

        elif router.match('/test-anime/:name'):
            p.views.append(
                View(
                    route=p.route,
                    controls=[
                        Container(
                            padding=10,
                            margin=0,
                            width=720,
                            height=600,
                            bgcolor=colors.BLACK,
                            content=Stack(
                                width=350,
                                height=550,
                                controls=[
                                    AnimeView(
                                        page=p,
                                        anime_qeury=router.name,
                                    )
                                ], # END OF "controls->Stack" LIST
                            ) # END OF "Stack"
                        ), # END OF "Container"
                    ], # END OF "controls->View" LIST
                ), # END OF "View"
            ) # END OF `p.views.append`

        elif router.match("/404"):
            p.views.append(
                View(
                    "/404",
                    [
                        NotFoundView(
                            page=p,
                        )
                    ]
                )
            )

        elif router.match("/anime/:name"):
            pass

        else:
            await p.go_async("/404")

        await p.update_async(); print("update")

    async def view_pop(view):
        p.views.pop()
        top_view = p.views[-1]
        await p.go_async(top_view.route)

    p.on_route_change = routes_handler
    p.on_view_pop = view_pop
    await p.go_async(p.route)


if __name__=="__main__":
    loop = get_event_loop()
    loop.run_until_complete(
        app_async(
            main,
            port=8001,
            assets_dir="assets",
            view = WEB_BROWSER,
            web_renderer="html",
            use_color_emoji=True
        )
    )
