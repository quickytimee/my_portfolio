# 👋 Ahmad Armin Ramadan — Personal Portfolio

Web portofolio pribadi yang dibangun menggunakan **Python** dan framework **Reflex**, terintegrasi langsung dengan **Spotify Web API (OAuth 2.0)** untuk menampilkan *Top Tracks* secara real-time.

## ✨ Fitur Utama
- **Spotify Top Tracks Integration**: Mengambil daftar lagu yang paling sering diputar menggunakan autentikasi Refresh Token Spotify API.
- **Modular Architecture**: Struktur kode terpisah antara tampilan (`sections.py`), logika API (`spotify.py`), dan konfigurasi halaman utama (`my_portfolio.py`).
- **Dark / Light Mode**: Mendukung pergantian tema gelap dan terang secara dinamis.

## 🛠️ Tech Stack
- **Framework**: [Reflex](https://reflex.dev/) (Full-stack Python Web)
- **API & Library**: `spotipy`, `requests`, `python-dotenv`

## 🚀 Cara Menjalankan secara Lokal

1. Clone repository ini:
   ```bash
   git clone [https://github.com/quickytimee/my_portfolio.git](https://github.com/quickytimee/my_portfolio.git)
   cd my_portfolio