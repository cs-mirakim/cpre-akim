import json
import base64
import os
import copy

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(ROOT_DIR, 'assets', 'diagrams')
DATA_PATH = os.path.join(ROOT_DIR, 'data', 'app_data.json')

def get_b64(filename):
    path = os.path.join(ASSETS_DIR, filename)
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"
    return ""

img_vessel = get_b64('predicted_vessel_statemachine.png')
img_q18 = get_b64('predicted_q18_class.png')
img_q21 = get_b64('predicted_q21_activity.png')
img_q23 = get_b64('predicted_q23_activity.png')

with open(DATA_PATH, 'r', encoding='utf-8') as f:
    app_data = json.load(f)

# Start with a copy of predicted set G
base_g = copy.deepcopy(app_data['sets']['predicted']['questions'])
maritime_map = {q['id']: copy.deepcopy(q) for q in base_g}

# ==============================================================================
# UPGRADED HIGH-YIELD AUTHENTIC EXAM QUESTIONS (COMMUNITY / FORUM DEBRIEFS)
# ==============================================================================

# --- EU1: Fundamentals of RE ---
maritime_map[1] = {
    "id": 1,
    "code": "GM0101",
    "type": "K",
    "pts": 2.0,
    "eo": "1.1.2",
    "euNo": 1,
    "title": "Categorization of Requirements: Functional, Quality, and Constraints",
    "question": "A requirements engineer in a mission-critical logistics system receives various stakeholder statements. Which of the following classifications are true and which are false according to IREB definitions?",
    "options": [
        { "id": "A", "text": "'The system shall encrypt all maritime positioning telematics using AES-256-GCM' is a technical constraint.", "truth": True },
        { "id": "B", "text": "'The port dispatcher shall be able to filter arriving vessels by gross tonnage' is a functional requirement.", "truth": True },
        { "id": "C", "text": "'The database backup routine must execute daily at 03:00 AM UTC' is a quality requirement regarding usability.", "truth": False },
        { "id": "D", "text": "'The telemetry telemetry dashboard shall render updated radar coordinates within 800 milliseconds' is a quality requirement regarding performance efficiency.", "truth": True }
    ],
    "correctDisplay": "A=True, B=True, C=False, D=True",
    "whyCorrect": "• A: True. Spesifikasi algoritma enkripsi tertentu (AES-256) mengehadkan kebebasan reka bentuk arkitek, menjadikannya Technical Constraint.\n• B: True. Keupayaan menapis kapal berdasarkan tan adalah tingkah laku/fungsi sistem (Functional Requirement).\n• D: True. Had masa respons (< 800ms) ialah keperluan kualiti prestasi (Quality Requirement: Performance Efficiency).",
    "whyWrong": "• C: False. Arahan jadual sandaran harian pada jam 03:00 AM ialah Operational Constraint, bukan keperluan kualiti kebolehgunaan (Usability).",
    "extra": "Handbook Bab 1.1: 3 Kategori Keperluan IREB: Functional Requirements, Quality Requirements, dan Constraints (Organizational & Technical).",
    "mnemonic": "Constraint = Menghadkan kebebasan solusi. Functional = Apa sistem buat. Quality = Sejauh mana sistem berfungsi dengan baik."
}

# --- EU2: Context & Boundaries ---
maritime_map[6] = {
    "id": 6,
    "code": "GM0203",
    "type": "K",
    "pts": 2.0,
    "eo": "2.2.1",
    "euNo": 2,
    "title": "System Boundary, Context Boundary, and the Grey Zone",
    "question": "During the scoping of a harbor vessel traffic service, the boundaries of the system under development must be determined. Which of the following statements regarding boundaries and the grey zone are true and which are false?",
    "options": [
        { "id": "A", "text": "The system boundary separates what will be designed and implemented inside the software from the operational environment.", "truth": True },
        { "id": "B", "text": "The context boundary delineates the relevant operational context from the irrelevant environment that has no impact on requirements.", "truth": True },
        { "id": "C", "text": "The grey zone consists of aspects where the requirements engineer has conclusively confirmed that no stakeholder cares about them.", "truth": False },
        { "id": "D", "text": "Aspects situated within the grey zone must be clarified during requirements analysis so they are assigned either inside the system, into the context, or into the irrelevant environment.", "truth": True }
    ],
    "correctDisplay": "A=True, B=True, C=False, D=True",
    "whyCorrect": "• A: True. System boundary menetapkan sempadan apa yang dibina dalam perisian berbanding dunia luar.\n• B: True. Context boundary memisahkan persekitaran yang relevan daripada persekitaran yang tidak relevan (irrelevant environment).\n• D: True. Zon kelabu (grey zone) wajib diselesaikan semasa analisis supaya setiap aspek jelas lokasinya.",
    "whyWrong": "• C: False. Zon kelabu bukan perkara yang diabaikan, tetapi perkara yang belum diputuskan sama ada ia termasuk dalam skop sistem atau di luar.",
    "extra": "Handbook Bab 2.2: Sempadan sistem sentiasa boleh beralih semasa proses elisitasi.",
    "mnemonic": "System Boundary: Skop binaan. Context Boundary: Relevan vs Tak Relevan. Grey Zone: Belum diputuskan."
}

# --- EU3: Work Products & SOPHIST ---
maritime_map[13] = {
    "id": 13,
    "code": "GM0306",
    "type": "K",
    "pts": 2.0,
    "eo": "3.3.1",
    "euNo": 3,
    "title": "Quality Criteria for Individual Requirements (IREB Standard)",
    "question": "An engineering team reviews textual requirements specifications for compliance with IREB quality criteria. Which of the following statements regarding criteria for individual requirements are true and which are false?",
    "options": [
        { "id": "A", "text": "A requirement is 'Verifiable' if a practical test or inspection procedure can be devised to prove whether the requirement has been met.", "truth": True },
        { "id": "B", "text": "A requirement is 'Unambiguous' only if it is expressed purely in formal mathematical logic and contains no natural language.", "truth": False },
        { "id": "C", "text": "A requirement is 'Traceable' if it can be tracked back to its originating stakeholder rationale and forward to its design and verification artifacts.", "truth": True },
        { "id": "D", "text": "A requirement containing the phrase 'The system should be as fast as reasonably possible' violates the verifiability criterion.", "truth": True }
    ],
    "correctDisplay": "A=True, B=False, C=True, D=True",
    "whyCorrect": "• A: True. Verifiable bermaksud ada cara praktikal (ujian/semakan) untuk mengesahkan pematuhan.\n• C: True. Traceable membolehkan jejak ke punca asal (backward) dan ke artifak hiliran (forward).\n• D: True. Frasa kabur 'as fast as reasonably possible' tidak boleh diuji secara objektif.",
    "whyWrong": "• B: False. Unambiguous bermaksud hanya mempunyai satu tafsiran sahaja; ia tidak mewajibkan penggunaan logik matematik formal semata-mata.",
    "extra": "Handbook Bab 3.3: Kriteria kualiti individu: Complete, Consistent, Unambiguous, Verifiable, Modifiable, Traceable.",
    "mnemonic": "Kualiti Keperluan: Jelas (Unambiguous), Boleh Diuji (Verifiable), Boleh Dijejak (Traceable)."
}

maritime_map[14] = {
    "id": 14,
    "code": "GM0307",
    "type": "P",
    "pts": 2.0,
    "eo": "3.3.3",
    "euNo": 3,
    "title": "SOPHIST Requirements Phrase Templates and Legal Modals",
    "question": "You are formulating natural language requirements using the SOPHIST sentence template. Which TWO (2) of the following statements are correct regarding template construction and modal verb selection? (Select 2 answers)",
    "options": [
        { "id": "A", "text": "The modal verb 'shall' indicates a strictly mandatory requirement with full legal binding commitment.", "truth": True },
        { "id": "B", "text": "The modal verb 'should' indicates a desirable or future goal that carries no legal necessity under contract.", "truth": True },
        { "id": "C", "text": "Passive voice constructions ('The vessel manifest shall be exported') are recommended by SOPHIST because they keep sentences concise.", "truth": False },
        { "id": "D", "text": "The modal verb 'will' represents the highest level of legal necessity in IREB contractual requirements specifications.", "truth": False }
    ],
    "correctDisplay": "A, B",
    "whyCorrect": "• A: Betul. 'Shall' menetapkan kewajipan mutlak mengikat (mandatory/legally binding).\n• B: Betul. 'Should' menunjukkan cadangan atau matlamat masa hadapan yang wajar dilaksanakan tetapi tidak membawa liabiliti mutlak.",
    "whyWrong": "• C: Salah. Ayat pasif dilarang dalam SOPHIST kerana ia menyembunyikan pelaku/ejen (siapa yang mengeksport manifest?).\n• D: Salah. 'Will' hanya menyatakan niat masa depan atau penerangan maklumat (bukan tahap perundangan tertinggi; 'shall' yang tertinggi).",
    "extra": "Handbook Bab 3.3.3: Struktur SOPHIST: [Syarat] + <Sistem> + <shall/should/will> + [Aktiviti] + [Objek].",
    "mnemonic": "SHALL = Wajib undang-undang. SHOULD = Cadangan kuat. PASSIVE = Perangkap bahaya (hilang pelaku)."
}

maritime_map[15] = {
    "id": 15,
    "code": "GM0308",
    "type": "A",
    "pts": 1.0,
    "eo": "3.3.2",
    "euNo": 3,
    "title": "Natural Language Transformation Defects: Nominalization",
    "question": "A specification contains the sentence: 'The authentication of port operators occurs before access to berth allocation data is granted.'\n\nWhich natural language defect is prominently present in this requirement, and why is it problematic according to IREB? (Select 1 answer)",
    "options": [
        { "id": "A", "text": "Nominalization (converting a process verb into a noun 'authentication'), which obscures the executing actor and procedural sequence.", "truth": True },
        { "id": "B", "text": "Universal quantifier ('all port operators'), which leads to unfulfillable blanket commitments.", "truth": False },
        { "id": "C", "text": "Synonym collision between 'port operators' and 'berth allocators'.", "truth": False },
        { "id": "D", "text": "Structural grammar inversion between subordinate and main clauses.", "truth": False }
    ],
    "correctDisplay": "A",
    "whyCorrect": "• A: Betul. 'Authentication' adalah nominalisasi (kata kerja 'authenticate' dijadikan kata nama). Ini menyembunyikan siapa yang mengesahkan, bagaimana pengesahan berlaku, dan apa akibat jika gagal.",
    "whyWrong": "• B: Salah. Tiada penggunaan universal quantifier ('all', 'always', 'never') yang mencetuskan komitmen mutlak tanpa had dalam ayat ini.\n• C: Salah. Tiada pertembungan atau percanggahan sinonim (synonym collision) antara dua istilah berbeza yang merujuk konsep yang sama.\n• D: Salah. Ayat ini tidak mengalami penyongsangan struktur tatabahasa (structural grammar inversion) antara klausa utama dan klausa bawahan.",
    "extra": "Handbook Bab 3.3.2: 4 Kesan Transformasi Bahasa: Deletion, Nominalization, Generalization, Distortion.",
    "mnemonic": "Nominalization = Kata kerja jadi kata nama. Ia menyorokkan siapa pembuat dan bagaimana proses berlaku."
}

# Question 18, 20, 21, 23 Diagrams are preserved with diagrams
maritime_map[20] = {
    "id": 20,
    "code": "GM0313",
    "type": "K",
    "pts": 2.0,
    "eo": "3.4.5",
    "euNo": 3,
    "title": "UML State Machine: Container Vessel Navigation & Harbor Clearance",
    "question": "The following UML state machine diagram specifies the operational lifecycle of a commercial container vessel navigating to an international port:\n\nWhich of the following statements are true and which are false based on this diagram?",
    "diagramHtml": f'<div class="diagram-wrapper"><img src="{img_vessel}" alt="UML State Machine Container Vessel" class="diagram-img" /></div>',
    "options": [
        { "id": "A", "text": "A vessel can transition from 'At Sea' directly to 'Entering Harbor' without waiting at anchorage if the berth is not busy.", "truth": True },
        { "id": "B", "text": "If a storm warning with wind > 40 knots occurs while entering the harbor, the vessel returns to 'Waiting at Anchorage'.", "truth": True },
        { "id": "C", "text": "A vessel can transition directly from 'At Sea' to 'Cargo Operations' in a single step.", "truth": False },
        { "id": "D", "text": "'Moored at Berth' and 'Cargo Operations' are executed concurrently as parallel states in this diagram.", "truth": False }
    ],
    "correctDisplay": "A=True, B=True, C=False, D=False",
    "whyCorrect": "• A: True. Terdapat transisi 'approach_port [berth_busy == false]' yang membenarkan kapal masuk terus ke fasa 'Entering Harbor' tanpa perlu berlabuh sauh.\n• B: True. Transisi kecemasan 'storm_warning [wind > 40kn]' mengarahkan kapal yang sedang memasuki alur pelabuhan kembali berlabuh selamat di 'Waiting at Anchorage'.",
    "whyWrong": "• C: False. Tiada anak panah terus dari 'At Sea' ke 'Cargo Operations'; kapal wajib merapat di dermaga (Moored at Berth) terlebih dahulu.\n• D: False. Kedua-dua keadaan ini berlaku secara berurutan (sequential), bukan serentak (tiada garis putus-putus atau composite orthogonal states).",
    "extra": "Handbook Bab 3.4.5: State Machine Diagram memodelkan kitaran hayat tingkah laku objek dinamik berdasarkan Events, Guard Conditions [syarat], dan Actions /tindakan.",
    "mnemonic": "State Machine Kapal: Semak Guard [syarat] & arah anak panah. Masuk pelabuhan wajib ikut urutan selamat."
}

# --- EU4: Elicitation & Conflict Resolution ---
maritime_map[24] = {
    "id": 24,
    "code": "GM0401",
    "type": "A",
    "pts": 1.0,
    "eo": "4.1.2",
    "euNo": 4,
    "title": "Eliciting Tacit and Implicit Knowledge from Operational Experts",
    "question": "In a maritime terminal control center, experienced harbor pilots make rapid split-second navigation decisions that they find difficult to articulate or explain verbally in meeting rooms.\n\nWhich elicitation technique is the MOST effective to uncover this tacit knowledge? (Select 1 answer)",
    "options": [
        { "id": "A", "text": "Field Observation / Apprenticeship (observing the pilots on-site while they execute real-time vessel guidance).", "truth": True },
        { "id": "B", "text": "Distributing a standardized multiple-choice questionnaire via email.", "truth": False },
        { "id": "C", "text": "Conducting a formal structured interview in an off-site conference room.", "truth": False },
        { "id": "D", "text": "Performing keyword frequency analysis on archived terminal log reports.", "truth": False }
    ],
    "correctDisplay": "A",
    "whyCorrect": "• A: Betul. Pengetahuan tersirat (tacit knowledge) tidak dapat dijelaskan secara lisan dalam temu bual. Kaedah Pemerhatian Lapangan (Field Observation / Apprenticeship) adalah satu-satunya teknik yang membolehkan jurutera keperluan melihat tindakan sebenar pakar dalam konteks kerja sebenar.",
    "whyWrong": "• B: Salah. Soal selidik aneka pilihan bertulis (questionnaires) tidak mampu menangkap pengetahuan tersirat (tacit knowledge) dan nuansa keputusan spontan jurumudi pelabuhan.\n• C: Salah. Temu bual formal di bilik mesyuarat di luar lokasi bergantung kepada keupayaan pakar untuk menyatakan proses secara lisan dan sedar (explicit knowledge sahaja), tanpa konteks real-time.\n• D: Salah. Analisis kekerapan kata kunci log arkib terminal hanya membaca ringkasan data komputer yang telah lepas, bukan proses penaakulan dan kemahiran sebenar pakar.",
    "extra": "Handbook Bab 4.1.2: Jenis pengetahuan: Explicit, Tacit (tersirat), Unconscious.",
    "mnemonic": "Tacit Knowledge = Susah cakap, senang buat. Kena tengok secara langsung (Observation/Apprenticeship)."
}

maritime_map[26] = {
    "id": 26,
    "code": "GM0403",
    "type": "A",
    "pts": 1.0,
    "eo": "4.1.3",
    "euNo": 4,
    "title": "Kano Model: Temporal Migration of Delighters into Basic Factors",
    "question": "According to Noriaki Kano's model of customer satisfaction, how does the classification of product characteristics typically evolve over time as market adoption matures? (Select 1 answer)",
    "options": [
        { "id": "A", "text": "Excitement factors (Delighters) gradually transition into Performance factors and eventually become Basic factors (Must-be).", "truth": True },
        { "id": "B", "text": "Basic factors migrate into Delighters as customers appreciate their enduring reliability.", "truth": False },
        { "id": "C", "text": "Reverse factors spontaneously convert into One-dimensional Performance factors without user redesign.", "truth": False },
        { "id": "D", "text": "Classifications remain completely static throughout the entire product lifecycle.", "truth": False }
    ],
    "correctDisplay": "A",
    "whyCorrect": "• A: Betul. Mengikut Model Kano, ciri yang asalnya 'Delighter' (mengujakan pengguna kerana ia baharu) akan menjadi kebiasaan lama-kelamaan, bertukar menjadi faktor prestasi, dan akhirnya menjadi faktor asas (Must-be) yang wajib ada.",
    "whyWrong": "• B: Salah. Faktor asas (Must-be) tidak pernah bermigrasi menjadi faktor keterujaan (Delighters) kerana pelanggan sentiasa menganggapnya sebagai perkara asas yang wajib ada secara lumrah.\n• C: Salah. Faktor terbalik (Reverse factors) yang menyebabkan rasa jengkel tidak bertukar sendiri menjadi faktor prestasi satu dimensi tanpa reka bentuk semula.\n• D: Salah. Klasifikasi faktor dalam Model Kano tidak kekal statik sepanjang hayat produk; jangkaan pelanggan sentiasa meningkat mengikut peredaran masa (kesan pembiasaan / habituation).",
    "extra": "Handbook Bab 4.1.3: Contoh: Wi-Fi percuma di hotel dulunya Delighter, kini menjadi Basic Factor (Must-be).",
    "mnemonic": "Evolusi Kano: Delighter ➔ Performance ➔ Must-be. Jangkaan pengguna sentiasa naik."
}

maritime_map[28] = {
    "id": 28,
    "code": "GM0405",
    "type": "A",
    "pts": 1.0,
    "eo": "4.2.2",
    "euNo": 4,
    "title": "Legitimate Conflict Resolution Techniques in Requirements Engineering",
    "question": "During a requirements negotiation workshop, two key department heads hold conflicting objectives regarding vessel scheduling automation. Which of the following is NOT recognized by IREB as a constructive conflict resolution technique? (Select 1 answer)",
    "options": [
        { "id": "A", "text": "Unilateral avoidance / Disregard (deliberately omitting the contested requirement from the backlog without informing stakeholders).", "truth": True },
        { "id": "B", "text": "Consensus building through moderated stakeholder dialogue.", "truth": False },
        { "id": "C", "text": "Compromise (each party concedes certain parameters to establish an acceptable middle ground).", "truth": False },
        { "id": "D", "text": "Hierarchical Escalation (referring the conflict to an authorized governance board or steering committee).", "truth": False }
    ],
    "correctDisplay": "A",
    "whyCorrect": "• A: Betul (ia BUKAN teknik sah). Mengelak atau membuang keperluan secara senyap tanpa persetujuan pihak berkepentingan (Avoidance/Disregard) bukanlah penyelesaian konflik yang sah, malah akan mengundang kegagalan projek.",
    "whyWrong": "• B: Salah (ia adalah teknik resolusi konflik yang sah). Pembinaan konsensus melalui dialog berpandu bersama pihak berkepentingan adalah pendekatan kolaboratif yang diiktiraf IREB.\n• C: Salah (ia adalah teknik resolusi konflik yang sah). Kompromi membolehkan setiap pihak bertolak ansur untuk mencapai penyelesaian titik tengah yang boleh diterima bersama.\n• D: Salah (ia adalah teknik resolusi konflik yang sah). Eskalasi hierarki (Hierarchical Escalation) merujuk keputusan konflik kepada badan tadbir urus atau pihak atasan yang diberi kuasa membuat keputusan pemutus.",
    "extra": "Handbook Bab 4.2.2: 5 Teknik Resolusi Konflik: Agreement, Compromise, Voting, Overruling/Escalation, Variance creation.",
    "mnemonic": "Elak konflik senyap-senyap = Gagal. Selesaikan dengan Konsensus, Kompromi, Undian, atau Eskalasi."
}

maritime_map[31] = {
    "id": 31,
    "code": "GM0408",
    "type": "A",
    "pts": 1.0,
    "eo": "4.2.1",
    "euNo": 4,
    "title": "Classification of Requirements Conflict Types",
    "question": "The safety auditor insists on 100% manual confirmation for each container crane movement, while the operational logistics manager demands full automation to maximize throughput. Both agree on the terminal data and technical facts, but prioritize conflicting organizational goals.\n\nWhich type of conflict is this according to IREB? (Select 1 answer)",
    "options": [
        { "id": "A", "text": "Interest Conflict (divergent individual or departmental goals and objectives).", "truth": True },
        { "id": "B", "text": "Data / Subject-matter Conflict (differing information or interpretation of facts).", "truth": False },
        { "id": "C", "text": "Structural Conflict (power imbalances caused by hierarchical reporting lines).", "truth": False },
        { "id": "D", "text": "Relationship Conflict (interpersonal animosity and negative emotional friction).", "truth": False }
    ],
    "correctDisplay": "A",
    "whyCorrect": "• A: Betul. Pihak-pihak bersetuju tentang data teknikal, tetapi mempunyai matlamat dan keutamaan yang bercanggah (Keselamatan vs Kepantasan Operasi). Ini ialah Takrifan tepat untuk Konflik Kepentingan (Interest Conflict).",
    "whyWrong": "• B: Salah. Konflik Data/Subjek berlaku apabila terdapat percanggahan maklumat, fakta, atau tafsiran data teknikal (dalam senario ini kedua-dua pihak bersetuju tentang data teknikal).\n• C: Salah. Konflik Struktur berpunca daripada ketidakseimbangan kuasa hierarki, birokrasi, atau kekangan sumber organisasi.\n• D: Salah. Konflik Hubungan berpunca daripada ketegangan interpersonal, permusuhan emosi, atau prasangka peribadi antara individu.",
    "extra": "Handbook Bab 4.2.1: Jenis Konflik: Subject-matter, Interest, Value, Relationship, Structural.",
    "mnemonic": "Bercanggah matlamat/kepentingan = Interest Conflict. Bercanggah fakta/maklumat = Data Conflict."
}

maritime_map[33] = {
    "id": 33,
    "code": "GM0410",
    "type": "A",
    "pts": 2.0,
    "eo": "4.3.2",
    "euNo": 4,
    "title": "Formal Inspection Roles according to Fagan",
    "question": "A safety-critical automated navigation module undergoes a formal requirements inspection. In Michael Fagan's inspection methodology, who is responsible for leading the meeting, ensuring adherence to the process rules, and maintaining objective focus? (Select 1 answer)",
    "options": [
        { "id": "A", "text": "The Moderator", "truth": True },
        { "id": "B", "text": "The Author", "truth": False },
        { "id": "C", "text": "The Scribe (Recorder)", "truth": False },
        { "id": "D", "text": "The Lead Architect", "truth": False }
    ],
    "correctDisplay": "A",
    "whyCorrect": "• A: Betul. Moderator ialah individu yang bertanggungjawab menguruskan proses semakan, memimpin mesyuarat, memastikan peraturan dipatuhi, dan mengawal dinamik perbincangan secara objektif.",
    "whyWrong": "• B: Salah. Penulis (Author) tidak boleh memoderasi mesyuarat sendiri bagi mengelakkan bias.\n• C: Salah. Pencatat (Scribe) mencatat kecacatan/isu yang ditemui.\n• D: Salah. Arkitek bertindak sebagai Reviewer/Inspector.",
    "extra": "Handbook Bab 4.3.2: 4 Peranan Utama Fagan Inspection: Moderator, Author, Reviewer/Inspector, Scribe.",
    "mnemonic": "Moderator = Ketua Proses. Author = Pencipta dokumen. Scribe = Tukang catat kecacatan."
}

# --- EU5: Process Configuration (Q35 already updated, Q36 enhanced) ---
maritime_map[35] = {
    "id": 35,
    "code": "GM0501",
    "type": "K",
    "pts": 2.0,
    "eo": "5.2.1",
    "euNo": 5,
    "title": "RE Process Facets: Configuring Working Structure for Maritime Systems",
    "question": "An engineering firm is designing an automated ship traffic management system. The team needs to configure an appropriate Requirements Engineering process. Which of the following statements regarding RE process facets are true and which are false?",
    "options": [
        { "id": "A", "text": "Safety-critical sub-systems (such as collision avoidance radar) mandate a more prescriptive and rigorously validated documentation process.", "truth": True },
        { "id": "B", "text": "An exploratory RE process is selected when requirements and stakeholder operational goals are completely fixed and legally binding before project kickoff.", "truth": False },
        { "id": "C", "text": "In a customer-specific project setting, requirements are primarily elicited from designated customer representatives rather than broad market surveys.", "truth": True },
        { "id": "D", "text": "The time facet (linear vs iterative) dictates whether requirements are defined upfront in one pass or evolved continuously across increments.", "truth": True }
    ],
    "correctDisplay": "A=True, B=False, C=True, D=True",
    "whyCorrect": "• A: True. Sistem keselamatan tinggi (Safety-Critical) memerlukan dokumentasi preskriptif dan validasi ketat (seperti Inspection).\n• C: True. Projek khusus pelanggan (Customer-specific) berurusan terus dengan wakil pelanggan yang dikenal pasti.\n• D: True. Time facet menentukan kaedah masa: Linear (sekali harung) atau Iterative (berulang mengikut kitaran).",
    "whyWrong": "• B: False. Exploratory process dipilih apabila keperluan masih kabur atau inovatif. Jika keperluan telah tetap dan mengikat, prescriptive process yang digunakan.",
    "extra": "Handbook Bab 5.2: 4 Facets proses RE mengikut IREB: Time, Purpose, Target, Interaction.",
    "mnemonic": "Safety-Critical = Prescriptive & Formal. Inovasi/Kabur = Explorative."
}

maritime_map[36] = {
    "id": 36,
    "code": "GM0502",
    "type": "P",
    "pts": 2.0,
    "eo": "5.1.2",
    "euNo": 5,
    "title": "The Four Process Facets of Requirements Engineering (IREB Standard)",
    "question": "IREB characterizes Requirements Engineering processes along four orthogonal dimensions (facets). Which TWO (2) of the following represent recognized IREB process facets? (Select 2 answers)",
    "options": [
        { "id": "A", "text": "Time Facet (Linear vs. Iterative)", "truth": True },
        { "id": "B", "text": "Purpose Facet (Prescriptive vs. Explorative)", "truth": True },
        { "id": "C", "text": "Budget Facet (Fixed-Price vs. Time-and-Materials)", "truth": False },
        { "id": "D", "text": "Architecture Facet (Monolithic vs. Microservices)", "truth": False }
    ],
    "correctDisplay": "A, B",
    "whyCorrect": "• A: Betul. Time Facet membahagikan proses kepada Linear (sekali harung / Waterfall) atau Iterative (berperingkat / Agile).\n• B: Betul. Purpose Facet membahagikan proses kepada Prescriptive (spesifikasi kontrak terperinci) atau Explorative (penerokaan keperluan inovatif).",
    "whyWrong": "• C: Salah. Faset Belanjawan (Budget: Fixed-Price vs Time-and-Materials) adalah model komersial kewangan/kontrak perniagaan, bukan salah satu daripada 4 faset proses RE piawai IREB (Time, Purpose, Target, Interaction).\n• D: Salah. Faset Seni Bina (Architecture: Monolithic vs Microservices) adalah corak reka bentuk teknologi seni bina perisian, bukan faset konfigurasi proses RE IREB.",
    "extra": "Handbook Bab 5.1: 4 Faset Proses RE: Time (Linear/Iterative), Purpose (Prescriptive/Explorative), Target (Customer-specific/Market-driven), Interaction (Close/Distant).",
    "mnemonic": "4 Faset RE: TIME, PURPOSE, TARGET, INTERACTION (T-P-T-I)."
}

# --- EU6: Traceability & Management ---
maritime_map[39] = {
    "id": 39,
    "code": "GM0602",
    "type": "A",
    "pts": 1.0,
    "eo": "6.2.1",
    "euNo": 6,
    "title": "Pre-RS Traceability vs Post-RS Traceability",
    "question": "A maritime software vendor must demonstrate traceability across the lifecycle. Which of the following correctly describes 'Pre-RS Traceability' according to IREB? (Select 1 answer)",
    "options": [
        { "id": "A", "text": "Tracing a requirement backward to the stakeholder statement, business goal, or regulatory standard that originated it.", "truth": True },
        { "id": "B", "text": "Tracing a requirement forward to the source code classes and automated regression test scripts.", "truth": False },
        { "id": "C", "text": "Tracing dependencies exclusively between requirements within the same specification document.", "truth": False },
        { "id": "D", "text": "Tracing historical defect tickets recorded during user acceptance testing.", "truth": False }
    ],
    "correctDisplay": "A",
    "whyCorrect": "• A: Betul. Pre-RS (Pre-Requirements Specification) Traceability membolehkan keperluan dijejak kembali ke asal-usul kelahirannya (stakeholder, mesyuarat, peraturan undang-undang).",
    "whyWrong": "• B: Salah. Menjejak keperluan ke hadapan ke kelas kod sumber dan skrip ujian regresi automatik adalah takrifan bagi Post-RS Traceability.\n• C: Salah. Menjejak hubungan kebergantungan sesama keperluan dalam dokumen spesifikasi yang sama merujuk kepada Inter-Requirements Traceability.\n• D: Salah. Menjejak tiket kecacatan ujian penerimaan pengguna (UAT defect tickets) adalah pengurusan jejak kecacatan (defect traceability), bukan Pre-RS traceability.",
    "extra": "Handbook Bab 6.2: Pre-RS = Sebelum keperluan ditulis (punca asal). Post-RS = Selepas keperluan ditulis (seni bina, kod, ujian).",
    "mnemonic": "Pre-RS = Jejak ke belakang (Punca/Stakeholder). Post-RS = Jejak ke depan (Kod/Ujian)."
}

maritime_map[41] = {
    "id": 41,
    "code": "GM0604",
    "type": "P",
    "pts": 2.0,
    "eo": "6.4.1",
    "euNo": 6,
    "title": "Change Control Board (CCB) and Impact Analysis Workflow",
    "question": "A major customer requests a change to the automated harbor docking sequence during mid-development. Which TWO (2) of the following activities are standard steps in the formal Change Management workflow? (Select 2 answers)",
    "options": [
        { "id": "A", "text": "Conducting an Impact Analysis to evaluate technical effort, budget variance, and ripple effects across existing requirements.", "truth": True },
        { "id": "B", "text": "Submitting the change request and impact evaluation to the Change Control Board (CCB) for formal approval or rejection.", "truth": True },
        { "id": "C", "text": "Immediately altering source code repositories before documenting the change request to maximize delivery speed.", "truth": False },
        { "id": "D", "text": "Discarding previously approved test cases without creating an updated baseline.", "truth": False }
    ],
    "correctDisplay": "A, B",
    "whyCorrect": "• A: Betul. Analisis Impak wajib dijalankan terlebih dahulu untuk melihat kesan perubahan terhadap kos, jadual, dan komponen lain.\n• B: Betul. Lembaga Kawalan Perubahan (CCB) adalah badan berwibawa yang membuat keputusan meluluskan, menolak, atau menangguhkan permohonan perubahan.",
    "whyWrong": "• C: Salah. Mengubah kod secara terus tanpa kelulusan formal (uncontrolled change) memusnahkan integriti kebolehkesanan.\n• D: Salah. Menghapuskan kes ujian tanpa rekod melanggar tatakelola RE.",
    "extra": "Handbook Bab 6.4: Aliran Perubahan: Request ➔ Impact Analysis ➔ CCB Decision ➔ Update Baseline.",
    "mnemonic": "Change Management: Request ➔ Analisis Impak ➔ Kelulusan CCB ➔ Kemas kini Baseline."
}

maritime_map[42] = {
    "id": 42,
    "code": "GM0605",
    "type": "K",
    "pts": 2.0,
    "eo": "6.8.1",
    "euNo": 6,
    "title": "Multi-Criteria Prioritization Techniques in Complex Systems",
    "question": "Prioritizing requirements is essential when project resources, time, and budget cannot accommodate all requirements. Which of the following statements regarding prioritization techniques are true and which are false?",
    "options": [
        { "id": "A", "text": "The Analytic Hierarchy Process (AHP) evaluates requirements by performing systematic pairwise comparisons across defined criteria.", "truth": True },
        { "id": "B", "text": "In Wiegers' method, the priority score increases when the estimated implementation cost and technical risk of a requirement increase.", "truth": False },
        { "id": "C", "text": "MoSCoW categorization (Must, Should, Could, Won't) is an example of an absolute, single-criterion ranking technique.", "truth": True },
        { "id": "D", "text": "Prioritization should only consider business value to the customer, completely ignoring regulatory penalties and implementation risks.", "truth": False }
    ],
    "correctDisplay": "A=True, B=False, C=True, D=False",
    "whyCorrect": "• A: True. AHP menggunakan perbandingan berpasangan (pairwise comparison) yang sangat matematik dan berstruktur.\n• C: True. MoSCoW membahagikan keperluan kepada 4 bakul keutamaan mutlak mengikut tahap kepentingan segera.",
    "whyWrong": "• B: False. Dalam formula Wiegers: Priority = Value% / (Cost% + Risk%). Kos dan risiko berada di bahagian pembahagi (denominator); jika kos/risiko tinggi, keutamaan akan MENURUN, bukan meningkat.\n• D: False. IREB menegaskan pengutamaan mesti menyeimbangkan pelbagai kriteria termasuk denda undang-undang, kos, dan risiko.",
    "extra": "Handbook Bab 6.8: Formula Karl Wiegers: Nilai relatif (Benefit + Penalty) dibahagikan dengan (Cost + Risk).",
    "mnemonic": "Wiegers: Keutamaan = Nilai / (Kos + Risiko). Kos tinggi = Keutamaan turun."
}

maritime_map[43] = {
    "id": 43,
    "code": "GM0606",
    "type": "A",
    "pts": 1.0,
    "eo": "6.5.1",
    "euNo": 6,
    "title": "Requirements Baseline Concept and Purpose",
    "question": "Which of the following statements BEST defines a 'Requirements Baseline' in Requirements Management? (Select 1 answer)",
    "options": [
        { "id": "A", "text": "A stable, internally consistent, and formally approved set of requirements frozen at a specific milestone to serve as the benchmark for further work and change control.", "truth": True },
        { "id": "B", "text": "An informal scratchpad list of ideas brainstormed during initial stakeholder elicitation sessions.", "truth": False },
        { "id": "C", "text": "The minimum number of test cases required to achieve 100% statement coverage in source code.", "truth": False },
        { "id": "D", "text": "A live, unversioned database where requirements are continually overwritten without change history.", "truth": False }
    ],
    "correctDisplay": "A",
    "whyCorrect": "• A: Betul. Baseline ialah konfigurasi keperluan yang stabil, lengkap, telah diluluskan secara rasmi (frozen/signed off), dan menjadi titik rujukan untuk pembangunan fasa seterusnya serta kawalan perubahan.",
    "whyWrong": "• B: Salah. Senarai nota draf atau lakaran idea awal (scratchpad) semasa sesi sumbang saran tidak stabil dan belum diluluskan secara formal, menjadikannya bukan baseline.\n• C: Salah. Bilangan kes ujian minimum untuk mencapai 100% liputan pernyataan kod (statement coverage) ialah metrik ujian perisian, bukan baseline keperluan.\n• D: Salah. Pangkalan data langsung tanpa kawalan versi di mana rekod sentiasa ditulis ganti tanpa sejarah jejak perubahan bercanggah secara langsung dengan integriti konsep baseline.",
    "extra": "Handbook Bab 6.5: Baseline membolehkan perbandingan perubahan (delta analysis) antara versi keluaran.",
    "mnemonic": "Baseline = Versi beku yang diluluskan secara rasmi (Approved & Frozen Snapshot)."
}

# --- EU7: Tool Support ---
maritime_map[44] = {
    "id": 44,
    "code": "GM0701",
    "type": "K",
    "pts": 2.0,
    "eo": "7.1.1",
    "euNo": 7,
    "title": "Criteria for Selecting Requirements Engineering Tools",
    "question": "An enterprise plans to introduce a dedicated Requirements Engineering tool suite across distributed engineering centers. Which of the following statements regarding tool selection and deployment are true and which are false?",
    "options": [
        { "id": "A", "text": "A suitable RE tool must support bidirectional traceability between requirements and verification artifacts across tool boundaries.", "truth": True },
        { "id": "B", "text": "Role-based access control and comprehensive version history are essential capabilities for multi-user collaborative RE tools.", "truth": True },
        { "id": "C", "text": "Introducing a sophisticated RE tool automatically corrects poorly phrased or missing requirements without training analysts.", "truth": False },
        { "id": "D", "text": "Tool integration interfaces (such as REST APIs or OSLC standards) are vital to connect RE data with test management and bug tracking systems.", "truth": True }
    ],
    "correctDisplay": "A=True, B=True, C=False, D=True",
    "whyCorrect": "• A: True. Kebolehkesanan dwi-arah (bidirectional traceability) adalah ciri utama alat RE moden.\n• B: True. Kawalan akses (RBAC) dan sejarah versi diperlukan untuk pengurusan kolaboratif pelbagai pengguna.\n• D: True. Integrasi melalui API/OSLC membolehkan pertukaran data lancar dengan alat hiliran.",
    "whyWrong": "• C: False. Alat perisian hanyalah pemudah cara; 'A fool with a tool is still a fool'. Ia tidak boleh menggantikan kemahiran manusia dalam mengenal pasti keperluan yang hilang.",
    "extra": "Handbook Bab 7.1: Faktor kejayaan alatan: Latihan, penyesuaian proses, sokongan kebolehkesanan.",
    "mnemonic": "Tool = Pemudah cara, bukan pengganti otak jurutera. Wajib ada Traceability, Versioning, dan Integrasi."
}

# Assemble all questions back into ordered list
final_questions = [maritime_map[i] for i in range(1, 46)]

# Verify tally
total_pts = sum(q['pts'] for q in final_questions)
print(f"Total Questions: {len(final_questions)}, Total Points: {total_pts:.2f}")
assert len(final_questions) == 45, "Must be exactly 45 questions"
assert abs(total_pts - 72.0) < 0.001, f"Points must equal 72.00, got {total_pts}"

# Update data
if 'predicted_maritime' not in app_data['sets']:
    app_data['sets']['predicted_maritime'] = {
        "id": "predicted_maritime",
        "name": "Set Ramalan Peperiksaan G+ (Maritime & Authentic Pool)",
        "badge": "Set Ramalan G+",
        "maxPoints": 72.0,
        "passPoints": 50.4,
        "passPct": 70.0,
        "totalQuestions": 45,
        "eus": app_data['sets']['predicted']['eus'],
        "questions": []
    }
app_data['sets']['predicted_maritime']['questions'] = final_questions

with open(DATA_PATH, 'w', encoding='utf-8') as f:
    json.dump(app_data, f, indent=2, ensure_ascii=False)

print("Successfully saved upgraded authentic maritime set G+ to app_data.json!")
