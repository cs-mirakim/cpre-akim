import json
import base64
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(ROOT_DIR, 'assets', 'diagrams')
DATA_PATH = os.path.join(ROOT_DIR, 'data', 'app_data.json')

def get_b64(filename):
    path = os.path.join(ASSETS_DIR, filename)
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"
    return ""

img_q18 = get_b64('clean_q18.png')
img_q20 = get_b64('clean_q20.png')
img_q21 = get_b64('clean_q21.png')
img_q23 = get_b64('clean_q23.png')

eus = [
  { "no": 1, "name": "Introduction and Overview of Requirements Engineering", "range": "Q1–Q3", "pts": 4, "qCount": 3 },
  { "no": 2, "name": "Fundamental Principles of Requirements Engineering", "range": "Q4–Q7", "pts": 6, "qCount": 4 },
  { "no": 3, "name": "Work Products and Documentation Practices", "range": "Q8–Q25", "pts": 30, "qCount": 18 },
  { "no": 4, "name": "Practices for Requirements Elaboration", "range": "Q26–Q35", "pts": 14, "qCount": 10 },
  { "no": 5, "name": "Process and Working Structure", "range": "Q36–Q37", "pts": 3, "qCount": 2 },
  { "no": 6, "name": "Management Practices for Requirements", "range": "Q38–Q43", "pts": 10, "qCount": 6 },
  { "no": 7, "name": "Tool Support", "range": "Q44–Q45", "pts": 3, "qCount": 2 }
]

with open(os.path.join(ROOT_DIR, 'scripts', 'scratch', 'questions_authentic_base.json'), 'r', encoding='utf-8') as f:
    raw_questions = json.load(f)

# Comprehensive High-Yield Explanations & Meta
meta_data = {
  1: {
    "euNo": 1,
    "title": "Quality Requirements vs Functional Requirements",
    "correctDisplay": "A=False, B=True, C=False, D=True",
    "whyCorrect": "• B: True. Quality requirements melengkapi functional requirements dengan menetapkan tahap kualiti (cth: performance, usability, security, reliability) yang perlu dicapai oleh fungsi tersebut.\n• D: True. Quality requirements boleh diperincikan (substantiated) menjadi functional requirements baharu (contoh: keperluan keselamatan 'Akses mesti dilindungi' diperincikan kepada fungsi 'Sistem mesti menyediakan Two-Factor Authentication').",
    "whyWrong": "• A: False. Quality requirements merujuk kepada kualiti PRODUK (sistem), bukannya proses pembangunan (keperluan proses dirujuk sebagai Project / Process Requirements).\n• C: False. Quality requirements TIDAK semestinya di-elicit selepas fungsi; dalam praktis RE sebenar, kedua-duanya di-elicit serentak secara berulang (intertwined).",
    "extra": "Handbook Bab 1.1 / Syllabus EO 1.1.1: 3 jenis keperluan mengikut piawaian IREB ialah: 1. Functional Requirements, 2. Quality Requirements, 3. Constraints.",
    "mnemonic": "Quality = Sifat Produk. Boleh melahirkan Functional Requirement baharu (Substantiated)."
  },
  2: {
    "euNo": 1,
    "title": "Core Tasks of the Requirements Engineer",
    "correctDisplay": "B (Formalizing requirements)",
    "whyCorrect": "• Pilihan B adalah jawapan yang betul (bukan tugas teras). Mengikut silibus IREB FL, 4 aktiviti teras seorang Requirements Engineer ialah: 1. Elicitation, 2. Documentation, 3. Validation & Negotiation, dan 4. Management. 'Formalizing' (menggunakan notasi matematik formal yang ketat) bukan aktiviti teras am.",
    "whyWrong": "• Pilihan A (Eliciting), C (Documenting), dan D (Validating) merupakan aktiviti teras fundamental dalam kitaran kerja Requirements Engineering.",
    "extra": "Handbook Bab 1.4 / Syllabus EO 1.4.1: 4 Teras Utama RE: Elicitation, Documentation, Validation/Negotiation, Management.",
    "mnemonic": "4 Aktiviti Teras RE = E-D-V-M (Elicit, Document, Validate, Manage)."
  },
  3: {
    "euNo": 1,
    "title": "System Requirements vs Project/Process Requirements",
    "correctDisplay": "C, E",
    "whyCorrect": "• C (Requirement C): Betul. 'Throughput 100 transactions/sec' adalah Quality Requirement (Performance) yang merujuk terus kepada keupayaan sistem yang direalisasikan.\n• E (Requirement E): Betul. 'Response time <= 2 seconds dalam 90% kes' adalah Quality Requirement (Performance) yang merujuk kepada kelajuan operasi sistem.",
    "whyWrong": "• A (Requirement A): Ini adalah Process / Project Requirement bagi kontraktor (tempoh masa memproses change request).\n• B (Requirement B): Ini adalah Project Deliverable / Management Requirement (penyerahan laporan ujian).\n• D (Requirement D): Ini adalah Project Constraint untuk pengurusan konfigurasi kontraktor.",
    "extra": "Handbook Bab 1.1 / Syllabus EO 1.1.2: Bezakan antara System Requirements (keperluan produk akhir) dengan Project/Process Requirements (cara projek/organisasi dijalankan).",
    "mnemonic": "System Requirement = Sifat & tingkah laku perisian yang siap (Throughput, Response Time)."
  },
  4: {
    "euNo": 2,
    "title": "Fundamental Principles of Requirements Engineering",
    "correctDisplay": "C (Regular retrospectives)",
    "whyCorrect": "• Pilihan C adalah jawapan yang betul (bukan prinsip asas RE). 'Regular retrospectives' adalah amalan proses Agile / Scrum (Process Practice), bukan salah satu daripada 9 Prinsip Asas RE yang digariskan oleh IREB.",
    "whyWrong": "• A (Value orientation): Prinsip 1 RE — Requirements are a means to an end, not an end in themselves.\n• B (Problem - requirement - solution): Prinsip 5 RE — Memahami masalah sebelum melompat ke solusi teknikal.\n• D (Systematic and disciplined work): Prinsip 9 RE — RE memerlukan kaedah kerja yang berdisiplin dan boleh diulang.",
    "extra": "Handbook Bab 2 / Syllabus EO 2.1.1: 9 Prinsip Asas RE IREB:\n1. Value-Orientation\n2. Stakeholders\n3. Shared Understanding\n4. Context\n5. Problem-Requirement-Solution\n6. Validation\n7. Evolution\n8. Innovation\n9. Systematic Work.",
    "mnemonic": "9 Prinsip IREB: V-S-S-C-P-V-E-I-S. 'Retrospectives' adalah amalan Agile, bukan prinsip teras RE."
  },
  5: {
    "euNo": 2,
    "title": "Principle 3: Shared Understanding",
    "correctDisplay": "A=True, B=True, C=True, D=True",
    "whyCorrect": "• A: True. Mencapai explicit shared understanding adalah salah satu matlamat utama RE untuk mengelakkan salah faham antara stakeholder dan pembangun.\n• B: True. Tanpa shared understanding asas, mustahil untuk mengenal pasti punca dan sumber keperluan (requirements sources) yang tepat dan relevan.\n• C: True. Sesetengah tahap implicit shared understanding adalah sangat penting kerana mustahil untuk mendokumentasikan setiap butiran secara eksplisit.\n• D: True. RE dalam pembangunan Agile sangat bergantung kepada implicit shared understanding (kerjasama rapat dan komunikasi bersemuka).",
    "whyWrong": "• Kesemua 4 kenyataan (A, B, C, D) adalah TEPAT dan BENAR (True) mengikut perbincangan Prinsip 3: Shared Understanding dalam IREB Handbook Bab 2.3.",
    "extra": "Handbook Bab 2.3 / Syllabus EO 2.2.1 (Principle 3: Shared Understanding):\n• Shared understanding terdiri daripada Explicit (didokumenkan) dan Implicit (pengetahuan bersama yang difahami).\n• Alat meningkatkan Shared Understanding: Glossary, Prototaip, Model Visual, dan Analogi.",
    "mnemonic": "Shared Understanding = Explicit (ditulis) + Implicit (difahami bersama). Agile bersandar pada Implicit."
  },
  6: {
    "euNo": 2,
    "title": "Principle 4: Context Boundaries",
    "correctDisplay": "A=Needs to be considered, B=Needs to be considered, C=Needs to be considered, D=Needs to be considered",
    "whyCorrect": "• A: Needs to be considered. Sistem itu sendiri mentakrifkan apa yang berada di dalam System Boundary.\n• B: Needs to be considered. System Context adalah persekitaran relevan yang berinteraksi dengan sistem (Stakeholders, sistem luaran, proses perniagaan, undang-undang).\n• C: Needs to be considered. Application Domain adalah domain aplikasi di mana sistem dan konteks beroperasi (mempunyai peraturan dan kekangan domain tersendiri).\n• D: Needs to be considered. Antara muka (Interfaces) menghubungkan sistem dengan konteks sistem merentasi System Boundary.",
    "whyWrong": "• Kesemua 4 aspek (A, B, C, D) WAJIB dipertimbangkan semasa mentakrifkan System Boundary dan Context Boundary mengikut IREB Handbook Bab 2.4.",
    "extra": "Handbook Bab 2.4 / Syllabus EO 2.3.1 (Principle 4: Context):\n1. System Boundary: Memisahkan sistem daripada konteksnya.\n2. Context Boundary: Memisahkan persekitaran relevan daripada persekitaran yang tidak relevan (Irrelevant Environment).\n3. Context: Sumber kepada segala keperluan.",
    "mnemonic": "Semua 4 aspek (System, Context, Domain, Interfaces) wajib dipertimbangkan untuk Context Boundary."
  },
  7: {
    "euNo": 2,
    "title": "System Boundary vs Context Boundary Influence",
    "correctDisplay": "B (Context boundary)",
    "whyCorrect": "• Pilihan B adalah jawapan yang betul. Undang-undang perlindungan data (Data Protection Regulations) adalah elemen persekitaran luar. Apabila ia didapati tidak terpakai kerana data telah di-anonymize, elemen peraturan tersebut dialihkan keluar dari Konteks Relevan ke 'Irrelevant Environment'. Oleh itu, yang berubah ialah Context Boundary.",
    "whyWrong": "• A (System boundary): Sempadan sistem mentakrifkan skop sistem yang dibangunkan (bukan penentuan peraturan luar relevan/tidak).\n• C (System interfaces): Antara muka teknikal sistem tidak berubah secara langsung semata-mata kerana penentuan status peraturan undang-undang.\n• D (Application boundary): Bukan istilah piawai sempadan RE mengikut IREB.",
    "extra": "Handbook Bab 2.4 / Syllabus EO 2.3.2: Context Boundary membezakan antara aspek persekitaran yang relevan (termasuk undang-undang & piawaian) dengan aspek persekitaran yang tidak berkaitan.",
    "mnemonic": "Undang-undang luar tak relevan ➔ Context Boundary berubah (berpindah ke Irrelevant Environment)."
  },
  8: {
    "euNo": 3,
    "title": "Definition & Scope of Work Products",
    "correctDisplay": "D (Only final requirements documents that describe a fixed set of requirements...)",
    "whyCorrect": "• Pilihan D adalah kenyataan yang SALAH / TIDAK TEPAT (maka jawapan yang betul). Work products BUKAN hanya dokumen keperluan akhir yang tetap; mana-mana artifak perantaraan seperti User Stories, lakaran prototaip, model Use Case, dan minit bengkel juga merupakan Work Products yang sah dalam RE.",
    "whyWrong": "• A, B, dan C adalah kenyataan yang BENAR mengenai Work Products mengikut silibus IREB (sebarang maklumat yang direkodkan semasa RE adalah work product).",
    "extra": "Handbook Bab 3.1 / Syllabus EO 3.1.2: Work Products merangkumi Individual Work Products (User Story, Use Case) dan Work Product Sets / Aggregates (SRS, Product Backlog).",
    "mnemonic": "Work Product = Sebarang artifak bertulis (Draf, Cerita Pengguna, Model, Dokumen Akhir)."
  },
  9: {
    "euNo": 3,
    "title": "UML Class Diagram vs Behavior Diagrams (States)",
    "correctDisplay": "B (States)",
    "whyCorrect": "• Pilihan B adalah jawapan yang betul. 'States' (keadaan / status kitaran hayat objek) adalah konsep dalam State Machine Diagram (Model Tingkah Laku Dinamik), bukannya Class Diagram yang memodelkan Struktur Statik.",
    "whyWrong": "• A (Attributes), C (Operations), dan D (Associations) kesemuanya merupakan elemen teras dalam UML Class Diagram.",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.6: Class Diagram memaparkan struktur data, entiti domain, atribut, operasi, dan hubungan persatuan (associations).",
    "mnemonic": "Class Diagram = Struktur Statik (Attributes, Operations, Associations). States = State Machine."
  },
  10: {
    "euNo": 3,
    "title": "Work Products for Stakeholder Comprehensibility",
    "correctDisplay": "C, D",
    "whyCorrect": "• C (Establishing a glossary): Betul. Glossary menyelaraskan istilah domain, menghapuskan sinonim/homonim yang mengelirukan antara stakeholder dan pemaju.\n• D (Creating a use case diagram and specifying the use cases): Betul. Use case diagram memberikan gambaran visual skop sistem yang mudah difahami oleh stakeholder dari perspektif perniagaan.",
    "whyWrong": "• A (Writing formal mathematical specifications): Bahasa formal menyukarkan stakeholder biasa memahami keperluan.\n• B (Documenting in code comments): Komen kod tidak boleh diakses atau dinilai oleh stakeholder perniagaan.\n• E (Avoiding functional requirements): Menghapuskan keperluan fungsi menyebabkan sistem tidak mempunyai panduan binaan.",
    "extra": "Handbook Bab 3.1 / Syllabus EO 3.1.3: Cara meningkatkan kefahaman stakeholder: Gunakan Glossary, Model Visual (Use Cases/Activity), dan Teks Berstruktur.",
    "mnemonic": "Fahamkan Stakeholder = Glossary (Kamus Istilah) + Use Case (Model Skop Visual)."
  },
  11: {
    "euNo": 3,
    "title": "Tender Preparation Activity Diagram Execution",
    "correctDisplay": "B, D",
    "whyCorrect": "• B: Betul. Aliran proses menunjukkan aktiviti analisis risiko projek dan analisis teknikal berjalan selari (parallel branches).\n• D: Betul. Menyediakan cadangan (Prepare proposal) memerlukan aktiviti analisis selesai sebelum diteruskan.",
    "whyWrong": "• A, C, E tidak mematuhi logik aliran token Fork dan Join pada rajah aktiviti.",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.3: Activity Diagram Control Flows: Fork Node (Cabang Selari) & Join Node (Penyelarasan Aliran).",
    "mnemonic": "Fork = Aliran Selari. Join = Penyatuan Aliran."
  },
  12: {
    "euNo": 3,
    "title": "Notations for Requirements Documentation",
    "correctDisplay": "A=True, B=False, C=True, D=True",
    "whyCorrect": "• A: True. Notasi standard (UML/SysML/BPMN) memastikan konsistensi dan mengurangkan kekaburan.\n• C: True. Menggabungkan model grafik bersama teks penerangan (Hybrid) memberikan kejelasan maksimum.\n• D: True. Bahasa semulajadi adalah format paling universal untuk disemak oleh semua stakeholder.",
    "whyWrong": "• B: False. Model grafik tidak sepatutnya diabaikan; rajah visual mengurangkan beban kognitif secara signifikan.",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.1: Bentuk dokumentasi: Natural Language, Conceptual Models, dan Hybrid.",
    "mnemonic": "Dokumentasi Terbaik = Gabungan Teks Semulajadi + Model Konseptual (Hybrid)."
  },
  13: {
    "euNo": 3,
    "title": "Quality Criteria for Work Products (IREB Standards)",
    "correctDisplay": "A=True, B=True, C=True, D=False",
    "whyCorrect": "• A: True. Keperluan yang tidak boleh diuji (untestable) tidak mempunyai sifat Verifiability.\n• B: True. Traceability mempermudah penilaian impak (Impact Analysis) apabila berlaku perubahan.\n• C: True. Kelengkapan (Completeness) perlu diseimbangkan dengan kos penyediaannya (Prinsip Value-Orientation).",
    "whyWrong": "• D: False. Format perwakilan yang seragam untuk semua keperluan tidak semestinya menjamin kebolehfahaman; variasi format (teks, jadual, model) selalunya lebih berkesan.",
    "extra": "Handbook Bab 3.1 / Syllabus EO 3.1.4: Kriteria Kualiti: Unambiguous, Complete, Consistent, Verifiable, Modifiable, Traceable.",
    "mnemonic": "Kualiti = Verifiable (Boleh Uji) + Traceable (Boleh Kesan) + Value-Oriented."
  },
  14: {
    "euNo": 3,
    "title": "Benefits of Phrase Templates (Sentence Templates)",
    "correctDisplay": "A, C",
    "whyCorrect": "• A: Betul. Penulis dibimbing oleh struktur templat semasa merumuskan keperluan.\n• C: Betul. Keperluan yang ditulis menggunakan templat mengandungi kurang kekaburan linguistik (fewer linguistic ambiguities).",
    "whyWrong": "• B: Templat tidak menjamin kelengkapan isi kandungan semantik.\n• D & E: Templat tidak memendekkan masa berfikir dan tidak secara automatik mematuhi kekangan undang-undang.",
    "extra": "Handbook Bab 3.3 / Syllabus EO 3.3.2: Sentence Template (SOPHIST): [Condition] [System] <SHALL/SHOULD/WILL> [Action] [Object].",
    "mnemonic": "Sentence Template = Membimbing Penulis (Guided) + Kurang Kekaburan (Less Ambiguity)."
  },
  15: {
    "euNo": 3,
    "title": "Transformation Effects (Universal Quantifiers)",
    "correctDisplay": "B (Universal quantifiers have been used)",
    "whyCorrect": "• Pilihan B adalah jawapan yang betul. Penggunaan kata penentu sejagat (Universal Quantifiers) seperti 'all', 'always', 'every', 'never' sering kali tidak tepat dan menyembunyikan kekecualian (exceptions) yang wujud dalam situasi sebenar.",
    "whyWrong": "• A (Nominalization), C (Incomplete condition), D (Passive voice) merujuk kepada kesan transformasi bahasa yang lain.",
    "extra": "Handbook Bab 3.3 / Syllabus EO 3.3.1: 4 Kesan Transformasi Bahasa: 1. Nominalization, 2. Deletion/Omission, 3. Incomplete Condition, 4. Universal Quantification.",
    "mnemonic": "Universal Quantifiers = Perkataan melampau (All, Always, Every, Never)."
  },
  16: {
    "euNo": 3,
    "title": "Template-based Work Products",
    "correctDisplay": "A=True, B=True, C=False, D=False",
    "whyCorrect": "• A: True. Struktur templat dokumen boleh disesuaikan (tailored) mengikut keperluan projek spesifik.\n• B: True. Menggunakan templat standard memudahkan perkongsian dan guna semula (reuse) keperluan antara projek berbeza.",
    "whyWrong": "• C: False. Templat tidak menjamin kandungan lengkap sepenuhnya.\n• D: False. Templat bukan bersifat 'wajib rigid tanpa pengubahsuaian'; ia boleh diadaptasi.",
    "extra": "Handbook Bab 3.1 / Syllabus EO 3.1.5: Template dokumen menyediakan standardisasi dan mempermudah navigasi pembaca.",
    "mnemonic": "Template Dokumen = Boleh Disesuaikan (Tailored) + Memudahkan Guna Semula (Reuse)."
  },
  17: {
    "euNo": 3,
    "title": "Use Case Modeling Diagram Choice",
    "correctDisplay": "A (Use case diagram)",
    "whyCorrect": "• Pilihan A adalah jawapan yang betul. Use Case Diagram adalah model terbaik untuk memberikan gambaran keseluruhan (overview) perkhidmatan sistem dan pelakunya (actors) kepada pihak pengurusan.",
    "whyWrong": "• B (State machine): Model kitaran hayat status dalaman.\n• C (Class diagram): Model struktur data teknikal.\n• D (Deployment diagram): Model seni bina perkakasan fizikal.",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.4: Use Case Diagram memaparkan skop fungsi dari perspektif pengguna luar.",
    "mnemonic": "Gambaran Skop Pengguna = Use Case Diagram."
  },
  18: {
    "euNo": 3,
    "title": "UML Class Diagram: Film Contest Multiplicities",
    "diagramHtml": f"<img src='{img_q18}' alt='Diagram Q18' />",
    "correctDisplay": "A=False, B=True, C=True, D=True, E=False",
    "whyCorrect": "• B: True. Filem dengan hanya seorang pelakon boleh dihantar mengikut multiplicity (1..*).\n• C: True. Pengarah boleh mengarah dua filem yang dihantar (0..*).\n• D: True. Pelakon boleh berlakon dalam sebarang bilangan filem (*).",
    "whyWrong": "• A: False. Multiplicity membenarkan pengarah mengarah bersama secara kolaboratif.\n• E: False. Filem TIDAK diwajibkan mempunyai 10 pelakon (multiplicity ialah 1..*, bukan 10).",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.6: Membaca Multiplicities UML Class Diagram (1..*, 0..*, 1, *).",
    "mnemonic": "Semak multiplicities pada hujung kelas persatuan dengan teliti."
  },
  19: {
    "euNo": 3,
    "title": "What is NOT Depicted in a Use Case Diagram",
    "correctDisplay": "A (The process steps of an application)",
    "whyCorrect": "• Pilihan A adalah jawapan yang betul. Use Case Diagram TIDAK memaparkan langkah-langkah proses terperinci (process steps / sequence of actions). Langkah proses hanya dipaparkan dalam Activity Diagram atau Use Case Specification bertulis.",
    "whyWrong": "• B (Actors), C (System boundary), D (Use cases) kesemuanya dipaparkan dalam Use Case Diagram.",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.4: Use Case Diagram = Gambaran Skop Fungsi (Bukan Urutan Proses).",
    "mnemonic": "Use Case Diagram = Skop Sistem (Bukan Langkah Proses Dalaman)."
  },
  20: {
    "euNo": 3,
    "title": "State Machine Diagram: Token Lifecycle",
    "diagramHtml": f"<img src='{img_q20}' alt='Diagram Q20' />",
    "correctDisplay": "A=False, B=True, C=True, D=False",
    "whyCorrect": "• B: True. Dari keadaan 'Active', sistem boleh kembali ke 'Idle' melalui timeout/expiration atau token returned.\n• C: True. Peralihan berlaku apabila token tamat tempoh masa yang ditetapkan.",
    "whyWrong": "• A & D: Tidak mematuhi laluan peralihan dan guard condition yang dipaparkan dalam rajah.",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.5: State Machine Diagram: States, Transitions, Events, Guards, Actions.",
    "mnemonic": "State Machine = Kitaran Hayat Keadaan Objek (State Transitions)."
  },
  21: {
    "euNo": 3,
    "title": "Activity Diagram: Performing a Measurement",
    "diagramHtml": f"<img src='{img_q21}' alt='Diagram Q21' />",
    "correctDisplay": "A=Does not match, B=Does not match, C=Does not match, D=Matches",
    "whyCorrect": "• D: Matches. Berdasarkan rajah aktiviti, 'Deactivate measuring device' dieksekusi sebaik sahaja isyarat 'Data receipt confirmed' diterima (True).",
    "whyWrong": "• A: Does not match. 'Initialize measuring device' dan 'Initialize network connection' berada dalam cabang Fork selari, urutannya bebas.\n• B: Does not match. 'Register at server' memerlukan KEDUA-DUA aliran masuk ke Join Node selesai (Network initialized DAN Certificates loaded).\n• C: Does not match. Join node menunggu kedua-dua cabang selesai, tetapi tidak mewajibkan ia selesai serentak pada detik masa yang sama.",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.3: Activity Diagram Control Flows: Fork Node (Split) & Join Node (Synchronization).",
    "mnemonic": "Join Node = Tunggu kedua-dua cabang siap (tak semestinya siap serentak)."
  },
  22: {
    "euNo": 3,
    "title": "Advantages of Graphical Conceptual Models",
    "correctDisplay": "A, C",
    "whyCorrect": "• A: Betul. Model grafik menumpukan perhatian kepada perspektif tertentu dan mengurangkan beban kognitif (cognitive load).\n• C: Betul. Model mempunyai sintaksis terhad (restricted syntax) yang mengurangkan kekaburan berbanding teks semulajadi bebas.",
    "whyWrong": "• B: Model tidak boleh menggambarkan 100% perincian tanpa sokongan teks.\n• D & E: Model tidak secara automatik menghapuskan keperluan ujian perisian.",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.1: 3 Perspektif Model RE: Structure, Function, Behavior.",
    "mnemonic": "Kelebihan Model Visual = Kurang Beban Kognitif (Focus) + Sintaksis Ketat (Kurang Kabur)."
  },
  23: {
    "euNo": 3,
    "title": "UML Class Diagram: Route Calculation System",
    "diagramHtml": f"<img src='{img_q23}' alt='Diagram Q23' />",
    "correctDisplay": "A=True, B=True, C=False, D=True",
    "whyCorrect": "• A: True. Laluan (route) boleh dikira tanpa maklumat trafik (0..1).\n• B: True. Laluan boleh dikira selepas mendapatkan maklumat trafik.\n• D: True. Urutan memasukkan destinasi dan koordinat GPS adalah bebas mengikut model.",
    "whyWrong": "• C: False. Kenyataan C menyalahi penggandaan (multiplicity) persatuan yang ditetapkan.",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.6: Membaca Multiplicities UML Class Diagram (0..1, 1..*, *).",
    "mnemonic": "Baca multiplicities pada hujung kelas sasaran persatuan."
  },
  24: {
    "euNo": 3,
    "title": "Process Flow Modeling Notations (BPMN & Activity)",
    "correctDisplay": "A, C",
    "whyCorrect": "• A (BPMN diagram): Betul. BPMN (Business Process Model and Notation) direka khas untuk memodelkan proses perniagaan dan aliran kerja.\n• C (Activity diagram): Betul. UML Activity Diagram memodelkan aliran aktiviti, kawalan dan data dalam proses.",
    "whyWrong": "• B (Class diagram): Model struktur data statik.\n• D (State machine): Model status kitaran hayat objek.\n• E (Use case diagram): Model skop fungsi peringkat tinggi.",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.2 & 3.2.3: Notasi Aliran Proses: BPMN dan UML Activity Diagram.",
    "mnemonic": "Model Proses / Aliran Kerja = BPMN Diagram & Activity Diagram."
  },
  25: {
    "euNo": 3,
    "title": "Functional Perspective of Conceptual Modeling (DFD)",
    "correctDisplay": "D (Transformation of input data into output data)",
    "whyCorrect": "• Pilihan D adalah jawapan yang betul. Perspektif fungsi (Functional Perspective seperti Data Flow Diagram) menggambarkan bagaimana data input ditransformasikan menjadi data output melalui proses pemprosesan.",
    "whyWrong": "• A, B, C merujuk kepada perspektif tingkah laku (Behavior/States) atau struktur data (Class Diagram).",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.1: Perspektif Fungsi = Transformasi Input ➔ Proses ➔ Output.",
    "mnemonic": "Perspektif Fungsi (DFD) = Transformasi Data Input kepada Output."
  },
  26: {
    "euNo": 4,
    "title": "First Step in Stakeholder Identification",
    "correctDisplay": "B (Search in the existing project documentation for stakeholders)",
    "whyCorrect": "• Pilihan B adalah tindakan pertama yang paling efisien dan profesional. Menyemak dokumentasi sedia ada (Project Charter, Kontrak, Carta Organisasi) mengenal pasti stakeholder yang telah direkodkan tanpa membuang masa mereka.",
    "whyWrong": "• A: Mengadakan bengkel tanpa mengetahui siapa stakeholder adalah pramatang.\n• C: Bergantung kepada ingatan lisan rakan sekerja tidak formal.\n• D: Penentuan sempadan memerlukan penglibatan stakeholder yang telah dikenal pasti.",
    "extra": "Handbook Bab 4.2 / Syllabus EO 4.2.1: Langkah Pertama Stakeholder Identification = Semak Dokumentasi Projek Sedia Ada.",
    "mnemonic": "Langkah pertama = Semak Dokumentasi Sedia Ada."
  },
  27: {
    "euNo": 4,
    "title": "Requirements Sources Types (IREB Taxonomy)",
    "correctDisplay": "A, C",
    "whyCorrect": "• A (Stakeholders): Betul. Sumber berasaskan manusia (pengguna, penaja, pakar domain).\n• C (Documents): Betul. Sumber bertulis (manual, undang-undang, piawaian industri).",
    "whyWrong": "• B (Prototypes), D (Tools), E (Templates) bukan jenis sumber keperluan primer (3 sumber utama: Stakeholders, Documents, Systems in Operation).",
    "extra": "Handbook Bab 4.1 / Syllabus EO 4.1.1: 3 Sumber Keperluan Utama: Stakeholders, Documents, Systems in Operation.",
    "mnemonic": "3 Sumber Keperluan = Stakeholders (Orang) + Documents (Kertas) + Systems in Operation (Sistem)."
  },
  28: {
    "euNo": 4,
    "title": "Kano Model: Eliciting Basic Factors (Dissatisfiers)",
    "correctDisplay": "C (Field observation)",
    "whyCorrect": "• Pilihan C adalah jawapan yang betul. Basic factors (keperluan asas yang dianggap 'taken for granted') jarang dinyatakan dalam temuduga. Teknik Field Observation (Pemerhatian Lapangan / Apprenticeship) membolehkan Requirements Engineer melihat tabiat sebenar pengguna.",
    "whyWrong": "• A (Interview) & B (Survey): Sesuai untuk Performance Factors (keperluan eksplisit).\n• D (Brainstorming): Sesuai untuk Excitement Factors (faktor inovasi).",
    "extra": "Handbook Bab 4.3 / Syllabus EO 4.3.3: Basic Factors ➔ Elicit via Observation & System Archeology.",
    "mnemonic": "Basic Factors (Tersirat) = Field Observation (Pemerhatian Lapangan)."
  },
  29: {
    "euNo": 4,
    "title": "Factors Influencing Elicitation Technique Selection",
    "correctDisplay": "A, C",
    "whyCorrect": "• A (The availability of the involved people): Betul. Ketersediaan masa stakeholder menentukan sama ada temuduga, bengkel, atau soal selidik sesuai dijalankan.\n• C (The category of requirements based on Kano classification): Betul. Jenis keperluan (Basic, Performance, Excitement) memerlukan teknik elisitasi yang berbeza.",
    "whyWrong": "• B, D, E bukan faktor utama penentu pemilihan teknik elisitasi mengikut silibus IREB.",
    "extra": "Handbook Bab 4.3 / Syllabus EO 4.3.2: Kriteria Pemilihan Teknik Elisitasi: Ketersediaan Stakeholder, Risiko Projek, Jenis Faktor Kano.",
    "mnemonic": "Pilih Teknik Elisitasi = Ketersediaan Masa Stakeholder + Kategori Faktor Kano."
  },
  30: {
    "euNo": 4,
    "title": "Document Analysis Elicitation Technique (Sampling)",
    "correctDisplay": "D (Sampling)",
    "whyCorrect": "• Pilihan D adalah jawapan yang betul. Apabila berhadapan dengan jumlah dokumen atau data rekod yang sangat besar, teknik pensampelan (Sampling) digunakan untuk menganalisis sampel representatif secara saintifik.",
    "whyWrong": "• A, B, C bukan teknik persampelan dokumen representatif.",
    "extra": "Handbook Bab 4.3 / Syllabus EO 4.3.4: Document Analysis Techniques: Content Analysis, Form Analysis, Sampling.",
    "mnemonic": "Banyak dokumen besar = Sampling (Persampelan Representatif)."
  },
  31: {
    "euNo": 4,
    "title": "Stakeholder Management: Key Stakeholder Attributes",
    "correctDisplay": "A, D",
    "whyCorrect": "• A (Their function/role): Betul. Mengetahui fungsi dan peranan stakeholder dalam organisasi.\n• D (Their relevance): Betul. Menilai tahap relevansi dan pengaruh stakeholder terhadap kejayaan sistem.",
    "whyWrong": "• B, C, E adalah data peribadi yang tidak relevan dengan pengurusan kejuruteraan keperluan.",
    "extra": "Handbook Bab 4.2 / Syllabus EO 4.2.2: Atribut Stakeholder Penting: Peranan (Role), Relevansi/Kuasa (Power), Minat (Interest), Ketersediaan (Availability).",
    "mnemonic": "Atribut Stakeholder = Peranan (Role) + Relevansi & Pengaruh (Relevance/Power)."
  },
  32: {
    "euNo": 4,
    "title": "Advantages of Questionnaires (Surveys)",
    "correctDisplay": "A, B",
    "whyCorrect": "• A: Betul. Soal selidik membolehkan penglibatan bilangan responden yang sangat ramai (high number of participants).\n• B: Betul. Data soal selidik membolehkan analisis statistik yang sahih (statistically relevant statements) dilakukan.",
    "whyWrong": "• C, D, E: Soal selidik tidak sesuai untuk membina hubungan peribadi atau meneroka idea baharu secara mendalam.",
    "extra": "Handbook Bab 4.3 / Syllabus EO 4.3.2: Kelebihan Soal Selidik (Surveys): Skala Besar, Kos Rendah, Data Kuantitatif Statistik.",
    "mnemonic": "Soal Selidik = Ramai Responden (Skala Besar) + Analisis Statistik Kuantitatif."
  },
  33: {
    "euNo": 4,
    "title": "Elicitation Techniques Classification",
    "correctDisplay": "A=True, B=False, C=False, D=True",
    "whyCorrect": "• A: True. Temuduga (Interview) ialah Gathering Technique.\n• D: True. Apprenticing (Perantisan) ialah Observation Technique.",
    "whyWrong": "• B: False. Analogy technique ialah Creativity Technique (bukan Gathering).\n• C: False. System archaeology ialah Artifact-based Technique (bukan Observation).",
    "extra": "Handbook Bab 4.3 / Syllabus EO 4.3.1: Klasifikasi Teknik Elisitasi IREB: Gathering, Observation, Creativity, Document/Artifact-based.",
    "mnemonic": "Interview = Gathering. Apprenticing = Observation. Analogy = Creativity."
  },
  34: {
    "euNo": 4,
    "title": "Types of Conflicts in Requirements Engineering",
    "correctDisplay": "D (Value conflict)",
    "whyCorrect": "• Pilihan D adalah jawapan yang betul. Konflik nilai (Value Conflict) berlaku apabila stakeholders mempunyai perbezaan pegangan nilai asas, etika, atau keutamaan falsafah perniagaan yang bercanggah.",
    "whyWrong": "• A (Data conflict): Percanggahan maklumat data.\n• B (Interest conflict): Percanggahan matlamat keuntungan.\n• C (Structural conflict): Percanggahan kuasa hierarki.",
    "extra": "Handbook Bab 4.4 / Syllabus EO 4.4.1: 5 Jenis Konflik RE: Subject-matter conflict, Interest conflict, Value conflict, Relationship conflict, Structural conflict.",
    "mnemonic": "Konflik Nilai & Etika = Value Conflict."
  },
  35: {
    "euNo": 4,
    "title": "Validation Techniques (Safety-Critical Train Braking)",
    "correctDisplay": "D (Inspection)",
    "whyCorrect": "• Pilihan D adalah jawapan yang betul. Untuk sistem kritikal keselamatan (Safety-Critical System) seperti sistem brek kereta api laju, 'Inspection' adalah teknik semakan paling formal, teliti, dan berdisiplin tinggi (Fagan Inspection).",
    "whyWrong": "• A (Walkthrough) & B (Informal review) & C (Desk checking) tidak mempunyai ketelitian dan protokol formal yang mencukupi untuk standard keselamatan nyawa.",
    "extra": "Handbook Bab 4.5 / Syllabus EO 4.5.2: Spektrum Ketelitian Validasi: Desk Checking ➔ Walkthrough ➔ Inspection (Paling Formal & Ketat).",
    "mnemonic": "Safety-Critical (Kereta Api / Perubatan) = Wajib Inspection (Formal Maksimum)."
  },
  36: {
    "euNo": 5,
    "title": "Three Facets of the Requirements Engineering Process",
    "correctDisplay": "A, C",
    "whyCorrect": "• A (The time facet: linear vs. iterative): Betul. Dimensi Masa mentakrifkan sama ada proses dijalankan secara Sekali Lalu (Linear) atau Berulang (Iterative/Agile).\n• C (The purpose facet: prescriptive vs. explorative): Betul. Dimensi Tujuan mentakrifkan sama ada keperluan bersifat Kontrak Ketat (Prescriptive) atau Penerokaan Dinamik (Explorative).",
    "whyWrong": "• B, D, E bukan 3 dimensi konfigurasi proses teras RE mengikut silibus IREB.",
    "extra": "Handbook Bab 5.1 / Syllabus EO 5.1.1: 3 Dimensi / Facets Konfigurasi Proses RE IREB:\n1. Time facet (Linear vs Iterative)\n2. Purpose facet (Prescriptive vs Explorative)\n3. Target/Change facet (Customer-specific vs Market-driven / Product Line).",
    "mnemonic": "3 Facets Proses RE = Masa (Linear/Iterative) + Tujuan (Prescriptive/Explorative) + Sasaran (Customer/Market)."
  },
  37: {
    "euNo": 5,
    "title": "RE Process Types (Linear vs Iterative)",
    "correctDisplay": "B (Human-oriented RE process (linear, process-based, individual...))",
    "whyCorrect": "• Pilihan B adalah jawapan yang betul mengikut taksonomi proses IREB. Situasi dengan keperluan stabil, pematuhan kontrak tender, dan struktur organisasi formal paling sesuai menggunakan proses berorientasikan linear berstruktur.",
    "whyWrong": "• A, C, D merujuk kepada proses eksploratori lelaran pantas (Agile) yang tidak sesuai untuk keperluan tender tetap.",
    "extra": "Handbook Bab 5.2 / Syllabus EO 5.2.1: Pemilihan proses RE mengikut pemacu konteks (Context Drivers).",
    "mnemonic": "Tender Tetap & Stabil = Proses Linear Berstruktur."
  },
  38: {
    "euNo": 6,
    "title": "Views on Requirements (Complexity Reduction & Access)",
    "correctDisplay": "A=True, B=True, C=True, D=False",
    "whyCorrect": "• A: True. Pandangan (Views) mengurangkan kompleksiti dengan memaparkan hanya keperluan relevan bagi kumpulan stakeholder tertentu.\n• B: True. Views boleh dicipta melalui gabungan kriteria penapisan atribut (filtering).\n• C: True. Keperluan sensitif boleh disembunyikan daripada capaian stakeholder yang tidak diberi kebenaran (access control).",
    "whyWrong": "• D: False. Mencipta Views tidak memerlukan bahasa spesifikasi formal; teks biasa berstruktur dan jadual atribut sudah memadai.",
    "extra": "Handbook Bab 6.4 / Syllabus EO 6.4.1: Views on Requirements: Selective Views & Aggregate Views.",
    "mnemonic": "Views = Tapis ikut Atribut + Kawal Capaian Stakeholder."
  },
  39: {
    "euNo": 6,
    "title": "Requirements Traceability Benefits (NOT a Benefit)",
    "correctDisplay": "C (Traceability facilitates exports from a requirements management tool)",
    "whyCorrect": "• Pilihan C adalah kenyataan yang TIDAK BENAR mengenai faedah utama Traceability (maka jawapan yang betul). Fungsi eksport data adalah keupayaan alat perisian am, bukannya tujuan teras mewujudkan pautan kebolehkesanan kejuruteraan.",
    "whyWrong": "• A (Impact analysis), B (Verification coverage), D (Change assessment) adalah faedah teras Traceability.",
    "extra": "Handbook Bab 6.5 / Syllabus EO 6.5.1: Faedah Traceability: Impact Analysis, Coverage Analysis, Change Tracking, Accountability.",
    "mnemonic": "Traceability = Jejak Impak Perubahan & Pematuhan Ujian (Bukan eksport fail alat)."
  },
  40: {
    "euNo": 6,
    "title": "Requirements Attributes: Purpose of Unique ID",
    "correctDisplay": "A=False, B=True, C=True, D=True",
    "whyCorrect": "• B: True. Unique ID menyediakan asas rujukan komunikasi yang tepat dan tidak meragukan.\n• C: True. Unique ID membolehkan pautan rujukan antara keperluan diwujudkan.\n• D: True. Unique ID adalah prasyarat mutlak untuk membina matriks kebolehkesanan (Traceability).",
    "whyWrong": "• A: False. Unique ID semata-mata tidak digunakan untuk menganggar saiz keseluruhan spesifikasi (saiz dianggar melalui Function Points atau Story Points).",
    "extra": "Handbook Bab 6.1 / Syllabus EO 6.1.1: Atribut Keperluan Standard: Identifier (Kekal & Unik), Status, Author, Priority, Source.",
    "mnemonic": "Unique ID = Rujukan Tepat + Asas Traceability (Bukan kira saiz saiz projek)."
  },
  41: {
    "euNo": 6,
    "title": "Recognized Traceability Types (IREB Taxonomy)",
    "correctDisplay": "B, C",
    "whyCorrect": "• B (Traceability to stakeholders / Pre-RS): Betul. Menjejaki keperluan ke belakang kepada sumber asalnya (Stakeholders, Dokumen).\n• C (Traceability to system architecture / Post-RS): Betul. Menjejaki keperluan ke hadapan kepada seni bina sistem, modul kod, dan kes ujian.",
    "whyWrong": "• A, D, E bukan jenis kebolehkesanan piawai dalam taksonomi IREB (3 jenis utama: Pre-RS, Post-RS, Inter-RS).",
    "extra": "Handbook Bab 6.5 / Syllabus EO 6.5.1: 3 Jenis Traceability IREB:\n1. Pre-RS (Keperluan ➔ Sumber/Stakeholder)\n2. Post-RS (Keperluan ➔ Seni Bina/Kod/Ujian)\n3. Inter-RS (Keperluan ➔ Keperluan Lain).",
    "mnemonic": "Traceability = Pre-RS (Ke Sumber Stakeholder) + Post-RS (Ke Seni Bina & Kod)."
  },
  42: {
    "euNo": 6,
    "title": "Requirements Attributes (Priority Purpose)",
    "correctDisplay": "A=True, B=True, C=False, D=False",
    "whyCorrect": "• A: True. Keutamaan (Priority) digunakan untuk menentukan susunan pelepasan keluaran (Release Planning).\n• B: True. Keutamaan digunakan untuk memutuskan fokus keperluan mana yang perlu diuji dahulu dalam aktiviti ujian (Test Prioritization).",
    "whyWrong": "• C: False. Kos pelaksanaan didokumenkan dalam atribut 'Estimated Cost / Effort', bukan atribut Priority.\n• D: False. Potensi guna semula didokumenkan dalam atribut 'Reusability'.",
    "extra": "Handbook Bab 6.1 & 6.3 / Syllabus EO 6.1.2: Kegunaan Priority: Perancangan Keluaran (Release Planning) & Keutamaan Ujian (Test Focus).",
    "mnemonic": "Atribut Priority = Rancang Keluaran (Release) + Fokus Pengujian (Testing)."
  },
  43: {
    "euNo": 6,
    "title": "Requirements Baseline Definition",
    "correctDisplay": "C (A released configuration of requirements)",
    "whyCorrect": "• Pilihan C adalah definisi tepat mengikut IREB Glossary & Handbook. Baseline ialah konfigurasi stabil bagi satu set artifak keperluan yang telah disemak, diluluskan, dan dilepaskan (released configuration of requirements) pada satu ketika masa tertentu.",
    "whyWrong": "• A (Initial draft): Draf belum diluluskan.\n• B (Database backup): Salinan teknikal pangkalan data.\n• D (Change request): Permohonan perubahan.",
    "extra": "Handbook Bab 6.2 / Syllabus EO 6.2.1: Baseline membolehkan perbandingan versi (diffing), pengurusan keluaran, dan kawalan perubahan (Change Control).",
    "mnemonic": "Baseline = Konfigurasi Keperluan yang Dilepaskan & Diluluskan (Released Configuration)."
  },
  44: {
    "euNo": 7,
    "title": "Tool Support Principles in Requirements Engineering",
    "correctDisplay": "A=True, B=False, C=False, D=True",
    "whyCorrect": "• A: True. Alat mesti menyokong proses RE yang telah matang dalam organisasi (bukan proses dipaksa mengikut kehendak alat).\n• D: True. Kos TCO (Total Cost of Ownership) merangkumi kos lesen, perkakasan, penyelenggaraan, dan latihan pengguna.",
    "whyWrong": "• B: False. Pemilihan alat tidak sepatutnya diserahkan sepenuhnya kepada citarasa peribadi pengguna individu tanpa piawaian organisasi.\n• C: False. Tiada satu alat tunggal yang sempurna untuk semua aktiviti RE tanpa integrasi.",
    "extra": "Handbook Bab 7.1 / Syllabus EO 7.1.1: Prinsip Alatan RE: Sokong proses organisasi, kira kos penuh TCO, buat projek perintis.",
    "mnemonic": "Alat sokong proses. Kira kos penuh TCO (bukan lesen semata-mata)."
  },
  45: {
    "euNo": 7,
    "title": "Core Application of RE Tools",
    "correctDisplay": "B (Modelling of requirements)",
    "whyCorrect": "• Pilihan B adalah jawapan yang betul. Pemodelan keperluan (Modelling of requirements seperti Use Cases, Activity Diagrams, Class Diagrams, State Machines) adalah fungsi teras alatan RE untuk mengurangkan kekaburan dan meningkatkan kefahaman.",
    "whyWrong": "• A, C, D merujuk kepada aktiviti pembangunan hiliran seperti penjanaan kod automatik penuh atau pengurusan belanjawan kewangan.",
    "extra": "Handbook Bab 7.1 / Syllabus EO 7.2.1: Fungsi Utama Alatan RE: Management, Modeling, Collaboration, Validation.",
    "mnemonic": "Alatan RE = Pengurusan & Pemodelan Keperluan (Modeling of Requirements)."
  }
}

questions_final = []
for q in raw_questions:
    qid = q['id']
    meta = meta_data.get(qid, {})
    
    # Diagram HTML
    diag_html = ""
    if qid == 18: diag_html = f"<img src='{img_q18}' alt='Diagram Q18' />"
    elif qid == 20: diag_html = f"<img src='{img_q20}' alt='Diagram Q20' />"
    elif qid == 21: diag_html = f"<img src='{img_q21}' alt='Diagram Q21' />"
    elif qid == 23: diag_html = f"<img src='{img_q23}' alt='Diagram Q23' />"
    
    questions_final.append({
        "id": qid,
        "code": q['code'],
        "type": q['type'],
        "pts": q['pts'],
        "eo": q['eo'],
        "euNo": meta.get('euNo', 1),
        "title": meta.get('title', f"Question {qid}"),
        "question": q['stem'],
        "options": q['options'],
        "diagramHtml": diag_html,
        "correctDisplay": meta.get('correctDisplay', ''),
        "whyCorrect": meta.get('whyCorrect', ''),
        "whyWrong": meta.get('whyWrong', ''),
        "extra": meta.get('extra', ''),
        "mnemonic": meta.get('mnemonic', '')
    })

app_data = {
  "eus": eus,
  "questions": questions_final
}

with open(DATA_PATH, 'w', encoding='utf-8') as f:
    json.dump(app_data, f, indent=2, ensure_ascii=False)

print(f"Generated pristine dataset with {len(questions_final)} questions!")
print(f"Total points: {sum(q['pts'] for q in questions_final)}")
