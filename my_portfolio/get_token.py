import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "2a404cb8fd56461ebf58a7992f4fb6e5"
CLIENT_SECRET = "480b5ecd8caa4925b09dcbd6c96d0c2c"
REDIRECT_URI = "http://127.0.0.1:8888/callback"

print("Membuka browser untuk otorisasi...")

auth_manager = SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="user-top-read",
    open_browser=True
)
sp = spotipy.Spotify(auth_manager=auth_manager)
sp.current_user_top_tracks(limit=1)

token_info = auth_manager.get_cached_token()
print("\n" + "="*50)
print("BERHASIL! INI REFRESH TOKEN LU, SIMPAN DI NOTEPAD:")
print(token_info["refresh_token"])
print("="*50 + "\n")