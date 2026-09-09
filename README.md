# CPRE FL 3.3.2 Study Master • IREB Exam Hub

Platform ulangkaji interaktif berasaskan web statik untuk persediaan peperiksaan **IREB Certified Professional for Requirements Engineering (CPRE) Foundation Level 3.3.2**.

Dibina khusus untuk pembelajaran pantas, mesra mudah alih (*mobile-first*), berkontras tinggi (*shadcn/ui style*), dan bebas *AI-slop*.

---

## 🌟 Ciri-Ciri Utama

1. **45 Soalan Lengkap Mengikut 7 Educational Units (EU)**:
   - Dilengkapi teks soalan penuh, pilihan jawapan, rasional jawapan betul, dan amaran perangkap (*Trap Alert*).
2. **Gambar Rajah Rasmi Berdefinisi Tinggi**:
   - Gambar rajah rasmi (Q18, Q20, Q21, Q23) diekstrak terus daripada set soalan peperiksaan rasmi dengan sokongan modal zum skrin penuh (*fullscreen lightbox*).
3. **Dua Mod Pembelajaran**:
   - **Study Mode**: Paparan penuh jawapan dan huraian mendalam untuk ulangkaji.
   - **Quiz Mode**: Mod ujian interaktif dengan pengiraan markah langsung (*Live Quiz HUD*), pemarkahan IREB (A, P, K-Type), dan penjejak skor semasa.
4. **Penapis Pintar & Bookmark**:
   - Tanda soalan bertanda bintang (*Star Bookmark*) dan tapis soalan fokus dengan 1-klik.
   - Carian kata kunci pantas dengan sokongan pintasan papan kekunci (`/` dan `Esc`).
5. **Tema Mod Gelap & Terang (*Dark & Light Mode*)**:
   - Kontras visual yang jelas untuk keselesaan membaca dalam jangka masa panjang.
6. **Cheat Sheet 1-Muka Surat**:
   - Ringkasan konsep utama (*Natural Language Defects*, *Model-based RE Rules*, *EU5 Process Facets*, *EU6 Management & Baselines*).

---

## 🚀 Cara Aktifkan GitHub Pages (Percuma)

Aplikasi ini adalah **100% fail statik kendiri (*self-contained `index.html`*)**, jadi anda boleh *deploy* secara percuma ke GitHub Pages dalam beberapa saat:

1. Pergi ke repositori anda di GitHub: [https://github.com/cs-mirakim/cpre-akim](https://github.com/cs-mirakim/cpre-akim)
2. Klik tab **Settings** (di bar navigasi atas repositori).
3. Di menu sebelah kiri, klik pada bahagian **Pages**.
4. Di bawah **Build and deployment**:
   - **Source**: Pilih `Deploy from a branch`.
   - **Branch**: Pilih `main` dan folder `/ (root)`.
   - Klik butang **Save**.
5. Tunggu kira-kira 1–2 minit, laman web anda akan siap diakses di URL:
   `https://cs-mirakim.github.io/cpre-akim/`

---

## 📁 Struktur Folder Projek

```text
cpre/
├── index.html                    # 🚀 Single-page app (GitHub Pages live entry point)
├── README.md                     # 📖 Dokumentasi & panduan projek
├── .gitignore                    # 🛡️ Konfigurasi Git ignore
│
├── assets/                       # 🎨 Aset media & gambar
│   └── diagrams/                 # 🖼️ Gambar rajah rasmi soalan (Q18, Q20, Q21, Q23)
│
├── data/                         # 📊 Pangkalan data JSON
│   ├── app_data.json             # ⭐ Data 45 soalan & huraian rasmi (70 markah)
│   └── raw/                      # 🗄️ Arkib ekstraksi data terdahulu
│
├── docs/                         # 📚 5 Dokumen Rujukan Rasmi IREB 2025
│   ├── AnswersToThePracticeExam_EN_2025-09-11.pdf
│   ├── CPRE Foundation Level - Handbook V.1.2.0.pdf
│   ├── CPRE Foundation Level - Syllabus V.3.2.0.pdf
│   ├── CPRE Glossary V.2.2.0.pdf
│   └── IREB_CPRE_FL_Questionnaire_Set_Public_EN_2025-09-11.pdf
│
├── scripts/                      # ⚙️ Skrip Bina & Ujian Integriti
│   ├── generate_app.js           # 🔨 Compiler membina index.html
│   ├── generate_authentic_dataset.py # 🧠 Penjana dataset rasmi IREB
│   ├── test_exam_integrity.py    # 🧪 Ujian automatik skema & markah
│   └── scratch/                  # 🔬 Skrip audit & analisis ekstraksi
│
└── legacy/                       # 📦 Versi draf terdahulu
    ├── Cpre-Full-Guide.html
    └── Cpre-Full-Guide-Fixed-V2.html
```

---

## 🛠️ Pembangunan & Penjanaan Semula (*Development*)

Sekiranya anda ingin mengemaskini soalan atau menjana semula fail web:

```bash
# 1. Bina dataset rasmi dari skema
python scripts/generate_authentic_dataset.py

# 2. Uji integriti 45 soalan & markah (70 Pts)
python scripts/test_exam_integrity.py

# 3. Kompilasi semula index.html
node scripts/generate_app.js
```

---

## 📄 Struktur Peperiksaan & Skor Sasaran (IREB CPRE FL)

- **Jumlah Soalan**: 45 Soalan (EU1 hingga EU7)
- **Jumlah Markah Penuh**: 70.00 Markah
- **Had Masa**: 75 Minit (~1.6 minit/soalan)
- **Markah Kelayakan (*Passing Mark*)**: 70.00% (49.00 Markah)
- **Format Soalan**:
  - **A-Type** (Single Choice • 1–2 Markah)
  - **P-Type** (Multiple Choice • 1–2 Markah dengan penalti jika salah)
  - **K-Type** (Matrix True/False • 2 Markah: 4/4 betul = 2 pts, 3/4 betul = 1 pt)

