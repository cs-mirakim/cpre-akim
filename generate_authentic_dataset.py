import json
import base64
import os

# Helper for diagrams
def get_b64(path):
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"
    return ""

img_q18 = get_b64('diagram_q_page_12_1.png')
img_q20 = get_b64('diagram_q_page_13_1.png')
img_q21 = get_b64('diagram_q_page_14_1.png')
img_q23 = get_b64('diagram_q_page_16_1.png')

eus = [
  { "no": 1, "name": "Introduction & Overview to Requirements Engineering", "range": "Q1–Q3", "pts": 5 },
  { "no": 2, "name": "Fundamental Principles of Requirements Engineering", "range": "Q4–Q7", "pts": 6 },
  { "no": 3, "name": "Work Products & Documentation Practices", "range": "Q8–Q25", "pts": 27 },
  { "no": 4, "name": "Practices for Requirements Elaboration", "range": "Q26–Q35", "pts": 13 },
  { "no": 5, "name": "Process & Working Structure", "range": "Q35–Q37", "pts": 3 },
  { "no": 6, "name": "Management Practices for Requirements", "range": "Q38–Q43", "pts": 9 },
  { "no": 7, "name": "Tool Support", "range": "Q44–Q45", "pts": 3 }
]

# Educational Units Table of Contents
# Total: 45 Questions, 63 Points

questions = [
  # ------------------------------------------------------------------------------------------------
  # EU1: Introduction and Overview of Requirements Engineering (Q1–Q3, 5 Pts)
  # ------------------------------------------------------------------------------------------------
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
    "whyCorrect": "• B: Betul (True). Quality requirements melengkapi functional requirements dengan menetapkan tahap kualiti (cth: prestasi, kebolehgunaan, keselamatan) yang perlu dicapai oleh fungsi tersebut.\n• D: Betul (True). Quality requirements boleh diperincikan (substantiated) menjadi functional requirements tambahan (contoh: keperluan keselamatan 'sistem mesti dilindungi' diperincikan kepada fungsi 'sistem mesti menyediakan log masuk 2-faktor').",
    "whyWrong": "• A: Salah (False). Quality requirements merujuk kepada kualiti PRODUK (sistem), bukan proses penghasilan perisian (keperluan proses dirujuk sebagai Project/Process Requirements).\n• C: Salah (False). Quality requirements TIDAK semestinya diperolehi selepas fungsi; ia boleh dan lazimnya diperolehi secara serentak (intertwined) semasa elisitasi.",
    "extra": "Handbook Bab 1.1 / Syllabus EO 1.1.1: Tiga jenis keperluan utama mengikut IREB ialah Functional Requirements, Quality Requirements, dan Constraints.",
    "mnemonic": "Quality = Sifat Produk (bukan Proses). Boleh lahirkan fungsi baharu (Substantiated)."
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
    "whyCorrect": "• Pilihan B adalah jawapan yang betul (bukan tugas teras). Mengikut silibus IREB FL, empat aktiviti teras Requirements Engineer ialah: 1. Elicitation, 2. Documentation, 3. Validation & Negotiation, dan 4. Management. 'Formalizing' (membuat spesifikasi matematik formal) bukan aktiviti teras am.",
    "whyWrong": "• A (Eliciting), C (Documenting), dan D (Validating) kesemuanya merupakan tugas teras fundamental seorang Requirements Engineer.",
    "extra": "Handbook Bab 1.4 / Syllabus EO 1.4.1: Core tasks: Eliciting, Documenting, Validating/Negotiating, Managing.",
    "mnemonic": "4 Teras RE = E-D-V-M (Elicit, Document, Validate, Manage)."
  },
  {
    "id": 3,
    "code": "P0113",
    "type": "P",
    "pts": 1,
    "eo": "1.1.2",
    "euNo": 1,
    "title": "Functional Requirements Identification",
    "question": "Amongst other things, the customer demands the following from the contractor responsible for delivering an information system:\n\nA) The contractor shall process a change request within five days.\nB) The test reports from the integration test must be disclosed for examination and the test report from the system test must be handed over.\nC) At any time, the system shall enable a throughput of 100 transactions per second.\nD) The Subversion tool must be used for configuration management.\nE) Under normal load, the response time must be not more than two seconds.\n\nWhich two of the above demands are functional requirements? (2 answers)",
    "options": [
      { "id": "A", "text": "The contractor shall process a change request within five days.", "truth": False },
      { "id": "B", "text": "The test reports from the integration test must be disclosed for examination and the test report from the system test must be handed over.", "truth": False },
      { "id": "C", "text": "At any time, the system shall enable a throughput of 100 transactions per second.", "truth": True },
      { "id": "D", "text": "The Subversion tool must be used for configuration management.", "truth": False },
      { "id": "E", "text": "Under normal load, the response time must be not more than two seconds.", "truth": True }
    ],
    "correctDisplay": "C, E",
    "whyCorrect": "• Pilihan C & E: Di dalam skema soalan IREB, pernyataan pemprosesan transaksi (Throughput 100 txn/s) dan keupayaan memberikan masa respons (Response time <= 2s) dihuraikan secara langsung sebagai keupayaan tingkah laku operasi sistem (operational functional capability).",
    "whyWrong": "• A & B: Merupakan keperluan proses/projek pengurusan kontrak (Contractual/Process Requirements), bukan keperluan sistem.\n• D: Merupakan kekangan teknologi/alat (Constraint/Tool mandate).",
    "extra": "Handbook Bab 1.1 / Syllabus EO 1.1.2: Membezakan System Requirements vs Process Requirements vs Constraints.",
    "mnemonic": "Proses kontraktor (A, B) & Alat (D) = Bukan fungsi sistem. Keupayaan operasi sistem (C, E) = Functional."
  },

  # ------------------------------------------------------------------------------------------------
  # EU2: Fundamental Principles of Requirements Engineering (Q4–Q7, 6 Pts)
  # ------------------------------------------------------------------------------------------------
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
    "whyCorrect": "• Pilihan C adalah betul (bukan prinsip asas RE). 'Regular retrospectives' adalah amalan Agile/Scrum, bukannya 9 Prinsip Asas RE yang digariskan oleh IREB.",
    "whyWrong": "• 9 Prinsip Asas IREB ialah: 1. Value orientation, 2. Stakeholders, 3. Shared understanding, 4. Context, 5. Problem-requirement-solution, 6. Validation, 7. Diversity of work products, 8. Continuous innovation, 9. Systematic and disciplined work.",
    "extra": "Handbook Bab 2.1 / Syllabus EO 2.1.1: Sembilan Prinsip Asas IREB CPRE FL.",
    "mnemonic": "Retrospectives = Amalan Scrum/Agile, bukan 9 Prinsip Asas RE IREB."
  },
  {
    "id": 5,
    "code": "K3206",
    "type": "K",
    "pts": 2,
    "eo": "2.2.1",
    "euNo": 2,
    "title": "Shared Understanding Principle",
    "question": "Shared understanding is a principle of Requirements Engineering. For each of the following statements about shared understanding decide, whether it is true or false.",
    "options": [
      { "id": "A", "text": "Explicitly documented knowledge is only a means to achieve the actual goals of Requirements Engineering.", "truth": True },
      { "id": "B", "text": "The greater the shared understanding between the stakeholders, the less explicit requirements documentation is necessary.", "truth": True },
      { "id": "C", "text": "The shared understanding can be increased by creating a glossary.", "truth": True },
      { "id": "D", "text": "Shared understanding can be increased by using analogies and metaphors.", "truth": True }
    ],
    "correctDisplay": "A=True, B=True, C=True, D=True",
    "whyCorrect": "• A: Betul (True). Dokumentasi eksplisit adalah alat/cara untuk mencapai kefahaman bersama dan membina sistem yang bernilai, bukan matlamat akhir semata-mata.\n• B: Betul (True). Semakin tinggi kefahaman tersirat (shared implicit understanding), semakin sedikit perincian dokumen yang diperlukan.\n• C: Betul (True). Glosari menyelaraskan takrifan istilah dan mengelakkan kekeliruan makna.\n• D: Betul (True). Analogi dan metafora membantu pemegang taruh memahami domain baharu dengan membandingkannya dengan domain yang sedia difahami.",
    "whyWrong": "Semua kenyataan A, B, C, D adalah TEPAT dan selaras dengan prinsip Shared Understanding IREB (Keempat-empatnya bernilai True).",
    "extra": "Handbook Bab 2.2 / Syllabus EO 2.2.1: Shared Understanding (Explicit vs Implicit Knowledge, Enablers, Obstacles).",
    "mnemonic": "Shared Understanding = Semua (A, B, C, D) adalah TRUE."
  },
  {
    "id": 6,
    "code": "K0202",
    "type": "K",
    "pts": 2,
    "eo": "2.2.2",
    "euNo": 2,
    "title": "Delimiting System & Context",
    "question": "Which of the following aspects need to be considered when delimiting the system and its context, and which do not need to be considered?",
    "options": [
      { "id": "A", "text": "The system", "truth": "Needs to be considered" },
      { "id": "B", "text": "The system context", "truth": "Needs to be considered" },
      { "id": "C", "text": "The application domain", "truth": "Needs to be considered" },
      { "id": "D", "text": "The interfaces between system and system context", "truth": "Needs to be considered" }
    ],
    "correctDisplay": "A=Needs to be considered, B=Needs to be considered, C=Needs to be considered, D=Needs to be considered",
    "whyCorrect": "• A, B, C, D: Keempat-empat aspek (Sistem, Konteks Sistem, Domain Aplikasi, dan Antara Muka Antara Sistem & Konteks) WAJIB dipertimbangkan dalam penetapan sempadan sistem dan konteks.",
    "whyWrong": "Tiada satu pun aspek di atas yang boleh diabaikan dalam analisis sempadan konteks RE.",
    "extra": "Handbook Bab 2.3 / Syllabus EO 2.2.2: System boundary, Context boundary, Grey zone, and Interfaces.",
    "mnemonic": "System + Context + Domain + Interfaces = SEMUA Wajib Dipertimbangkan (Needs to be considered)."
  },
  {
    "id": 7,
    "code": "A0207",
    "type": "A",
    "pts": 1,
    "eo": "2.2.2",
    "euNo": 2,
    "title": "Context Boundary vs Anonymization",
    "question": "In a project for passenger transportation, a software system is to be developed. An external entity provides the passenger data with names and addresses. However, it is determined that in the future, due to data protection, this data must be anonymized before it is provided to the system. Which boundary is influenced by this decision? (1 answer)",
    "options": [
      { "id": "A", "text": "System boundary", "truth": False },
      { "id": "B", "text": "Context boundary", "truth": True },
      { "id": "C", "text": "Grey zone of the system boundary", "truth": False },
      { "id": "D", "text": "Grey zone of the context boundary", "truth": False }
    ],
    "correctDisplay": "B (Context boundary)",
    "whyCorrect": "• Pilihan B adalah betul. Keputusan sama ada data penumpang luar dianonymize sebelum masuk atau di mana data tersebut wujud dalam persekitaran menentukan apa yang relevan di luar sistem, iaitu mengubah Sempadan Konteks (Context Boundary).",
    "whyWrong": "• System boundary (A) memisahkan apa yang dibina dalam sistem vs di luar sistem. Perubahan sumber data luar adalah di peringkat context boundary.",
    "extra": "Handbook Bab 2.3 / Syllabus EO 2.2.2: Context boundary memisahkan konteks yang relevan daripada persekitaran yang tidak relevan (irrelevant environment).",
    "mnemonic": "Perubahan sumber/entiti luar = Context Boundary."
  },

  # ------------------------------------------------------------------------------------------------
  # EU3: Work Products and Documentation Practices (Q8–Q25, 27 Pts)
  # ------------------------------------------------------------------------------------------------
  {
    "id": 8,
    "code": "A3310",
    "type": "A",
    "pts": 1,
    "eo": "3.1.1",
    "euNo": 3,
    "title": "Requirements Work Products",
    "question": "Which of the following statements about requirements work products is FALSE? (1 answer)",
    "options": [
      { "id": "A", "text": "Requirements work products can be documented textually or using models.", "truth": False },
      { "id": "B", "text": "Requirements work products can be item-oriented or document-oriented.", "truth": False },
      { "id": "C", "text": "User stories and use case specifications are examples of requirements work products.", "truth": False },
      { "id": "D", "text": "Only finalized and approved documents are considered requirements work products.", "truth": True }
    ],
    "correctDisplay": "D (Only finalized and approved documents...)",
    "whyCorrect": "• Pilihan D adalah FALSE (kenyataan yang salah, maka jawapan betul bagi soalan). Mengikut takrifan IREB, sebarang hasil kerja (draf, model separa siap, kad user story) adalah work product, bukan dokumen akhir yang diluluskan sahaja.",
    "whyWrong": "• A, B, C semuanya adalah kenyataan yang BENAR mengenai takrifan dan kepelbagaian work products mengikut silibus IREB.",
    "extra": "Handbook Bab 3.1 / Syllabus EO 3.1.1: Work product = Any recorded intermediate or final result of work.",
    "mnemonic": "Work Product = Termasuk draf & hasil kerja perantaraan (Bukan hanya dokumen akhir)."
  },
  {
    "id": 9,
    "code": "A3311",
    "type": "A",
    "pts": 1,
    "eo": "3.4.6",
    "euNo": 3,
    "title": "Class Diagram Modeling Limitations",
    "question": "Which of the following CANNOT be modeled with a class diagram? (1 answer)",
    "options": [
      { "id": "A", "text": "Objects and their relationships", "truth": False },
      { "id": "B", "text": "States and state transitions", "truth": True },
      { "id": "C", "text": "Multiplicities", "truth": False },
      { "id": "D", "text": "Generalizations and specializations", "truth": False }
    ],
    "correctDisplay": "B (States and state transitions)",
    "whyCorrect": "• Pilihan B adalah betul. Keadaan dan peralihan keadaan (States and state transitions) dimodelkan menggunakan State Diagram / State Machine (Perspektif Tingkah Laku / Behavior), BUKAN Class Diagram (Perspektif Struktur).",
    "whyWrong": "• A (Objek & hubungan), C (Multiplicities 1..*), dan D (Generalizations) kesemuanya boleh dimodelkan dalam Class Diagram.",
    "extra": "Handbook Bab 3.4 / Syllabus EO 3.4.6: Structure perspective = Class diagram; Behavior perspective = State diagram.",
    "mnemonic": "Class Diagram = Struktur. State Transition = State Diagram (Behavior)."
  },
  {
    "id": 10,
    "code": "P0416",
    "type": "P",
    "pts": 2,
    "eo": "3.8.2",
    "euNo": 3,
    "title": "Quality Criteria for Requirements by Role",
    "question": "You want to design a requirements document in such a way that it is particularly well suited for the people who will work with the document in further phases of the development process.\nFrom the following sentences, choose the two best combinations of the role and its criteria for the requirements. (2 answers)",
    "options": [
      { "id": "A", "text": "For the software architect, the requirements have to be unambiguous.", "truth": False },
      { "id": "B", "text": "For the tester, the requirements have to be modifiable.", "truth": False },
      { "id": "C", "text": "For all people involved, the requirements in a work product have to be consistent.", "truth": True },
      { "id": "D", "text": "For the project manager, the requirements have to be necessary.", "truth": True },
      { "id": "E", "text": "For the developer, the requirements have to be prioritizeable.", "truth": False }
    ],
    "correctDisplay": "C, D",
    "whyCorrect": "• C: Bagi SEMUA pihak yang terlibat, keperluan mestilah konsisten (Consistency). Tanpa konsistensi, tiada pembangunan yang betul dapat dilakukan.\n• D: Bagi Pengurus Projek (Project Manager), keperluan mestilah perlu (Necessary) untuk mengelakkan pembaziran kos, skop yang membengkak (scope creep), dan perancangan jadual.",
    "whyWrong": "• A, B, E: Bukan kombinasi peranan utama yang paling spesifik mengikut skema pemarkahan kualiti IREB.",
    "extra": "Handbook Bab 3.8 / Syllabus EO 3.8.2: Quality criteria for single requirements and sets of requirements.",
    "mnemonic": "Konsisten untuk SEMUA (C), Necessary untuk Pengurus Projek (D)."
  },
  {
    "id": 11,
    "code": "P0417",
    "type": "P",
    "pts": 2,
    "eo": "3.1.2",
    "euNo": 3,
    "title": "Selection of Appropriate Notations",
    "question": "You are a Requirements Engineer in a project where requirements are documented mainly textually. However, due to communication issues between stakeholders from business and IT, you want to introduce additional forms of documentation to improve shared understanding.\nWhich two of the following approaches are best suited for this situation? (2 answers)",
    "options": [
      { "id": "A", "text": "Formulating requirements using mathematical logic formulas.", "truth": False },
      { "id": "B", "text": "Establishing a glossary.", "truth": True },
      { "id": "C", "text": "Translating all requirements into pseudocode.", "truth": False },
      { "id": "D", "text": "Creating a use case diagram and specifying the use cases.", "truth": True },
      { "id": "E", "text": "Documenting all requirements as source code comments.", "truth": False }
    ],
    "correctDisplay": "B, D",
    "whyCorrect": "• B: Membina Glosari (Glossary) menyelesaikan masalah percanggahan istilah antara Business dan IT.\n• D: Membina Use Case Diagram dan spesifikasi Use Case memberikan gambaran visual interaksi pengguna-sistem yang mudah difahami oleh kedua-dua pihak.",
    "whyWrong": "• A, C, E: Formula matematik, pseudocode, dan komen kod sumber adalah terlalu teknikal dan akan memburukkan lagi jurang komunikasi dengan pemegang taruh bisnes.",
    "extra": "Handbook Bab 3.1 & 3.4 / Syllabus EO 3.1.2: Pemilihan notasi dan penjajaran pemahaman.",
    "mnemonic": "Jambatan Business-IT = Glosari (B) + Use Case (D)."
  },
  {
    "id": 12,
    "code": "K0418",
    "type": "K",
    "pts": 2,
    "eo": "3.1.2",
    "euNo": 3,
    "title": "Notations for Functional Requirements",
    "question": "Which of the following statements on the choice of notations for the documentation of functional requirements apply and which do not apply?",
    "options": [
      { "id": "A", "text": "Stakeholders should be able to read the notation used for a work product.", "truth": "Applies" },
      { "id": "B", "text": "Diagrams have to be applied in projects with object-oriented development.", "truth": "Does not apply" },
      { "id": "C", "text": "The notation must be tailored to the specific type of requirement.", "truth": "Applies" },
      { "id": "D", "text": "Graphical notations are well suited for describing system structures.", "truth": "Applies" }
    ],
    "correctDisplay": "A=Applies, B=Does not apply, C=Applies, D=Applies",
    "whyCorrect": "• A: Applies. Pemegang taruh mesti boleh membaca notasi yang digunakan.\n• C: Applies. Notasi perlu disesuaikan mengikut jenis keperluan (struktur, fungsi, atau tingkah laku).\n• D: Applies. Notasi grafik (cth: class diagram) sangat sesuai untuk menggambarkan struktur sistem.",
    "whyWrong": "• B: Does not apply. Tiada kewajipan mutlak bahawa rajah 'mesti' digunakan semata-mata kerana projek menggunakan pembangunan berorientasikan objek (textual requirements pun masih boleh digunakan).",
    "extra": "Handbook Bab 3.1 / Syllabus EO 3.1.2: Kriteria pemilihan bentuk dokumentasi.",
    "mnemonic": "Semua 'Applies' KECUALI kewajipan mandatori rajah OO (B)."
  },
  {
    "id": 13,
    "code": "K3423",
    "type": "K",
    "pts": 2,
    "eo": "3.8.2",
    "euNo": 3,
    "title": "Quality Criteria for Sets of Requirements",
    "question": "Which of the following statements on quality criteria for sets of requirements are true and which are false?",
    "options": [
      { "id": "A", "text": "A set of requirements is non-redundant if every requirement is documented only once and does not overlap with others.", "truth": True },
      { "id": "B", "text": "Two requirements can be contradictory even if both of them are non-redundant.", "truth": True },
      { "id": "C", "text": "A set of requirements is consistent if no requirement contradicts with other requirements.", "truth": True },
      { "id": "D", "text": "A requirements specification is conformant if it contains all relevant use cases for the final product.", "truth": False }
    ],
    "correctDisplay": "A=True, B=True, C=True, D=False",
    "whyCorrect": "• A: True. Non-redundancy bermaksud tiada pertindihan atau penduaan.\n• B: True. Dua keperluan yang unik/tidak bertindih masih boleh bercanggah antara satu sama lain (contoh: Keperluan 1 kata 'butang warna biru', Keperluan 2 kata 'butang warna merah').\n• C: True. Konsistensi bermaksud tiada percanggahan dalam set keperluan.",
    "whyWrong": "• D: False. Mengandungi semua use case adalah kriteria 'Completeness' (Kerapian/Kelengkapan), BUKAN 'Conformance' (Pematuhan piawaian format/struktur).",
    "extra": "Handbook Bab 3.8 / Syllabus EO 3.8.2: Conformance vs Completeness vs Consistency vs Non-redundancy.",
    "mnemonic": "Conformant = Patuh Piawai Struktur. Mengandungi semua = Complete (Maka D adalah False)."
  },
  {
    "id": 14,
    "code": "P0510",
    "type": "P",
    "pts": 2,
    "eo": "3.3.1",
    "euNo": 3,
    "title": "Benefits of Phrase Templates",
    "question": "A phrase template can be used to document natural-language requirements. You want to introduce such a template in your project and have to convince your project manager of the benefits.\nWhich are the two best arguments? (2 answers)",
    "options": [
      { "id": "A", "text": "Phrase templates help to document well-structured requirements by providing a predefined syntactic structure.", "truth": True },
      { "id": "B", "text": "Requirements written using phrase templates contain no ambiguities.", "truth": False },
      { "id": "C", "text": "Learning how to write requirements in accordance with a phrase template does not require much time.", "truth": True },
      { "id": "D", "text": "Requirements written using phrase templates do not require any review.", "truth": False },
      { "id": "E", "text": "Phrase templates guarantee the completeness of the requirements specification.", "truth": False }
    ],
    "correctDisplay": "A, C",
    "whyCorrect": "• A: Template ayat menyediakan struktur sintaksis tetap (cth: 'The system shall...'), memudahkan penulisan yang teratur.\n• C: Mudah dipelajari dan tidak memerlukan masa latihan yang panjang bagi jurutera keperluan.",
    "whyWrong": "• B, D, E: Template ayat TIDAK menjamin sifar kekaburan (B), TIDAK menghapuskan keperluan review (D), dan TIDAK menjamin kelengkapan spesifikasi (E).",
    "extra": "Handbook Bab 3.3 / Syllabus EO 3.3.1: Phrase templates (SOPHIS, Rupp template).",
    "mnemonic": "Template = Struktur Mantap (A) + Cepat Belajar (C). Tiada jaminan magik (B, D, E salah)."
  },
  {
    "id": 15,
    "code": "A0508",
    "type": "A",
    "pts": 1,
    "eo": "3.2.1",
    "euNo": 3,
    "title": "Natural Language Defects Analysis",
    "question": "You receive the following requirement for a system to be developed: \"The system shall always display all available items in the warehouse.\"\nWhich defect of natural language is present in this requirement? (1 answer)",
    "options": [
      { "id": "A", "text": "Nominalization", "truth": False },
      { "id": "B", "text": "Universal quantifiers have been used.", "truth": True },
      { "id": "C", "text": "Passive voice without an agent", "truth": False },
      { "id": "D", "text": "Incompletely specified process verb", "truth": False }
    ],
    "correctDisplay": "B (Universal quantifiers have been used)",
    "whyCorrect": "• Pilihan B adalah betul. Perkataan 'always' dan 'all' merupakan penentu sejagat (Universal Quantifiers) yang mengitlakkan keadaan tanpa mengambil kira kekecualian (contoh: apa berlaku jika terdapat 100,000 item atau sambungan terputus).",
    "whyWrong": "• A (Nominalization): Tiada kata kerja bertukar kata nama.\n• C (Passive voice): Ayat menggunakan bentuk aktif 'The system shall display'.\n• D: Kata kerja 'display' mempunyai objek jelas.",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.1: 5 Kecacatan Bahasa Asli (Nominalization, Incomplete Conditions, Universal Quantifiers, Passive Voice, Incomplete Process Verbs).",
    "mnemonic": "Always + All = Universal Quantifiers (Kecacatan Bahasa)."
  },
  {
    "id": 16,
    "code": "K3520",
    "type": "K",
    "pts": 2,
    "eo": "3.3.1",
    "euNo": 3,
    "title": "Template-Based Work Products",
    "question": "Which of the following statements are true and which are false when working with template-based work products?",
    "options": [
      { "id": "A", "text": "Templates provide a blueprint for structuring single requirements, as well as whole specifications.", "truth": True },
      { "id": "B", "text": "Template-based work products for single requirements can help to prevent incomplete formulation of requirements in natural language.", "truth": True },
      { "id": "C", "text": "Writing requirements with templates is always faster than writing freely formulated requirements.", "truth": False },
      { "id": "D", "text": "Templates are obligatory for all authors of a requirements specification.", "truth": False }
    ],
    "correctDisplay": "A=True, B=True, C=False, D=False",
    "whyCorrect": "• A: True. Template berfungsi sebagai pelan struktur bagi keperluan tunggal (cth: phrase template) mahupun keseluruhan dokumen (cth: Volere/IEEE template).\n• B: True. Template membantu mengelakkan peninggalan maklumat penting (cth: syarat kekangan).",
    "whyWrong": "• C: False. Penulisan menggunakan template pada awalnya mungkin mengambil masa lebih lama kerana perlu mematuhi kekangan struktur.\n• D: False. Penggunaan template adalah disyorkan (recommended best practice) tetapi bukan kewajipan mandatori mutlak dalam semua situasi.",
    "extra": "Handbook Bab 3.3 / Syllabus EO 3.3.1: Document templates and phrase templates.",
    "mnemonic": "Template = Blueprint & Cegah Incomplete (A, B = True). Bukan 'always faster' atau 'obligatory' (C, D = False)."
  },
  {
    "id": 17,
    "code": "A3521",
    "type": "A",
    "pts": 1,
    "eo": "3.4.5",
    "euNo": 3,
    "title": "Behavior Perspective Modeling",
    "question": "You want to model the behavior of a user interface for entering personal data. The system behavior depends on the current state of data validation and user input.\nWhich of the following diagrams is best suited to model this behavior? (1 answer)",
    "options": [
      { "id": "A", "text": "State diagram", "truth": True },
      { "id": "B", "text": "Class diagram", "truth": False },
      { "id": "C", "text": "Entity-Relationship diagram (ERD)", "truth": False },
      { "id": "D", "text": "Data Flow diagram (DFD)", "truth": False }
    ],
    "correctDisplay": "A (State diagram)",
    "whyCorrect": "• Pilihan A adalah betul. Tingkah laku yang bergantung kepada keadaan semasa dan input luaran (State-dependent behavior) dimodelkan secara tepat menggunakan State Diagram / State Machine.",
    "whyWrong": "• B & C (Class diagram & ERD): Memodelkan perspektif struktur data.\n• D (DFD): Memodelkan perspektif fungsi dan aliran data.",
    "extra": "Handbook Bab 3.4 / Syllabus EO 3.4.5: Behavior perspective = State machines / State diagrams.",
    "mnemonic": "State-dependent behavior = State Diagram."
  },
  {
    "id": 18,
    "code": "K0619",
    "type": "K",
    "pts": 2,
    "eo": "3.4.6",
    "euNo": 3,
    "title": "Class Diagram Constraints & Multiplicities",
    "question": "To support young actors and directors, a contest for short films is held. The three best films will be presented with an award. The films submitted must have a maximum length of 20 minutes and must take the constraints depicted in the following diagram into consideration.\n\nDo the following statements match the diagram?",
    "diagramHtml": f"<img src='{img_q18}' alt='Diagram Q18' />",
    "options": [
      { "id": "A", "text": "Three directors may direct a film collaboratively.", "truth": "Does not match" },
      { "id": "B", "text": "A film with only one actor may be submitted.", "truth": "Matches" },
      { "id": "C", "text": "A director may direct two films submitted.", "truth": "Matches" },
      { "id": "D", "text": "An actor may star in any number of films.", "truth": "Matches" },
      { "id": "E", "text": "A film must have ten actors starring in it.", "truth": "Does not match" }
    ],
    "correctDisplay": "A=Does not match, B=Matches, C=Matches, D=Matches, E=Does not match",
    "whyCorrect": "• B: Matches. Multiplicity pada Actor ialah 1..* (sekurang-kurangnya 1 pelakon, jadi 1 pelakon sah).\n• C: Matches. Multiplicity Film ke Director ialah 1..* (Director boleh arah 1 atau lebih filem).\n• D: Matches. Actor ke Film ialah 1..* (Pelakon boleh berlakon dalam mana-mana bilangan filem).",
    "whyWrong": "• A: Does not match. Multiplicity Director pada Film ialah 1..2 (maksimum 2 pengarah sahaja dibenarkan, bukan 3).\n• E: Does not match. Tiada syarat wajib 10 pelakon (syaratnya 1..*).",
    "extra": "Handbook Bab 3.4 / Syllabus EO 3.4.6: Reading UML Class Diagram multiplicities (min..max).",
    "mnemonic": "Director: 1..2 (A salah). Actor: 1..* (B, C, D betul, E salah)."
  },
  {
    "id": 19,
    "code": "A0620",
    "type": "A",
    "pts": 1,
    "eo": "3.4.4",
    "euNo": 3,
    "title": "Activity Diagram Application",
    "question": "What is primarily modeled in a UML Activity Diagram? (1 answer)",
    "options": [
      { "id": "A", "text": "The process steps of an application", "truth": True },
      { "id": "B", "text": "The static structure of classes", "truth": False },
      { "id": "C", "text": "The state changes of an entity over time", "truth": False },
      { "id": "D", "text": "The data schema of database tables", "truth": False }
    ],
    "correctDisplay": "A (The process steps of an application)",
    "whyCorrect": "• Pilihan A adalah betul. Activity diagram digunakan untuk memodelkan aliran aktiviti, langkah proses, dan logik kawalan (Functional Perspective).",
    "whyWrong": "• B & D: Struktur kelas & skema data dimodelkan dengan Class diagram / ERD.\n• C: Perubahan keadaan entiti dimodelkan dengan State diagram.",
    "extra": "Handbook Bab 3.4 / Syllabus EO 3.4.4: Functional perspective = Activity diagrams & Data Flow diagrams.",
    "mnemonic": "Activity Diagram = Aliran Langkah Proses (Process Steps)."
  },
  {
    "id": 20,
    "code": "K3605",
    "type": "K",
    "pts": 2,
    "eo": "3.4.5",
    "euNo": 3,
    "title": "State Diagram User Authorization",
    "question": "A company wants to introduce an authorization process for accessing confidential parts of the company's intranet by issuing time-limited passwords. For that reason a state diagram is modeled to express the possible states and state transitions for a user.\n\nDetermine which of the following requirements match the state diagram and which do not match.",
    "diagramHtml": f"<img src='{img_q20}' alt='Diagram Q20' />",
    "options": [
      { "id": "A", "text": "Users in state blocked can be unblocked by resetting the user's password.", "truth": "Does not match" },
      { "id": "B", "text": "If password abuse for a user in state entitled has been noticed, the user's password is deleted and the user is set to state blocked.", "truth": "Matches" },
      { "id": "C", "text": "If password abuse for a user in state entitled has been noticed, the user's password is deleted and the user is set to state not entitled.", "truth": "Matches" },
      { "id": "D", "text": "If an application request is approved, the user gets an approval mail.", "truth": "Does not match" }
    ],
    "correctDisplay": "A=Does not match, B=Matches, C=Matches, D=Does not match",
    "whyCorrect": "• B & C: Matches. Rajah menunjukkan transisi tindakan bagi penyalahgunaan kata laluan (abuse detected) yang membawa kepada pemadaman kata laluan dan penetapan keadaan yang sepadan mengikut penjaga transisi (guard conditions).",
    "whyWrong": "• A: Does not match. Keadaan 'blocked' tidak mempunyai transisi terus reset kata laluan seperti yang dinyatakan.\n• D: Does not match. Tindakan pada transisi kelulusan menyatakan penghasilan kata laluan sementara, bukan penghantaran emel kelulusan semata-mata.",
    "extra": "Handbook Bab 3.4 / Syllabus EO 3.4.5: State machine modeling (states, events, guards, actions).",
    "mnemonic": "Semak anak panah transisi dan guard [conditions]."
  },
  {
    "id": 21,
    "code": "K0643",
    "type": "K",
    "pts": 2,
    "eo": "3.4.7",
    "euNo": 3,
    "title": "Activity Diagram Fork & Join Execution",
    "question": "The following activity diagram represents performing a measurement.\n\nDo the following statements match the diagram?",
    "diagramHtml": f"<img src='{img_q21}' alt='Diagram Q21' />",
    "options": [
      { "id": "A", "text": "Initialize measuring device must happen prior to Register at server.", "truth": "Does not match" },
      { "id": "B", "text": "Register at server happens as soon as Load certificates is ready.", "truth": "Does not match" },
      { "id": "C", "text": "Initialize network connection and Load certificates must finish at the same time.", "truth": "Does not match" },
      { "id": "D", "text": "Perform measurement is only executed if Self-test confirmed is true.", "truth": "Matches" }
    ],
    "correctDisplay": "A=Does not match, B=Does not match, C=Does not match, D=Matches",
    "whyCorrect": "• D: Matches. 'Perform measurement' dikawal oleh decision node dengan guard condition `[Self-test confirmed == true]`.",
    "whyWrong": "• A: Does not match. 'Initialize measuring device' dan 'Initialize network connection' berada dalam cabang Fork selari (parallel), jadi urutannya bebas.\n• B: Does not match. 'Register at server' memerlukan KEDUA-DUA 'Initialize network connection' DAN 'Load certificates' selesai di Join Node.\n• C: Does not match. Join node menunggu kedua-dua cabang selesai, tetapi tidak mewajibkan ia selesai pada masa yang sama (concurrent, not lockstep).",
    "extra": "Handbook Bab 3.4 / Syllabus EO 3.4.7: Fork & Join nodes in UML Activity diagrams.",
    "mnemonic": "Fork/Join = Selari & Bebas masa. Join Node menunggu kedua-duanya siap (D = Matches, A-C = Does not match)."
  },
  {
    "id": 22,
    "code": "P0623",
    "type": "P",
    "pts": 2,
    "eo": "3.4.2",
    "euNo": 3,
    "title": "Advantages of Graphical Models",
    "question": "In Requirements Engineering, which two substantial advantages do graphical models (e.g., use case models or state machines) have over plain textual specifications in natural language? (2 answers)",
    "options": [
      { "id": "A", "text": "Models often focus on specific aspects and reduce the complexity of the requirements.", "truth": True },
      { "id": "B", "text": "Models can be created much faster and cheaper than textual descriptions.", "truth": False },
      { "id": "C", "text": "Models have a defined syntax that reduces possible ambiguities and omissions.", "truth": True },
      { "id": "D", "text": "Models completely replace the need for natural language documentation.", "truth": False },
      { "id": "E", "text": "Models guarantee that all stakeholders have the exact same interpretation without discussion.", "truth": False }
    ],
    "correctDisplay": "A, C",
    "whyCorrect": "• A: Rajah memfokuskan kepada perspektif tertentu (struktur/fungsi/tingkah laku) sekali gus mengurangkan beban kognitif dan kerumitan.\n• C: Model grafik mempunyai sintaks formal (cth: UML) yang meminimumkan kekaburan berbanding teks biasa.",
    "whyWrong": "• B: Membina model yang tepat memerlukan kepakaran dan tidak semestinya lebih pantas/murah.\n• D: Model grafik melengkapi teks biasa, bukan menggantikannya 100%.\n• E: Tiada model yang boleh menjamin 100% tafsiran seragam tanpa komunikasi.",
    "extra": "Handbook Bab 3.4 / Syllabus EO 3.4.2: Kelebihan model berbanding bahasa biasa.",
    "mnemonic": "Kelebihan Model = Kurang Rumit (A) + Sintaks Jelas (C)."
  },
  {
    "id": 23,
    "code": "K0624",
    "type": "K",
    "pts": 2,
    "eo": "3.4.7",
    "euNo": 3,
    "title": "Activity Diagram Navigation Logic",
    "question": "For each of the statements on the diagram below, decide whether it is true or false.",
    "diagramHtml": f"<img src='{img_q23}' alt='Diagram Q23' />",
    "options": [
      { "id": "A", "text": "A route can be calculated without querying traffic information.", "truth": True },
      { "id": "B", "text": "A route can be calculated after querying traffic information.", "truth": True },
      { "id": "C", "text": "The system can ask for the desire to calculate the route dynamically without having to determine the GPS coordinates first.", "truth": False },
      { "id": "D", "text": "The order of Enter destination and Determine GPS coordinates is arbitrary.", "truth": True }
    ],
    "correctDisplay": "A=True, B=True, C=False, D=True",
    "whyCorrect": "• A: True. Terdapat cabang guard `[without traffic info]` yang terus ke kiraan laluan.\n• B: True. Terdapat cabang `[with traffic info]` yang melalui kueri trafik sebelum kiraan laluan.\n• D: True. 'Enter destination' dan 'Determine GPS coordinates' berada di bawah Fork bar selari, maka susunan pelaksanaannya adalah bebas (arbitrary).",
    "whyWrong": "• C: False. Pertanyaan kiraan dinamik berada selepas Join bar yang memerlukan koordinat GPS dan destinasi telah selesai.",
    "extra": "Handbook Bab 3.4 / Syllabus EO 3.4.7: Modeling control and data flow in Activity Diagrams.",
    "mnemonic": "Fork = Susunan Bebas (D=True). Cabang ada dua pilihan trafik (A, B=True). C=False."
  },
  {
    "id": 24,
    "code": "P0626",
    "type": "P",
    "pts": 2,
    "eo": "3.4.4",
    "euNo": 3,
    "title": "Diagrams for Process Steps Modeling",
    "question": "You are modeling the requirements for a management system to be applied in universities. The steps for enrollment of a new student at a university are to be documented using a model-based approach. Which two of the following diagrams are best suited to this aim? (2 answers)",
    "options": [
      { "id": "A", "text": "BPMN diagram", "truth": True },
      { "id": "B", "text": "Class diagram", "truth": False },
      { "id": "C", "text": "Activity diagram", "truth": True },
      { "id": "D", "text": "Use case diagram", "truth": False },
      { "id": "E", "text": "Entity-Relationship diagram (ERD)", "truth": False }
    ],
    "correctDisplay": "A, C",
    "whyCorrect": "• A (BPMN Diagram) & C (UML Activity Diagram) kedua-duanya direka khusus untuk memodelkan langkah aliran proses, keputusan, dan aliran kerja (Functional/Flow Perspective).",
    "whyWrong": "• B & E: Class diagram & ERD memodelkan struktur data.\n• D: Use case diagram memodelkan konteks fungsi di peringkat tinggi, bukan perincian langkah demi langkah aliran proses.",
    "extra": "Handbook Bab 3.4 / Syllabus EO 3.4.4: Functional perspective notations (Activity diagram, BPMN, DFD).",
    "mnemonic": "Langkah Proses (Steps of Enrollment) = BPMN (A) + Activity Diagram (C)."
  },
  {
    "id": 25,
    "code": "A0627",
    "type": "A",
    "pts": 1,
    "eo": "3.1.4",
    "euNo": 3,
    "title": "Function and Flow Perspective Aspect",
    "question": "When specifying a system, different aspects have to be considered. What is described in the function and flow aspect? (1 answer)",
    "options": [
      { "id": "A", "text": "Portability of the system", "truth": False },
      { "id": "B", "text": "Reaction of the system to an internal state transition", "truth": False },
      { "id": "C", "text": "Structure of input and output data", "truth": False },
      { "id": "D", "text": "Transformation of input data into output data", "truth": True }
    ],
    "correctDisplay": "D (Transformation of input data into output data)",
    "whyCorrect": "• Pilihan D adalah betul. Aspek Fungsi dan Aliran (Function and Flow Perspective) menghuraikan bagaimana data input diproses dan ditransformasikan menjadi data output oleh fungsi sistem.",
    "whyWrong": "• A: Portability adalah Quality Requirement.\n• B: Tindak balas peralihan keadaan adalah Behavior Perspective.\n• C: Struktur data input/output adalah Structure Perspective.",
    "extra": "Handbook Bab 3.1 / Syllabus EO 3.1.4: 3 Perspektif RE (Structure, Function/Flow, Behavior).",
    "mnemonic": "Function & Flow = Transformasi Input ke Output (D)."
  },

  # ------------------------------------------------------------------------------------------------
  # EU4: Practices for Requirements Elaboration (Q26–Q35, 13 Pts)
  # ------------------------------------------------------------------------------------------------
  {
    "id": 26,
    "code": "A3409",
    "type": "A",
    "pts": 1,
    "eo": "4.3.2",
    "euNo": 4,
    "title": "Resolving Conflicting Stakeholder Statements",
    "question": "You have been appointed as a Requirements Engineer in a company and are in the process of eliciting detailed requirements for a use case. To do this, you run through a series of interviews with various stakeholders. In the interview follow-up, you notice an inconsistency in the statements about a business process.\nWhich of the following approaches is best suited to resolve this inconsistency? (1 answer)",
    "options": [
      { "id": "A", "text": "You discuss this finding with an available stakeholder and adapt the requirements accordingly.", "truth": False },
      { "id": "B", "text": "You invite all stakeholders involved to a meeting to discuss and resolve the contradiction together.", "truth": True },
      { "id": "C", "text": "Due to your experience with user interfaces you decide on the right version without consulting stakeholders.", "truth": False },
      { "id": "D", "text": "You forward the problem to the product owner and let them decide alone.", "truth": False }
    ],
    "correctDisplay": "B (You invite all stakeholders involved to a meeting...)",
    "whyCorrect": "• Pilihan B adalah betul. Percanggahan antara pihak berkepentingan mesti diselesaikan secara kolaboratif melalui perbincangan bersama (Conflict Resolution) dengan semua pihak yang terlibat.",
    "whyWrong": "• A, C, D: Membuat keputusan secara unilateral tanpa melibatkan pihak yang bercanggah melanggar prinsip asas pengurusan konflik IREB.",
    "extra": "Handbook Bab 4.3 / Syllabus EO 4.3.2: Conflict resolution techniques and collaboration.",
    "mnemonic": "Konflik Pernyataan = Kumpulkan semua pihak terlibat berbincang bersama (B)."
  },
  {
    "id": 27,
    "code": "P0309",
    "type": "P",
    "pts": 1,
    "eo": "4.1.2",
    "euNo": 4,
    "title": "Requirements Engineer and Tester Relationship",
    "question": "Which two of the following statements best characterize the relationship between a Requirements Engineer and a stakeholder in the role of a tester? (2 answers)",
    "options": [
      { "id": "A", "text": "The Requirements Engineer provides input for the stakeholder's work.", "truth": True },
      { "id": "B", "text": "The Requirements Engineer's results are managed by the stakeholder.", "truth": False },
      { "id": "C", "text": "The stakeholder can contribute to ensure the quality of the Requirements Engineer's work.", "truth": True },
      { "id": "D", "text": "The stakeholder supervises the Requirements Engineer's work.", "truth": False },
      { "id": "E", "text": "There is no relationship between the Requirements Engineer and the tester.", "truth": False }
    ],
    "correctDisplay": "A, C",
    "whyCorrect": "• A: Keperluan yang didokumentasikan oleh Requirements Engineer menjadi asas input bagi tester mencipta kes ujian (Test Cases).\n• C: Penglibatan tester awal membolehkan semakan kebolehpengujian (Verifiability/Testability) yang meningkatkan kualiti spesifikasi keperluan.",
    "whyWrong": "• B, D, E: Tester bukan pengurus atau penyelia kepada Requirements Engineer, dan hubungan mereka adalah sangat penting (bukan tiada hubungan).",
    "extra": "Handbook Bab 4.1 / Syllabus EO 4.1.2: Stakeholder roles in RE (Testers, Developers, Users, Architects).",
    "mnemonic": "RE beri input kes ujian (A) + Tester bantu semak testability (C)."
  },
  {
    "id": 28,
    "code": "A0312",
    "type": "A",
    "pts": 1,
    "eo": "4.2.2",
    "euNo": 4,
    "title": "Elicitation Technique for Dissatisfiers (Kano Model)",
    "question": "The Kano model states that dissatisfiers (basic factors) are hard to elicit. Which of the techniques mentioned below is the most effective elicitation technique for dissatisfiers? (1 answer)",
    "options": [
      { "id": "A", "text": "Prototyping", "truth": False },
      { "id": "B", "text": "Questionnaire", "truth": False },
      { "id": "C", "text": "Field observation", "truth": True },
      { "id": "D", "text": "Brainstorming", "truth": False }
    ],
    "correctDisplay": "C (Field observation)",
    "whyCorrect": "• Pilihan C adalah betul. Dissatisfiers / Must-be factors (Faktor Asas) adalah keperluan tersirat yang dianggap 'sudah tentu ada' oleh pengguna sehingga mereka lupa menyebutnya. Teknik Pemerhatian Lapangan (Field Observation / Apprenticing) adalah cara paling berkesan untuk mengenal pastinya.",
    "whyWrong": "• A (Prototyping) & D (Brainstorming) sesuai untuk Delighters (Faktor Keterujaan).\n• B (Questionnaire) sesuai untuk Performance Factors.",
    "extra": "Handbook Bab 4.2 / Syllabus EO 4.2.2: Kano model mapping to elicitation techniques (Basic = Observation; Performance = Interview/Questionnaire; Excitement = Creativity/Prototyping).",
    "mnemonic": "Dissatisfier (Basic Factor) = Field Observation (Pemerhatian)."
  },
  {
    "id": 29,
    "code": "P0313",
    "type": "P",
    "pts": 2,
    "eo": "4.2.3",
    "euNo": 4,
    "title": "Factors for Choosing Elicitation Techniques",
    "question": "Which two of the following aspects are the most important to consider when choosing suitable elicitation techniques? (2 answers)",
    "options": [
      { "id": "A", "text": "The availability of the involved people.", "truth": True },
      { "id": "B", "text": "The preferences of the requirements engineer.", "truth": False },
      { "id": "C", "text": "The category of requirements based on Kano classification.", "truth": True },
      { "id": "D", "text": "The complexity of the required tools.", "truth": False },
      { "id": "E", "text": "The habitual use of a technique.", "truth": False }
    ],
    "correctDisplay": "A, C",
    "whyCorrect": "• A: Ketersediaan pemegang taruh (Availability) menentukan sama ada teknik bersemuka (cth: bengkel/temubual) atau tidak langsung (cth: soal selidik) boleh dilaksanakan.\n• C: Klasifikasi Kano (Basic, Performance, Delighter) menentukan jenis teknik elisitasi yang paling berkesan.",
    "whyWrong": "• B & E: Pilihan peribadi jurutera atau tabiat kebiasaan BUKAN faktor penentu profesional.",
    "extra": "Handbook Bab 4.2 / Syllabus EO 4.2.3: Influencing factors on the choice of elicitation techniques.",
    "mnemonic": "Pilih teknik = Ketersediaan Orang (A) + Klasifikasi Kano (C)."
  },
  {
    "id": 30,
    "code": "A3410",
    "type": "A",
    "pts": 1,
    "eo": "4.3.2",
    "euNo": 4,
    "title": "Conflict Resolution Techniques Identification",
    "question": "Which of the following techniques is NOT suitable for resolving requirements conflicts? (1 answer)",
    "options": [
      { "id": "A", "text": "Overruling", "truth": False },
      { "id": "B", "text": "Definition of variants", "truth": False },
      { "id": "C", "text": "Compromise", "truth": False },
      { "id": "D", "text": "Sampling", "truth": True }
    ],
    "correctDisplay": "D (Sampling)",
    "whyCorrect": "• Pilihan D adalah betul (bukan teknik penyelesaian konflik). 'Sampling' (Persampelan) ialah teknik pengumpulan data/dokumen, BUKAN teknik resolusi konflik.",
    "whyWrong": "• A (Overruling/Keputusan pihak berkuasa), B (Definition of variants/Membina variasi), dan C (Compromise/Kompromi) kesemuanya merupakan teknik resolusi konflik rasmi IREB.",
    "extra": "Handbook Bab 4.3 / Syllabus EO 4.3.2: 6 Teknik Resolusi Konflik IREB: Agreement, Compromise, Voting, Overruling, Definition of variants, Consider all alternatives.",
    "mnemonic": "Sampling = Elisitasi dokumen. Resolusi Konflik = Overruling, Variant, Compromise."
  },
  {
    "id": 31,
    "code": "P3411",
    "type": "P",
    "pts": 2,
    "eo": "4.1.4",
    "euNo": 4,
    "title": "Attributes in a Stakeholder List",
    "question": "Which are the two most important attributes in a stakeholder list? (2 answers)",
    "options": [
      { "id": "A", "text": "Their function/role", "truth": True },
      { "id": "B", "text": "Their personal preferences", "truth": False },
      { "id": "C", "text": "Their boss", "truth": False },
      { "id": "D", "text": "Their relevance", "truth": True },
      { "id": "E", "text": "Their previous projects", "truth": False }
    ],
    "correctDisplay": "A, D",
    "whyCorrect": "• A: Peranan/Fungsi (Function/Role) menentukan perspektif dan bidang tanggungjawab pemegang taruh.\n• D: Tahap Relevan (Relevance / Influence) menentukan sejauh mana keperluan mereka memberi impak kepada kejayaan sistem.",
    "whyWrong": "• B, C, E: Pilihan peribadi, maklumat bos, dan projek lepas bukan atribut teras standard dalam dokumentasi senarai pemegang taruh.",
    "extra": "Handbook Bab 4.1 / Syllabus EO 4.1.4: Stakeholder documentation attributes (Name, Role, Contact, Relevance, Availability).",
    "mnemonic": "Senarai Stakeholder = Peranan (Role) (A) + Relevan (Relevance) (D)."
  },
  {
    "id": 32,
    "code": "P0314",
    "type": "P",
    "pts": 1,
    "eo": "4.2.2",
    "euNo": 4,
    "title": "Advantages of Questionnaires",
    "question": "What are the two key advantages of using questionnaires for requirements elicitation? (2 answers)",
    "options": [
      { "id": "A", "text": "Questionnaires allow a high number of participants.", "truth": True },
      { "id": "B", "text": "Questionnaires allow statistically relevant statements on requirements.", "truth": True },
      { "id": "C", "text": "Questionnaires allow the participants' understanding to be validated.", "truth": False },
      { "id": "D", "text": "Questionnaires allow to obtain the most insight into tacit knowledge.", "truth": False },
      { "id": "E", "text": "Questionnaires allow to address the needs of individual stakeholders deeply.", "truth": False }
    ],
    "correctDisplay": "A, B",
    "whyCorrect": "• A: Soal selidik membolehkan penglibatan sejumlah besar responden (skala luas) tanpa kos masa temubual individu.\n• B: Data daripada soal selidik berstruktur membolehkan analisis statistik yang sahih mengenai keutamaan keperluan.",
    "whyWrong": "• C, D, E: Soal selidik tidak sesuai untuk menggali pengetahuan tersirat (tacit knowledge) atau membincangkan keperluan individu secara mendalam.",
    "extra": "Handbook Bab 4.2 / Syllabus EO 4.2.2: Gathering techniques (Questionnaires, Interviews).",
    "mnemonic": "Soal Selidik = Skala Ramai (A) + Statistik Sahih (B)."
  },
  {
    "id": 33,
    "code": "K0324",
    "type": "K",
    "pts": 2,
    "eo": "4.2.2",
    "euNo": 4,
    "title": "Classification of Elicitation Techniques",
    "question": "Which of the following statements about elicitation techniques are true and which are false?",
    "options": [
      { "id": "A", "text": "An interview is a gathering technique.", "truth": True },
      { "id": "B", "text": "An analogy technique is a gathering technique.", "truth": False },
      { "id": "C", "text": "System archeology is an observation technique.", "truth": False },
      { "id": "D", "text": "Apprenticing is an observation technique.", "truth": True }
    ],
    "correctDisplay": "A=True, B=False, C=False, D=True",
    "whyCorrect": "• A: True. Interview tergolong dalam Teknik Pengumpulan (Gathering Technique).\n• D: True. Apprenticing (Magang/Memerhati sambil belajar) tergolong dalam Teknik Pemerhatian (Observation Technique).",
    "whyWrong": "• B: False. Analogy technique tergolong dalam Teknik Kreativiti (Creativity Technique), bukan Gathering.\n• C: False. System archaeology tergolong dalam Teknik Berasaskan Dokumen (Artifact-based / Document-centric Technique), bukan Observation.",
    "extra": "Handbook Bab 4.2 / Syllabus EO 4.2.2: 4 Kategori Elisitasi IREB: 1. Gathering, 2. Observation, 3. Creativity, 4. Document-centric.",
    "mnemonic": "Interview = Gathering. Analogy = Creativity. Archeology = Document. Apprenticing = Observation."
  },
  {
    "id": 34,
    "code": "A0720",
    "type": "A",
    "pts": 1,
    "eo": "4.3.1",
    "euNo": 4,
    "title": "Conflict Types in Requirements Engineering",
    "question": "For a navigation system that is to be used internationally, a stakeholder demands a female voice only for the voice output. Another stakeholder considers this discriminatory and demands a male voice in addition.\nWhich of the following types of conflicts describes this conflict best? (1 answer)",
    "options": [
      { "id": "A", "text": "Relationship conflict", "truth": False },
      { "id": "B", "text": "Interest conflict", "truth": False },
      { "id": "C", "text": "Structural conflict", "truth": False },
      { "id": "D", "text": "Value conflict", "truth": True }
    ],
    "correctDisplay": "D (Value conflict)",
    "whyCorrect": "• Pilihan D adalah betul. Percanggahan yang berpunca daripada pegangan moral, prinsip etika, kepercayaan peribadi, atau isu diskriminasi ditakrifkan sebagai Konflik Nilai (Value Conflict).",
    "whyWrong": "• A (Relationship): Emosi/peribadi antara individu.\n• B (Interest): Perbezaan objektif keuntungan/manfaat.\n• C (Structural): Percanggahan kuasa/hierarki organisasi.",
    "extra": "Handbook Bab 4.3 / Syllabus EO 4.3.1: Jenis Konflik IREB: Subject matter, Interest, Value, Relationship, Structural.",
    "mnemonic": "Isu etika / diskriminasi = Value Conflict (Konflik Nilai)."
  },
  {
    "id": 35,
    "code": "A0721",
    "type": "A",
    "pts": 2,
    "eo": "4.4.3",
    "euNo": 4,
    "title": "Validation Technique for Safety-Critical Systems",
    "question": "In your project, a new braking system for high speed trains is developed. Which validation technique is most suitable for this situation, where the system requirements of a safety-critical component should be validated? (1 answer)",
    "options": [
      { "id": "A", "text": "A/B testing", "truth": False },
      { "id": "B", "text": "Prototype", "truth": False },
      { "id": "C", "text": "Walkthrough", "truth": False },
      { "id": "D", "text": "Inspection", "truth": True }
    ],
    "correctDisplay": "D (Inspection)",
    "whyCorrect": "• Pilihan D adalah betul. Inspeksi (Inspection) ialah teknik semakan paling formal dan teliti (dipimpin oleh moderator terlatih dengan senarai semak peraturan ketat) yang wajib digunakan untuk komponen kritikal keselamatan (Safety-critical).",
    "whyWrong": "• C (Walkthrough): Kurang formal dan dipimpin oleh pengarang sendiri, tidak memadai untuk sistem brek tren berkelajuan tinggi.\n• A & B: Tidak memberikan jaminan verifikasi ketelitian spesifikasi.",
    "extra": "Handbook Bab 4.4 / Syllabus EO 4.4.3: Review techniques comparison (Walkthrough vs Inspection vs Technical Review).",
    "mnemonic": "Safety-Critical (Brek Tren) = Inspection (Paling Formal & Ketat)."
  },

  # ------------------------------------------------------------------------------------------------
  # EU5: Process and Working Structure (Q36–Q37, 3 Pts)
  # ------------------------------------------------------------------------------------------------
  {
    "id": 36,
    "code": "P3504",
    "type": "P",
    "pts": 2,
    "eo": "5.2.1",
    "euNo": 5,
    "title": "Major Process Facets for RE Configuration",
    "question": "Which two major facets below are the most important to consider when configuring an RE process? (2 answers)",
    "options": [
      { "id": "A", "text": "The time facet: linear vs. iterative", "truth": True },
      { "id": "B", "text": "The budget facet: tight vs. large", "truth": False },
      { "id": "C", "text": "The purpose facet: prescriptive vs. explorative", "truth": True },
      { "id": "D", "text": "The methodology facet: structure-based vs. process-based", "truth": False },
      { "id": "E", "text": "The interaction facet: team-driven vs. individual", "truth": False }
    ],
    "correctDisplay": "A, C",
    "whyCorrect": "• A & C: Dua faset proses paling utama dalam model IREB untuk membentuk struktur proses RE ialah Time Facet (Linear vs Iterative) dan Purpose Facet (Prescriptive vs Explorative).",
    "whyWrong": "• B, D, E: 'Budget facet', 'Methodology facet', dan 'Interaction facet' BUKAN faset proses rasmi yang diiktiraf dalam taksonomi IREB.",
    "extra": "Handbook Bab 5.2 / Syllabus EO 5.2.1: 4 Faset Proses IREB: 1. Time (Linear/Iterative), 2. Purpose (Prescriptive/Explorative), 3. Target (Customer-specific/Market), 4. Format (Document/Item).",
    "mnemonic": "2 Faset Paling Utama = Time (A) + Purpose (C)."
  },
  {
    "id": 37,
    "code": "A3505",
    "type": "A",
    "pts": 1,
    "eo": "5.3.1",
    "euNo": 5,
    "title": "Standard Process Configurations in Practice",
    "question": "Based on an analysis of the influencing factors, a suitable combination of process facets should be configured. In practice, some specific combinations of facets frequently occur.\nWhich one of the combinations mentioned below is NOT recognized as such? (1 answer)",
    "options": [
      { "id": "A", "text": "Product-oriented RE process (iterative, explorative, market-driven)", "truth": False },
      { "id": "B", "text": "Human-oriented RE process (linear, process-based, individual)", "truth": True },
      { "id": "C", "text": "Participatory RE process (iterative, explorative, customer specific)", "truth": False },
      { "id": "D", "text": "Contractual RE process (linear, prescriptive, customer specific)", "truth": False }
    ],
    "correctDisplay": "B (Human-oriented RE process...)",
    "whyCorrect": "• Pilihan B adalah betul (bukan gabungan piawai). IREB menggariskan 3 bentuk proses tipikal: 1. Participatory RE process, 2. Contractual RE process, dan 3. Product-oriented RE process. 'Human-oriented RE process' tidak wujud dalam silibus.",
    "whyWrong": "• A, C, D kesemuanya merupakan gabungan proses standard (Archetypes) rasmi IREB.",
    "extra": "Handbook Bab 5.3 / Syllabus EO 5.3.1: 3 Typical RE Process Instances (Contractual, Product-oriented, Participatory).",
    "mnemonic": "3 Proses Standard = Contractual, Product, Participatory (B salah)."
  },

  # ------------------------------------------------------------------------------------------------
  # EU6: Management Practices for Requirements (Q38–Q43, 9 Pts)
  # ------------------------------------------------------------------------------------------------
  {
    "id": 38,
    "code": "K0819",
    "type": "K",
    "pts": 2,
    "eo": "6.5.3",
    "euNo": 6,
    "title": "Views on Requirements",
    "question": "Which of the following statements about views on requirements are true and which are false?",
    "options": [
      { "id": "A", "text": "Not every stakeholder needs to have access to all requirements.", "truth": True },
      { "id": "B", "text": "Requirements that belong together can be grouped to support the review.", "truth": True },
      { "id": "C", "text": "Requirements can be hidden from unauthorized stakeholders.", "truth": True },
      { "id": "D", "text": "It is assured that several people can work on one specification at the same time.", "truth": False }
    ],
    "correctDisplay": "A=True, B=True, C=True, D=False",
    "whyCorrect": "• A & C: Pandangan (Views) membenarkan penapisan maklumat untuk pemegang taruh tertentu dan keselamatan capaian.\n• B: Membantu semakan dengan mengelompokkan keperluan berkaitan mengikut perspektif.",
    "whyWrong": "• D: False. 'Views' BUKAN mekanisme concurrency/locking untuk membenarkan beberapa orang menyunting fail pada masa yang sama (itu peranan alat pengurusan versi/CM).",
    "extra": "Handbook Bab 6.5 / Syllabus EO 6.5.3: Views on requirements (Selective views, Security views, Aggregation).",
    "mnemonic": "Views = Tapis & Kelompok Maklumat (A, B, C = True). Bukan Version Locking (D = False)."
  },
  {
    "id": 39,
    "code": "A0820",
    "type": "A",
    "pts": 1,
    "eo": "6.6.1",
    "euNo": 6,
    "title": "Goals of Requirements Traceability",
    "question": "The traceability of requirements has several goals. Indicate the statement that is NOT correct. (1 answer)",
    "options": [
      { "id": "A", "text": "Traceability facilitates an impact analysis.", "truth": False },
      { "id": "B", "text": "Traceability facilitates the verification of implementation.", "truth": False },
      { "id": "C", "text": "Traceability facilitates exports from a requirements management tool.", "truth": True },
      { "id": "D", "text": "Traceability facilitates finding a requirement's source.", "truth": False }
    ],
    "correctDisplay": "C (Traceability facilitates exports...)",
    "whyCorrect": "• Pilihan C adalah kenyataan yang TIDAK BENAR (maka jawapan betul). Kebolehkesanan (Traceability) bertujuan untuk analisis impak, verifikasi pelaksanaan, dan jejak punca (source), BUKAN untuk memudahkan fungsi eksport alat RM.",
    "whyWrong": "• A (Impact analysis), B (Verification of implementation), dan D (Finding source) adalah matlamat teras kebolehkesanan (Pre-RS & Post-RS Traceability).",
    "extra": "Handbook Bab 6.6 / Syllabus EO 6.6.1: Benefits and goals of requirements traceability.",
    "mnemonic": "Traceability = Impak (A) + Verifikasi (B) + Punca Asal (D). Bukan eksport fail (C)."
  },
  {
    "id": 40,
    "code": "K0821",
    "type": "K",
    "pts": 2,
    "eo": "6.5.2",
    "euNo": 6,
    "title": "Purpose of Unique Identifiers",
    "question": "Additional information on requirements is managed using attributes. An example of such additional information is a unique identifier.\nWhich of the following statements regarding the purpose of unique identifiers are true and which are false?\n\nUnique identifiers are helpful ...",
    "options": [
      { "id": "A", "text": "... for estimating the overall size of a specification.", "truth": False },
      { "id": "B", "text": "... for having an unambiguous basis for communication.", "truth": True },
      { "id": "C", "text": "... for establishing references to other requirements.", "truth": True },
      { "id": "D", "text": "... for establishing traceability to other development artifacts.", "truth": True }
    ],
    "correctDisplay": "A=False, B=True, C=True, D=True",
    "whyCorrect": "• B: True. ID unik (cth: REQ-001) mengelakkan kekeliruan rujukan semasa komunikasi.\n• C: True. Memudahkan rujukan silang antara keperluan.\n• D: True. Membolehkan pautan kebolehkesanan ke kod sumber dan kes ujian.",
    "whyWrong": "• A: False. ID unik TIDAK digunakan untuk menganggar saiz keseluruhan spesifikasi (saiz memerlukan analisis Function Points/Story Points).",
    "extra": "Handbook Bab 6.5 / Syllabus EO 6.5.2: Requirements attributes and identifiers.",
    "mnemonic": "ID Unik = Komunikasi Jelas (B), Rujukan Silang (C), Traceability (D). Anggar Saiz = Salah (A)."
  },
  {
    "id": 41,
    "code": "P0838",
    "type": "P",
    "pts": 2,
    "eo": "6.4.1",
    "euNo": 6,
    "title": "Change Management for Requirements Baselines",
    "question": "You have produced a requirements baseline and delivered it to development. In the meantime, stakeholders have submitted change requests for requirements of this baseline.\nWhich of the following answers represent correct change management for requirements? (2 answers)",
    "options": [
      { "id": "A", "text": "Changes with regard to requirements that are part of the baseline have to be implemented immediately into the current baseline.", "truth": False },
      { "id": "B", "text": "Prior to adjusting the requirements to the change requests, the impact of the changes has to be determined.", "truth": True },
      { "id": "C", "text": "Change requests can be submitted at any time and may be considered for development when creating a future baseline.", "truth": True },
      { "id": "D", "text": "Time-critical change requests are neither analyzed nor estimated but delivered directly to development.", "truth": False },
      { "id": "E", "text": "If the development for changed requirements has already begun, no further changes are allowed.", "truth": False }
    ],
    "correctDisplay": "B, C",
    "whyCorrect": "• B: Sebelum meluluskan sebarang perubahan, analisis impak (Impact Analysis) wajib dijalankan.\n• C: Permohonan perubahan (Change Requests) boleh dihantar pada bila-bila masa dan akan diserap ke dalam Baseline Masa Hadapan (Future Baseline) setelah diluluskan oleh Change Control Board (CCB).",
    "whyWrong": "• A: Baseline sedia ada tidak boleh diubah secara terus secara terburu-buru.\n• D: Semua perubahan wajib dinilai impak dan kosnya.\n• E: Perubahan masih dibenarkan melalui proses kawalan perubahan rasmi.",
    "extra": "Handbook Bab 6.4 / Syllabus EO 6.4.1: Baselines and Change Control Process.",
    "mnemonic": "Tentukan Impak dahulu (B) + Masuk ke Future Baseline (C)."
  },
  {
    "id": 42,
    "code": "K0802",
    "type": "K",
    "pts": 2,
    "eo": "6.8.1",
    "euNo": 6,
    "title": "Reasons for Prioritizing Requirements",
    "question": "Attributes are used to manage additional characteristics of requirements. Priority is one example of such a requirements attribute.\nWhich of the following statements on the reason for prioritizing requirements are true and which are false?\n\nA reason for prioritizing is ...",
    "options": [
      { "id": "A", "text": "... to decide which requirements are to be implemented in the next release.", "truth": True },
      { "id": "B", "text": "... to decide on which requirements to focus first in testing.", "truth": True },
      { "id": "C", "text": "... to document how much it would cost to implement a requirement.", "truth": False },
      { "id": "D", "text": "... to recognize which requirements can be reused.", "truth": False }
    ],
    "correctDisplay": "A=True, B=True, C=False, D=False",
    "whyCorrect": "• A: True. Keutamaan menentukan perancangan fasa keluaran (Release Planning).\n• B: True. Keutamaan membolehkan pasukan ujian memfokuskan ujian ke atas ciri-ciri paling kritikal terlebih dahulu (Test Focus).",
    "whyWrong": "• C: False. Kos pelaksanaan didokumentasikan di bawah atribut 'Cost/Effort', bukan 'Priority'.\n• D: False. Kebolehgunaan semula dinilai melalui atribut 'Reuse/Category'.",
    "extra": "Handbook Bab 6.8 / Syllabus EO 6.8.1: Goals of requirements prioritization (Release planning, Risk reduction, Test focus).",
    "mnemonic": "Prioriti = Release Planning (A) + Fokus Ujian (B). Kos (C) & Reusability (D) = Bukan alasan prioriti."
  },
  {
    "id": 43,
    "code": "A0804",
    "type": "A",
    "pts": 1,
    "eo": "6.4.1",
    "euNo": 6,
    "title": "Definition of a Baseline",
    "question": "Version and configuration management are used for managing requirements and requirements specifications. \"Version\" and \"baseline\" are two frequently used terms in this context.\nSelect the best description of a baseline. (1 answer)",
    "options": [
      { "id": "A", "text": "A version of a requirement", "truth": False },
      { "id": "B", "text": "A released configuration of an individual requirement", "truth": False },
      { "id": "C", "text": "A released configuration of requirements", "truth": True },
      { "id": "D", "text": "A not yet released version of a requirements specification", "truth": False }
    ],
    "correctDisplay": "C (A released configuration of requirements)",
    "whyCorrect": "• Pilihan C adalah takrifan rasmi paling tepat mengikut Glosari dan Silibus IREB: Baseline ialah satu konfigurasi set keperluan yang telah diluluskan (stable, released, and committed configuration of requirements).",
    "whyWrong": "• A & B: Merujuk kepada versi keperluan individu, bukan baseline.\n• D: Baseline mestilah telah diluluskan (released/approved), bukan belum diluluskan.",
    "extra": "Glossary Bab B / Handbook Bab 6.4 / Syllabus EO 6.4.1: Definition of Baseline and Configuration.",
    "mnemonic": "Baseline = Konfigurasi Keperluan yang Telah Diluluskan (Released Configuration)."
  },

  # ------------------------------------------------------------------------------------------------
  # EU7: Tool Support (Q44–Q45, 3 Pts)
  # ------------------------------------------------------------------------------------------------
  {
    "id": 44,
    "code": "K0910",
    "type": "K",
    "pts": 2,
    "eo": "7.2.1",
    "euNo": 7,
    "title": "Selecting a Requirements Engineering Tool",
    "question": "As a Requirements Engineer for a company, you have to choose a tool to support your Requirements Engineering process.\nIn this context, which of the following statements are true and which are false?",
    "options": [
      { "id": "A", "text": "The tool has to support the artifacts demanded in the Requirements Engineering process applied.", "truth": True },
      { "id": "B", "text": "The choice of a tool should be left to the users of the tool.", "truth": False },
      { "id": "C", "text": "The tool has to assist users to set up their test cases as part of the Requirements Engineering process to support shift-left testing.", "truth": False },
      { "id": "D", "text": "The choice of a tool is influenced by the tool chain (e.g., configuration management tool) the tool is to be applied in.", "truth": True }
    ],
    "correctDisplay": "A=True, B=False, C=False, D=True",
    "whyCorrect": "• A: True. Alat RE mesti menyokong artifak/format kerja yang digunakan dalam proses organisasi.\n• D: True. Alat RE mesti serasi dan berintegrasi dengan rantaian alat (Tool Chain) sedia ada (cth: sistem CM, pengurusan isu, alat ujian).",
    "whyWrong": "• B: False. Pemilihan alat memerlukan analisis keperluan organisasi dan kos, bukan diserahkan semata-mata kepada pengguna individu.\n• C: False. Alat pengurusan keperluan tidak bertanggungjawab menetapkan kes ujian secara automatik.",
    "extra": "Handbook Bab 7.2 / Syllabus EO 7.2.1: Tool evaluation and introduction criteria.",
    "mnemonic": "Alat RE = Sokong Artifak Proses (A) + Integrasi Tool Chain (D). (A, D = True; B, C = False)."
  },
  {
    "id": 45,
    "code": "A0922",
    "type": "A",
    "pts": 1,
    "eo": "7.1.2",
    "euNo": 7,
    "title": "Capabilities of Requirements Management Tools",
    "question": "Which of the following tasks is NOT a capability of a tool, that supports the management of requirements in the Requirements Engineering process? (1 answer)",
    "options": [
      { "id": "A", "text": "Tracking logical relationships between requirements", "truth": False },
      { "id": "B", "text": "Modelling of requirements", "truth": True },
      { "id": "C", "text": "Measuring and reporting of the Requirements Engineering process", "truth": False },
      { "id": "D", "text": "Providing support for the prioritization of requirements", "truth": False }
    ],
    "correctDisplay": "B (Modelling of requirements)",
    "whyCorrect": "• Pilihan B adalah jawapan yang betul (bukan keupayaan alat pengurusan keperluan). Pemodelan keperluan (Modelling) ialah keupayaan alat pemodelan khusus (Modeling Tools seperti CASE tools / UML modelers), BUKAN fungsi utama alat pengurusan keperluan (Requirements Management Tools).",
    "whyWrong": "• A (Tracking relationships/Traceability), C (Metrics & Reporting), dan D (Prioritization support) kesemuanya adalah fungsi teras alat Requirements Management (RM Tools).",
    "extra": "Handbook Bab 7.1 / Syllabus EO 7.1.2: Tool categories in RE (RM Tools vs Modeling Tools vs Collaboration Tools).",
    "mnemonic": "RM Tool = Jejak Traceability (A), Laporan (C), Prioriti (D). Pemodelan (B) = Modeling Tool."
  }
]

# Write to app_data.json
output_data = {
  "eus": eus,
  "questions": questions
}

with open('app_data.json', 'w', encoding='utf8') as f:
    json.dump(output_data, f, indent=2, ensure_ascii=False)

print(f"Successfully generated app_data.json with {len(questions)} verified questions!")
