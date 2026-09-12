# 🎯 IREB CPRE Foundation Level • Interactive Exam Simulator & Study Hub

Platform ulangkaji dan simulasi peperiksaan interaktif berasaskan web kendiri (*single-page application*) yang dibina khusus untuk persediaan menghadapi peperiksaan persijilan **IREB Certified Professional for Requirements Engineering (CPRE) Foundation Level (Syllabus v3.2 / v3.4)**.

🌐 **Akses Laman Web Langsung (GitHub Pages):** [https://cs-mirakim.github.io/cpre-akim/](https://cs-mirakim.github.io/cpre-akim/)

---

## 📚 3 Modul Set Peperiksaan Lengkap

Aplikasi ini menyokong **3 set peperiksaan berasingan** dengan simulasi penilaian masa nyata (*real-time scoring engine*):

### 1. 📘 Set Latihan Rasmi (IREB Official Practice Exam)
* **Format:** 45 Soalan • **70.0 Mata** (Lulus: 49.0 Mata / 70%)
* **Sumber:** Berpandukan 100% dokumen rasmi *IREB Questionnaire & Correction Aid*.
* **Tujuan:** Menguji pemahaman asas menyeluruh mengikut soalan piawai antarabangsa IREB.

### 2. 📙 Set Ramalan Peperiksaan G (Slip Sebenar)
* **Format:** 45 Soalan • **72.0 Mata** (Lulus: 50.40 Mata / 70%)
* **Struktur:** 34 soalan teras rasmi + 11 soalan ramalan variasi baharu yang mematuhi agihan markah slip peperiksaan sebenar (EU1–EU7).
* **Rajah UML Baharu:** Termasuk rajah *UML Class Multiplicity* (Q18), *Order State Machine* (Q20), *Activity Concurrency Fork/Join* (Q21), dan *Activity Logistics Decision/Merge* (Q23).

### 3. 🚢 Set Ramalan Peperiksaan G+ (Maritime & Authentic Pool Leaks)
* **Format:** 45 Soalan • **72.0 Mata** (Lulus: 50.40 Mata / 70%)
* **Struktur:** 23 soalan dinaik taraf berpandukan perkongsian komuniti calon peperiksaan (*exam pool debriefs*) dan senario sistem maritim/pelabuhan.
* **Sorotan Khas:** Rajah *Maritime Vessel Navigation State Machine* (Q20), soalan *Tacit Knowledge* (Q24), *Kano Model Dynamics* (Q26), *Fagan Inspection Roles* (Q33), *Pre-RS Traceability* (Q39), dan *Wiegers Prioritization Formula* (Q42).

---

## 🌟 Ciri-Ciri Utama Aplikasi

* 💡 **Dwi-Mod Pembelajaran (Study Mode vs Quiz Mode):**
  * **Study Mode:** Semak terus jawapan rasmi berserta huraian mendalam (*whyCorrect*, *whyWrong*, petikan *Handbook*, dan tip mnemonik) bagi setiap soalan.
  * **Quiz Mode:** Simulasi peperiksaan sebenar dengan sistem penandaan interaktif, pemasa masa nyata (*Live Timer HUD*), dan pengiraan markah serta peratusan kelulusan secara automatik.
* 🖼️ **Gambar Rajah UML Berdefinisi Tinggi & Zum Penuh (*Modal Lightbox*):**
  * Gambar rajah kelas, *state machine*, dan aktiviti yang tajam dan boleh dizum skrin penuh untuk pemeriksaan rapi.
* 🔍 **Carian Pantas & Penapis Pintar:**
  * Penapis soalan mengikut **7 Educational Units (EU)** atau jenis soalan (**A**, **P**, **K**).
  * Pintasan carian papan kekunci (`/` untuk cari, `Esc` untuk batal).
* ⭐ **Sistem Bookmark & Semakan Soalan Silap:**
  * Tandakan soalan sukar (*Star Bookmark*) dan tapis soalan yang dijawab salah untuk ulangkaji bersasar.
* 🌓 **Tema Gelap & Terang (*Dark / Light Mode*):**
  * Reka bentuk moden berkontras tinggi (*shadcn/ui style*) yang mesra mata untuk sesi ulangkaji yang panjang.
* 📋 **Pusat Rujukan 1-Muka Surat (*Summary & Cheat Sheets*):**
  * Akses pantas kepada ringkasan peraturan templat *SOPHIST*, 4 faset proses RE, matriks kebolehkesanan (*Traceability*), dan jenis-jenis konflik.

---

## 📊 Format Soalan & Formula Pemarkahan IREB

| Jenis Soalan | Jenis Pilihan | Kaedah Pemarkahan & Peraturan |
| :--- | :--- | :--- |
| **Jenis A** *(Single-Choice)* | 1 Pilihan Betul | • Pilih **tepat 1** jawapan.<br>• **1.0 atau 2.0 Markah** jika betul, 0 markah jika salah. |
| **Jenis P** *(Multiple-Choice)* | 2 atau 3 Pilihan Betul | • Pilih bilangan jawapan mengikut arahan soalan.<br>• Markah penuh (1.0–3.0 Pts) jika semua betul.<br>• Markah separa berkadar jika sebahagian betul.<br>• **Penalti:** Menanda pilihan salah akan menolak markah bahagian tersebut (skor minimum soalan adalah 0 pt). |
| **Jenis K** *(True/False Matrix)* | 4 Baris Kenyataan | • Setiap baris bernilai **0.50 Markah** (Jumlah 2.0 Pts):<br>  - 4/4 betul = **2.00 Pts**<br>  - 3/4 betul = **1.50 Pts** (atau 1.0 pt bergantung skala exam)<br>  - 2/4 betul = **1.00 Pt**<br>  - 1/4 betul = **0.50 Pt**<br>  - Tiada markah negatif. |

---

## 🧠 7 Unit Pembelajaran Rasmi IREB (EU1 – EU7)

1. **EU 1: Pengenalan & Gambaran Keseluruhan RE** *(Aktiviti Teras: Elicit, Document, Validate, Manage • 3 Kategori Keperluan)*
2. **EU 2: Prinsip Asas RE** *(Prinsip Shared Understanding, Sempadan Sistem & Konteks, Nilai & Kepentingan)*
3. **EU 3: Hasil Kerja & Amalan Dokumentasi** *(Spesifikasi Teks, SOPHIST Sentence Template, Model UML: Use Case, Class, Activity, State Machine)*
4. **EU 4: Amalan Pengeluran & Penghuraian Keperluan** *(Teknik Elisitasi, Pengetahuan Tersirat/Tacit, Model Kano, Resolusi Konflik)*
5. **EU 5: Struktur Proses & Kerja** *(4 Faset Proses RE: Time, Purpose, Target, Interaction)*
6. **EU 6: Amalan Pengurusan Keperluan** *(Atribut Keperluan, Pre/Post-RS Traceability, Pengurusan Perubahan CCB, Baseline & Pengutamaan)*
7. **EU 7: Sokongan Alatan** *(Kriteria Pemilihan Alatan RE, Integrasi & Kawalan Versi)*

---

## 💡 Tips & Strategi Menduduki Peperiksaan

* **Untuk Soalan Jenis K (True / False):**
  * Berhati-hati dengan kenyataan yang menggunakan perkataan mutlak/ekstrem seperti *only*, *strictly forbids*, *under no circumstances* — selalunya **FALSE**.
  * Kenyataan yang fleksibel dan kontekstual (*can*, *may*, *some degree of*) selalunya **TRUE**.
  * **Jangan panik jika semua baris adalah True** — IREB kerap mempunyai skema di mana kesemua 4 kenyataan adalah benar.
* **Untuk Soalan Jenis A (Single-Choice):**
  * Gunakan teknik penyingkiran (*elimination*) untuk membuang 2 pilihan yang jelas bertentangan dengan etika/standard IREB.
* **Untuk Soalan Jenis P (Multiple-Choice):**
  * Perhatikan bilangan jawapan yang diminta dalam kurungan soalan. Menanda pilihan berlebihan akan mengakibatkan pemotongan markah penalti.
* **SOPHIST Modal Verbs:**
  * **`SHALL`** = Wajib undang-undang (*legally binding commitment*).
  * **`SHOULD`** = Matlamat atau cadangan masa depan (*desirable goal*).
  * **`WILL`** = Pernyataan fakta/maklumat masa depan.
  * **Ayat Pasif** dilarang kerana menghilangkan identiti pelaku (*actor*).

---

## 📄 Hak Cipta & Rujukan Silibus

Kandungan pembelajaran dan format soalan diselaraskan berpandukan sukatan pelajaran terbuka antarabangsa oleh **International Requirements Engineering Board (IREB e.V.)**:
* *CPRE Foundation Level Syllabus Version 3.2.0 / 3.4*
* *CPRE Foundation Level Handbook Version 1.2.0*
* *IREB Standard Glossary of Requirements Engineering Terminology Version 2.2.0*
