import reflex as rx
from .spotify import spotify_widget, spotify_playlist_embed
from .sections import (
    profile_header,
    about_card,
    education_card,
    why_built_card,
    social_links,
)


class State(rx.State):
    """The app state."""
    pass


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            profile_header(),
            about_card(),
            education_card(),
            why_built_card(),
            spotify_widget(),
            social_links(),
            width="100%",
            max_width="500px",
            spacing="4",
            align_items="center",
            padding="4",
        )
    )


app = rx.App()
app.add_page(index)