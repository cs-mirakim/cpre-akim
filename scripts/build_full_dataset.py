import json
import base64
import os
import re

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

def clean_pdf_artifacts(text):
    if not text:
        return ""
    # Remove running footer text like "Foundation Level | Examination  IREB 22 | 27"
    text = re.sub(r'Foundation Level\s*\|\s*Examination\s*[\uFFFD\u2013\-\?A-Za-z0-9\s]+\|\s*27', '', text)
    # Remove trailing K-type table headers
    text = re.sub(r'\s+(True\s+False|Needs to be considered\s+Does not need to be considered|Matches\s+Does not match|Correctly modeled\s+Incorrect or not modeled|Applies\s+Does not apply)$', '', text.strip())
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

# Formatted authentic questions data
formatted_stems = {
  1: "Which of the following statements on quality requirements are true and which are false?",
  2: "Which of the following tasks is NOT a core task of the Requirements Engineer? (1 answer)",
  3: "Amongst other things, the customer demands the following from the contractor responsible for delivering an information system:\n\n• A) The contractor shall process a change request within five days.\n• B) The test reports from the integration test must be disclosed for examination and the test report from the system test must be handed over.\n• C) At any time, the system shall enable a throughput of 100 transactions per second.\n• D) The Subversion tool must be used for configuration management.\n• E) Under normal load, the response time must be no more than two seconds in 90 percent of the cases.\n\nWhich two requirements refer to the system to be realized? (2 answers)",
  4: "Which of the following statements does NOT represent a fundamental principle of Requirements Engineering? (1 answer)",
  5: "Shared understanding is a principle of Requirements Engineering.\n\nFor each of the following statements about shared understanding decide, whether it is true or false.",
  6: "When defining the system boundary and the context boundary, which aspects need to be considered and which do not need to be considered?",
  7: "During the Requirements Engineering process for an online database application, you find out that data protection regulations do not apply, as the data processed by the system is anonymized.\n\nWhat will be influenced by this finding? (1 answer)",
  8: "Which of the following statements regarding work products is NOT correct? (1 answer)",
  9: "Which of the following concepts CANNOT be found in UML class diagrams? (1 answer)",
  10: "You want to design a requirements document in such a way that it is particularly well suited for the people who will work with the document in further phases of the development process.\n\nFrom the following sentences, choose the two best combinations of the role and its criteria for the requirements. (2 answers)",
  11: "A company wants to support its process of tender preparation with an information system. You are the Requirements Engineer responsible in this project. During initial discussions with different representatives, you discover, among other aspects, the following:\n\n• You do not understand some of the company's terminology.\n• It is obvious that the company representatives do not use consistent terminology.\n• Your main contact person at the company described their ideas by telling you the expected interactions between specialists and the information system in the form of different flows of user actions and system reactions.\n\nWhich two of the following approaches are particularly well suited to eliciting and documenting the requirements in this case? (2 answers)",
  12: "Which of the following statements on the choice of notations for the documentation of functional requirements apply and which do not apply?",
  13: "IREB defines quality criteria for work products.\n\nWhich of the following statements about quality criteria are true and which are false?",
  14: "A phrase template can be used to document natural-language requirements. You want to introduce such a template in your project and have to convince your project manager of the benefits.\n\nWhich are the two best arguments? (2 answers)",
  15: "You are given the following requirement:\n\n\"The system Alpha should display all data sets in all submenus\".\n\nWhat is the most severe issue in this requirement? (1 answer)",
  16: "Requirements can be documented using different forms of work products.\n\nFor each of the work products listed below, decide whether it is a template-based work product or not.",
  17: "A system needs to be developed for managing the fleet of a courier service. The system shall periodically transmit the geographical position of a vehicle to the central unit. The following requirements were documented:\n\n• R1: \"The system should be in operation as long as the ignition key is in the ignition lock.\"\n• R2: \"The system should be in operation as long as a driver is seated in the driver's seat.\"\n• R3: \"The system should switch to lost-signal if less than three satellites are available.\"\n\nWhich diagram best supports this type of requirement? (1 answer)",
  18: "To support young actors and directors, a contest for short films is held. The three best films will be presented with an award. The films submitted must have a maximum length of 20 minutes and must take the constraints depicted in the following diagram into consideration:\n\nDo the following statements match the above diagram?",
  19: "What is NOT depicted in a use case diagram? (1 answer)",
  20: "A company wants to introduce an authorization process for accessing confidential parts of the company's intranet by issuing time-limited passwords. For that reason a state diagram is modeled to express the possible states and state transitions for a user.\n\nDetermine which of the following requirements are modeled correctly in the state diagram above and which are modeled incorrectly or are not modeled at all.",
  21: "The following activity diagram represents performing a measurement:\n\nDo the following statements match the above diagram?",
  22: "In Requirements Engineering, which two substantial advantages do graphical models (e.g., use case models or state machines) have over plain textual specifications in natural language? (2 answers)",
  23: "The following activity diagram models the route calculation process for a vehicle navigation system:\n\nFor each of the statements on the diagram below, decide whether it is true or false.",
  24: "You are modeling the requirements for a management system to be applied in universities. The steps for enrollment of a new student at a university are to be documented using a model-based approach.\n\nWhich two of the following diagrams are best suited to this aim? (2 answers)",
  25: "When specifying a system, different aspects have to be considered.\n\nWhat is described in the function and flow aspect? (1 answer)",
  26: "You have been appointed as a Requirements Engineer in a company and are in the process of eliciting detailed requirements for a use case. To do this, you run through a series of interviews with various stakeholders. In the interview follow-up, you notice an inconsistency in the statements about the arrangement of functions in the menu on the user interface.\n\nWhat is the best way to deal with this situation? (1 answer)",
  27: "Which two of the following statements best characterize the relationship between a Requirements Engineer and a stakeholder in the role of a tester? (2 answers)",
  28: "The Kano model states that dissatisfiers (basic factors) are hard to elicit.\n\nWhich of the techniques mentioned below is the most effective elicitation technique for dissatisfiers? (1 answer)",
  29: "Which two of the following aspects are the most important to consider when choosing suitable elicitation techniques? (2 answers)",
  30: "Which of the following techniques is NOT suitable for resolving requirements conflicts? (1 answer)",
  31: "Which are the two most important attributes in a stakeholder list? (2 answers)",
  32: "What are the two key advantages of using questionnaires for requirements elicitation? (2 answers)",
  33: "Which of the following statements about elicitation techniques are true and which are false?",
  34: "For a navigation system that is to be used internationally, a stakeholder demands a female voice only for the voice output. Another stakeholder considers this discriminatory and demands a male voice in addition.\n\nWhich of the following types of conflicts describes this conflict best? (1 answer)",
  35: "In your project, a new braking system for high speed trains is developed.\n\nWhich validation technique is most suitable for this situation, where the system requirements of a safety-critical component should be validated? (1 answer)",
  36: "Which two major facets below are the most important to consider when configuring an RE process? (2 answers)",
  37: "Based on an analysis of the influencing factors, a suitable combination of process facets should be configured. In practice, some specific combinations of facets frequently occur.\n\nWhich one of the combinations mentioned below is NOT recognized as such? (1 answer)",
  38: "Which of the following statements about views on requirements are true and which are false?",
  39: "The traceability of requirements has several goals.\n\nIndicate the statement that is NOT correct. (1 answer)",
  40: "Additional information on requirements is managed using attributes. An example of such additional information is a unique identifier.\n\nWhich of the following statements regarding the purpose of unique identifiers are true and which are false?",
  41: "You have produced a requirements baseline and delivered it to development. In the meantime, stakeholders have submitted change requests for requirements of this baseline.\n\nWhich of the following answers represent correct change management for requirements? (2 answers)",
  42: "Attributes are used to manage additional characteristics of requirements. Priority is one example of such a requirements attribute.\n\nWhich of the following statements on the reason for prioritizing requirements are true and which are false?",
  43: "Version and configuration management are used for managing requirements and requirements specifications. \"Version\" and \"baseline\" are two frequently used terms in this context.\n\nSelect the best description of a baseline. (1 answer)",
  44: "As a Requirements Engineer for a company, you have to choose a tool to support your Requirements Engineering process.\n\nIn this context, which of the following statements are true and which are false?",
  45: "Which of the following tasks is NOT a capability of a tool that supports the management of requirements in the Requirements Engineering process? (1 answer)"
}

meta_data = {
  1: {
    "euNo": 1,
    "title": "Quality Requirements vs Functional Requirements",
    "correctDisplay": "A=False, B=True, C=False, D=True",
    "whyCorrect": "• B: True. Quality requirements melengkapi functional requirements dengan menetapkan tahap kualiti (seperti performance, usability, security, reliability) yang perlu dicapai oleh sesuatu fungsi.\n• D: True. Quality requirements boleh diperincikan (substantiated) menjadi functional requirements baharu (contoh: keperluan keselamatan 'Akses mesti dilindungi' diperincikan kepada fungsi 'Sistem mesti menyediakan Two-Factor Authentication').",
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
    "mnemonic": "System Requirement = Sifat sistem yang dibina (Throughput & Response Time). Bukan proses kerja kontraktor."
  },
  4: {
    "euNo": 2,
    "title": "9 Fundamental Principles of Requirements Engineering",
    "correctDisplay": "D (Requirements that have been completely documented...)",
    "whyCorrect": "• Pilihan D adalah jawapan yang betul (BUKAN prinsip RE). Prinsip 7 (Evolution) menegaskan bahawa keperluan TIDAK statik dan akan sentiasa berubah (evolving) sepanjang kitaran hayat sistem.",
    "whyWrong": "• A, B, C mematuhi 9 Prinsip RE:\n- A = Prinsip 1 (Value-Orientation: Keperluan adalah alat capai nilai, bukan matlamat mutlak).\n- B = Prinsip 3 (Shared Understanding: Gabungan pemahaman eksplisit & implisit).\n- C = Prinsip 4 (Context: RE tidak boleh dilakukan secara terasing tanpa memahami konteks).",
    "extra": "Handbook Bab 2 / Syllabus EO 2.1.1: 9 Prinsip Asas RE: 1. Value-Orientation, 2. Stakeholders, 3. Shared Understanding, 4. Context, 5. Problem-Req-Solution, 6. Validation, 7. Evolution, 8. Innovation, 9. Systematic Work.",
    "mnemonic": "9 Prinsip: Nilai, Stakeholder, Kefahaman, Konteks, Masalah, Validasi, Evolusi, Inovasi, Sistematik."
  },
  5: {
    "euNo": 2,
    "title": "Principle 3: Shared Understanding (Explicit vs Implicit)",
    "correctDisplay": "A=True, B=True, C=False, D=False",
    "whyCorrect": "• A: True. Shared understanding dibina daripada gabungan pemahaman eksplisit (ditulis/dimodelkan) dan pemahaman implisit (difahami bersama melalui budaya/pengalaman).\n• B: True. Istilah teknikal yang ditakrifkan dalam Glossary membolehkan pemahaman eksplisit yang tepat dan mengelakkan kekeliruan sinonim.",
    "whyWrong": "• C: False. Shared understanding TIDAK semestinya didokumentasikan sepenuhnya; dalam pasukan Agile yang matang, pemahaman implisit yang kukuh memadai tanpa perlu mendokumentasikan setiap butiran kecil.\n• D: False. Pasukan baharu yang belum pernah bekerjasama mempunyai pemahaman implisit yang rendah, maka mereka memerlukan dokumentasi eksplisit yang LEBIH banyak (bukan kurang).",
    "extra": "Handbook Bab 2.3 / Syllabus EO 2.3.1 (Principle 3: Shared Understanding): Komunikasi berkesan mengurangkan jarak pemahaman antara stakeholder dan pasukan teknikal.",
    "mnemonic": "Shared Understanding = Explicit (Glossary/Model) + Implicit (Pengalaman/Budaya). Pasukan baharu perlu lebih banyak eksplisit."
  },
  6: {
    "euNo": 2,
    "title": "Principle 4: Context Boundaries (System vs Context)",
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
    "title": "Roles and Criteria for Requirements Work Products",
    "correctDisplay": "C, D",
    "whyCorrect": "• C (System architects / Non-ambiguity & Completeness): Betul. System Architects memerlukan keperluan yang lengkap dan tidak kabur untuk mereka bentuk struktur seni bina teknikal yang kukuh.\n• D (Testers / Verifiability): Betul. Jurutera Ujian (Testers) memerlukan keperluan yang boleh disahkan (Verifiable / Testable) agar kriteria penerimaan ujian dapat dibina.",
    "whyWrong": "• A (Developers / Redundancy): Pembangun perisian TIDAK mahu redundansi (pengulangan maklumat); redundansi meningkatkan risiko ketidakkonsistenan.\n• B (Project managers / Detailedness): Pengurus projek fokus pada skop dan nilai perniagaan, bukan butiran teknikal peringkat rendah.",
    "extra": "Handbook Bab 3.1 / Syllabus EO 3.1.4: Menyesuaikan gaya dokumentasi mengikut peranan pengguna hiliran (Downstream Roles).",
    "mnemonic": "Architect = Complete & Unambiguous. Tester = Verifiable (Boleh Diuji)."
  },
  11: {
    "euNo": 3,
    "title": "Approaches for Terminology & Interaction Flows (Tender Preparation)",
    "correctDisplay": "B, D",
    "whyCorrect": "• B (Creating a use case diagram and specifying the use cases): Betul. Interaksi antara pakar dan sistem dalam bentuk aliran tindakan pengguna & tindak balas sistem paling tepat dimodelkan menggunakan Use Case Diagram & spesifikasi Use Case.\n• D (Establishing a glossary): Betul. Menghadapi masalah istilah syarikat yang tidak difahami dan tidak konsisten diselesaikan secara langsung dengan membina Glossary (Kamus Istilah).",
    "whyWrong": "• A (Writing formal mathematical specifications): Notasi matematik formal tidak menyelesaikan masalah salah faham istilah dan menyukarkan komunikasi dengan wakil syarikat.\n• C (Documenting interactions exclusively in code comments): Komen kod tidak boleh disemak oleh stakeholder perniagaan.\n• E (Avoiding functional requirements): Menolak keperluan fungsi merosakkan projek.",
    "extra": "Handbook Bab 3.1 & 3.2 / Syllabus EO 3.1.3 & 3.2.2: Masalah istilah ➔ Glossary. Aliran tindakan pengguna vs sistem ➔ Use Cases.",
    "mnemonic": "Istilah tak faham ➔ Glossary. Interaksi Pengguna & Sistem ➔ Use Case."
  },
  12: {
    "euNo": 3,
    "title": "Notations for Requirements Documentation (Natural vs Model vs Hybrid)",
    "correctDisplay": "A=Applies, B=Does not apply, C=Applies, D=Applies",
    "whyCorrect": "• A: Applies. Notasi standard (UML/SysML/BPMN) memastikan konsistensi dan mengurangkan kekaburan antara pihak berkepentingan.\n• C: Applies. Menggabungkan model grafik bersama teks penerangan (Hybrid Representation) memberikan kejelasan maksimum.\n• D: Applies. Bahasa semulajadi adalah format paling fleksibel dan universal untuk disemak oleh semua jenis stakeholder.",
    "whyWrong": "• B: Does not apply. Model grafik TIDAK sepatutnya diabaikan; rajah visual mengurangkan beban kognitif pembaca dengan sangat ketara.",
    "extra": "Handbook Bab 3.1 / Syllabus EO 3.1.5: 3 bentuk dokumentasi: Natural Language, Conceptual Models, Hybrid.",
    "mnemonic": "Notasi: Standard kurangkan salah faham, Hybrid paling berkesan, Teks biasa paling universal."
  },
  13: {
    "euNo": 3,
    "title": "Quality Criteria for Work Products (IREB Standards)",
    "correctDisplay": "A=False, B=True, C=True, D=False",
    "whyCorrect": "• B: True. Kriteria kualiti untuk himpunan keperluan (Work Product Sets) termasuklah: Completeness, Consistency, Non-redundancy, Modifiability, dan Traceability.\n• C: True. Keperluan individu mestilah: Unambiguous, Atomic, Verifiable, dan Necessary.",
    "whyWrong": "• A: False. Work products TIDAK boleh dinilai hanya berdasarkan ketebalan dokumen; kualiti diukur dari segi ketepatan dan kegunaan sebenar.\n• D: False. Kriteria kualiti berbeza antara Individual Work Products (Atomic, Verifiable) dengan Sets (Completeness, Consistency).",
    "extra": "Handbook Bab 3.1 / Syllabus EO 3.1.6: Kualiti Keperluan: 1. Individual Requirements Criteria vs 2. Work Product Set Criteria.",
    "mnemonic": "Individu = Atomic, Verifiable, Unambiguous. Set = Complete, Consistent, Traceable."
  },
  14: {
    "euNo": 3,
    "title": "Benefits of Phrase Templates (Sentence Templates / SOPHIST / MARE)",
    "correctDisplay": "A, C",
    "whyCorrect": "• A (Requirements written using a phrase template contain fewer linguistic defects): Betul. Templat ayat mengelakkan kecacatan bahasa seperti Nominalization dan ayat pasif.\n• C (Using phrase templates is easy to learn for everyone): Betul. Struktur templat ayat mudah dipelajari oleh jurutera dan stakeholder dalam masa yang singkat.",
    "whyWrong": "• B (Phrase templates eliminate the need to write functional requirements): Salah, templat ayat digunakan khusus untuk MENULIS functional requirements.\n• D (Using phrase templates completely avoids any ambiguities): Tiada templat yang dapat menghapuskan kekaburan 100% jika perkataan yang diisi tidak jelas.",
    "extra": "Handbook Bab 3.3 / Syllabus EO 3.3.1: Sentence Templates (SOPHIST/MARE): Mengurangkan kecacatan bahasa dan membina struktur konsisten.",
    "mnemonic": "Sentence Template: Kurangkan kecacatan bahasa & Mudah dipelajari."
  },
  15: {
    "euNo": 3,
    "title": "Natural Language Defects: Universal Quantifiers",
    "correctDisplay": "B (Universal quantifiers)",
    "whyCorrect": "• Pilihan B adalah jawapan yang betul. Perkataan 'ALL data sets' dan 'ALL submenus' adalah contoh Universal Quantifiers (Kuantifier Universal). Ia mengitlakkan keadaan secara melampau dan menyembunyikan pengecualian (exceptions) yang perlu dikendalikan.",
    "whyWrong": "• A (Nominalization): Tiada kata kerja yang diubah menjadi kata nama dalam ayat tersebut.\n• C (Passive voice): Ayat menggunakan struktur aktif ('The system Alpha should display...').\n• D (Incompletely specified process words): Masalah paling utama dalam ayat ini ialah generalisasi melampau perkataan 'ALL'.",
    "extra": "Handbook Bab 3.3 / Syllabus EO 3.3.2: 4 Kecacatan Bahasa Semulajadi: 1. Nominalization, 2. Universal Quantifiers, 3. Incompletely Specified Conditions, 4. Passive Voice.",
    "mnemonic": "All, Every, Always, Never = Universal Quantifiers (Bahaya generalisasi tanpa pengecualian)."
  },
  16: {
    "euNo": 3,
    "title": "Classification of Template-based Work Products",
    "correctDisplay": "A=False, B=True, C=False, D=True",
    "whyCorrect": "• B (User Story): True. User Story mempunyai struktur templat piawai: 'As a <role>, I want <feature>, so that <benefit>'.\n• D (Use Case Template): True. Use case specification ditulis menggunakan templat berstruktur (Preconditions, Main Flow, Alternate Flows, Postconditions).",
    "whyWrong": "• A (Free textual documentation): False. Teks bebas tidak mempunyai struktur templat tetap.\n• C (Mind map): False. Mind map adalah graf pokok visual tanpa templat ayat tetap.",
    "extra": "Handbook Bab 3.1 / Syllabus EO 3.1.2: Template-based Work Products: User Stories, Use Case Templates, Quality Requirements Templates.",
    "mnemonic": "User Story (As a... I want...) & Use Case Specification = Template-based Work Products."
  },
  17: {
    "euNo": 3,
    "title": "Modeling Fleet Management States & Transitions (State Machine)",
    "correctDisplay": "A (State machine)",
    "whyCorrect": "• Pilihan A adalah jawapan yang betul. Keperluan R1, R2, dan R3 memodelkan mod operasi kenderaan berdasarkan keadaan tertentu (kunci dalam suis, pemandu duduk, kehilangan isyarat satelit). Ini adalah model keadaan dinamik dan transisi yang paling tepat dimodelkan menggunakan State Machine Diagram.",
    "whyWrong": "• B (Class diagram): Memodelkan struktur data statik, bukan mod operasi.\n• C (Use case diagram): Memodelkan skop interaksi perniagaan peringkat tinggi.\n• D (Deployment diagram): Memodelkan penempatan fizikal perkakasan.",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.7: Behavior Perspective: UML State Machine Diagram memodelkan States, Transitions, Events, dan Guards.",
    "mnemonic": "In operation / Lost-signal / Conditions ➔ State Machine Diagram (Behavior Perspective)."
  },
  18: {
    "euNo": 3,
    "title": "UML Class Diagram: Film Contest Multiplicities & Associations",
    "correctDisplay": "A=Does not match, B=Matches, C=Matches, D=Matches, E=Does not match",
    "whyCorrect": "• B: Matches. Hubungan Actor ➔ Film mempunyai multiplicity `1..10` ke `0..*`. Ini bermaksud satu filem boleh dilakonkan oleh sekurang-kurangnya 1 dan maksimum 10 orang pelakon.\n• C: Matches. Multiplicity `0..*` pada Film bermaksud seseorang pelakon boleh tidak berlakon dalam mana-mana filem yang bertanding (0) atau membintangi banyak filem (*).\n• D: Matches. Hubungan Film ➔ Director mempunyai multiplicity `1..3` ke `1`. Ini bermaksud sebuah filem diarahkan oleh 1 hingga 3 orang pengarah.",
    "whyWrong": "• A: Does not match. Multiplicity Director ialah `1`, bermaksud seorang pengarah HANYA boleh mengarah 1 filem (tidak boleh mengarah pelbagai filem serentak dalam model ini).\n• E: Does not match. Hubungan pengarah ke pelakon tidak dimodelkan secara langsung.",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.6: UML Class Diagram Multiplicities: 0..1 (Optional), 1 (Exact one), 1..* (At least one), 0..* / * (Any number), 1..10 (Min 1, Max 10).",
    "mnemonic": "Baca multiplicity dari hujung bertentangan garisan persatuan (Association Ends)."
  },
  19: {
    "euNo": 3,
    "title": "Elements NOT Depicted in a Use Case Diagram",
    "correctDisplay": "A (The internal flow of events in the use case)",
    "whyCorrect": "• Pilihan A adalah jawapan yang betul (TIDAK dipaparkan). Aliran peristiwa terperinci di dalam use case (aliran langkah 1, 2, 3) diterangkan dalam spesifikasi teks Use Case atau Activity Diagram, bukannya di atas rajah Use Case Diagram itu sendiri.",
    "whyWrong": "• B (Actors), C (Use cases / Elips), dan D (System boundary / Kotak sempadan) kesemuanya merupakan komponen grafik rasmi dalam UML Use Case Diagram.",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.2: Use Case Diagram memaparkan: System Boundary, Actors, Use Cases, Associations, <<include>>, <<extend>>, Generalization.",
    "mnemonic": "Use Case Diagram = Pandangan Luar / Black Box (Actors & Use Cases). Aliran dalaman = Spesifikasi Use Case / Activity Diagram."
  },
  20: {
    "euNo": 3,
    "title": "State Machine Diagram: Intranet Password Lifecycle Verification",
    "correctDisplay": "A=Incorrect or not modeled, B=Correctly modeled, C=Incorrect or not modeled, D=Incorrect or not modeled",
    "whyCorrect": "• B: Correctly modeled. Transisi daripada 'not entitled' ke 'application in progress' berlaku apabila event 'application filed / check application' dipicu.",
    "whyWrong": "• A: Incorrect or not modeled. Kitaran tamat tempoh kata laluan tidak membolehkan pembaharuan automatik terus tanpa melalui proses semakan semula.\n• C: Incorrect or not modeled. Transisi penolakan permohonan mengembalikan status ke 'not entitled' dan bukannya 'blocked'.\n• D: Incorrect or not modeled. Keadaan 'blocked' adalah sink state yang memerlukan tindakan pentadbir khas, bukan transisi terus.",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.7: Semak ketepatan model State Machine: Source State, Event [Guard] / Action, Target State.",
    "mnemonic": "Semak setiap anak panah transisi: Keadaan Asal ➔ Event/Action ➔ Keadaan Sasaran."
  },
  21: {
    "euNo": 3,
    "title": "Activity Diagram: Performing Measurement Control Flow Verification",
    "correctDisplay": "A=Matches, B=Does not match, C=Matches, D=Matches",
    "whyCorrect": "• A: Matches. 'Initialize network connection' dan 'Load certificates' berada di antara Fork dan Join bar, maka kedua-duanya dilaksanakan secara selari (parallel).\n• C: Matches. Transisi gelung 'Resend measurement data' berlaku jika 'waiting time elapsed' tercapai.\n• D: Matches. Aktiviti 'Deactivate measuring device' dilaksanakan sebaik sahaja guard condition '[Data receipt confirmed]' bernilai benar.",
    "whyWrong": "• B: Does not match. 'Register at server' hanya boleh bermula selepas KEDUA-DUA aktiviti selari (network connection & certificates) selesai pada Join bar (bukan serta merta selepas satu sahaja selesai).",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.3: Activity Diagram: Fork Node memecahkan aliran kepada selari; Join Node menyegerakkan semua aliran sebelum mara ke hadapan.",
    "mnemonic": "Fork = Mula Selari. Join = Tunggu Semua Cawangan Selesai."
  },
  22: {
    "euNo": 3,
    "title": "Advantages of Graphical Conceptual Models over Textual Specifications",
    "correctDisplay": "B, C",
    "whyCorrect": "• B (A model can be verified more easily): Betul. Model grafik mempunyai sintaks formal yang memudahkan pengesahan logik dan integriti berbanding teks panjang.\n• C (A model allows a faster overview of the requirements): Betul. Rajah visual memberikan gambaran skop menyeluruh sepintas lalu (higher comprehensibility & lower cognitive load).",
    "whyWrong": "• A (Models can only be interpreted in one way): Salah, model yang kurang dianotasi juga boleh disalah tafsir jika pembaca tidak memahami notasi.\n• D (Models are always completely error-free): Salah, pencipta model masih boleh membuat kesilapan logik domain.\n• E (Models eliminate all documentation effort): Salah, membina model memerlukan kemahiran dan usaha masa.",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.1: Nilai Model Konseptual: Gambaran pantas, fokus perspektif khusus, dan mudah disahkan.",
    "mnemonic": "Model Grafik = Gambaran Pantas (Faster Overview) + Mudah Disahkan (Easier Verification)."
  },
  23: {
    "euNo": 3,
    "title": "Activity Diagram: Vehicle Navigation Route Calculation Flow",
    "correctDisplay": "A=True, B=False, C=False, D=True",
    "whyCorrect": "• A: True. 'Enter destination' dan 'Determine GPS coordinates' berada di bawah Fork bar, maka kedua-duanya dilaksanakan secara serentak/selari (concurrently).\n• D: True. Aktiviti 'Calculate route' hanya boleh dilaksanakan selepas cawangan keputusan (sama ada Query traffic information atau pintasan cawangan lain) disatukan pada Merge node.",
    "whyWrong": "• B: False. 'Query traffic information' HANYA dilaksanakan jika pengguna memilih guard '[Avoid congestions]', bukan dalam semua keadaan.\n• C: False. 'Display route' adalah aktiviti selepas laluan dikira, bukan dilaksanakan serentak.",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.3: UML Activity Diagram Nodes: Initial Node, Activity, Fork (Selari), Decision Diamond (Pilihan bersyarat), Merge, Final Node.",
    "mnemonic": "Fork = Serentak. Decision Diamond = Bersyarat (Pilih satu ikut Guard)."
  },
  24: {
    "euNo": 3,
    "title": "Process Flow Modeling Notations (BPMN & Activity Diagram)",
    "correctDisplay": "A, C",
    "whyCorrect": "• A (BPMN diagram): Betul. BPMN (Business Process Model and Notation) direka khas oleh industri untuk memodelkan proses perniagaan dan langkah aliran kerja.\n• C (Activity diagram): Betul. UML Activity Diagram memodelkan aliran aktiviti, kawalan proses, dan peralihan data dari satu langkah ke langkah seterusnya.",
    "whyWrong": "• B (Class diagram): Memodelkan struktur data statik, bukan urutan langkah proses.\n• D (State machine): Memodelkan kitaran hayat status satu objek entiti.\n• E (Use case diagram): Memodelkan skop fungsi peringkat tinggi tanpa butiran aliran langkah dalaman.",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.3 & 3.2.4: Function & Flow Perspective: UML Activity Diagram & BPMN.",
    "mnemonic": "Aliran Langkah Proses = BPMN + UML Activity Diagram."
  },
  25: {
    "euNo": 3,
    "title": "3 Perspectives of Conceptual Modeling: Function and Flow Aspect (DFD)",
    "correctDisplay": "A (Data flows and the transformation of data by the system)",
    "whyCorrect": "• Pilihan A adalah jawapan yang betul. Perspektif Fungsi dan Aliran (Function and Flow Perspective) menerangkan bagaimana data bergerak (Data Flows) dan bagaimana data tersebut diproses atau diubah oleh aktiviti sistem (Data Transformation melalui DFD atau Activity Diagram).",
    "whyWrong": "• B (Structure and relationships of domain objects): Ini adalah Structure Perspective (Class Diagram / ERD).\n• C (State transitions and events): Ini adalah Behavior Perspective (State Machine Diagram).\n• D (Physical deployment nodes): Ini adalah Deployment View.",
    "extra": "Handbook Bab 3.2 / Syllabus EO 3.2.5: 3 Perspektif IREB:\n1. Structure Perspective (Class / ERD)\n2. Function Perspective (DFD / Activity / BPMN)\n3. Behavior Perspective (State Machine).",
    "mnemonic": "3 Perspektif: Struktur (Data/Class), Fungsi (Transformasi/DFD), Tingkah Laku (Status/State)."
  },
  26: {
    "euNo": 4,
    "title": "Handling Inconsistencies Discovered in Stakeholder Interviews",
    "correctDisplay": "C (You consult with the affected stakeholders to agree on a common solution)",
    "whyCorrect": "• Pilihan C adalah tindakan profesional yang betul. Apabila terdapat percanggahan kenyataan antara stakeholder dalam temubual, jurutera keperluan mesti mengadakan perbincangan/bengkel bersama stakeholder terbabit untuk mencapai kata sepakat (Conflict Resolution).",
    "whyWrong": "• A (You decide on your own): Jurutera keperluan tidak mempunyai kuasa membuat keputusan sepihak mengenai fungsi perniagaan tanpa persetujuan stakeholder.\n• B (You ignore the inconsistency): Mengabaikan percanggahan akan menyebabkan ralat besar semasa pembangunan.\n• D (You ask the developers to decide): Pembangun tidak bertanggungjawab mentakrifkan keperluan bisnes.",
    "extra": "Handbook Bab 4.3 / Syllabus EO 4.3.1: Resolusi Konflik: Kenalpasti percanggahan, bincang bersama stakeholder terbabit, dan pilih teknik penyelesaian yang dipersetujui.",
    "mnemonic": "Ada percanggahan ➔ Bincang bersama stakeholder terbabit (Jangan buat keputusan sendiri)."
  },
  27: {
    "euNo": 4,
    "title": "Relationship between Requirements Engineer and Tester",
    "correctDisplay": "A, C",
    "whyCorrect": "• A (The Requirements Engineer supports the tester in creating the acceptance test cases): Betul. Jurutera keperluan membantu jurutera ujian memahami kriteria penerimaan (Acceptance Criteria) untuk membina kes ujian.\n• C (The tester supports the Requirements Engineer in reviewing the requirements for verifiability): Betul. Jurutera ujian membantu menyemak sama ada sesuatu keperluan boleh diuji (Verifiable / Testable) seawal mungkin.",
    "whyWrong": "• B (The tester defines the business requirements): Penguji tidak mentakrifkan keperluan bisnes.\n• D (The Requirements Engineer executes the integration tests): Pelaksanaan ujian integrasi adalah tugas jurutera perisian/penguji, bukan RE.",
    "extra": "Handbook Bab 4.1 / Syllabus EO 4.1.2: Hubungan RE & Ujian (Shift-Left Testing): Keperluan yang jelas membolehkan kes ujian dibuat awal.",
    "mnemonic": "RE bantu Tester faham skop. Tester bantu RE pastikan keperluan boleh diuji (Verifiable)."
  },
  28: {
    "euNo": 4,
    "title": "Kano Model: Most Effective Elicitation Technique for Dissatisfiers (Basic Factors)",
    "correctDisplay": "C (Observation techniques)",
    "whyCorrect": "• Pilihan C adalah jawapan yang betul. Faktor Asas (Basic Factors / Dissatisfiers) adalah ciri yang dianggap lumrah oleh pengguna (diambil mudah) sehingga mereka terlupa untuk menyatakannya semasa temubual. Oleh itu, teknik pemerhatian (Observation seperti Field Observation atau Shadowing) adalah kaedah paling berkesan untuk mengenal pasti faktor tersirat ini.",
    "whyWrong": "• A (Questionnaires) & B (Interviews): Pengguna jarang menyebut ciri asas dalam soal selidik/temubual kerana menganggapnya terlalu jelas.\n• D (Creativity techniques): Teknik kreativiti (Brainstorming) lebih berkesan untuk mencari Excitement Factors (Delighters).",
    "extra": "Handbook Bab 4.2 / Syllabus EO 4.2.2 (Model Kano):\n1. Basic Factors ➔ Observation & Artifact Analysis\n2. Performance Factors ➔ Interview & Survey\n3. Excitement Factors ➔ Creativity Techniques (Brainstorming).",
    "mnemonic": "Basic Factors (Dissatisfiers) = Observation (Pemerhatian). Excitement Factors = Creativity."
  },
  29: {
    "euNo": 4,
    "title": "Key Factors for Selecting Requirements Elicitation Techniques",
    "correctDisplay": "A, C",
    "whyCorrect": "• A (The availability of the stakeholders): Betul. Ketersediaan masa dan lokasi stakeholder menentukan sama ada bengkel bersemuka atau soal selidik atas talian perlu digunakan.\n• C (The level of detail required for the requirements): Betul. Tahap perincian yang diperlukan menentukan kedalaman teknik elisitasi yang dipilih.",
    "whyWrong": "• B (The programming language used): Bahasa pengaturcaraan hiliran tidak menentukan teknik elisitasi.\n• D (The test automation framework): Kerangka kerja ujian tidak mempengaruhi cara menyoal stakeholder.",
    "extra": "Handbook Bab 4.2 / Syllabus EO 4.2.3: Faktor Pemilihan Teknik Elisitasi: Risiko projek, ketersediaan stakeholder, pengalaman RE, kekangan masa/kos.",
    "mnemonic": "Pilih teknik elisitasi berdasarkan: Ketersediaan Stakeholder + Tahap Perincian Diperlukan."
  },
  30: {
    "euNo": 4,
    "title": "Techniques for Resolving Requirements Conflicts (NOT Suitable)",
    "correctDisplay": "D (Separation of concerns)",
    "whyCorrect": "• Pilihan D adalah jawapan yang betul (BUKAN teknik resolusi konflik). 'Separation of concerns' adalah prinsip reka bentuk seni bina perisian, bukannya kaedah menyelesaikan perselisihan pendapat antara stakeholder.",
    "whyWrong": "• A (Agreement / Persetujuan), B (Compromise / Kompromi), dan C (Voting / Undian) kesemuanya merupakan teknik resolusi konflik standard mengikut IREB.",
    "extra": "Handbook Bab 4.3 / Syllabus EO 4.3.2: 5 Teknik Resolusi Konflik IREB: 1. Agreement, 2. Compromise, 3. Voting, 4. Overruling, 5. Decision Matrix (Criteria-based evaluation).",
    "mnemonic": "Resolusi Konflik: Persetujuan, Kompromi, Undian, Overruling, Matriks Keputusan."
  },
  31: {
    "euNo": 4,
    "title": "Stakeholder Management: Key Attributes in a Stakeholder List",
    "correctDisplay": "A, D",
    "whyCorrect": "• A (Name and role in the project): Betul. Nama dan peranan projek adalah atribut asas untuk mengenal pasti tanggungjawab setiap individu.\n• D (Influence and interest with regard to the project): Betul. Tahap pengaruh (Influence/Power) dan kepentingan (Interest) menentukan strategi penglibatan stakeholder (Stakeholder Matrix).",
    "whyWrong": "• B (Salary) & C (Date of birth): Maklumat peribadi sensitif ini tidak berkaitan dengan pengurusan keperluan projek.",
    "extra": "Handbook Bab 4.1 / Syllabus EO 4.1.3: Atribut Stakeholder List: Nama, Peranan, Kepentingan (Interest), Pengaruh (Power), Ketersediaan, Saluran Komunikasi.",
    "mnemonic": "Senarai Stakeholder = Nama & Peranan + Tahap Pengaruh & Kepentingan (Power vs Interest)."
  },
  32: {
    "euNo": 4,
    "title": "Advantages of Questionnaires (Surveys) in Requirements Elicitation",
    "correctDisplay": "A, B",
    "whyCorrect": "• A (Questionnaires allow to elicit information from a large number of participants with little effort): Betul. Soal selidik boleh diedarkan kepada ratusan responden serentak secara kos efektif.\n• B (Questionnaires allow statistically valid evaluations): Betul. Jawapan kuantitatif daripada sampel besar membolehkan analisis statistik yang sah.",
    "whyWrong": "• C: Soal selidik tidak membolehkan pengesahan kefahaman secara dua hala.\n• D: Soal selidik sukar mencungkil delighters (faktor keterujaan).\n• E: Soal selidik tidak disesuaikan khusus untuk individu secara mendalam.",
    "extra": "Handbook Bab 4.2 / Syllabus EO 4.2.1: Gathering Techniques: Interview (Mendalam) vs Questionnaire (Meluas & Statistik).",
    "mnemonic": "Questionnaire / Soal Selidik = Skala Besar (Large Sample) + Analisis Statistik Sah."
  },
  33: {
    "euNo": 4,
    "title": "Classification of Elicitation Techniques (IREB Taxonomy)",
    "correctDisplay": "A=True, B=False, C=False, D=True",
    "whyCorrect": "• A: True. Temubual (Interview) tergolong dalam Gathering Techniques.\n• D: True. Perantisan (Apprenticing) tergolong dalam Observation Techniques (pemerhati belajar dan melakukan tugas pengguna sebenar).",
    "whyWrong": "• B: False. Analogy technique tergolong dalam Creativity Techniques (bukan gathering).\n• C: False. System Archeology tergolong dalam Artifact-based Techniques (bukan observation).",
    "extra": "Handbook Bab 4.2 / Syllabus EO 4.2.1: 4 Kategori Teknik Elisitasi IREB:\n1. Gathering (Interview, Questionnaire)\n2. Observation (Field Observation, Apprenticing)\n3. Creativity (Brainstorming, Analogy)\n4. Artifact-based (Document Analysis, System Archeology).",
    "mnemonic": "4 Kategori: Gathering (Tanya), Observation (Tengok), Creativity (Cipta), Artifact-based (Kaji Dokumen/Sistem Lama)."
  },
  34: {
    "euNo": 4,
    "title": "Conflict Types: Value Conflict vs Interest vs Structural",
    "correctDisplay": "D (Value conflict)",
    "whyCorrect": "• Pilihan D adalah jawapan yang betul. Percanggahan ini berpunca daripada perbezaan pegangan prinsip etika, persepsi diskriminasi jantina, dan nilai moral asas stakeholder (Value Conflict).",
    "whyWrong": "• A (Relationship conflict): Konflik interpersonal/emosi peribadi.\n• B (Interest conflict): Konflik pertembungan matlamat keuntungan/sumber.\n• C (Structural conflict): Konflik hirarki organisasi/kuasa.",
    "extra": "Handbook Bab 4.3 / Syllabus EO 4.3.1: Jenis Konflik: 1. Subject Matter Conflict, 2. Interest Conflict, 3. Value Conflict, 4. Relationship Conflict, 5. Structural Conflict.",
    "mnemonic": "Isu Etika / Diskriminasi / Moral = Value Conflict (Konflik Nilai)."
  },
  35: {
    "euNo": 4,
    "title": "Requirements Validation: Formal Inspection for Safety-Critical Systems",
    "correctDisplay": "D (Inspection)",
    "whyCorrect": "• Pilihan D adalah jawapan yang betul. Untuk komponen kritikal keselamatan tinggi (Safety-Critical seperti sistem brek kereta api berkelajuan tinggi), Inspection adalah teknik semakan yang paling formal, berdisiplin, dan berstruktur dengan peranan khusus (Moderator, Author, Inspector, Scribe) dan senarai semak peraturan yang ketat.",
    "whyWrong": "• A (A/B testing): Kaedah ujian pasaran perbandingan produk pengguna.\n• B (Prototype): Prototaip bagus untuk reka bentuk awal tetapi tidak mencukupi untuk semakan keselamatan kritikal tanpa formaliti.\n• C (Walkthrough): Sesi semakan tidak formal yang dipimpin oleh pengarang (kurang ketat berbanding Inspection).",
    "extra": "Handbook Bab 4.4 / Syllabus EO 4.4.2: Teknik Validasi: Inspection (Paling Formal & Ketat) > Walkthrough (Sederhana Formal) > Peer Review (Santai).",
    "mnemonic": "Safety-Critical (Keselamatan Nyawa) = Wajib Formal Inspection."
  },
  36: {
    "euNo": 5,
    "title": "Key Facets for Configuring an RE Process (Time & Purpose Facets)",
    "correctDisplay": "A, C",
    "whyCorrect": "• A (The time facet: linear vs. iterative): Betul. Time facet menentukan sama ada proses bergerak secara lurus (Waterfall/V-Model) atau berulang (Agile/Scrum).\n• C (The purpose facet: prescriptive vs. explorative): Betul. Purpose facet menentukan sama ada keperluan berfungsi sebagai kontrak tetap (Prescriptive) atau ruang penerokaan inovasi (Explorative).",
    "whyWrong": "• B, D, E bukan merupakan 3 Dimensi/Facet proses piawai yang diiktiraf dalam silibus IREB FL.",
    "extra": "Handbook Bab 5.1 / Syllabus EO 5.1.1: 3 Dimensi Proses RE IREB:\n1. Time Facet (Linear vs Iterative)\n2. Purpose Facet (Prescriptive vs Explorative)\n3. Target/Customer Facet (Customer-specific vs Market-driven).",
    "mnemonic": "Dua facet paling utama menentukan bentuk proses RE = Time Facet + Purpose Facet."
  },
  37: {
    "euNo": 5,
    "title": "Recognized RE Process Configurations in Practice",
    "correctDisplay": "B (Human-oriented RE process (linear, process-based, individual))",
    "whyCorrect": "• Pilihan B adalah jawapan yang betul (BUKAN konfigurasi proses yang diiktiraf). Istilah 'Human-oriented RE process' tidak wujud dalam taksonomi konfigurasi proses IREB.",
    "whyWrong": "• A (Product-oriented), C (Participatory), dan D (Contractual) merupakan 3 konfigurasi proses klasik yang diiktiraf secara rasmi dalam silibus IREB.",
    "extra": "Handbook Bab 5.2 / Syllabus EO 5.2.1: 3 Contoh Proses Tipikal IREB:\n1. Contractual RE Process (Linear, Prescriptive, Customer-specific)\n2. Product-oriented RE Process (Iterative, Explorative, Market-driven)\n3. Participatory RE Process (Iterative, Explorative, Customer-specific).",
    "mnemonic": "3 Proses Tipikal IREB: Contractual, Product-oriented, Participatory."
  },
  38: {
    "euNo": 6,
    "title": "Views on Requirements: Cognitive Load Reduction & Access Control",
    "correctDisplay": "A=True, B=True, C=True, D=False",
    "whyCorrect": "• A: True. Setiap stakeholder hanya perlu melihat pandangan yang relevan dengan tugas mereka.\n• B: True. Keperluan yang saling berkaitan boleh dihimpunkan dalam satu view untuk memudahkan semakan review.\n• C: True. Keperluan sensitif/rahsia boleh disembunyikan daripada capaian stakeholder yang tidak diberi kebenaran.",
    "whyWrong": "• D: False. Mencipta 'view' hanyalah penapisan data paparan; ia tidak menjamin sokongan konkurensi (penyuntingan serentak memerlukan mekanisme penguncian/version control sistem).",
    "extra": "Handbook Bab 6.1 / Syllabus EO 6.1.3: Views on Requirements: Mengurangkan beban kognitif pembaca dan mengawal hak capaian maklumat.",
    "mnemonic": "Views = Tapis maklumat mengikut peranan, kumpul untuk review, dan lindungi maklumat sulit."
  },
  39: {
    "euNo": 6,
    "title": "Goals and Benefits of Requirements Traceability (NOT a Goal)",
    "correctDisplay": "C (Traceability facilitates exports from a requirements management tool)",
    "whyCorrect": "• Pilihan C adalah jawapan yang betul (BUKAN matlamat utama kebolehkesanan). Mengeksport fail adalah ciri teknikal alatan perisian semata-mata, bukannya tujuan konseptual mengapa kebolehkesanan (traceability) diwujudkan.",
    "whyWrong": "• A (Impact analysis), B (Verification of implementation), dan D (Finding requirement source) kesemuanya merupakan matlamat teras kebolehkesanan (Pre-RS, Post-RS, Inter-RS Traceability).",
    "extra": "Handbook Bab 6.2 / Syllabus EO 6.2.1: Matlamat Traceability:\n1. Bukti pematuhan (Verification)\n2. Analisis impak perubahan (Impact Analysis)\n3. Mengetahui sumber asal (Pre-RS)\n4. Mengesan komponen hiliran (Post-RS).",
    "mnemonic": "Traceability = Bukti Pematuhan, Analisis Impak, dan Sumber Asal (Bukan untuk fungsi eksport fail)."
  },
  40: {
    "euNo": 6,
    "title": "Requirements Attributes: Purpose of Unique Identifiers (ID)",
    "correctDisplay": "A=False, B=True, C=True, D=True",
    "whyCorrect": "• B: True. Unique ID membolehkan asas komunikasi yang jelas tanpa kekeliruan.\n• C: True. Unique ID membolehkan rujukan silang antara keperluan yang berbeza.\n• D: True. Unique ID membolehkan pautan kebolehkesanan (traceability links) ke kod sumber, kes ujian, dan reka bentuk.",
    "whyWrong": "• A: False. Unique ID tidak digunakan untuk menganggar saiz keseluruhan spesifikasi (saiz diukur melalui metrik fungsi / function points / bilangan perkataan).",
    "extra": "Handbook Bab 6.1 / Syllabus EO 6.1.2: Atribut Keperluan Penting: Unique ID (Kekal seumur hidup projek), Status, Priority, Author, Verifier.",
    "mnemonic": "Unique ID = Asas Komunikasi, Rujukan Silang, dan Kebolehkesanan (Traceability)."
  },
  41: {
    "euNo": 6,
    "title": "Change Management for Requirements Baselines",
    "correctDisplay": "B, C",
    "whyCorrect": "• B (Prior to adjusting requirements, the impact of changes has to be determined): Betul. Sebelum sebarang perubahan diluluskan, analisis impak (Impact Analysis) terhadap kos, jadual, dan seni bina sistem WAJIB dinilai terlebih dahulu.\n• C (Change requests can be submitted at any time and considered when creating a future baseline): Betul. Permohonan perubahan boleh dikemukakan bila-bila masa dan akan diserap ke dalam **Future Baseline** yang seterusnya.",
    "whyWrong": "• A: Baseline yang telah diluluskan tidak boleh diubah secara terus dalam baseline sedia ada.\n• D: Permohonan kecemasan tetap memerlukan penilaian impak pantas.\n• E: Semua perubahan rasmi memerlukan kawalan baseline.",
    "extra": "Handbook Bab 6.3 / Syllabus EO 6.3.2: Baselines & Change Control: Analisis impak ➔ Keputusan CCB ➔ Masukkan ke Future Baseline.",
    "mnemonic": "Perubahan Baseline: Buat analisis impak dahulu, kemudian masukkan ke Future Baseline."
  },
  42: {
    "euNo": 6,
    "title": "Requirements Prioritization: Key Reasons and Purposes",
    "correctDisplay": "A=True, B=True, C=False, D=False",
    "whyCorrect": "• A: True. Menetapkan keutamaan menentukan keperluan mana yang perlu direalisasikan dalam keluaran (Release) yang terdekat.\n• B: True. Keutamaan membantu pasukan ujian memberi fokus kepada fungsi yang paling kritikal terlebih dahulu.",
    "whyWrong": "• C: False. Keutamaan BUKAN untuk mendokumentasikan kos (kos didokumentasikan dalam atribut 'Estimated Cost').\n• D: False. Keutamaan tidak menentukan kebolehgunaan semula (reusability).",
    "extra": "Handbook Bab 6.1 / Syllabus EO 6.1.4: Tujuan Prioritization: 1. Release Planning, 2. Focus of Implementation, 3. Focus of Testing.",
    "mnemonic": "Prioritization = Release Planning + Test Focus (Bukan untuk catat kos projek)."
  },
  43: {
    "euNo": 6,
    "title": "Requirements Baseline Definition and Concept",
    "correctDisplay": "C (A released configuration of requirements)",
    "whyCorrect": "• Pilihan C adalah takrifan tepat mengikut standard IREB. Baseline ialah satu konfigurasi keperluan yang stabil, telah disemak, diluluskan secara rasmi (released), dan ditandatangani untuk menjadi asas pembangunan seterusnya.",
    "whyWrong": "• A (A version of a requirement): Ini adalah versi individu, bukan baseline.\n• B (A released configuration of an individual requirement): Baseline merangkumi himpunan konfigurasi keseluruhan set keperluan yang konsisten.\n• D (A not yet released version): Baseline hanya wujud selepas dikeluarkan dan diluluskan secara rasmi.",
    "extra": "Handbook Bab 6.3 / Syllabus EO 6.3.1: Definisi Baseline: 'A released configuration of work products that is committed to by the stakeholders.'",
    "mnemonic": "Baseline = Himpunan Keperluan yang Diluluskan & Ditandatangani (Released Configuration)."
  },
  44: {
    "euNo": 7,
    "title": "Principles for RE Tool Selection and Toolchain Integration",
    "correctDisplay": "A=True, B=False, C=False, D=True",
    "whyCorrect": "• A: True. Alatan perisian mesti menyokong jenis Work Products dan proses RE yang diamalkan oleh organisasi.\n• D: True. Pemilihan alat sangat dipengaruhi oleh kesesuaian integrasi dengan rantai alatan sedia ada (Tool Chain seperti alatan pengurusan konfigurasi dan pengujian).",
    "whyWrong": "• B: False. Pemilihan alatan RE organisasi tidak boleh diserahkan semata-mata kepada citarasa individu tanpa strategi integrasi piawai.\n• C: False. Pembinaan kes ujian adalah peranan alat ujian (Testing Tools), bukan kriteria wajib alatan RE.",
    "extra": "Handbook Bab 7.1 / Syllabus EO 7.1.1: Prinsip Alatan RE: 1. Sokong proses organisasi, 2. Integrasi Toolchain, 3. Kira kos pemilikan penuh (TCO), 4. Jalankan projek perintis (Pilot Project).",
    "mnemonic": "Alat mesti sokong proses organisasi dan serasi dengan rantai alatan (Tool Chain)."
  },
  45: {
    "euNo": 7,
    "title": "Core Application and Capabilities of RE Tools (NOT a Management Capability)",
    "correctDisplay": "B (Modelling of requirements)",
    "whyCorrect": "• Pilihan B adalah jawapan yang betul. 'Modelling of requirements' (seperti melukis Use Case atau State Machine) adalah keupayaan alat pemodelan konseptual (Modeling Tools), bukannya tugas teras alatan Pengurusan Keperluan (Requirements Management Tools).",
    "whyWrong": "• A (Tracking logical relationships / Traceability), C (Measuring and reporting), dan D (Providing support for prioritization) kesemuanya merupakan keupayaan teras alatan Requirements Management.",
    "extra": "Handbook Bab 7.2 / Syllabus EO 7.2.1: Perbezaan Kategori Alatan:\n1. Requirements Management Tools (Attributes, Traceability, Views, Prioritization, Reporting)\n2. Requirements Modeling Tools (UML, SysML, BPMN diagrams).",
    "mnemonic": "Management Tools = Atribut, Traceability, Status. Modeling Tools = Lukis Rajah Model."
  }
}

with open(os.path.join(ROOT_DIR, 'scripts', 'scratch', 'questions_authentic_base.json'), 'r', encoding='utf-8') as f:
    raw_questions = json.load(f)

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
    
    # Clean options
    clean_opts = []
    for opt in q['options']:
        clean_opts.append({
            "id": opt['id'],
            "text": clean_pdf_artifacts(opt['text']),
            "truth": opt.get('truth')
        })
    
    # Get beautifully formatted stem
    stem = formatted_stems.get(qid, clean_pdf_artifacts(q['stem']))
    
    questions_final.append({
        "id": qid,
        "code": q['code'],
        "type": q['type'],
        "pts": q['pts'],
        "eo": q['eo'],
        "euNo": meta.get('euNo', 1),
        "title": meta.get('title', f"Question {qid}"),
        "question": stem,
        "options": clean_opts,
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
