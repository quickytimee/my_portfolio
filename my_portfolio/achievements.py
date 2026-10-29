import asyncio
import hmac
import json
import os
import uuid
from pathlib import Path
import reflex as rx

DATA_FILE = Path("data/achievements.json")
ALLOWED_EXT = {".jpg", ".jpeg", ".png", ".webp", ".gif"}
MAX_IMAGE_BYTES = 5 * 1024 * 1024  # 5 MB


def _read() -> list[dict]:
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def _write(items: list[dict]) -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    tmp = DATA_FILE.with_suffix(".tmp")
    tmp.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(DATA_FILE)


class AchievementState(rx.State):
    items: list[dict] = []
    is_admin: bool = False
    password: str = ""
    login_error: str = ""

    title: str = ""
    category: str = "Achievement"
    description: str = ""
    achieved_on: str = ""
    message: str = ""

    def set_category(self, value: str):
        self.category = value

    # -----------------------------------

    def set_password(self, value: str):
        self.password = value

    def set_title(self, value: str):
        self.title = value


    def load(self):
        self.items = _read()

    async def login(self):
        expected = os.environ.get("ADMIN_PASSWORD", "")
        await asyncio.sleep(1)
        if not expected:
            self.login_error = "ADMIN_PASSWORD belum di-set di server."
        elif hmac.compare_digest(self.password.encode(), expected.encode()):
            self.is_admin = True
            self.login_error = ""
        else:
            self.login_error = "Password salah."
        self.password = ""

    def logout(self):
        self.is_admin = False
        self.message = ""

    async def save(self, files: list[rx.UploadFile]):
        if not self.is_admin:
            return
        if not self.title.strip():
            self.message = "Judul wajib diisi."
            return

        filename = ""
        if files:
            f = files[0]
            original = getattr(f, "filename", None) or getattr(f, "name", None) or ""
            ext = Path(original).suffix.lower()
            if ext not in ALLOWED_EXT:
                self.message = "Format foto harus jpg, png, webp, atau gif."
                return
            data = await f.read()
            if len(data) > MAX_IMAGE_BYTES:
                self.message = "Foto maksimal 5 MB."
                return
            filename = f"{uuid.uuid4().hex}{ext}"
            upload_dir = rx.get_upload_dir()
            upload_dir.mkdir(parents=True, exist_ok=True)
            (upload_dir / filename).write_bytes(data)

        items = _read()
        items.insert(
            0,
            {
                "id": uuid.uuid4().hex,
                "title": self.title.strip(),
                "category": self.category,
                "description": self.description.strip(),
                "date": self.achieved_on,
                "image": filename,
            },
        )
        _write(items)
        self.items = items
        self.title = ""
        self.description = ""
        self.achieved_on = ""
        self.message = "Berhasil disimpan!"
        return rx.clear_selected_files("upload_img")

    def delete(self, item_id: str):
        if not self.is_admin:
            return
        items = _read()
        for it in items:
            if it["id"] == item_id and it.get("image"):
                (rx.get_upload_dir() / Path(it["image"]).name).unlink(missing_ok=True)
        items = [it for it in items if it["id"] != item_id]
        _write(items)
        self.items = items
        self.message = "Item dihapus."
def item_card(item: dict) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.cond(
                item["image"] != "",
                rx.image(
                    src=rx.get_upload_url(item["image"]),
                    width="100%",
                    max_height="220px",
                    object_fit="cover",
                    border_radius="8px",
                ),
            ),
            rx.text(item["title"], weight="bold", size="4", color="#191919"),
            rx.cond(
                item["date"] != "",
                rx.text(item["date"], size="1", color="var(--gray-11)"),
            ),
            rx.text(
                item["description"],
                size="2",
                color="#666666",
                white_space="pre-wrap",
            ),
            align_items="start",
            spacing="2",
            width="100%",
        ),
        width="100%",
        padding="4",
        background="#ffffff",
        border="1px solid #e0dfd5",
        border_radius="12px",
    )
def achievements_section() -> rx.Component:
    return rx.vstack(
        rx.heading("🏆 Pencapaian & Prestasi", size="5", color="#191919", width="100%"),
        rx.foreach(
            AchievementState.items,
            lambda item: rx.cond(
                item["category"] == "Achievement",
                item_card(item),
                rx.fragment()
            )
        ),
        width="100%",
        spacing="3",
    )

def certifications_section() -> rx.Component:
    return rx.vstack(
        rx.heading("📜 Sertifikasi & Lisensi", size="5", color="#191919", width="100%"),
        rx.foreach(
            AchievementState.items,
            lambda item: rx.cond(
                item["category"] == "Certification",
                item_card(item),
                rx.fragment()
            )
        ),
        width="100%",
        spacing="3",
    )
def _login_card() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("Admin Login", size="6"),
            rx.input(
                type="password",
                placeholder="Password Admin",
                value=AchievementState.password,
                on_change=AchievementState.set_password,
                width="100%",
            ),
            rx.button("Masuk", on_click=AchievementState.login, width="100%", background="#0a66c2", color="white"),
            rx.cond(
                AchievementState.login_error != "",
                rx.text(AchievementState.login_error, color="red", size="2"),
            ),
            spacing="3",
            width="100%",
        ),
        width="100%",
        padding="4",
    )
def _admin_item(item: dict) -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.hstack(
                rx.badge(item.get("category", "Achievement"), color_scheme="blue", size="1"),
                rx.text(item["title"], weight="bold", size="2"),
                spacing="2",
                align_items="center",
            ),
            rx.text(item["date"], size="1", color="var(--gray-11)"),
            align_items="start",
            spacing="1",
        ),
        rx.spacer(),
        rx.button(
            "Hapus",
            color_scheme="red",
            variant="soft",
            size="1",
            on_click=lambda: AchievementState.delete(item["id"]),
        ),
        width="100%",
        align_items="center",
    )
def _editor() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.heading("Kelola Portofolio", size="5"),
            rx.spacer(),
            rx.button("Keluar", variant="soft", size="1", on_click=AchievementState.logout),
            width="100%",
            align_items="center",
        ),
        rx.card(
            rx.vstack(
                rx.select(
                    ["Achievement", "Certification"],
                    value=AchievementState.category,
                    on_change=AchievementState.set_category,
                    width="100%",
                ),
                rx.input(placeholder="Judul (Contoh: Juara 2 Lari 100m / Sertifikat Python)",
                         value=AchievementState.title, on_change=AchievementState.set_title, width="100%"),
                rx.input(type="date", value=AchievementState.achieved_on, on_change=AchievementState.set_achieved_on,
                         width="100%"),
                rx.text_area(placeholder="Keterangan singkat...", value=AchievementState.description,
                             on_change=AchievementState.set_description, rows="3", width="100%"),
                rx.upload(rx.text("Klik atau drop file foto/sertifikat di sini", size="2"), id="upload_img",
                          max_files=1, width="100%"),
                rx.text(rx.selected_files("upload_img"), size="1"),
                rx.button("Simpan Data", width="100%",
                          on_click=lambda: AchievementState.save(rx.upload_files(upload_id="upload_img"))),
                rx.cond(AchievementState.message != "", rx.text(AchievementState.message, size="2")),
                spacing="3",
                width="100%",
            ),
            width="100%",
            padding="4",
        ),
        rx.heading("Daftar Data Saat Ini", size="4"),
        rx.foreach(AchievementState.items, _admin_item),
        rx.link("Lihat Web Utama", href="/"),
        spacing="3",
        width="100%",
    )
def admin_page() -> rx.Component:
    return rx.center(
        rx.box(
            rx.cond(AchievementState.is_admin, _editor(), _login_card()),
            width="100%",
            max_width="500px",
            padding="4",
        ),
        min_height="100vh",
        background="#f3f2ef",
    )