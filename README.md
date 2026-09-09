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

## 🛠️ Pembangunan Tempatan (*Local Development*)

Sekiranya anda ingin menambah atau mengemaskini soalan:

```bash
# 1. Edit data dalam app_data.json
# 2. Jana semula index.html
node generate_app.js
```

---

## 📄 Struktur Peperiksaan & Skor Sasaran (CPRE FL)

- **Jumlah Soalan**: 45 Soalan
- **Jumlah Markah**: 63 Markah
- **Had Masa**: 75 Minit (~1.6 minit/soalan)
- **Markah Kelayakan (*Passing Mark*)**: 70.0% (44.1 Markah)
- **Format Soalan**:
  - **A-Type** (Single Choice • 1 Markah)
  - **P-Type** (Multiple Choice • 1–3 Markah)
  - **K-Type** (Matrix True/False • 2 Markah)
