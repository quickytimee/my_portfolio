import reflex as rx
def profile_header() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.image(
                src="/profile.jpg",
                width="100px",
                height="100px",
                border_radius="full",
            ),
            width="100%",
        ),
        rx.heading("Hi, I'm Armin! 👋", size="8", weight="bold", text_align="center", width="100%"),
        rx.text(
            "IT at Telkom University | Python & Cloud Engineering Enthusiast",
            color="var(--gray-11)",
            text_align="center",
            width="100%",
        ),
        rx.box(height="2"),
        width="100%",
        align_items="center",
    )
def about_card() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("🧑‍💻 About Me", size="6", text_align="center", width="100%"),
            rx.text(
                "Perkenalkan nama saya Ahmad Armin Ramadan, saya biasa dipanggil Amat kalau nggak Armin. Hobi saya adalah main game, belajar tentang teknologi, berolahraga, dengerin musik, dan hiking.",
                size="2",
                color="var(--gray-11)",
                text_align="center",
                width="100%",
            ),
            align_items="center",
        ),
        width="100%",
        padding="4",
    )
def education_card() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("🎓 Education", size="6", text_align="center", width="100%"),
            rx.hstack(
                rx.image(
                    src="/telkom_logo.png",
                    width="50px",
                    height="50px",
                    border_radius="full",
                ),
                rx.vstack(
                    rx.text("Telkom University", weight="bold", size="3"),
                    rx.text("Bachelor's Degree in Information Technology", size="2"),
                    rx.text("Sep 2026 - 2030", size="1", color="var(--gray-11)"),
                    align_items="start",
                    spacing="1",
                ),
                align_items="center",
                width="100%",
            ),
            align_items="start",
            width="100%",
        ),
        width="100%",
        padding="4",
    )
def why_built_card() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.badge("Reflex + Python", color_scheme="blue", variant="soft"),
            rx.text("💡 Why I Built This", weight="bold", size="4"),
            rx.box(height="1"),
            rx.text(
                "Tujuan utama bikin web ini supaya memudahkan orang yang ingin kutualan sosmed saya, sekaligus jadi debut pertama kali dalam dunia programmer, saya sendiri membuat project kecil-kecilan dengan Python & Reflex",
                color="var(--gray-11)",
                text_align="center",
                width="100%",
            ),
            align_items="center",
            width="100%",
        ),
        width="100%",
        padding="4",
    )
def social_links() -> rx.Component:
    hover_style = {"transform": "scale(1.05)", "transition": "all 0.2s ease-in-out"}
    return rx.hstack(
        rx.link(
            rx.button("Instagram 📸", color_scheme="pink", _hover=hover_style),
            href="https://www.instagram.com/ahmadarminr/?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
            is_external=True,
        ),
        rx.link(
            rx.button("GitHub 💻", color_scheme="gray", _hover=hover_style),
            href="https://github.com/quickytiome",
            is_external=True,
        ),
        rx.link(
            rx.button("LinkedIn 💼", color_scheme="blue", _hover=hover_style),
            href="https://www.linkedin.com/in/ahmad-armin-ramadan/",
            is_external=True,
        ),
        rx.link(
            rx.button("Discord 🎮", color_scheme="purple", _hover=hover_style),
            href="https://discord.com/users/742331557053726743",
            is_external=True,
        ),
        rx.link(
            rx.button("Spotify 🎧", color_scheme="grass", _hover=hover_style),
            href="https://open.spotify.com/user/31gc35rxwhp4aqaszr2htclz2fk4?si=b440d4a8be584bf4",
            is_external=True,
        ),
        wrap="wrap",
        spacing="3",
        justify="center",
        width="100%",
    )
def top_bar() -> rx.Component:
    return rx.hstack(
        rx.spacer(),
        rx.color_mode.button(size="2", variant="ghost"),
        width="100%",
    )


def skills_card() -> rx.Component:
    skills = ["Python", "Reflex", "Git & GitHub", "REST APIs", "Spotipy", "VS Code", "PyCharm"]
    return rx.card(
        rx.vstack(
            rx.heading("🛠️ Tech Stack & Tools", size="5", text_align="center", width="100%"),
            rx.flex(
                *[rx.badge(skill, variant="soft", color_scheme="indigo", size="2") for skill in skills],
                wrap="wrap",
                spacing="2",
                justify="center",
                width="100%",
                padding_top="2",
            ),
            align_items="center",
            width="100%",
        ),
        width="100%",
        padding="4",
    )
def projects_card() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("🚀 Featured Projects", size="5", text_align="center", width="100%"),
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.text("Personal Portfolio Web App", weight="bold", size="3"),
                        rx.spacer(),
                        rx.link(
                            rx.badge("GitHub ↗", color_scheme="gray", variant="surface"),
                            href="https://github.com/quickytimee/my_portfolio",
                            is_external=True,
                        ),
                        width="100%",
                        align_items="center",
                    ),
                    rx.text(
                        "Web portofolio interaktif full-stack dengan Python & Reflex, dilengkapi integrasi real-time Spotify API OAuth.",
                        size="2",
                        color="var(--gray-11)",
                    ),
                    rx.hstack(
                        rx.badge("Python", size="1", color_scheme="blue"),
                        rx.badge("Reflex", size="1", color_scheme="purple"),
                        rx.badge("Spotify API", size="1", color_scheme="green"),
                        spacing="2",
                    ),
                    align_items="start",
                    spacing="2",
                ),
                width="100%",
                padding_top="2",
            ),
            align_items="start",
            width="100%",
        ),
        width="100%",
        padding="4",
    )
def footer_text() -> rx.Component:
    return rx.text(
        "© 2026 Ahmad Armin Ramadan. Built with Python & Reflex.",
        size="1",
        color="var(--gray-10)",
        text_align="center",
        padding_top="4",
        padding_bottom="2",
    )