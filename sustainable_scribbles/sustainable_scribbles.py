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
    rx.button: {
        "background_color": "#8ba888",
        "font_family": "Monospace",
    },
}




def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Sustainable Scribbles"),
            rx.text(
                "Doodle with us, and Mr. Raccoon will guess your answer!"
            ),
            rx.button(
                "PLAY →",
                on_click=rx.redirect(
                    "/directions"
                ),
                size="4",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )


app = rx.App(
    style=style,
    stylesheets=[
        "/fonts/myfont.css",  # This path is relative to assets/
    ]
    )

app.add_page(index, route="/")
