# Spesifikasi Desain: Presentasi IMATIKA FT-KMUP pada PKKMB FT 2026

Dokumen ini memuat spesifikasi lengkap rancangan presentasi interaktif untuk Ikatan Mahasiswa Teknik Informatika Fakultas Teknik Keluarga Mahasiswa Universitas Pancasila (IMATIKA FT-KMUP) pada kegiatan Pengenalan Kehidupan Kampus Mahasiswa Baru (PKKMB) Fakultas Teknik 2026.

---

## 1. Konteks dan Sasaran

- **Acara**: PKKMB FT Universitas Pancasila 2026
- **Audiens**: Mahasiswa Baru Teknik Informatika Angkatan 2026
- **Alokasi Waktu**: 20 Menit
- **Tujuan Utama**:
  - Memperkenalkan IMATIKA sebagai wadah berproses, berkreasi, dan menyalurkan aspirasi resmi mahasiswa IT.
  - Menciptakan suasana yang hangat, aman, dan bersahabat bagi mahasiswa baru.
  - Mendorong audiens untuk langsung mengikuti akun Instagram resmi `@imatika_ftkmup`.
- **Gaya Bahasa**: Menerapkan pedoman *humanizer* (bahasa Indonesia lugas, akrab, tanpa jargon berlebihan, tanpa kalimat klise seperti "not X but Y", dan tanpa tanda pisah em-dash yang berlebihan).

---

## 2. Palet Warna dan Tipografi

Palet warna diturunkan langsung dari identitas logo IMATIKA FT-KMUP dan disesuaikan dengan kontras layar presentasi:

- **Navy Blue (Warna Utama Logo)**: `#201e72`
- **Gold / Kuning (Aksen Logo)**: `#facc15`
- **Sky Blue (Aksen Terang)**: `#38bdf8`
- **Latar Belakang Slide**: Slate Gelap `#0b0f19` ke `#0f172a`
- **Warna Teks Utama**: `#f8fafc` (putih gading)
- **Warna Teks Sekunder**: `#94a3b8` (abu-abu netral)
- **Tipografi**:
  - Judul dan isi: Sans-serif modern (Inter / system font)
  - Struktur dan kode: Monospace (Fira Code / JetBrains Mono)

---

## 3. Arsitektur Teknis (Reveal.js)

- **Framework**: `reveal.js` versi 5.x via CDN terpercaya (cdnjs / jsdelivr), sehingga file `index.html` dapat dijalankan mandiri di browser secara langsung.
- **Plugin Reveal.js**:
  - `RevealHighlight`: Untuk penyorotan sintaks kode C++ dan animasi baris bertahap (`data-line-numbers`).
- **Logo Pojok Permanen**:
  - Logo Universitas Pancasila di pojok kanan atas.
  - Logo IMATIKA di pojok kiri atas (muncul menetap setelah transisi Slide 3 ke Slide 4).
- **Mekanisme Auto-Animate Indikator**:
  - Menggunakan atribut `data-auto-animate` antar section.
  - Tiga kotak pembuka menggunakan `data-id="box-1"`, `data-id="box-2"`, dan `data-id="box-3"`.

---

## 4. Rincian dan Narasi Slide (Total 11 Slide / 20 Menit)

### Slide 1: Pembuka Minimalis (1.5 Menit)
- **Visual**: Latar gelap dengan 3 kotak berwarna polos di bagian bawah (`#201e72`, `#facc15`, `#38bdf8`) sebagai penanda awal.
- **Teks**: "PKKMB FT 2026 // Teknik Informatika".
- **Narasi**: Sapaan awal yang santai menyapa mahasiswa baru angkatan 2026.

### Slide 2: Selamat Datang Angkatan 2026 (1.5 Menit)
- **Visual (`data-auto-animate`)**: Ketiga kotak bertransformasi menuju tengah slide membentuk bingkai fokus bersatu.
- **Teks**: "Selamat Datang di Kampus FT-KMUP".
- **Narasi**: Memberikan selamat kepada maba yang telah resmi menjadi bagian dari keluarga besar IT FT-KMUP.

### Slide 3: Reveal Identitas IMATIKA (1.5 Menit)
- **Visual (`data-auto-animate`)**: Bingkai tengah membuka dan memunculkan `Logo IMATIKA.png` berukuran besar.
- **Teks**: "IKATAN MAHASISWA TEKNIK INFORMATIKA".
- **Subteks**: "Fakultas Teknik Universitas Pancasila".
- **Narasi**: Memperkenalkan nama dan identitas IMATIKA sebagai lembaga resmi mahasiswa IT tingkat program studi.

### Slide 4: Ruang dan Wadah Aspirasi Mahasiswa IT (2.5 Menit)
- **Visual (`data-auto-animate`)**: Logo IMATIKA mengecil dan berpindah ke pojok kiri atas. Logo Universitas Pancasila tampil di pojok kanan atas.
- **Poin Presentasi**:
  - Perkuliahan di jurusan IT bukan cuma tentang menyelesaikan tugas coding di laboratorium.
  - Ada saatnya mahasiswa menghadapi kendala fasilitas komputer, persoalan akademik, atau butuh sarana mengusulkan kegiatan.
  - IMATIKA bertindak sebagai penyambung aspirasi mahasiswa IT ke tingkat jurusan maupun fakultas.
  - Tempat mahasiswa merasa aman untuk berpendapat dan bertumbuh bersama.

### Slide 5: Struktur Organisasi dalam Kode C++ (3 Menit)
- **Visual**: Window code editor menyerupai file `imatika_ftkmup.hpp`.
- **Kode C++**:
  ```cpp
  class IMATIKA_FTKMUP {
  public:
      // Badan Pengurus Harian Inti
      string ketua;
      string wakil_ketua;
      string sekretaris;
      string bendahara;

      // Bidang I: Akademik
      struct BidangAkademik {
          DivisiPenelitian techno_it;
          DivisiPengajaranKaderisasi kelas_organisasi;
      } bidang_1;

      // Bidang II: Minat dan Bakat
      struct BidangMinatBakat {
          DivisiOlahraga turnamen_positif;
          DivisiPSDM komunitas_dan_softskill;
      } bidang_2;

      // Bidang III: Kesejahteraan Mahasiswa
      struct BidangKesma {
          DivisiSosial pengabdian_masyarakat;
          DivisiKerohanian buka_bersama;
      } bidang_3;

      // Bidang IV: Humas dan Inventaris
      struct BidangHumasInventaris {
          DivisiHumas studi_banding;
          DivisiMediaKreatif publikasi_dan_konten;
          DivisiInventaris sarana_dan_gedung;
      } bidang_4;
  };
  ```
- **Tahapan Highlight (`data-line-numbers`)**:
  - Langkah 1: Garis BPH Inti (Ketua, Wakil Ketua, Sekretaris, Bendahara).
  - Langkah 2: Garis Bidang I.
  - Langkah 3: Garis Bidang II.
  - Langkah 4: Garis Bidang III.
  - Langkah 5: Garis Bidang IV.

### Slide 6: Bidang I - Akademik (2 Menit)
- **Fokus**: Pendidikan dan Penelitian.
- **Divisi & Proker**:
  - *Divisi Penelitian*: **Techno IT** (eksplorasi inovasi teknologi, workshop perangkat lunak, dan dasar penelitian komputer).
  - *Divisi Pengajaran / Kaderisasi*: **Kelas Organisasi** (pelatihan kepemimpinan, persidangan mahasiswa, serta pembekalan kerja organisasi).

### Slide 7: Bidang II - Minat dan Bakat (2 Menit)
- **Fokus**: Olahraga, Seni, dan Pengembangan Potensi.
- **Divisi & Proker**:
  - *Divisi Olahraga*: **POSITIF** (Pekan Olahraga Mahasiswa Teknik Informatika, turnamen olahraga internal tahunan).
  - *Divisi PSDM*: Wadah komunitas santai seperti mabar e-sports (Mobile Legends, Valorant) dan olahraga rutin bersama senior serta rekan seangkatan.

### Slide 8: Bidang III - Kesejahteraan Mahasiswa (2 Menit)
- **Fokus**: Sosial dan Kerohanian.
- **Divisi & Proker**:
  - *Divisi Sosial*: **Pengabdian Masyarakat** (kegiatan sosial mahasiswa IT untuk masyarakat dan lingkungan sekitar kampus).
  - *Divisi Kerohanian*: **Bukber (Buka Bersama)** (silaturahmi lintas angkatan di bulan Ramadan dan kegiatan kebersamaan).

### Slide 9: Bidang IV - Humas dan Inventaris (2 Menit)
- **Fokus**: Hubungan Luar, Aset, dan Media.
- **Divisi & Proker**:
  - *Divisi Humas*: **STUBAN (Studi Banding)** (kunjungan studi ke kampus lain atau perusahaan industri teknologi).
  - *Divisi Media Kreatif*: Pengelolaan identitas visual, video, dan media informasi resmi.
  - *Divisi Inventaris*: Pemeliharaan sarana prasarana serta fasilitas gedung sekretariat IMATIKA.

### Slide 10: Terhubung dengan IMATIKA (Call to Action) (2 Menit)
- **Fokus Tunggal**: Akun Instagram Resmi `@imatika_ftkmup`.
- **Komponen Visual**:
  - Mockup kartu profil Instagram IMATIKA yang bersih.
  - Kode QR berukuran besar di tengah yang langsung mengarah ke `https://instagram.com/imatika_ftkmup`.
  - Pesan ajakan: Mahasiswa baru dipersilakan mengeluarkan ponsel untuk langsung memindai QR code sekarang.

### Slide 11: Penutup & Tanya Jawab (2 Menit)
- **Konten**:
  - Ucapan terima kasih dan semangat menempuh masa perkuliahan bagi Angkatan 2026.
  - Alamat Sekretariat: Gedung IMATIKA FT-KMUP, Srengseng Sawah, Jagakarsa.
  - Sesi tanya jawab santai dengan audiens.

---

## 5. Kriteria Verifikasi

1. File `index.html` dapat dibuka langsung di Google Chrome dan browser modern tanpa error konsol.
2. Animasi perpindahan 3 kotak (Slide 1-2) menuju logo IMATIKA (Slide 3) dan bergeser ke pojok atas (Slide 4) berjalan lancar.
3. Fitur code highlight pada Slide 5 berjalan berurutan sesuai tombol navigasi keyboard (panah / spasi).
4. Kedua logo (`Logo Universitas Pancasila.png` dan `Logo IMATIKA.png`) termuat dengan proporsi rapi dan tajam.
5. QR Code Instagram berfungsi baik saat dipindai kamera ponsel.
