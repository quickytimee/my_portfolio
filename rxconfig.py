import reflex as rx

config = rx.Config(
    app_name="my_portfolio",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)