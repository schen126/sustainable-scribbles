import reflex as rx
from rxconfig import config

style = {
    rx.heading: {
        "font_family": "MoonPretty",
        "font_weight": "500",
        "font_size": "75px",
        "color": "#8ba888",
    },
    rx.text: {
        "font_family": "Monospace",
        "font_size": "20px",
        "color": "#44624a",
    },
    rx.container: {
        "background_color": "#f1ebe1",
    },
}


def directions() -> rx.Component:
    return rx.text("Directions Page")

app = rx.App(
    style=style,
    stylesheets=[
        "/fonts/myfont.css",  # This path is relative to assets/
    ],
    theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="large",
    ))

app.add_page(directions, route="/directions")