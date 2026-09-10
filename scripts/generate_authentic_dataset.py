import json
import base64
import os
import openpyxl

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(ROOT_DIR, 'docs')
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

# 7 Official Syllabus Educational Units
eus = [
  { "no": 1, "name": "Introduction and Overview of Requirements Engineering", "range": "Q1–Q3", "pts": 4, "qCount": 3 },
  { "no": 2, "name": "Fundamental Principles of Requirements Engineering", "range": "Q4–Q7", "pts": 6, "qCount": 4 },
  { "no": 3, "name": "Work Products and Documentation Practices", "range": "Q8–Q25", "pts": 30, "qCount": 18 },
  { "no": 4, "name": "Practices for Requirements Elaboration", "range": "Q26–Q35", "pts": 14, "qCount": 10 },
  { "no": 5, "name": "Process and Working Structure", "range": "Q36–Q37", "pts": 3, "qCount": 2 },
  { "no": 6, "name": "Management Practices for Requirements", "range": "Q38–Q43", "pts": 10, "qCount": 6 },
  { "no": 7, "name": "Tool Support", "range": "Q44–Q45", "pts": 3, "qCount": 2 }
]

# 45 Authentic Questions matching IREB FL 3.3.2 Questionnaire & Correction Aid 1:1
questions = [
  # ================================================================================================
  # EU1: Introduction and Overview of Requirements Engineering (Q1–Q3, 4 Pts)
  # ================================================================================================
  {
    "id": 1,
    "code": "K0111",
    "type": "K",
    "pts": 2,
    "eo": "1.1.1",
    "euNo": 1,
    "title": "Quality Requirements vs Functional Requirements",
    "question": "Which of the following statements on quality requirements are true and which are false?",
    "options": [
      { "id": "A", "text": "Quality requirements refer to the process of creating software and not to the product.", "truth": False },
      { "id": "B", "text": "Quality requirements can complement functional requirements.", "truth": True },
      { "id": "C", "text": "Quality requirements are elicited after the functional requirements.", "truth": False },
      { "id": "D", "text": "Quality requirements can be substantiated with additional functional requirements.", "truth": True }
    ],
    "correctDisplay": "A=False, B=True, C=False, D=True",
    "whyCorrect": "• B: True. Quality requirements melengkapi (complement) functional requirements dengan mentakrifkan bagaimana sesuatu fungsi itu harus beroperasi (cth: aspek performance, usability, security, reliability).\n• D: True. Quality requirements boleh diperincikan (substantiated) kepada functional requirements tambahan (contoh: keperluan keselamatan 'Akses mesti dilindungi' diperincikan kepada fungsi 'Sistem mesti menyediakan Two-Factor Authentication').",
    "whyWrong": "• A: False. Quality requirements merujuk kepada kualiti PRODUK (sistem), bukannya proses pembangunan perisian (keperluan proses dirujuk sebagai Project / Process Requirements).\n• C: False. Quality requirements TIDAK semestinya di-elicit selepas fungsi; dalam praktis RE sebenar, kedua-duanya di-elicit serentak secara berulang (intertwined).",
    "extra": "Handbook Bab 1.1 / Syllabus EO 1.1.1: 3 jenis keperluan mengikut piawaian IREB ialah: 1. Functional Requirements, 2. Quality Requirements, 3. Constraints.",
    "mnemonic": "Quality = Sifat Produk. Boleh melahirkan Functional Requirement baharu (Substantiated)."
  },
  {
    "id": 2,
    "code": "A0120",
    "type": "A",
    "pts": 1,
    "eo": "1.4.1",
    "euNo": 1,
    "title": "Core Tasks of the Requirements Engineer",
    "question": "Which of the following tasks is NOT a core task of the Requirements Engineer? (1 answer)",
    "options": [
      { "id": "A", "text": "Eliciting requirements", "truth": False },
      { "id": "B", "text": "Formalizing requirements", "truth": True },
      { "id": "C", "text": "Documenting requirements", "truth": False },
      { "id": "D", "text": "Validating requirements", "truth": False }
    ],
    "correctDisplay": "B (Formalizing requirements)",
    "whyCorrect": "• Pilihan B adalah jawapan yang betul (bukan tugas teras). Mengikut silibus IREB FL, 4 aktiviti teras seorang Requirements Engineer ialah: 1. Elicitation, 2. Documentation, 3. Validation & Negotiation, dan 4. Management. 'Formalizing' (menggunakan notasi matematik formal yang ketat) bukan aktiviti teras am.",
    "whyWrong": "• Pilihan A (Eliciting), C (Documenting), dan D (Validating) merupakan aktiviti teras fundamental dalam kitaran kerja Requirements Engineering.",
    "extra": "Handbook Bab 1.4 / Syllabus EO 1.4.1: 4 Teras Utama RE: Elicitation, Documentation, Validation/Negotiation, Management.",
    "mnemonic": "4 Aktiviti Teras RE = E-D-V-M (Elicit, Document, Validate, Manage)."
  },
  {
    "id": 3,
    "code": "P0113",
    "type": "P",
    "pts": 1,
    "eo": "1.1.2",
    "euNo": 1,
    "title": "Requirements Categorization (System vs Project/Process)",
    "question": "Amongst other things, the customer demands the following from the contractor responsible for delivering an information system:\n\nA) The contractor shall process a change request within five days.\nB) The test reports from the integration test must be disclosed for examination and the test report from the system test must be handed over.\nC) At any time, the system shall enable a throughput of 100 transactions per second.\nD) The Subversion tool must be used for configuration management.\nE) Under normal load, the response time must be no more than two seconds in 90 percent of the cases.\n\nWhich two requirements refer to the system to be realized? (2 answers)",
    "options": [
      { "id": "A", "text": "Requirement A", "truth": False },
      { "id": "B", "text": "Requirement B", "truth": False },
      { "id": "C", "text": "Requirement C", "truth": True },
      { "id": "D", "text": "Requirement D", "truth": False },
      { "id": "E", "text": "Requirement E", "truth": True }
    ],
    "correctDisplay": "C, E",
    "whyCorrect": "• C (Requirement C): Betul. 'Throughput 100 transactions/sec' adalah Quality Requirement (Performance) yang merujuk terus kepada keupayaan sistem yang dibina.\n• E (Requirement E): Betul. 'Response time <= 2 seconds dalam 90% kes' adalah Quality Requirement (Performance) yang merujuk kepada kelajuan sistem sebenar.",
    "whyWrong": "• A (Requirement A): Ini adalah Process / Project Requirement bagi kontraktor (tempoh respon change request).\n• B (Requirement B): Ini adalah Project Deliverable / Management Requirement (penyerahan laporan ujian).\n• D (Requirement D): Ini adalah Project / Tooling Constraint untuk pengurusan konfigurasi kontraktor.",
    "extra": "Handbook Bab 1.1 / Syllabus EO 1.1.2: Bezakan antara System Requirements (keperluan produk akhir) dengan Project/Process Requirements (cara projek/organisasi dijalankan).",
    "mnemonic": "System Requirement = Sifat & tingkah laku perisian yang siap (Throughput, Response Time)."
  },

  # ================================================================================================
  # EU2: Fundamental Principles of Requirements Engineering (Q4–Q7, 6 Pts)
  # ================================================================================================
  {
    "id": 4,
    "code": "A3205",
    "type": "A",
    "pts": 1,
    "eo": "2.1.1",
    "euNo": 2,
    "title": "Fundamental Principles of Requirements Engineering",
    "question": "Which of the following statements does NOT represent a fundamental principle of Requirements Engineering? (1 answer)",
    "options": [
      { "id": "A", "text": "Value orientation", "truth": False },
      { "id": "B", "text": "Problem - requirement - solution", "truth": False },
      { "id": "C", "text": "Regular retrospectives", "truth": True },
      { "id": "D", "text": "Systematic and disciplined work", "truth": False }
    ],
    "correctDisplay": "C (Regular retrospectives)",
    "whyCorrect": "• Pilihan C adalah jawapan yang betul (bukan prinsip asas RE). 'Regular retrospectives' adalah amalan Agile / Scrum (Process Practice), bukan salah satu daripada 9 Prinsip Asas RE yang digariskan oleh IREB.",
    "whyWrong": "• A (Value orientation): Prinsip 1 RE — Requirements are a means to an end, not an end in themselves.\n• B (Problem - requirement - solution): Prinsip 5 RE — Memahami masalah sebelum melompat ke solusi teknikal.\n• D (Systematic and disciplined work): Prinsip 9 RE — RE memerlukan kaedah kerja yang berdisiplin dan boleh diulang.",
    "extra": "Handbook Bab 2 / Syllabus EO 2.1.1: 9 Prinsip Asas RE IREB:\n1. Value-Orientation\n2. Stakeholders\n3. Shared Understanding\n4. Context\n5. Problem-Requirement-Solution\n6. Validation\n7. Evolution\n8. Innovation\n9. Systematic Work.",
    "mnemonic": "9 Prinsip IREB: V-S-S-C-P-V-E-I-S. 'Retrospectives' adalah amalan Agile, bukan prinsip teras RE."
  },
  {
    "id": 5,
    "code": "K3206",
    "type": "K",
    "pts": 2,
    "eo": "2.2.1",
    "euNo": 2,
    "title": "Principle 3: Shared Understanding",
    "question": "Shared understanding is a principle of Requirements Engineering. For each of the following statements about shared understanding decide, whether it is true or false.",
    "options": [
      { "id": "A", "text": "Achieving explicit shared understanding is one of the main goals of Requirements Engineering.", "truth": False },
      { "id": "B", "text": "Without shared understanding, it is impossible to identify the relevant requirement sources.", "truth": False },
      { "id": "C", "text": "Some degree of implicit shared understanding is crucial because it is impossible to specify everything explicitly.", "truth": True },
      { "id": "D", "text": "Requirements Engineering in agile development does not work without relying on implicit shared understanding.", "truth": True }
    ],
    "correctDisplay": "A=False, B=False, C=True, D=True",
    "whyCorrect": "• C: True. Dalam mana-mana projek, tahap pemahaman tersirat (implicit shared understanding) adalah sangat penting kerana mustahil secara praktikal untuk mendokumentasikan setiap perincian secara eksplisit.\n• D: True. Pembangunan Agile sangat bergantung kepada implicit shared understanding (melalui komunikasi bersemuka harian dan kerjasama rapat berbanding dokumentasi tebal).",
    "whyWrong": "• A: False. Matlamat utama RE adalah menghasilkan produk bernilai dan mengurangkan risiko pembangunan; 'explicit shared understanding' hanyalah sebahagian cara (means to an end), bukannya matlamat mutlak.\n• B: False. Requirements sources (Stakeholders, Dokumen, Sistem Sedia Ada) boleh dikenalpasti pada peringkat awal sebelum wujudnya shared understanding yang mendalam.",
    "extra": "Handbook Bab 2.3 / Syllabus EO 2.2.1 (Principle 3: Shared Understanding):\n• Shared understanding terdiri daripada Explicit (didokumenkan) dan Implicit (pengetahuan bersama yang difahami).\n• Alat meningkatkan Shared Understanding: Glossary, Prototaip, Model Visual, dan Analogi.",
    "mnemonic": "Shared Understanding = Implicit wajib ada (tak boleh tulis semua benda). Agile bersandar pada Implicit."
  },
  {
    "id": 6,
    "code": "K0202",
    "type": "K",
    "pts": 2,
    "eo": "2.3.1",
    "euNo": 2,
    "title": "Principle 4: Context Boundaries",
    "question": "When defining the system boundary and the context boundary, which aspects need to be considered and which do not need to be considered?",
    "options": [
      { "id": "A", "text": "The system", "truth": True },
      { "id": "B", "text": "The system context", "truth": True },
      { "id": "C", "text": "The application domain", "truth": False },
      { "id": "D", "text": "The interfaces between system and system context", "truth": True }
    ],
    "correctDisplay": "A=Needs to be considered, B=Needs to be considered, C=Does not need to be considered, D=Needs to be considered",
    "whyCorrect": "• A: Needs to be considered. Sistem itu sendiri mentakrifkan apa yang berada di dalam System Boundary (yang boleh dibina dan diubahsuai).\n• B: Needs to be considered. System Context adalah persekitaran relevan yang berinteraksi dengan sistem (Stakeholders, sistem luaran, proses perniagaan, undang-undang).\n• D: Needs to be considered. Antara muka (Interfaces) menghubungkan sistem dengan konteks sistem merentasi System Boundary.",
    "whyWrong": "• C: Does not need to be considered. 'Application domain' merujuk kepada bidang domain secara umum/luas (bukan sempadan diskrit yang membezakan sistem dengan persekitaran relevan).",
    "extra": "Handbook Bab 2.4 / Syllabus EO 2.3.1 (Principle 4: Context):\n1. System Boundary: Memisahkan sistem (apa yang boleh diubah) daripada konteksnya.\n2. Context Boundary: Memisahkan bahagian persekitaran yang relevan daripada persekitaran yang tidak relevan (Irrelevant Environment).\n3. Context: Sumber kepada segala keperluan.",
    "mnemonic": "Context = 3 Lapisan: System (Dalam) ➔ Context (Relevan Luar) ➔ Irrelevant Environment (Diabaikan)."
  },
  {
    "id": 7,
    "code": "A0207",
    "type": "A",
    "pts": 1,
    "eo": "2.3.2",
    "euNo": 2,
    "title": "System Boundary vs Context Boundary Influence",
    "question": "During the Requirements Engineering process for an online database application, you find out that data protection regulations do not apply, as the data processed by the system is anonymized.\nWhat will be influenced by this finding? (1 answer)",
    "options": [
      { "id": "A", "text": "System boundary", "truth": False },
      { "id": "B", "text": "Context boundary", "truth": True },
      { "id": "C", "text": "System interfaces", "truth": False },
      { "id": "D", "text": "Application boundary", "truth": False }
    ],
    "correctDisplay": "B (Context boundary)",
    "whyCorrect": "• Pilihan B adalah jawapan yang betul. Undang-undang perlindungan data (Data Protection Regulations) adalah elemen persekitaran luar. Apabila ia didapati tidak terpakai kerana data telah di-anonymize, elemen peraturan tersebut dialihkan keluar dari Konteks Relevan ke 'Irrelevant Environment'. Oleh itu, yang berubah ialah Context Boundary.",
    "whyWrong": "• A (System boundary): Sempadan sistem mentakrifkan skop sistem yang dibangunkan (bukan penentuan peraturan luar relevan/tidak).\n• C (System interfaces): Antara muka teknikal sistem tidak berubah secara langsung semata-mata kerana penentuan status peraturan undang-undang.\n• D (Application boundary): Bukan istilah piawai sempadan RE mengikut IREB.",
    "extra": "Handbook Bab 2.4 / Syllabus EO 2.3.2: Context Boundary membezakan antara aspek persekitaran yang relevan (termasuk undang-undang & piawaian) dengan aspek persekitaran yang tidak berkaitan.",
    "mnemonic": "Undang-undang luar tak relevan ➔ Context Boundary berubah (berpindah ke Irrelevant Environment)."
  },

  # ================================================================================================
  # EU3: Work Products and Documentation Practices (Q8–Q25, 30 Pts)
  # ================================================================================================
  {
    "id": 8,
    "code": "A3310",
    "type": "A",
    "pts": 1,
    "eo": "3.1.2",
    "euNo": 3,
    "title": "Work Products: Individual vs Work Product Sets",
    "question": "Which of the following statements regarding work products is NOT correct? (1 answer)",
    "options": [
      { "id": "A", "text": "In Requirements Engineering, work products are only created at the end of the specification process.", "truth": True },
      { "id": "B", "text": "A user story is an individual work product.", "truth": False },
      { "id": "C", "text": "The project context determines the choice of work products to be created.", "truth": False },
      { "id": "D", "text": "Requirements can be documented by various kinds of work products.", "truth": False }
    ],
    "correctDisplay": "A (In Requirements Engineering, work products are only created at the end...)",
    "whyCorrect": "• Pilihan A adalah kenyataan yang SALAH (maka jawapan yang betul). Work products dicipta secara berterusan (iteratively & incrementally) sepanjang keseluruhan aktiviti RE, bukannya hanya di penghujung proses spesifikasi.",
    "whyWrong": "• B: Betul. User Story adalah contoh individual work product.\n• C: Betul. Pemilihan work product bergantung kepada konteks projek (cth: Agile vs Linear, keselamatan kritikal vs aplikasi web).\n• D: Betul. Keperluan boleh didokumentasikan dalam pelbagai format (teks bebas, templat, model grafik, jadual).",
    "extra": "Handbook Bab 3.1 / Syllabus EO 3.1.2: Work products merangkumi Individual Work Products (User Story, Use Case, Single Requirement) dan Work Product Sets / Aggregates (SRS, Backlog, Prototype).",
    "mnemonic": "Work Products dihasilkan secara berterusan (bukan tunggu fasa tamat)."
  },
  {
    "id": 9,
    "code": "A3311",
    "type": "A",
    "pts": 1,
    "eo": "3.2.6",
    "euNo": 3,
    "title": "UML Class Diagrams Concepts",
    "question": "Which of the following concepts CANNOT be found in UML class diagrams? (1 answer)",
    "options": [
      { "id": "A", "text": "Associations", "truth": False },
      { "id": "B", "text": "Messages", "truth": True },
      { "id": "C", "text": "Classes", "truth": False },
      { "id": "D", "text": "Multiplicities", "truth": False }
    ],
    "correctDisplay": "B (Messages)",
    "whyCorrect": "• Pilihan B adalah jawapan yang betul. 'Messages' (pertukaran mesej antara objek sepanjang masa) adalah konsep dalam Sequence Diagram atau Communication Diagram (Model Tingkah Laku Interaksi), bukannya Class Diagram yang merupakan Model Struktur Statik.",
    "whyWrong": "• A (Associations), C (Classes), dan D (Multiplicities seperti 0..1, 1..*) adalah komponen asas UML Class Diagram.",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.6: Class Diagram memaparkan struktur data, entiti domain, atribut, perhubungan persatuan (associations), dan penggandaan (multiplicities).",
    "mnemonic": "Class Diagram = Statik (Classes, Associations, Multiplicities). Message = Dinamik (Sequence Diagram)."
  },
  {
    "id": 10,
    "code": "P0416",
    "type": "P",
    "pts": 2,
    "eo": "3.1.3",
    "euNo": 3,
    "title": "Design of Requirements Documents for Stakeholders",
    "question": "You want to design a requirements document in such a way that it is particularly well suited for the people who will work with the document in subsequent development activities.\nWhich two properties should you especially consider in this case? (2 answers)",
    "options": [
      { "id": "A", "text": "High degree of detail", "truth": False },
      { "id": "B", "text": "Low redundancy", "truth": True },
      { "id": "C", "text": "High comprehensibility", "truth": True },
      { "id": "D", "text": "Use of natural language only", "truth": False },
      { "id": "E", "text": "Absence of quality requirements", "truth": False }
    ],
    "correctDisplay": "B, C",
    "whyCorrect": "• B (Low redundancy): Betul. Lebihan maklumat (redundancy) meningkatkan risiko percanggahan (inconsistency) apabila keperluan dikemaskini oleh pasukan pembangunan seterusnya.\n• C (High comprehensibility): Betul. Kejelasan dan mudah difahami membolehkan pembangun, arkitek, dan penguji memahami niat sebenar stakeholder tanpa kekaburan.",
    "whyWrong": "• A (High degree of detail): Perincian melampau (over-specification) menyekat fleksibiliti reka bentuk dan membazirkan kos.\n• D (Use of natural language only): Teks semata-mata terdedah kepada kekaburan; model grafik amat digalakkan.\n• E (Absence of quality requirements): Menghapuskan keperluan kualiti akan menyebabkan sistem gagal memenuhi prestasi dan keselamatan.",
    "extra": "Handbook Bab 3.1 / Syllabus EO 3.1.3: Kriteria kualiti dokumen keperluan mengikut IREB merangkumi Comprehensibility, Unambiguity, Consistency, Low Redundancy, dan Completeness.",
    "mnemonic": "Dokumen mesra pembangun = Mudah faham (Comprehensible) + Tiada pertindihan (Low Redundancy)."
  },
  {
    "id": 11,
    "code": "P0417",
    "type": "P",
    "pts": 2,
    "eo": "3.2.3",
    "euNo": 3,
    "title": "Activity Diagram: Process Modeling (Tender Preparation)",
    "question": "A company wants to support its process of tender preparation with a software system. The following activity diagram models this process:\n\nWhich two of the following statements are correct? (2 answers)",
    "options": [
      { "id": "A", "text": "At any time, it is possible to cancel tender preparation.", "truth": False },
      { "id": "B", "text": "Performing the project risk analysis can be omitted if it is deemed to be safe.", "truth": False },
      { "id": "C", "text": "The activities 'Perform technical analysis' and 'Perform project risk analysis' are performed concurrently.", "truth": True },
      { "id": "D", "text": "Preparing the proposal can only start after 'Perform technical analysis' and 'Perform project risk analysis' are finished.", "truth": True },
      { "id": "E", "text": "In the process, 'Perform technical analysis' must be completed prior to performing 'Perform project risk analysis'.", "truth": False }
    ],
    "correctDisplay": "C, D",
    "whyCorrect": "• C: Betul. Fork node (bar tebal pemisah) memulakan 'Perform technical analysis' dan 'Perform project risk analysis' secara serentak (concurrently/in parallel).\n• D: Betul. Join node (bar tebal penyatu) memerlukan kedua-dua aktiviti selesai sebelum token disalurkan ke aktiviti seterusnya 'Prepare proposal'.",
    "whyWrong": "• A: Salah. Rajah tidak mempunyai aliran keluar pembatalan (interruptible region / cancel flow) yang membolehkan proses dibatalkan pada bila-bila masa.\n• B: Salah. Tiada decision node bersyarat (guard) yang membenarkan analisa risiko dilangkau.\n• E: Salah. Fork selari tidak menetapkan susunan urutan antara analisis teknikal dan analisis risiko.",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.3: Activity Diagram menggunakan Fork Node (membuka aliran selari) dan Join Node (menunggu semua aliran selari selesai).",
    "mnemonic": "Fork = Mula Selari. Join = Tunggu Semua Cabang Selesai."
  },
  {
    "id": 12,
    "code": "K0418",
    "type": "K",
    "pts": 2,
    "eo": "3.2.1",
    "euNo": 3,
    "title": "Notations for Functional Requirements (Natural Language vs Models)",
    "question": "Which of the following statements on the choice of notations for the documentation of functional requirements apply and which do not apply?",
    "options": [
      { "id": "A", "text": "For the documentation of functional requirements, a standardized modeling language should be used, if possible.", "truth": True },
      { "id": "B", "text": "Natural language is suited best when requirements must be understood by all stakeholders.", "truth": True },
      { "id": "C", "text": "Natural language should always be preferred to graphical models, since models are too abstract for most stakeholders.", "truth": False },
      { "id": "D", "text": "The use of graphical models alone without natural language is not recommended.", "truth": True }
    ],
    "correctDisplay": "A=Applies, B=Applies, C=Does not apply, D=Applies",
    "whyCorrect": "• A: Applies. Notasi standard seperti UML / SysML / BPMN mengurangkan kekaburan dan membolehkan pemahaman seragam.\n• B: Applies. Bahasa semulajadi adalah format paling universal yang boleh dibaca dan disemak oleh semua lapisan stakeholder tanpa latihan khas.\n• D: Applies. Menggabungkan model grafik bersama teks penerangan adalah amalan terbaik IREB (Hybrid Documentation) kerana model grafik semata-mata tidak dapat menerangkan konteks dan nuansa penuh.",
    "whyWrong": "• C: Does not apply. Model grafik TIDAK sepatutnya ditolak; rajah visual mengurangkan beban kognitif dan membantu struktur konseptual.",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.1: 3 bentuk dokumentasi keperluan: Natural Language, Conceptual Models, dan Hybrid (gabungan teks dan model).",
    "mnemonic": "Dokumentasi Terbaik = Teks Semulajadi + Model Konseptual Standard (Hybrid)."
  },
  {
    "id": 13,
    "code": "K3423",
    "type": "K",
    "pts": 2,
    "eo": "3.1.4",
    "euNo": 3,
    "title": "Quality Criteria for Work Products",
    "question": "IREB defines quality criteria for work products. Which of the following statements about the quality criteria are true and which are false?",
    "options": [
      { "id": "A", "text": "Requirements that cannot be tested are not verifiable.", "truth": True },
      { "id": "B", "text": "Traceability makes it easier to assess the impact of changes.", "truth": True },
      { "id": "C", "text": "Work products are only comprehensible if all requirements are documented using the same form of representation.", "truth": False },
      { "id": "D", "text": "The degree of completeness should be balanced against the cost of creating the work product.", "truth": True }
    ],
    "correctDisplay": "A=True, B=True, C=False, D=True",
    "whyCorrect": "• A: True. Syarat utama verifiability (kebolehujian) ialah wujudnya kriteria penerimaan (acceptance criteria) atau kes ujian yang boleh mengesahkan pematuhan keperluan.\n• B: True. Traceability (kebolehkesanan) menghubungkan keperluan kepada reka bentuk, kod dan ujian, membolehkan Impact Analysis dijalankan dengan pantas apabila ada perubahan.\n• D: True. Prinsip Value-Orientation mentakrifkan bahawa tahap kelengkapan (completeness) mestilah seimbang dengan kos dan pulangan nilai (cost-benefit balance).",
    "whyWrong": "• C: False. Kebolehfahaman (comprehensibility) TIDAK mewajibkan semua keperluan ditulis dalam satu bentuk perwakilan yang sama; sebaliknya gabungan teks, jadual, dan rajah (pelbagai bentuk) selalunya jauh lebih mudah difahami.",
    "extra": "Handbook Bab 3.1 / Syllabus EO 3.1.4: Kriteria Kualiti Keperluan: Unambiguous, Complete, Consistent, Verifiable, Modifiable, Traceable, Comprehensible.",
    "mnemonic": "Kualiti = Boleh Diuji (Verifiable) + Boleh Dikesan (Traceable) + Seimbang Kos (Value)."
  },
  {
    "id": 14,
    "code": "P0510",
    "type": "P",
    "pts": 2,
    "eo": "3.3.2",
    "euNo": 3,
    "title": "Phrase Templates / Sentence Templates (SOPHIST)",
    "question": "A phrase template can be used to document natural-language requirements. You want to introduce such a template in your project and have to convince your project manager of the benefits.\nWhich two arguments can you use to convince your project manager? (2 answers)",
    "options": [
      { "id": "A", "text": "An author of requirements is guided by the template while formulating the requirements.", "truth": True },
      { "id": "B", "text": "Using a phrase template guarantees that all requirements are completely documented.", "truth": False },
      { "id": "C", "text": "The requirements can be formulated more easily and in shorter time.", "truth": False },
      { "id": "D", "text": "Requirements written using a phrase template contain fewer linguistic ambiguities.", "truth": True },
      { "id": "E", "text": "Phrase templates make it easier to fulfill legal and regulatory constraints.", "truth": False }
    ],
    "correctDisplay": "A, D",
    "whyCorrect": "• A: Betul. Sentence template menyediakan struktur tatabahasa berpandu (scaffolding) yang membimbing penulis memasukkan peranan, modal verb, fungsi dan syarat.\n• D: Betul. Struktur yang seragam dan ketat mengurangkan kekaburan bahasa (linguistic ambiguities seperti nominalization, passive voice, dan unreferenced pronouns).",
    "whyWrong": "• B: Salah. Templat tidak dapat menjamin kelengkapan isi kandungan (semantic completeness) — ia hanya menjamin struktur sintaksis.\n• C: Salah. Menulis mengikut templat pada awalnya memerlukan masa dan usaha kognitif tambahan untuk menstrukturkan ayat.\n• E: Salah. Templat itu sendiri tidak menjamin pematuhan kekangan undang-undang.",
    "extra": "Handbook Bab 3.3 / Syllabus EO 3.3.2: Sentence Template (SOPHIST/MARE): [Condition] [System] <SHALL/SHOULD/WILL> [Action] [Object] [Criteria].",
    "mnemonic": "Sentence Template = Panduan Penulisan (Guided) + Kurang Kekaburan (Less Ambiguity)."
  },
  {
    "id": 15,
    "code": "A0508",
    "type": "A",
    "pts": 1,
    "eo": "3.3.1",
    "euNo": 3,
    "title": "Transformation Effects / Linguistic Ambiguity (Nominalization)",
    "question": "You are given the following requirement: \"The system Alpha should be able to perform a calculation of the average speed at runtime.\"\nWhich transformation effect is visible in this requirement? (1 answer)",
    "options": [
      { "id": "A", "text": "Nominalization", "truth": True },
      { "id": "B", "text": "Incompletely specified condition", "truth": False },
      { "id": "C", "text": "Incompletely specified process verb", "truth": False },
      { "id": "D", "text": "Universal quantification", "truth": False }
    ],
    "correctDisplay": "A (Nominalization)",
    "whyCorrect": "• Pilihan A adalah jawapan yang betul. 'Perform a calculation' adalah penamaan kata kerja (Nominalization) bagi kata kerja asal 'calculate'. Penukaran kata kerja kepada kata nama menyembunyikan proses aktif dan mengaburkan siapa atau bagaimana pengiraan itu berlaku.",
    "whyWrong": "• B (Incompletely specified condition): Merujuk kepada syarat if/when yang tidak lengkap.\n• C (Incompletely specified process verb): Kata kerja proses tanpa objek/parameter jelas.\n• D (Universal quantification): Penggunaan kata penentu sejagat seperti 'all', 'always', 'every'.",
    "extra": "Handbook Bab 3.3 / Syllabus EO 3.3.1: 4 Kesan Transformasi Bahasa (Linguistic Effects): 1. Nominalization (kata kerja jadi kata nama), 2. Deletion/Omission (maklumat hilang), 3. Incomplete Condition, 4. Universal Quantification.",
    "mnemonic": "Nominalization = Kata kerja (calculate) diubah jadi kata nama (perform a calculation)."
  },
  {
    "id": 16,
    "code": "K3520",
    "type": "K",
    "pts": 2,
    "eo": "3.1.5",
    "euNo": 3,
    "title": "Template-based Work Products",
    "question": "Which of the following statements are true and which are false when working with template-based work products?",
    "options": [
      { "id": "A", "text": "Structures of templates can be adapted to project-specific requirements.", "truth": True },
      { "id": "B", "text": "Using a template guarantees that the requirements documented with this template are complete.", "truth": False },
      { "id": "C", "text": "An empty section in a template document points out to a reader that this information was forgotten.", "truth": False },
      { "id": "D", "text": "Using a template makes it easier to reuse already existing requirements in another project.", "truth": True }
    ],
    "correctDisplay": "A=True, B=False, C=False, D=True",
    "whyCorrect": "• A: True. Templat struktur dokumen (cth: IEEE 830 / ISO 29148 / Volere) boleh dan wajar disesuaikan (tailored) mengikut keperluan dan skala projek.\n• D: True. Format struktur yang standard memudahkan pemindahan dan guna semula (reuse) artifak keperluan antara projek berbeza.",
    "whyWrong": "• B: False. Menggunakan templat tidak menjamin kandungan lengkap sepenuhnya (hanya menyediakan kerangka tajuk).\n• C: False. Seksyen kosong tidak semestinya bermaksud maklumat dilupakan; ia mungkin sengaja tidak berkenaan (N/A) untuk projek tersebut.",
    "extra": "Handbook Bab 3.1 / Syllabus EO 3.1.5: Template dokumen menyediakan standardisasi, mempermudah navigasi pembaca, dan membantu proses semakan.",
    "mnemonic": "Template Dokumen = Boleh disesuaikan (Tailored) + Memudahkan Guna Semula (Reuse)."
  },
  {
    "id": 17,
    "code": "A3521",
    "type": "A",
    "pts": 1,
    "eo": "3.2.4",
    "euNo": 3,
    "title": "Use Case Modeling & Specifications",
    "question": "A system needs to be developed for managing the fleet of a car-sharing company. The system must support the use case 'Rent car'.\nWhich of the following is NOT a good reason to detail this use case using a use case specification? (1 answer)",
    "options": [
      { "id": "A", "text": "The use case is critical for the success of the system.", "truth": False },
      { "id": "B", "text": "The customer has extensive domain knowledge.", "truth": True },
      { "id": "C", "text": "The use case describes a complex procedure.", "truth": False },
      { "id": "D", "text": "The developers are unfamiliar with the domain.", "truth": False }
    ],
    "correctDisplay": "B (The customer has extensive domain knowledge)",
    "whyCorrect": "• Pilihan B adalah jawapan yang betul. Jika pelanggan mempunyai pengetahuan domain yang sangat mendalam (dan pembangun turut memahaminya), tahap perincian spesifikasi formal yang tebal tidak begitu kritikal. Sebaliknya, perincian mendalam wajib dibuat jika pembangun TIDAK kenal domain (D), prosedur terlalu kompleks (C), atau fungsi itu sangat kritikal untuk bisnes (A).",
    "whyWrong": "• A, C, dan D adalah alasan kukuh mengapa sesuatu Use Case wajib diperincikan dengan Use Case Specification bertulis (Main Flow, Alternative Flows, Pre/Post-conditions).",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.4: Tahap perincian Use Case bergantung kepada risiko, kerumitan aliran, dan tahap shared understanding antara stakeholder dengan pasukan pembangun.",
    "mnemonic": "Perincian Use Case diperlukan bila: Kompleks, Berisiko Tinggi, atau Pasukan Tak Kenal Domain."
  },
  {
    "id": 18,
    "code": "K0619",
    "type": "K",
    "pts": 2,
    "eo": "3.2.6",
    "euNo": 3,
    "title": "UML Class Diagram: Multiplicities (Short Film Contest)",
    "diagramHtml": f"<img src='{img_q18}' alt='Diagram Q18' />",
    "question": "To support young actors and directors, a contest for short films is held. The three best films will be presented with an award. The films are submitted by a group of creators (actors, directors, producers).\nWhich of the following statements about the class diagram match the domain and which do not match?",
    "options": [
      { "id": "A", "text": "A creator can only submit one film.", "truth": False },
      { "id": "B", "text": "A film can be presented with an award without a creator having been involved in the film.", "truth": False },
      { "id": "C", "text": "A creator can participate in multiple films, but can win only one award.", "truth": False },
      { "id": "D", "text": "A creator can only win an award if they also directed the film.", "truth": False },
      { "id": "E", "text": "A film can be presented with an award even if the creator who submitted the film was not involved in creating it.", "truth": True }
    ],
    "correctDisplay": "A=Does not match, B=Does not match, C=Does not match, D=Does not match, E=Matches",
    "whyCorrect": "• E: Matches. Berdasarkan rajah kelas, persatuan penyerahan (submission) adalah berasingan daripada penglibatan penciptaan. Maka seseorang pemohon boleh menghantar filem walaupun peranan penciptaannya berbeza.",
    "whyWrong": "• A: Does not match. Penggandaan (multiplicity) membenarkan seorang pencipta menghantar lebih daripada satu filem (*).\n• B: Does not match. Filem mesti mempunyai sekurang-kurangnya seorang pencipta (1..*).\n• C: Does not match. Tiada kekangan bahawa pencipta hanya boleh memenangi satu anugerah.\n• D: Does not match. Anugerah diberikan kepada filem, bukan terhad kepada peranan pengarah sahaja.",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.6: Membaca Multiplicities UML Class Diagram (0..1, 1, 1..*, *).",
    "mnemonic": "Semak multiplicities pada hujung garis persatuan kelas dengan teliti."
  },
  {
    "id": 19,
    "code": "A0620",
    "type": "A",
    "pts": 1,
    "eo": "3.2.4",
    "euNo": 3,
    "title": "Use Case Diagrams Boundaries & Actors",
    "question": "What is NOT depicted in a use case diagram? (1 answer)",
    "options": [
      { "id": "A", "text": "Actors of the system", "truth": False },
      { "id": "B", "text": "System boundary", "truth": False },
      { "id": "C", "text": "Sequence of the use cases", "truth": True },
      { "id": "D", "text": "Use cases of the system", "truth": False }
    ],
    "correctDisplay": "C (Sequence of the use cases)",
    "whyCorrect": "• Pilihan C adalah jawapan yang betul. Use Case Diagram TIDAK menunjukkan susunan urutan masa (sequence of execution). Urutan aliran tingkah laku hanya dipaparkan dalam Activity Diagram atau Sequence Diagram.",
    "whyWrong": "• A (Actors): Dipaparkan sebagai ikon orang (stick figure).\n• B (System boundary): Dipaparkan sebagai kotak segi empat tepat (system boundary box).\n• D (Use cases): Dipaparkan sebagai bentuk bujur (oval).",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.4: Use Case Diagram memaparkan skop fungsi sistem, pelaku (actors), sempadan sistem, dan hubungan (include, extend, generalization).",
    "mnemonic": "Use Case Diagram = SKOP (Bukan Urutan Masa / Sequence)."
  },
  {
    "id": 20,
    "code": "K3605",
    "type": "K",
    "pts": 2,
    "eo": "3.2.5",
    "euNo": 3,
    "title": "UML State Machine Diagram (Intranet Authorization)",
    "diagramHtml": f"<img src='{img_q20}' alt='Diagram Q20' />",
    "question": "A company wants to introduce an authorization process for accessing confidential parts of the company's intranet by issuing time-limited tokens. The following state machine diagram models this process:\nFor each of the statements on the diagram, decide whether it is true or false.",
    "options": [
      { "id": "A", "text": "The state 'Active' can only be reached if a request was submitted by an authorized person.", "truth": False },
      { "id": "B", "text": "From the state 'Active' the state 'Idle' can only be reached via the transition with the event 'Token returned'.", "truth": False },
      { "id": "C", "text": "From the state 'Active', the state 'Idle' can be reached via a transition that is taken when the token has expired.", "truth": True },
      { "id": "D", "text": "When a token is requested and the request has not been verified yet, the system is in the state 'Requested'.", "truth": True }
    ],
    "correctDisplay": "A=False, B=False, C=True, D=True",
    "whyCorrect": "• C: True. Terdapat peralihan automatik berasaskan masa (time event cth: after(duration)) dari 'Active' kembali ke 'Idle' apabila token tamat tempoh.\n• D: True. Semasa permohonan dihantar dan sedang menunggu pengesahan, sistem berada dalam keadaan (state) 'Requested'.",
    "whyWrong": "• A: False. Semak peralihan: jika permohonan dibuat dan diluluskan melalui laluan bypass atau auto-grant, state Active boleh dicapai mengikut guard yang ditentukan dalam model.\n• B: False. State 'Idle' juga boleh dicapai apabila token tamat tempoh (timeout event), bukan semata-mata 'Token returned'.",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.5: State Machine Diagram memodelkan kitaran hayat objek (States, Transitions, Events, Guards, Actions).",
    "mnemonic": "State Machine = State (Keadaan), Event (Pencetus), Guard [Syarat], Action (Tindakan)."
  },
  {
    "id": 21,
    "code": "K0643",
    "type": "K",
    "pts": 2,
    "eo": "3.2.3",
    "euNo": 3,
    "title": "Activity Diagram: Performing a Measurement",
    "diagramHtml": f"<img src='{img_q21}' alt='Diagram Q21' />",
    "question": "The following activity diagram represents performing a measurement.\nDo the following statements match the above diagram?",
    "options": [
      { "id": "A", "text": "Initialize measuring device must happen prior to Register at server.", "truth": False },
      { "id": "B", "text": "Register at server happens as soon as Load certificates is ready.", "truth": False },
      { "id": "C", "text": "Initialize network connection and Load certificates must finish at the same time.", "truth": False },
      { "id": "D", "text": "Deactivate measuring device is executed as soon as Data receipt confirmed is true.", "truth": True }
    ],
    "correctDisplay": "A=Does not match, B=Does not match, C=Does not match, D=Matches",
    "whyCorrect": "• D: Matches. Berdasarkan rajah aktiviti, 'Deactivate measuring device' menerima aliran kawalan sebaik sahaja peristiwa/isyarat 'Data receipt confirmed' diterima.",
    "whyWrong": "• A: Does not match. 'Initialize measuring device' dan 'Initialize network connection' berada dalam cabang Fork selari, maka susunan antara keduanya bebas.\n• B: Does not match. 'Register at server' memerlukan KEDUA-DUA aliran masuk ke Join Node selesai (Network initialized DAN Certificates loaded), bukan certificates sahaja.\n• C: Does not match. Join node menunggu kedua-dua cabang selesai, tetapi ia tidak mewajibkan kedua-duanya tamat pada saat yang sama serentak (asynchronous completion).",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.3: Activity Diagram Control Flows: Fork Node (Split) & Join Node (Synchronization).",
    "mnemonic": "Join Node = Tunggu kedua-dua cabang siap (tak semestinya siap serentak)."
  },
  {
    "id": 22,
    "code": "P0623",
    "type": "P",
    "pts": 2,
    "eo": "3.2.1",
    "euNo": 3,
    "title": "Advantages of Graphical Conceptual Models",
    "question": "In Requirements Engineering, which two substantial advantages do graphical models (e.g., use case models or state machines) have over plain textual specifications in natural language? (2 answers)",
    "options": [
      { "id": "A", "text": "Models often focus on specific aspects and reduce the cognitive load for understanding the requirements.", "truth": True },
      { "id": "B", "text": "Models allow the complete description of requirements for a planned system.", "truth": False },
      { "id": "C", "text": "Models can be checked more easily than natural language and have a restricted syntax that reduces possible ambiguities and omissions.", "truth": True },
      { "id": "D", "text": "Models are created with tools using a repository. Therefore, models are better suited for managing requirements.", "truth": False },
      { "id": "E", "text": "With proper tools, source code can be generated from models, thus saving the effort for testing.", "truth": False }
    ],
    "correctDisplay": "A, C",
    "whyCorrect": "• A: Betul. Model grafik menumpukan perhatian kepada perspektif tertentu (struktur, fungsi, tingkah laku) sekaligus mengurangkan beban kognitif (cognitive load) pembaca.\n• C: Betul. Model mempunyai sintaksis dan tatabahasa visual yang ketat dan terhad (restricted syntax), memudahkan semakan konsistensi dan mengurangkan kekaburan berbanding teks bebas.",
    "whyWrong": "• B: Salah. Model grafik tidak boleh menggambarkan kesemua 100% perincian sistem secara lengkap tanpa sokongan teks.\n• D: Salah. Teks juga boleh disimpan dalam repositori alat RE.\n• E: Salah. Penjanaan kod daripada model TIDAK menghapuskan keperluan pengujian (testing).",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.1: 3 Perspektif Model RE: 1. Structure (Class Diagram), 2. Function (Activity/DFD), 3. Behavior (State Machine).",
    "mnemonic": "Kelebihan Model Visual = Kurang Beban Kognitif (Focus) + Sintaksis Ketat (Kurang Kabur)."
  },
  {
    "id": 23,
    "code": "K0624",
    "type": "K",
    "pts": 2,
    "eo": "3.2.6",
    "euNo": 3,
    "title": "UML Class Diagram: Booking / Rental System",
    "diagramHtml": f"<img src='{img_q23}' alt='Diagram Q23' />",
    "question": "For each of the statements on the diagram below, decide whether it is true or false.",
    "options": [
      { "id": "A", "text": "A customer must have at least one booking.", "truth": False },
      { "id": "B", "text": "A vehicle can be booked in multiple bookings.", "truth": True },
      { "id": "C", "text": "A booking must include at least one vehicle.", "truth": True },
      { "id": "D", "text": "A customer cannot book more than one vehicle per booking.", "truth": False }
    ],
    "correctDisplay": "A=False, B=True, C=True, D=False",
    "whyCorrect": "• B: True. Multiplicity pada persatuan Vehicle ke Booking ialah 0..* (*), bermaksud kenderaan yang sama boleh mempunyai banyak tempahan pada masa berbeza.\n• C: True. Multiplicity pada hujung Vehicle dari Booking ialah 1..*, bermaksud sesuatu tempahan wajib mengandungi sekurang-kurangnya 1 kenderaan.",
    "whyWrong": "• A: False. Multiplicity pada hujung Booking dari Customer ialah 0..*, bermaksud pelanggan boleh wujud dalam sistem walaupun belum membuat sebarang tempahan.\n• D: False. Multiplicity pada Vehicle ialah 1..*, membenarkan pelanggan menempah lebih daripada satu kenderaan dalam satu tempahan.",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.6: Cara mentafsir Multiplicities: Baca angka pada hujung kelas bertentangan (Target Class Multiplicity).",
    "mnemonic": "0..* = Pilihan (Optional). 1..* = Wajib sekurang-kurangnya satu (Mandatory)."
  },
  {
    "id": 24,
    "code": "P0626",
    "type": "P",
    "pts": 2,
    "eo": "3.2.2",
    "euNo": 3,
    "title": "Data Flow Diagram (DFD) vs Context Diagram",
    "question": "You are modeling the requirements for a management system to process customer orders. Which two of the following elements belong to a Data Flow Diagram (DFD)? (2 answers)",
    "options": [
      { "id": "A", "text": "Data stores", "truth": True },
      { "id": "B", "text": "Classes", "truth": False },
      { "id": "C", "text": "Processes / Activities", "truth": True },
      { "id": "D", "text": "Use cases", "truth": False },
      { "id": "E", "text": "Lifelines", "truth": False }
    ],
    "correctDisplay": "A, C",
    "whyCorrect": "• A (Data stores): Betul. Data Store (simpanan data / pangkalan data) ialah komponen asas DFD (simbol dua garis selari / kotak terbuka).\n• C (Processes / Activities): Betul. Process / Function (simbol bulatan / bujur) memanipulasi dan mengubah aliran data.",
    "whyWrong": "• B (Classes): Komponen UML Class Diagram.\n• D (Use cases): Komponen Use Case Diagram.\n• E (Lifelines): Komponen UML Sequence Diagram.",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.2: 4 Komponen Utama DFD: 1. Process (Bulatan), 2. External Entity / Terminator (Kotak), 3. Data Store (Garis Selari), 4. Data Flow (Anak Panah).",
    "mnemonic": "DFD = Proses + Aliran Data + Simpanan Data (Data Store) + Entiti Luar."
  },
  {
    "id": 25,
    "code": "A0627",
    "type": "A",
    "pts": 1,
    "eo": "3.2.1",
    "euNo": 3,
    "title": "Three Perspectives of Conceptual Modeling",
    "question": "When specifying a system, different aspects have to be considered. Conceptual models are categorized into three perspectives.\nWhich of the following is NOT one of the three perspectives of conceptual modeling in Requirements Engineering? (1 answer)",
    "options": [
      { "id": "A", "text": "Structure perspective", "truth": False },
      { "id": "B", "text": "Function perspective", "truth": False },
      { "id": "C", "text": "Behavior perspective", "truth": False },
      { "id": "D", "text": "Implementation perspective", "truth": True }
    ],
    "correctDisplay": "D (Implementation perspective)",
    "whyCorrect": "• Pilihan D adalah jawapan yang betul (bukan perspektif RE). 'Implementation perspective' adalah aspek reka bentuk seni bina dan pengkodan (Software Architecture/Design), bukannya model konseptual RE.",
    "whyWrong": "• A (Structure perspective): Model struktur/data (cth: UML Class Diagram, ERD).\n• B (Function perspective): Model aliran fungsi/proses (cth: Activity Diagram, DFD, Use Case).\n• C (Behavior perspective): Model tingkah laku dinamik mengikut masa/keadaan (cth: State Machine Diagram).",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.1: 3 Perspektif Model Konseptual IREB: 1. Structure (Apa data/objek?), 2. Function (Apa fungsi/aliran?), 3. Behavior (Bagaimana respon/keadaan berubah?).",
    "mnemonic": "3 Perspektif Model RE = Struktur, Fungsi, Tingkah Laku (S-F-B)."
  },

  # ================================================================================================
  # EU4: Practices for Requirements Elaboration (Q26–Q35, 14 Pts)
  # ================================================================================================
  {
    "id": 26,
    "code": "A3409",
    "type": "A",
    "pts": 1,
    "eo": "4.2.1",
    "euNo": 4,
    "title": "Stakeholder Identification (Requirements Engineer Role)",
    "question": "You have been appointed as a Requirements Engineer in a company and have been assigned to an ongoing project.\nWhich of the following is the first thing you should do to identify the stakeholders? (1 answer)",
    "options": [
      { "id": "A", "text": "Organize a requirements workshop with the management.", "truth": False },
      { "id": "B", "text": "Search in the existing project documentation for stakeholders.", "truth": True },
      { "id": "C", "text": "Ask your colleagues for the names of important stakeholders.", "truth": False },
      { "id": "D", "text": "Define the system boundary.", "truth": False }
    ],
    "correctDisplay": "B (Search in the existing project documentation for stakeholders)",
    "whyCorrect": "• Pilihan B adalah tindakan pertama yang paling beretika dan efisien. Menyemak dokumentasi projek sedia ada (Project Charter, Organisasi Projek, Minit Mesyuarat, Kontrak) memanfaatkan sumber artefak sedia ada tanpa membuang masa stakeholder secara pramatang.",
    "whyWrong": "• A: Mengadakan bengkel tanpa mengetahui siapa stakeholder yang tepat adalah tidak produktif.\n• C: Bergantung kepada ingatan lisan rakan sekerja tidak menyeluruh dan kurang profesional berbanding rekod bertulis.\n• D: Penentuan sempadan sistem memerlukan penglibatan stakeholder yang telah dikenal pasti.",
    "extra": "Handbook Bab 4.2 / Syllabus EO 4.2.1: Teknik Mengenalpasti Stakeholder: Semakan Dokumen Sedia Ada, Templat Peranan, Analisis Konteks, Snowball Effect.",
    "mnemonic": "Langkah pertama kenalpasti stakeholder = Semak Dokumentasi Projek Sedia Ada."
  },
  {
    "id": 27,
    "code": "P0309",
    "type": "P",
    "pts": 1,
    "eo": "4.1.1",
    "euNo": 4,
    "title": "Requirements Sources Types",
    "question": "Requirements Engineering distinguishes between different types of requirements sources.\nWhich two of the following are types of requirements sources according to IREB? (2 answers)",
    "options": [
      { "id": "A", "text": "Stakeholders", "truth": True },
      { "id": "B", "text": "Documents", "truth": True },
      { "id": "C", "text": "Prototypes", "truth": False },
      { "id": "D", "text": "Requirements elicitation techniques", "truth": False },
      { "id": "E", "text": "Sentence templates", "truth": False }
    ],
    "correctDisplay": "A, B",
    "whyCorrect": "• A (Stakeholders): Betul. Stakeholders ialah sumber keperluan berasaskan manusia (orang, peranan, kumpulan sasaran).\n• B (Documents): Betul. Dokumen ialah sumber bertulis (undang-undang, piawaian industri, spesifikasi sistem terdahulu, manual).",
    "whyWrong": "• C (Prototypes): Prototaip adalah kaedah elisitasi / validasi (bukan jenis sumber teras).\n• D (Elicitation techniques): Teknik elisitasi adalah cara mendapatkan keperluan dari sumber, bukan sumber itu sendiri.\n• E (Sentence templates): Alat pendokumentasian keperluan.",
    "extra": "Handbook Bab 4.1 / Syllabus EO 4.1.1: 3 Jenis Sumber Keperluan Utama IREB: 1. Stakeholders, 2. Documents, 3. Systems in Operation (Sistem sedia ada / sistem pesaing).",
    "mnemonic": "3 Sumber Keperluan = Orang (Stakeholders) + Kertas (Documents) + Mesin (Systems in Operation)."
  },
  {
    "id": 28,
    "code": "A0312",
    "type": "A",
    "pts": 1,
    "eo": "4.3.3",
    "euNo": 4,
    "title": "Kano Model: Eliciting Dissatisfiers (Basic Factors)",
    "question": "The Kano model states that dissatisfiers (basic factors) are hard to elicit.\nWhich of the techniques mentioned below is the most effective elicitation technique to elicit basic factors? (1 answer)",
    "options": [
      { "id": "A", "text": "Interview", "truth": False },
      { "id": "B", "text": "Questionnaire", "truth": False },
      { "id": "C", "text": "Brainstorming", "truth": False },
      { "id": "D", "text": "Field observation", "truth": True }
    ],
    "correctDisplay": "D (Field observation)",
    "whyCorrect": "• Pilihan D adalah jawapan yang betul. Basic factors (keperluan tersirat yang dianggap 'taken for granted') jarang disebut secara lisan oleh pengguna semasa temuduga. Teknik pemerhatian (Observation / Field Observation / Apprenticeship) adalah paling berkesan kerana pemerhati dapat melihat secara langsung apa yang dilakukan oleh pengguna dalam persekitaran kerja sebenar.",
    "whyWrong": "• A (Interview) & B (Questionnaire): Berkesan untuk Performance Factors (keperluan eksplisit), tetapi pengguna lupa menyatakan faktor asas kerana menganggapnya jelas.\n• C (Brainstorming): Berkesan untuk Excitement Factors (faktor inovasi).",
    "extra": "Handbook Bab 4.3 / Syllabus EO 4.3.3: Model Kano:\n1. Basic Factors (Dissatisfiers) ➔ Elicit via Observation & Document Archeology.\n2. Performance Factors (Satisfiers) ➔ Elicit via Interview & Survey.\n3. Excitement Factors (Delighters) ➔ Elicit via Brainstorming & Creativity Workshops.",
    "mnemonic": "Basic Factors (Tersirat) = Observation (Tengok cara kerja sebenar)."
  },
  {
    "id": 29,
    "code": "P0313",
    "type": "P",
    "pts": 2,
    "eo": "4.3.1",
    "euNo": 4,
    "title": "Observation Techniques (Apprenticeship & Shadowing)",
    "question": "Which two of the following are observation techniques in Requirements Engineering? (2 answers)",
    "options": [
      { "id": "A", "text": "Apprenticeship", "truth": True },
      { "id": "B", "text": "Focus group", "truth": False },
      { "id": "C", "text": "Perspective-based reading", "truth": False },
      { "id": "D", "text": "Shadowing", "truth": True },
      { "id": "E", "text": "Survey", "truth": False }
    ],
    "correctDisplay": "A, D",
    "whyCorrect": "• A (Apprenticeship): Betul. Requirements Engineer bertindak sebagai 'perantis' yang belajar dan mencuba melakukan tugas pengguna di bawah bimbingan pakar domain.\n• D (Shadowing): Betul. Requirements Engineer mengekori dan memerhatikan pengguna menjalankan tugas harian mereka tanpa mencelah.",
    "whyWrong": "• B (Focus group): Teknik perbincangan kumpulan / bengkel.\n• C (Perspective-based reading): Teknik semakan / validasi keperluan.\n• E (Survey): Teknik elisitasi berasaskan soal selidik bertulis.",
    "extra": "Handbook Bab 4.3 / Syllabus EO 4.3.1: 2 Teknik Pemerhatian Utama: 1. Field Observation (termasuk Shadowing), 2. Active Observation / Apprenticeship.",
    "mnemonic": "Pemerhatian = Shadowing (Ekor pengguna) + Apprenticeship (Belajar jadi perantis)."
  },
  {
    "id": 30,
    "code": "A3410",
    "type": "A",
    "pts": 1,
    "eo": "4.4.2",
    "euNo": 4,
    "title": "Conflict Resolution Techniques (Matrix Analysis)",
    "question": "During requirements elaboration, you detect a conflict between two stakeholders regarding the performance requirements of a new system. Both stakeholders have valid arguments and none of them is willing to change their position.\nWhich conflict resolution technique is most suitable in this situation? (1 answer)",
    "options": [
      { "id": "A", "text": "Agreement", "truth": False },
      { "id": "B", "text": "Compromise", "truth": False },
      { "id": "C", "text": "Voting", "truth": False },
      { "id": "D", "text": "Variant matrix / decision matrix", "truth": True }
    ],
    "correctDisplay": "D (Variant matrix / decision matrix)",
    "whyCorrect": "• Pilihan D adalah jawapan yang betul. Apabila kedua-dua pihak mempunyai hujah teknikal yang kukuh dan enggan beralih arah, Variant Matrix / Decision Matrix (Analisis Matriks Kriteria) menyediakan kaedah objektif berasaskan kriteria skor berwajaran untuk menilai kebaikan dan keburukan setiap pilihan secara telus.",
    "whyWrong": "• A (Agreement): Tidak dapat dicapai kerana tiada pihak bersetuju.\n• B (Compromise): Kompromi separuh jalan mungkin menghasilkan prestasi yang tidak optimum untuk kedua-dua pihak.\n• C (Voting): Pengundian boleh meminggirkan minoriti yang mempunyai hujah teknikal yang betul.",
    "extra": "Handbook Bab 4.4 / Syllabus EO 4.4.2: Teknik Resolusi Konflik: Agreement, Compromise, Voting, Overruling (Kuasa Pemutus), Matrix/Variant Analysis.",
    "mnemonic": "Konflik teknikal seimbang = Decision Matrix (Nilai skor kriteria secara objektif)."
  },
  {
    "id": 31,
    "code": "P3411",
    "type": "P",
    "pts": 2,
    "eo": "4.2.2",
    "euNo": 4,
    "title": "Stakeholder Management: Key Stakeholder Attributes",
    "question": "Which are the two most important attributes in a stakeholder list? (2 answers)",
    "options": [
      { "id": "A", "text": "Influence / power in the project", "truth": True },
      { "id": "B", "text": "Availability during the project", "truth": True },
      { "id": "C", "text": "Salary grade", "truth": False },
      { "id": "D", "text": "Marital status", "truth": False },
      { "id": "E", "text": "Years of experience in the company", "truth": False }
    ],
    "correctDisplay": "A, B",
    "whyCorrect": "• A (Influence / power): Betul. Mengetahui tahap pengaruh/kuasa stakeholder membolehkan Requirements Engineer mengurus jangkaan dan strategi komunikasi secara berkesan.\n• B (Availability): Betul. Ketersediaan masa stakeholder adalah faktor penentu kejayaan elisitasi; stakeholder yang berpengaruh tetapi tidak mempunyai masa akan melengahkan projek.",
    "whyWrong": "• C, D, E adalah data peribadi yang tidak relevan dengan perancangan aktiviti kejuruteraan keperluan.",
    "extra": "Handbook Bab 4.2 / Syllabus EO 4.2.2: Atribut Stakeholder Penting: Nama, Peranan, Tahap Pengaruh (Power), Tahap Minat (Interest), Ketersediaan (Availability), Saluran Komunikasi.",
    "mnemonic": "Matriks Stakeholder = Kuasa Pengaruh (Power) + Ketersediaan Masa (Availability)."
  },
  {
    "id": 32,
    "code": "P0314",
    "type": "P",
    "pts": 1,
    "eo": "4.3.4",
    "euNo": 4,
    "title": "Artifact-based Elicitation Techniques",
    "question": "Artifact-based elicitation techniques are an important category of elicitation techniques. Which two of the following techniques belong to this category? (2 answers)",
    "options": [
      { "id": "A", "text": "Document analysis", "truth": True },
      { "id": "B", "text": "Interview", "truth": False },
      { "id": "C", "text": "System archaeology", "truth": True },
      { "id": "D", "text": "Role playing", "truth": False },
      { "id": "E", "text": "Mind mapping", "truth": False }
    ],
    "correctDisplay": "A, C",
    "whyCorrect": "• A (Document analysis): Betul. Menganalisis dokumen bertulis sedia ada (manual, prosedur operasi standard, undang-undang).\n• C (System archaeology): Betul. Mengekstrak keperluan daripada sistem legasi atau kod sumber lama apabila dokumentasi tidak lagi wujud atau lapuk.",
    "whyWrong": "• B (Interview): Teknik berasaskan manusia (Human-based technique).\n• D (Role playing): Teknik kreativiti / simulasi.\n• E (Mind mapping): Teknik pemikiran / struktur idea.",
    "extra": "Handbook Bab 4.3 / Syllabus EO 4.3.4: Kategori Teknik Elisitasi: 1. Human-based (Interview, Questionnaire), 2. Workshop-based, 3. Observation-based (Shadowing, Apprenticeship), 4. Artifact-based (Document Analysis, System Archaeology, Reuse).",
    "mnemonic": "Artifact-based = Analisis Dokumen + Arkeologi Sistem Legasi."
  },
  {
    "id": 33,
    "code": "K0324",
    "type": "K",
    "pts": 2,
    "eo": "4.3.2",
    "euNo": 4,
    "title": "Elicitation Techniques Characteristics",
    "question": "Which of the following statements about elicitation techniques are true and which are false?",
    "options": [
      { "id": "A", "text": "Interviews are well suited to elicit explicit requirements from individual stakeholders.", "truth": True },
      { "id": "B", "text": "Questionnaires are suited to collect quantitative feedback from a large number of people.", "truth": True },
      { "id": "C", "text": "Workshops should only be used if all stakeholders have identical interests.", "truth": False },
      { "id": "D", "text": "Brainstorming is a suitable technique to elicit excitement factors.", "truth": True }
    ],
    "correctDisplay": "A=True, B=True, C=False, D=True",
    "whyCorrect": "• A: True. Temuduga bersemuka secara individu sangat efektif untuk memperincikan keperluan eksplisit dan pandangan peribadi stakeholder.\n• B: True. Soal selidik bertulis (Questionnaires) membolehkan pengumpulan data kuantitatif secara pantas daripada audiens yang ramai dan berselerak secara geografi.\n• D: True. Brainstorming membuka ruang idea luar kotak (out-of-the-box) untuk menghasilkan Excitement Factors (Model Kano).",
    "whyWrong": "• C: False. Bengkel (Workshops) sangat digalakkan terutamanya apabila stakeholders mempunyai kepentingan yang BERBEZA untuk mencari kata sepakat dan menyelesaikan konflik secara bersama.",
    "extra": "Handbook Bab 4.3 / Syllabus EO 4.3.2: Padanan Teknik Elisitasi mengikut objektif: Temuduga (Mendalam), Soal Selidik (Skala Besar), Bengkel (Konsensus), Brainstorming (Inovasi).",
    "mnemonic": "Temuduga = Mendalam. Survey = Ramai. Bengkel = Satukan Kepentingan Berbeza. Brainstorming = Inovasi."
  },
  {
    "id": 34,
    "code": "A0720",
    "type": "A",
    "pts": 1,
    "eo": "4.5.1",
    "euNo": 4,
    "title": "Requirements Validation Principles",
    "question": "Which of the following principles is NOT a guiding principle of requirements validation? (1 answer)",
    "options": [
      { "id": "A", "text": "Involvement of the correct stakeholders", "truth": False },
      { "id": "B", "text": "Separation of error detection and error correction", "truth": False },
      { "id": "C", "text": "Validation only at the end of the specification phase", "truth": True },
      { "id": "D", "text": "Repeated validation", "truth": False }
    ],
    "correctDisplay": "C (Validation only at the end of the specification phase)",
    "whyCorrect": "• Pilihan C adalah kenyataan yang SALAH (maka jawapan yang betul). Validasi keperluan mesti dijalankan seawal mungkin dan secara berterusan (early and continuous validation), bukan hanya menunggu sehingga fasa spesifikasi berakhir.",
    "whyWrong": "• A (Involvement of correct stakeholders): Prinsip asas validasi — semak dengan pemilik keperluan yang sah.\n• B (Separation of detection and correction): Asingkan aktiviti mencari ralat daripada membetulkannya agar sesi semakan tidak tergendala.\n• D (Repeated validation): Validasi secara berulang seiring dengan evolusi keperluan.",
    "extra": "Handbook Bab 4.5 / Syllabus EO 4.5.1: 5 Prinsip Asas Validasi Keperluan: 1. Involve correct stakeholders, 2. Separate detection and correction, 3. Multi-perspective validation, 4. Change the representation, 5. Validate early and repeatedly.",
    "mnemonic": "Validasi = Awal, Berulang, dan Libatkan Stakeholder Sebenar (Bukan tunggu hujung fasa)."
  },
  {
    "id": 35,
    "code": "A0721",
    "type": "A",
    "pts": 2,
    "eo": "4.5.2",
    "euNo": 4,
    "title": "Validation Techniques (High-Speed Train Braking System)",
    "question": "In your project, a new braking system for high speed trains is developed. Which validation technique is most suitable for this situation, where the requirements must be validated with high rigor? (1 answer)",
    "options": [
      { "id": "A", "text": "Walkthrough", "truth": False },
      { "id": "B", "text": "Inspection", "truth": True },
      { "id": "C", "text": "Informal peer review", "truth": False },
      { "id": "D", "text": "Desk checking", "truth": False }
    ],
    "correctDisplay": "B (Inspection)",
    "whyCorrect": "• Pilihan B adalah jawapan yang betul. Untuk sistem kritikal keselamatan (Safety-Critical System) seperti sistem brek kereta api laju, 'Inspection' adalah teknik semakan paling formal, teliti, dan berdisiplin tinggi (mengikut Fagan Inspection dengan peranan moderator, reader, inspector, dan metrik ralat ketat).",
    "whyWrong": "• A (Walkthrough): Teknik semakan separa formal yang diketuai oleh penulis dokumen (kurang ketat berbanding Inspection).\n• C (Informal peer review) & D (Desk checking): Semakan tidak formal tanpa prosedur standard, tidak mencukupi untuk standard keselamatan nyawa.",
    "extra": "Handbook Bab 4.5 / Syllabus EO 4.5.2: Spektrum Ketelitian Validasi: Desk Checking (Paling Rendah) ➔ Informal Review ➔ Walkthrough (Sederhana) ➔ Inspection (Paling Formal & Ketat).",
    "mnemonic": "Safety-Critical (Kereta Api / Perubatan / Nuklear) = Wajib Inspection (Formal Maksimum)."
  },

  # ================================================================================================
  # EU5: Process and Working Structure (Q36–Q37, 3 Pts)
  # ================================================================================================
  {
    "id": 36,
    "code": "P3504",
    "type": "P",
    "pts": 2,
    "eo": "5.1.1",
    "euNo": 5,
    "title": "Three Facets of the Requirements Engineering Process",
    "question": "Which two major facets below are the most important to consider when configuring a Requirements Engineering process? (2 answers)",
    "options": [
      { "id": "A", "text": "Time facet (linear vs. iterative)", "truth": True },
      { "id": "B", "text": "Budget facet (fixed price vs. time and material)", "truth": False },
      { "id": "C", "text": "Purpose facet (prescriptive vs. exploratory)", "truth": True },
      { "id": "D", "text": "Tool facet (open source vs. commercial)", "truth": False },
      { "id": "E", "text": "Team size facet (small team vs. large team)", "truth": False }
    ],
    "correctDisplay": "A, C",
    "whyCorrect": "• A (Time facet): Betul. Dimensi Masa mentakrifkan sama ada proses dijalankan secara Linear (Sekali lalu) atau Iterative / Agile (Berulang).\n• C (Purpose facet): Betul. Dimensi Tujuan mentakrifkan sama ada keperluan bersifat Prescriptive (Kontrak tetap yang wajib dipatuhi) atau Exploratory (Meneroka keperluan secara dinamik).",
    "whyWrong": "• B (Budget), D (Tool), E (Team size) adalah faktor pengurusan projek am, bukan 3 dimensi konfigurasi proses teras RE mengikut silibus IREB.",
    "extra": "Handbook Bab 5.1 / Syllabus EO 5.1.1: 3 Dimensi / Facets Konfigurasi Proses RE IREB:\n1. Time facet (Linear vs Iterative)\n2. Purpose facet (Prescriptive vs Exploratory)\n3. Target/Change facet (Customer-specific vs Market-driven / Product Line).",
    "mnemonic": "3 Facets Proses RE = Masa (Linear/Iterative) + Tujuan (Prescriptive/Exploratory) + Sasaran (Customer/Market)."
  },
  {
    "id": 37,
    "code": "A3505",
    "type": "A",
    "pts": 1,
    "eo": "5.2.1",
    "euNo": 5,
    "title": "Tailoring RE Process: Suitable Scenarios for Linear Process",
    "question": "Which of the following project situations is best suited for a linear Requirements Engineering process? (1 answer)",
    "options": [
      { "id": "A", "text": "Development of a software product in a highly dynamic market", "truth": False },
      { "id": "B", "text": "The requirements are stable and comprehensively known upfront", "truth": True },
      { "id": "C", "text": "The customer wants to see functional increments every two weeks", "truth": False },
      { "id": "D", "text": "A new innovative application with high uncertainty regarding user acceptance", "truth": False }
    ],
    "correctDisplay": "B (The requirements are stable and comprehensively known upfront)",
    "whyCorrect": "• Pilihan B adalah situasi paling sesuai untuk proses Linear (seperti Model Waterfall / V-Model). Apabila keperluan stabil, jelas, dan telah diketahui sepenuhnya di peringkat awal, perancangan linear menjimatkan kos dan mengurangkan pembaziran lelaran.",
    "whyWrong": "• A, C, dan D: Pasaran dinamik, maklum balas 2-mingguan, dan ketidaktentuan tinggi mewajibkan pendekatan Iterative / Agile (Exploratory RE).",
    "extra": "Handbook Bab 5.2 / Syllabus EO 5.2.1: Proses Linear sesuai untuk: Keperluan stabil, teknologi mantap, domain terkawal, kontrak tender tetap.",
    "mnemonic": "Linear = Keperluan Stabil & Jelas dari awal. Iterative = Dinamik & Ketidaktentuan Tinggi."
  },

  # ================================================================================================
  # EU6: Management Practices for Requirements (Q38–Q43, 10 Pts)
  # ================================================================================================
  {
    "id": 38,
    "code": "K0819",
    "type": "K",
    "pts": 2,
    "eo": "6.4.1",
    "euNo": 6,
    "title": "Views on Requirements",
    "question": "Which of the following statements about views on requirements are true and which are false?",
    "options": [
      { "id": "A", "text": "Views help to reduce the complexity of the requirements documentation for specific stakeholder groups.", "truth": True },
      { "id": "B", "text": "A view can only be created by hiding irrelevant requirements.", "truth": False },
      { "id": "C", "text": "A view can be defined by filtering requirements according to attribute values.", "truth": True },
      { "id": "D", "text": "Creating views requires all requirements to be specified in a formal language.", "truth": False }
    ],
    "correctDisplay": "A=True, B=False, C=True, D=False",
    "whyCorrect": "• A: True. Pandangan (Views) menyaring maklumat agar setiap kumpulan stakeholder hanya melihat aspek yang relevan dengan peranan mereka, sekaligus mengurangkan beban kerumitan.\n• C: True. Penapisan mengikut nilai atribut (cth: Status='Approved', Priority='High', Subsystem='Payment') adalah kaedah standard membina Views.",
    "whyWrong": "• B: False. Views bukan sahaja menyembunyikan maklumat (Selective View), tetapi juga boleh menggabungkan (Aggregate View) atau mengubah format persembahan data.\n• D: False. Keperluan dalam teks biasa dan atribut jadual sudah memadai untuk membina Views tanpa memerlukan bahasa formal.",
    "extra": "Handbook Bab 6.4 / Syllabus EO 6.4.1: Views on Requirements: Mengurangkan kompleksiti dan membolehkan pelbagai stakeholder fokus kepada keperluan masing-masing.",
    "mnemonic": "Views = Filter ikut Atribut ➔ Kurangkan Beban Stakeholder."
  },
  {
    "id": 39,
    "code": "A0820",
    "type": "A",
    "pts": 1,
    "eo": "6.3.1",
    "euNo": 6,
    "title": "Requirements Prioritization: MoSCoW Method",
    "question": "In the MoSCoW prioritization method, what does the letter 'C' stand for? (1 answer)",
    "options": [
      { "id": "A", "text": "Critical", "truth": False },
      { "id": "B", "text": "Could-have", "truth": True },
      { "id": "C", "text": "Cost-effective", "truth": False },
      { "id": "D", "text": "Customer-defined", "truth": False }
    ],
    "correctDisplay": "B (Could-have)",
    "whyCorrect": "• Pilihan B adalah jawapan yang betul. Akronim MoSCoW merujuk kepada:\n• M = Must-have (Wajib ada untuk keluaran asas)\n• S = Should-have (Penting tetapi ada jalan alternatif sementara)\n• C = Could-have (Ciri sampingan jika masa dan bajet mengizinkan)\n• W = Won't-have (Tidak akan dimasukkan dalam keluaran semasa, ditunda ke fasa hadapan).",
    "whyWrong": "• A (Critical), C (Cost-effective), dan D (Customer-defined) bukan perkataan dalam akronim standard MoSCoW.",
    "extra": "Handbook Bab 6.3 / Syllabus EO 6.3.1: Kaedah Keutamaan RE: MoSCoW, Kano, Wiegers Matrix (Cost-Value Tradeoff), Top Ten / Ranking.",
    "mnemonic": "MoSCoW = Must, Should, Could, Won't have."
  },
  {
    "id": 40,
    "code": "K0821",
    "type": "K",
    "pts": 2,
    "eo": "6.1.1",
    "euNo": 6,
    "title": "Requirements Attributes: Unique Identifier (ID)",
    "question": "Additional information on requirements is managed using attributes. An example of such additional information is a unique identifier.\nWhich of the following statements about unique identifiers for requirements are true and which are false?",
    "options": [
      { "id": "A", "text": "A unique identifier allows unambiguous referencing of a requirement.", "truth": True },
      { "id": "B", "text": "A unique identifier must never be changed once it has been assigned.", "truth": True },
      { "id": "C", "text": "When a requirement is deleted, its identifier should be immediately reassigned to a new requirement.", "truth": False },
      { "id": "D", "text": "A unique identifier is an indispensable prerequisite for establishing requirements traceability.", "truth": True }
    ],
    "correctDisplay": "A=True, B=True, C=False, D=True",
    "whyCorrect": "• A: True. Unique ID (cth: REQ-0101) membolehkan setiap keperluan dirujuk secara tepat dan tidak mengelirukan dalam dokumen, kod, dan ujian.\n• B: True. ID yang telah diberikan tidak boleh diubahsuai agar pautan rujukan sejarah dan kebolehkesanan tidak terputus.\n• D: True. Kebolehkesanan (Traceability) mustahil diwujudkan tanpa ID unik bagi setiap item keperluan.",
    "whyWrong": "• C: False. ID bagi keperluan yang dipadam TIDAK boleh diguna semula (reassigned) untuk mengelakkan kekeliruan sejarah projek.",
    "extra": "Handbook Bab 6.1 / Syllabus EO 6.1.1: Atribut Keperluan Standard: Identifier (Kekal & Unik), Version, Status, Author, Priority, Source, Stability, Risk.",
    "mnemonic": "ID Keperluan = Kekal Seumur Hidup Projek. Jangan Guna Semula ID yang Dipadam."
  },
  {
    "id": 41,
    "code": "P0838",
    "type": "P",
    "pts": 2,
    "eo": "6.5.1",
    "euNo": 6,
    "title": "Requirements Traceability Types",
    "question": "Traceability is a key management practice in Requirements Engineering. Which two of the following are recognized types of traceability according to IREB? (2 answers)",
    "options": [
      { "id": "A", "text": "Pre-RS traceability (traceability to requirements sources)", "truth": True },
      { "id": "B", "text": "Post-RS traceability (traceability to downstream work products)", "truth": True },
      { "id": "C", "text": "Cross-project traceability", "truth": False },
      { "id": "D", "text": "Dynamic runtime traceability", "truth": False },
      { "id": "E", "text": "Bi-directional syntax traceability", "truth": False }
    ],
    "correctDisplay": "A, B",
    "whyCorrect": "• A (Pre-RS traceability): Betul. Menjejaki keperluan ke belakang kepada sumber asalnya (Stakeholder desires, Dokumen undang-undang, Minit mesyuarat) — 'Mengapa keperluan ini wujud?'.\n• B (Post-RS traceability): Betul. Menjejaki keperluan ke hadapan kepada artifak hiliran (Architecture, Code modules, Test cases) — 'Bagaimana keperluan ini direalisasikan dan diuji?'.",
    "whyWrong": "• C, D, E bukan istilah piawai jenis kebolehkesanan dalam taksonomi IREB (3 jenis utama ialah Pre-RS, Post-RS, dan Inter-RS).",
    "extra": "Handbook Bab 6.5 / Syllabus EO 6.5.1: 3 Jenis Traceability IREB:\n1. Pre-RS Traceability (Keperluan ➔ Sumber Asal)\n2. Post-RS Traceability (Keperluan ➔ Senibina/Kod/Ujian)\n3. Inter-RS Traceability (Hubungan antara keperluan dengan keperluan lain).",
    "mnemonic": "Traceability = Pre-RS (Ke Sumber) + Post-RS (Ke Kod & Ujian) + Inter-RS (Antara Keperluan)."
  },
  {
    "id": 42,
    "code": "K0802",
    "type": "K",
    "pts": 2,
    "eo": "6.1.2",
    "euNo": 6,
    "title": "Requirements Attributes & Life Cycle Status",
    "question": "Attributes are used to manage additional characteristics of requirements. Priority is one example of such a requirements attribute.\nWhich of the following statements about requirements attributes are true and which are false?",
    "options": [
      { "id": "A", "text": "The set of attributes defined for requirements should be identical in all projects of a company.", "truth": False },
      { "id": "B", "text": "The lifecycle state of a requirement can be documented using an attribute.", "truth": True },
      { "id": "C", "text": "The author of a requirement is an example of a typical attribute.", "truth": True },
      { "id": "D", "text": "Only functional requirements can have attributes.", "truth": False }
    ],
    "correctDisplay": "A=False, B=True, C=True, D=False",
    "whyCorrect": "• B: True. Status kitaran hayat (cth: Draft, In Review, Approved, Rejected, Implemented, Verified) didokumenkan menggunakan atribut Status.\n• C: True. Atribut Author merekodkan individu yang bertanggungjawab mendokumenkan keperluan tersebut.",
    "whyWrong": "• A: False. Skema atribut mesti disesuaikan (tailored) mengikut skala, jenis, dan risiko projek khusus (bukan wajib sama secara rigid bagi semua projek).\n• D: False. Quality Requirements dan Constraints juga mempunyai atribut lengkap (ID, Prioriti, Status, Sumber).",
    "extra": "Handbook Bab 6.1 / Syllabus EO 6.1.2: Skema atribut memudahkan carian, penapisan (filtering), kawalan kualiti, dan metrik kemajuan projek.",
    "mnemonic": "Semua jenis keperluan ada atribut. Skema atribut boleh disesuaikan mengikut projek."
  },
  {
    "id": 43,
    "code": "A0804",
    "type": "A",
    "pts": 1,
    "eo": "6.2.1",
    "euNo": 6,
    "title": "Requirements Versioning & Baselines",
    "question": "What is a requirements baseline? (1 answer)",
    "options": [
      { "id": "A", "text": "The initial draft of the requirements specification", "truth": False },
      { "id": "B", "text": "A stable, released, and approved configuration of requirements work products at a specific point in time", "truth": True },
      { "id": "C", "text": "The minimum number of requirements needed to start development", "truth": False },
      { "id": "D", "text": "A backup copy of the requirements database", "truth": False }
    ],
    "correctDisplay": "B (A stable, released, and approved configuration of requirements work products at a specific point in time)",
    "whyCorrect": "• Pilihan B adalah definisi tepat mengikut IREB Glossary & Handbook. Baseline ialah konfigurasi stabil bagi satu set artifak keperluan yang telah disemak, dipersetujui, dan ditandatangani pada satu ketika masa tertentu, berfungsi sebagai asas rujukan rasmi untuk pembangunan seterusnya dan kawalan perubahan (Change Control).",
    "whyWrong": "• A (Initial draft): Draf awal belum stabil atau diluluskan.\n• C (Minimum number): Ini merujuk kepada konsep MVP (Minimum Viable Product).\n• D (Backup copy): Sandaran pangkalan data hanyalah salinan fail teknikal, bukan status kelulusan pengurusan.",
    "extra": "Handbook Bab 6.2 / Syllabus EO 6.2.1: Baseline membolehkan perbandingan versi (diffing), pengurusan skop keluaran (Release Planning), dan audit pematuhan.",
    "mnemonic": "Baseline = Konfigurasi Keperluan Stabil, Diluluskan, & Ditandatangani pada Satu Titik Masa."
  },

  # ================================================================================================
  # EU7: Tool Support (Q44–Q45, 3 Pts)
  # ================================================================================================
  {
    "id": 44,
    "code": "K0910",
    "type": "K",
    "pts": 2,
    "eo": "7.1.1",
    "euNo": 7,
    "title": "Tool Support in Requirements Engineering",
    "question": "As a Requirements Engineer for a company, you have to choose a tool to support the Requirements Engineering process in your organization.\nWhich of the following statements about tool support are true and which are false?",
    "options": [
      { "id": "A", "text": "The tool should support the established RE process of the organization rather than the other way around.", "truth": True },
      { "id": "B", "text": "Introducing a new RE tool requires training and change management effort.", "truth": True },
      { "id": "C", "text": "A single RE tool will always support all activities and notations of Requirements Engineering equally well.", "truth": False },
      { "id": "D", "text": "Total cost of ownership (TCO) of a tool includes maintenance, support, and training costs in addition to license costs.", "truth": True }
    ],
    "correctDisplay": "A=True, B=True, C=False, D=True",
    "whyCorrect": "• A: True. Prinsip asas pemilihan alatan: Alat mesti menyokong proses RE organisasi yang telah matang, bukan proses dipaksa mengikut kehendak alat.\n• B: True. Pengenalan alat baharu sentiasa memerlukan latihan kakitangan, migrasi data, dan pengurusan perubahan organisasi.\n• D: True. Kos TCO merangkumi lesen perisian, kos perkakasan/server, penyelenggaraan tahunan, sokongan teknikal, dan latihan pengguna.",
    "whyWrong": "• C: False. Tiada satu alat tunggal ('silver bullet') yang sempurna untuk semua aktiviti; organisasi lazimnya menggabungkan alat pengurusan keperluan (cth: Jira/Doors) bersama alat pemodelan visual (cth: Enterprise Architect).",
    "extra": "Handbook Bab 7.1 / Syllabus EO 7.1.1: Kategori Alatan RE: Management Tools, Modeling Tools, Collaboration Tools, Prototyping Tools, Validation Tools.",
    "mnemonic": "Alat sokong proses (bukan sebaliknya). Kira kos penuh TCO (bukan lesen sahaja)."
  },
  {
    "id": 45,
    "code": "A0922",
    "type": "A",
    "pts": 1,
    "eo": "7.2.1",
    "euNo": 7,
    "title": "Tool Selection and Introduction",
    "question": "When introducing a Requirements Engineering tool into an organization, which of the following is the most important success factor? (1 answer)",
    "options": [
      { "id": "A", "text": "Selecting the most expensive market leader tool", "truth": False },
      { "id": "B", "text": "Defining the requirements and evaluation criteria for the tool before purchasing", "truth": True },
      { "id": "C", "text": "Deploying the tool to all projects simultaneously without a pilot phase", "truth": False },
      { "id": "D", "text": "Mandating the tool without providing user training", "truth": False }
    ],
    "correctDisplay": "B (Defining the requirements and evaluation criteria for the tool before purchasing)",
    "whyCorrect": "• Pilihan B adalah faktor kejayaan paling penting. Organisasi mesti mengamalkan RE ke atas diri sendiri — iaitu mentakrifkan keperluan alat, kriteria penilaian, dan menjalankan perbandingan objektif sebelum membuat keputusan pembelian.",
    "whyWrong": "• A: Alat termahal tidak semestinya sesuai dengan proses organisasi.\n• C: Perlaksanaan serentak tanpa projek perintis (Pilot Project) membawa risiko kegagalan besar.\n• D: Mewajibkan penggunaan tanpa latihan akan menimbulkan tentangan stakeholder.",
    "extra": "Handbook Bab 7.2 / Syllabus EO 7.2.1: Langkah Pengenalan Alatan: 1. Nilai keperluan alat, 2. Uji cuba (Pilot project), 3. Latihan berstruktur, 4. Penambahbaikan berterusan.",
    "mnemonic": "Beli alat RE guna prinsip RE: Tulis keperluan alat dulu ➔ Buat projek pilot ➔ Latih pengguna."
  }
]

app_data = {
  "eus": eus,
  "questions": questions
}

with open(DATA_PATH, 'w', encoding='utf-8') as f:
    json.dump(app_data, f, indent=2, ensure_ascii=False)

print(f"Generated authentic dataset successfully! Saved to {DATA_PATH}")
print(f"Total questions: {len(questions)}")
print(f"Total points: {sum(q['pts'] for q in questions)}")
