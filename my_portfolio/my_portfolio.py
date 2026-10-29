import reflex as rx
from .spotify import spotify_widget, TrackState
from .sections import (
    top_bar,
    profile_header,
    about_card,
    education_card,
    skills_card,
    projects_card,
    why_built_card,
    social_links,
    footer_text,
)
from .achievements import achievements_section, certifications_section, admin_page, AchievementState

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            top_bar(),
            profile_header(),
            about_card(),
            education_card(),
            skills_card(),
            projects_card(),
            achievements_section(),
            certifications_section(),
            why_built_card(),
            spotify_widget(),
            social_links(),
            footer_text(),
            width="100%",
            max_width="500px",
            spacing="4",
            align_items="center",
            padding="4",
        )
    )

app = rx.App()
app.add_page(index, route="/", title="Ahmad Armin Ramadan | Portfolio", on_load=AchievementState.load)
app.add_page(admin_page, route="/admin", title="Admin | Portfolio", on_load=AchievementState.load)