import os
import reflex as rx
import spotipy
from dotenv import load_dotenv

load_dotenv()

load_dotenv()

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REFRESH_TOKEN = os.environ.get("REFRESH_TOKEN")

class TrackState(rx.State):
    tracks: list[dict] = []

    def get_top_tracks(self):
        import requests
        import base64

        try:
            auth_string = f"{CLIENT_ID}:{CLIENT_SECRET}"
            auth_base64 = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')

            auth_url = "https://accounts.spotify.com/api/token"
            headers = {
                "Authorization": f"Basic {auth_base64}",
                "Content-Type": "application/x-www-form-urlencoded"
            }
            auth_data = {
                "grant_type": "refresh_token",
                "refresh_token": REFRESH_TOKEN
            }
            response = requests.post(auth_url, headers=headers, data=auth_data, timeout=10)
            token_info = response.json()
            access_token = token_info.get("access_token")
            if not access_token:
                print(f"GAGAL TOKEN SPOTIFY: {token_info}")
                return
            sp = spotipy.Spotify(auth=access_token, requests_timeout=10)
            results = sp.current_user_top_tracks(limit=10, time_range="short_term")

            new_tracks = []
            for item in results['items']:
                new_tracks.append({
                    "title": item['name'],
                    "artist": item['artists'][0]['name'],
                    "image": item['album']['images'][0]['url']
                })

            self.tracks = new_tracks

        except Exception as e:
            print(f"Error Spotify: {e}")

def track_item(track: dict):
    return rx.hstack(
        rx.image(src=track["image"], width="50px", height="50px", border_radius="8px"),
        rx.vstack(
            rx.text(track["title"], weight="bold", margin_bottom="0"),
            rx.text(track["artist"], size="2", color="gray", margin_top="0"),
            align_items="start",
            spacing="1"
        ),
        align_items="center",
        padding_y="2",
        width="100%"
    )
def spotify_widget():
    return rx.card(
        rx.vstack(
            rx.heading("🎵 My Top Tracks", size="5", text_align="center", width="100%"),
            rx.button("Muat Lagu", on_click=TrackState.get_top_tracks, color_scheme="green"),
            rx.foreach(TrackState.tracks, track_item),
            align_items="center",
            width="100%"
        ),
        width="100%",
        padding="4"
    )
class State(rx.State):
    """The app state."""
    pass

def spotify_playlist_embed() -> rx.Component:
    return rx.vstack(
        rx.heading("🎧 Currently On Repeat", size="5"),
        rx.html(
            """
            <iframe 
                style="border-radius:12px" 
                src="https://open.spotify.com/embed/playlist/37i9dQZF1Epz7peE67t?utm_source=generator&theme=0" 
                width="100%" 
                height="152" 
                frameBorder="0" 
                allowfullscreen="" 
                allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
                loading="lazy">
            </iframe>
            """
        ),
        align_items="center",
        width="100%",
        padding="4",
        spacing="2"
    )
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
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
            rx.card(
                rx.vstack(
                    rx.heading("💡 About Me", size="6", text_align="center", width="100%"),
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
            ),
            rx.card(
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
            ),
            rx.card(
                rx.vstack(
                    rx.badge("Reflex + Python", color_scheme="blue", variant="soft"),
                    rx.text("🚀 Why I Built This", weight="bold", size="4"),
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
            ),
            # spotify_playlist_embed(),
            spotify_widget(),

            rx.hstack(
                rx.link(
                    rx.button(
                        "Instagram 📸",
                        color_scheme="pink",
                        _hover={"transform": "scale(1.05)", "transition": "all 0.2s ease-in-out"}
                    ),
                    href="https://www.instagram.com/ahmadarminr/?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
                    is_external=True,
                ),
                rx.link(
                    rx.button(
                        "GitHub 💻",
                        color_scheme="gray",
                        _hover={"transform": "scale(1.05)", "transition": "all 0.2s ease-in-out"}
                    ),
                    href="https://github.com/quickytiome",
                    is_external=True,
                ),
                rx.link(
                    rx.button(
                        "LinkedIn 💼",
                        color_scheme="blue",
                        _hover={"transform": "scale(1.05)", "transition": "all 0.2s ease-in-out"}
                    ),
                    href="https://www.linkedin.com/in/ahmad-armin-ramadan/",
                    is_external=True,
                ),
                rx.link(
                    rx.button(
                        "Discord 👾",
                        color_scheme="purple",
                        _hover={"transform": "scale(1.05)", "transition": "all 0.2s ease-in-out"}
                    ),
                    href="https://discord.com/users/742331557053726743",
                    is_external=True,
                ),
                rx.link(
                    rx.button(
                        "Spotify 🎧",
                        color_scheme="grass",
                        _hover={"transform": "scale(1.05)", "transition": "all 0.2s ease-in-out"}
                    ),
                    href="https://open.spotify.com/user/31gc35rxwhp4aqaszr2htclz2fk4?si=b440d4a8be584bf4",
                    is_external=True,
                ),
                wrap="wrap",
                spacing="3",
                justify="center",
                width="100%",
            ),
            width="100%",
            max_width="500px",
            spacing="4",
            align_items="center",
            padding="4",
        )
    )
app = rx.App()
app.add_page(index)