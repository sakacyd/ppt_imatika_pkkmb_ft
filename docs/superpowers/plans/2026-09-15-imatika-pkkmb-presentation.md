# Implementasi Presentasi IMATIKA FT-KMUP PKKMB 2026

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Membangun slide presentasi interaktif dan minimalis berbasis reveal.js untuk IMATIKA FT-KMUP pada PKKMB FT 2026 lengkap dengan speaker notes dan naskah presentasi 20 menit.

**Architecture:** File presentasi mandiri `index.html` dengan CSS custom `assets/css/style.css`, plugin RevealHighlight dan RevealNotes, animasi multi-step C++ code, auto-animate logo, serta naskah presenter terpisah di `speaker_notes.md`.

**Tech Stack:** reveal.js 5.x, Highlight.js (C++ syntax), HTML5/CSS3, Python (verifikasi file & server pengujian).

## Global Constraints

- Palet warna brand IMATIKA: Navy Blue (`#201e72`), Gold (`#facc15`), Sky Blue (`#38bdf8`), Latar Gelap (`#0b0f19` / `#0f172a`).
- Bahasa dan penulisan menerapkan kaidah *humanizer*: santun, akrab, lugas, tanpa klise "not X but Y", tanpa tanda em-dash berlebihan.
- Slide 4 menggunakan istilah "IT" (bukan TI) dan fokus pada penyaluran aspirasi mahasiswa.
- Slide 10 Call to Action hanya difokuskan pada akun Instagram `@imatika_ftkmup`.
- Kode C++ struktur organisasi mendukung line-highlighting multi-step.

---

### Task 1: Setup Struktur Asset dan Styling Kustom IMATIKA

**Files:**
- Create: `assets/css/style.css`
- Test: `test_assets.py`

**Interfaces:**
- Consumes: `Logo IMATIKA.png`, `Logo Universitas Pancasila.png`
- Produces: CSS custom rules untuk tema gelap minimalis, layout kotak auto-animate, frame editor kode C++, dan posisi logo pojok permanen.

- [ ] **Step 1: Tulis script verifikasi asset dan CSS**

```python
# test_assets.py
import os

def test_assets():
    assert os.path.exists("Logo IMATIKA.png"), "Logo IMATIKA tidak ditemukan"
    assert os.path.exists("Logo Universitas Pancasila.png"), "Logo UP tidak ditemukan"
    assert os.path.exists("assets/css/style.css"), "File style.css belum dibuat"
    with open("assets/css/style.css", "r", encoding="utf-8") as f:
        content = f.read()
    assert "#201e72" in content, "Warna navy IMATIKA tidak ada di style.css"
    assert "#facc15" in content, "Warna gold IMATIKA tidak ada di style.css"
    print("Asset dan CSS test PASSED")

if __name__ == "__main__":
    test_assets()
```

- [ ] **Step 2: Jalankan test dan pastikan gagal karena style.css belum ada**

Run: `python test_assets.py`
Expected: FAIL with "File style.css belum dibuat"

- [ ] **Step 3: Buat `assets/css/style.css` dengan variabel CSS dan styling komponen**

Buat direktori `assets/css` dan implementasikan CSS dengan class layout, warna brand, typography, dan code window frame.

- [ ] **Step 4: Jalankan kembali test untuk memastikan lolos**

Run: `python test_assets.py`
Expected: PASS

- [ ] **Step 5: Commit perubahan**

```bash
git add assets/css/style.css test_assets.py
git commit -m "feat: setup custom style and asset verification"
```

---

### Task 2: Implementasi File Utama Presentasi `index.html` Reveal.js

**Files:**
- Create: `index.html`
- Test: `test_slides.py`

**Interfaces:**
- Consumes: `assets/css/style.css`, CDN reveal.js 5.x (reveal.css, theme/black.css, highlight monokai.css, reveal.js, plugin highlight.js, plugin notes.js)
- Produces: 11 slide interaktif lengkap dengan `data-auto-animate`, `data-line-numbers` pada kode C++, dan tag `<aside class="notes">` pada setiap slide.

- [ ] **Step 1: Tulis script verifikasi konten dan struktur HTML**

```python
# test_slides.py
import os
import re

def test_slides():
    assert os.path.exists("index.html"), "index.html tidak ditemukan"
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()
    
    # Periksa 11 section utama slide
    sections = re.findall(r'<section[\s>]', html)
    assert len(sections) >= 11, f"Jumlah slide kurang dari 11: ditemukan {len(sections)}"
    
    # Periksa keberadaan auto-animate data-id
    assert 'data-id="box-1"' in html, "data-id box-1 tidak ditemukan"
    assert 'data-id="imatika-logo"' in html, "data-id imatika-logo tidak ditemukan"
    
    # Periksa code highlight C++
    assert 'data-line-numbers' in html, "Atribut data-line-numbers tidak ditemukan pada kode"
    assert 'class IMATIKA_FTKMUP' in html, "Class C++ IMATIKA tidak ditemukan"
    
    # Periksa slide 4 IT & aspirasi
    assert 'IT' in html, "Istilah IT harus ada pada slide aspirasi"
    
    # Periksa slide 10 CTA Instagram
    assert '@imatika_ftkmup' in html, "Akun @imatika_ftkmup harus ada di slide CTA"
    
    # Periksa speaker notes
    notes = re.findall(r'<aside class="notes">', html)
    assert len(notes) >= 10, f"Speaker notes belum lengkap: ditemukan {len(notes)}"
    print("Slide structure test PASSED")

if __name__ == "__main__":
    test_slides()
```

- [ ] **Step 2: Jalankan test dan pastikan gagal karena `index.html` belum ada**

Run: `python test_slides.py`
Expected: FAIL with "index.html tidak ditemukan"

- [ ] **Step 3: Buat `index.html` secara utuh**

Susun 11 slide dengan rapi, minimalis, dan elegan:
- Slide 1-3: Sequence auto-animate pembuka (3 kotak brand color bertransformasi ke logo tengah).
- Slide 4: Ruang dan aspirasi mahasiswa IT dengan logo UP dan IMATIKA di pojok.
- Slide 5: Editor C++ class `IMATIKA_FTKMUP` dengan highlight bertahap per posisi kepengurusan.
- Slide 6-9: Pemaparan ringkas 4 bidang dan prokernya.
- Slide 10: Call to Action Instagram `@imatika_ftkmup` dengan SVG QR code tajam.
- Slide 11: Sesi tanya jawab dan kontak sekretariat.
- Injeksi `<aside class="notes">` pada setiap slide untuk panduan presenter.

- [ ] **Step 4: Jalankan test untuk memverifikasi struktur**

Run: `python test_slides.py`
Expected: PASS

- [ ] **Step 5: Commit perubahan**

```bash
git add index.html test_slides.py
git commit -m "feat: implement reveal.js presentation slides with speaker notes"
```

---

### Task 3: Penyusunan Naskah Presenter Lengkap `speaker_notes.md`

**Files:**
- Create: `speaker_notes.md`
- Test: `test_notes.py`

**Interfaces:**
- Consumes: Rincian 11 slide dari `index.html`
- Produces: Panduan narasi kata-demi-kata (speech transcript / cheat-sheet) dengan alokasi menit, cue klik/spasi keyboard, dan gaya bicara santai mahasiswa tingkat atas ke maba 2026.

- [ ] **Step 1: Tulis script verifikasi naskah presenter**

```python
# test_notes.py
import os

def test_speaker_notes():
    assert os.path.exists("speaker_notes.md"), "speaker_notes.md tidak ditemukan"
    with open("speaker_notes.md", "r", encoding="utf-8") as f:
        notes = f.read()
    assert "Slide 1" in notes, "Slide 1 tidak ada di speaker notes"
    assert "Slide 11" in notes, "Slide 11 tidak ada di speaker notes"
    assert "20 Menit" in notes or "20 menit" in notes, "Total durasi 20 menit tidak ada"
    assert "@imatika_ftkmup" in notes, "Akun Instagram tidak ada di notes"
    print("Speaker notes test PASSED")

if __name__ == "__main__":
    test_speaker_notes()
```

- [ ] **Step 2: Jalankan test dan pastikan gagal**

Run: `python test_notes.py`
Expected: FAIL with "speaker_notes.md tidak ditemukan"

- [ ] **Step 3: Tulis naskah lengkap di `speaker_notes.md`**

Tulis naskah per slide lengkap dengan petunjuk waktu, kapan harus menekan spasi, intonasi, dan materi yang disampaikan.

- [ ] **Step 4: Jalankan test verifikasi**

Run: `python test_notes.py`
Expected: PASS

- [ ] **Step 5: Commit perubahan**

```bash
git add speaker_notes.md test_notes.py
git commit -m "docs: add full speaker notes and transcript guide for 20-minute PKKMB session"
```

---

### Task 4: Verifikasi Visual dan Interaksi di Browser

**Files:**
- Test: Verifikasi interaktif dan visual melalui browser / server lokal

**Interfaces:**
- Consumes: `index.html`, `assets/css/style.css`, gambar logo
- Produces: Verifikasi bebas error di konsol browser, animasi auto-animate mulus, transisi highlight kode C++ responsif, dan speaker view (tombol 'S') berfungsi normal.

- [ ] **Step 1: Jalankan server HTTP lokal sederhana**

Run: `python -m http.server 8000` (atau verifikasi langsung file via headless/browser tooling)

- [ ] **Step 2: Validasi rendering halaman di browser**

Pastikan:
1. Tidak ada error 404 pada file CSS, gambar logo, atau plugin reveal.js.
2. Animasi perpindahan kotak dan logo berjalan presisi tanpa patah-patah.
3. Penekanan tombol panah kanan menelusuri baris C++ dengan mulus.
4. QR code Instagram dapat dipindai.

- [ ] **Step 3: Bersihkan file pengujian sementara**

```bash
git add test_assets.py test_slides.py test_notes.py
git commit -m "test: record automated verification tests"
```
