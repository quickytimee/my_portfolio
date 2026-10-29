# 👋 Ahmad Armin Ramadan — Personal Portfolio

Web portofolio pribadi yang dibangun menggunakan **Python** dan framework **Reflex**, terintegrasi dengan **Spotify Web API (OAuth 2.0)** untuk menampilkan *Top Tracks*.

## ✨ Fitur Utama
- **Spotify Top Tracks**: mengambil lagu yang paling sering diputar lewat Refresh Token Spotify API.
- **Pencapaian & Sertifikasi**: dikelola lewat halaman admin (`/admin`) yang dilindungi password.
- **Modular Architecture**: tampilan (`sections.py`), logika Spotify (`spotify.py`), pencapaian (`achievements.py`), dan konfigurasi halaman (`my_portfolio.py`) dipisah.
- **Dark / Light Mode**

## 🛠️ Tech Stack
- **Framework**: [Reflex](https://reflex.dev/)
- **Library**: `spotipy`, `requests`, `python-dotenv`

## 🚀 Cara Menjalankan Lokal

1. Clone repository:
   ```bash
   git clone https://github.com/quickytimee/my_portfolio.git
   cd my_portfolio
   ```
2. Buat virtual environment dan install dependensi:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Buat file `.env` di root project:
   ```env
   CLIENT_ID=...
   CLIENT_SECRET=...
   REFRESH_TOKEN=...
   ADMIN_PASSWORD=...
   ```
4. Jalankan:
   ```bash
   reflex run
   ```
   Buka `http://localhost:3000`. Halaman admin ada di `/admin`.