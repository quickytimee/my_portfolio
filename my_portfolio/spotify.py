import os
import base64
import requests
import reflex as rx
import spotipy
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REFRESH_TOKEN = os.environ.get("REFRESH_TOKEN")


class TrackState(rx.State):
    tracks: list[dict] = []

    def get_top_tracks(self):
        try:
            auth_string = f"{CLIENT_ID}:{CLIENT_SECRET}"
            auth_base64 = base64.b64encode(auth_string.encode("utf-8")).decode("utf-8")

            auth_url = "https://accounts.spotify.com/api/token"
            headers = {
                "Authorization": f"Basic {auth_base64}",
                "Content-Type": "application/x-www-form-urlencoded",
            }
            auth_data = {
                "grant_type": "refresh_token",
                "refresh_token": REFRESH_TOKEN,
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
            for item in results["items"]:
                new_tracks.append(
                    {
                        "title": item["name"],
                        "artist": item["artists"][0]["name"],
                        "image": item["album"]["images"][0]["url"],
                    }
                )
            self.tracks = new_tracks
        except Exception as e:
            print(f"Error Spotify: {e}")


def track_item(track: dict) -> rx.Component:
    return rx.hstack(
        rx.image(src=track["image"], width="50px", height="50px", border_radius="8px"),
        rx.vstack(
            rx.text(track["title"], weight="bold", margin_bottom="0"),
            rx.text(track["artist"], size="2", color="gray", margin_top="0"),
            align_items="start",
            spacing="1",
        ),
        align_items="center",
        padding_y="2",
        width="100%",
    )


def spotify_widget() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("🎵 My Top Tracks", size="5", text_align="center", width="100%"),
            rx.button("Muat Lagu", on_click=TrackState.get_top_tracks, color_scheme="green"),
            rx.foreach(TrackState.tracks, track_item),
            align_items="center",
            width="100%",
        ),
        width="100%",
        padding="4",
    )


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
        spacing="2",
    )