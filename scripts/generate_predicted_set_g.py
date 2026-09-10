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

# Load official diagrams
img_official_q18 = get_b64('clean_q18.png')
img_official_q20 = get_b64('clean_q20.png')
img_official_q21 = get_b64('clean_q21.png')
img_official_q23 = get_b64('clean_q23.png')

# Load predicted diagrams
img_predicted_q18 = get_b64('predicted_q18_class.png')
img_predicted_q20 = get_b64('predicted_q20_statemachine.png')
img_predicted_q21 = get_b64('predicted_q21_activity.png')
img_predicted_q23 = get_b64('predicted_q23_activity.png')

with open(DATA_PATH, 'r', encoding='utf-8') as f:
    existing_app_data = json.load(f)

if 'sets' in existing_app_data and 'official' in existing_app_data['sets']:
    official_questions = existing_app_data['sets']['official']['questions']
else:
    official_questions = existing_app_data.get('questions', [])

off_map = {q['id']: copy.deepcopy(q) for q in official_questions}

# 7 EUs for Official Set (70.0 Pts)
eus_official = [
  { "no": 1, "name": "Introduction and Overview of Requirements Engineering", "range": "Q1–Q3", "pts": 4.0, "qCount": 3 },
  { "no": 2, "name": "Fundamental Principles of Requirements Engineering", "range": "Q4–Q7", "pts": 6.0, "qCount": 4 },
  { "no": 3, "name": "Work Products and Documentation Practices", "range": "Q8–Q25", "pts": 30.0, "qCount": 18 },
  { "no": 4, "name": "Practices for Requirements Elaboration", "range": "Q26–Q35", "pts": 14.0, "qCount": 10 },
  { "no": 5, "name": "Process and Working Structure", "range": "Q36–Q37", "pts": 3.0, "qCount": 2 },
  { "no": 6, "name": "Management Practices for Requirements", "range": "Q38–Q43", "pts": 10.0, "qCount": 6 },
  { "no": 7, "name": "Tool Support", "range": "Q44–Q45", "pts": 3.0, "qCount": 2 }
]

# 7 EUs for Predicted Set G (72.0 Pts - Matching Real Exam Score Sheet 1:1)
eus_predicted = [
  { "no": 1, "name": "Introduction and Overview of Requirements Engineering", "range": "Q1–Q3", "pts": 5.0, "qCount": 3 },
  { "no": 2, "name": "Fundamental Principles of Requirements Engineering", "range": "Q4–Q7", "pts": 7.0, "qCount": 4 },
  { "no": 3, "name": "Work Products and Documentation Practices", "range": "Q8–Q23", "pts": 27.0, "qCount": 16 },
  { "no": 4, "name": "Practices for Requirements Elaboration", "range": "Q24–Q34", "pts": 15.0, "qCount": 11 },
  { "no": 5, "name": "Process and Working Structure", "range": "Q35–Q37", "pts": 5.0, "qCount": 3 },
  { "no": 6, "name": "Management Practices for Requirements", "range": "Q38–Q43", "pts": 10.0, "qCount": 6 },
  { "no": 7, "name": "Tool Support", "range": "Q44–Q45", "pts": 3.0, "qCount": 2 }
]

# Build Set G Questions:
# Blend of 34 authentic anchor questions (sebijik sama latihan rasmi) + 11 targeted predicted variants
predicted_questions = []

def anchor_q(official_id, new_id, eu_no, pts=None):
    q = copy.deepcopy(off_map[official_id])
    q['id'] = new_id
    q['euNo'] = eu_no
    if pts is not None:
        q['pts'] = float(pts)
    q['isAnchor'] = True
    return q

# =========================================================================
# EU1: Introduction & Overview (Q1–Q3, 5.0 Pts)
# =========================================================================
# Q1: Official Q1 (2.0 K) - Identical
predicted_questions.append(anchor_q(1, 1, 1))

# Q2: Predicted 2.0 P (Core Tasks: Eliciting & Validating)
predicted_questions.append({
  "id": 2,
  "code": "G0102",
  "type": "P",
  "pts": 2.0,
  "eo": "1.4.1",
  "euNo": 1,
  "title": "Core Activities of Requirements Engineering (E-D-V-M)",
  "question": "A newly formed project team wants to establish a solid Requirements Engineering approach. Which two of the following activities represent core activities of a Requirements Engineer according to IREB? (2 answers)",
  "options": [
    { "id": "A", "text": "Eliciting requirements from stakeholders, documents, and existing systems", "truth": True },
    { "id": "B", "text": "Writing production source code for system architecture components", "truth": False },
    { "id": "C", "text": "Validating and negotiating requirements with all relevant stakeholders", "truth": True },
    { "id": "D", "text": "Executing automated unit tests in continuous integration pipeline", "truth": False },
    { "id": "E", "text": "Managing financial project budgets and calculating vendor payments", "truth": False }
  ],
  "correctDisplay": "A, C",
  "whyCorrect": "• A (Eliciting requirements): Betul. Elicitation adalah aktiviti teras pertama dalam RE.\n• C (Validating and negotiating requirements): Betul. Validation & Negotiation adalah aktiviti teras ketiga dalam RE.",
  "whyWrong": "• B: Penulisan kod pengeluaran adalah tugas Software Developer/Engineer.\n• D: Pelaksanaan unit test adalah tugas Tester/Developer.\n• E: Pengurusan belanjawan kewangan adalah tugas Project Manager.",
  "extra": "Handbook Bab 1.4: 4 Aktiviti Teras RE: 1. Elicitation, 2. Documentation, 3. Validation & Negotiation, 4. Management (E-D-V-M).",
  "mnemonic": "4 Teras RE = E-D-V-M (Elicit, Document, Validate, Manage)."
})

# Q3: Official Q3 (1.0 P) - Identical
predicted_questions.append(anchor_q(3, 3, 1))

# =========================================================================
# EU2: Fundamental Principles of RE (Q4–Q7, 7.0 Pts)
# =========================================================================
# Q4: Official Q4 (1.0 A) - Identical
predicted_questions.append(anchor_q(4, 4, 2))

# Q5: Official Q5 (2.0 K) - Identical
predicted_questions.append(anchor_q(5, 5, 2))

# Q6: Official Q6 (2.0 K) - Identical
predicted_questions.append(anchor_q(6, 6, 2))

# Q7: Predicted 2.0 P (System vs Context Boundary)
predicted_questions.append({
  "id": 7,
  "code": "G0204",
  "type": "P",
  "pts": 2.0,
  "eo": "2.2.2",
  "euNo": 2,
  "title": "System Boundary vs Context Boundary in Practice",
  "question": "During a scoping workshop, the requirements engineering team is determining the system boundary and context boundary for a new automated baggage drop system at an international airport. Which two of the following statements about system and context boundaries are correct? (2 answers)",
  "options": [
    { "id": "A", "text": "The system boundary separates what is to be developed (the system) from its operational environment.", "truth": True },
    { "id": "B", "text": "Aspects lying within the grey zone of the context boundary can be ignored completely during elicitation.", "truth": False },
    { "id": "C", "text": "Interfaces between the system and its operational environment lie directly on the system boundary.", "truth": True },
    { "id": "D", "text": "The system boundary is permanently fixed at the project start and cannot be modified under any circumstances.", "truth": False },
    { "id": "E", "text": "The context boundary determines which programming languages and database engines must be selected.", "truth": False }
  ],
  "correctDisplay": "A, C",
  "whyCorrect": "• A: Betul. System boundary memisahkan sistem yang dibangunkan daripada persekitaran operasinya.\n• C: Betul. Antara muka (interfaces/sensors/APIs) terletak tepat di atas sempadan sistem.",
  "whyWrong": "• B: Grey zone (zon kelabu) TIDAK boleh diabaikan; jurutera keperluan mesti menyiasat sehingga ia dijelaskan.\n• D: Sempadan sistem boleh berubah (evolve) semasa projek berjalan melalui pengurusan perubahan.\n• E: Pemilihan bahasa pengaturcaraan adalah keputusan reka bentuk perisian, bukan sempadan konteks.",
  "extra": "Handbook Bab 2.4 (Prinsip 4): System boundary = apa yang boleh diubah pemaju. Context boundary = aspek relevan persekitaran.",
  "mnemonic": "System Boundary = Dalam Kawalan. Context Boundary = Persekitaran Relevan."
})

# =========================================================================
# EU3: Work Products and Documentation (Q8–Q23, 27.0 Pts, 16 Qs)
# =========================================================================
# Q8: Official Q8 (1.0 A) - Identical
predicted_questions.append(anchor_q(8, 8, 3))

# Q9: Official Q9 (1.0 A) - Identical
predicted_questions.append(anchor_q(9, 9, 3))

# Q10: Official Q10 (2.0 P) - Identical
predicted_questions.append(anchor_q(10, 10, 3))

# Q11: Official Q11 (2.0 P) - Identical
predicted_questions.append(anchor_q(11, 11, 3))

# Q12: Official Q12 (2.0 K) - Identical
predicted_questions.append(anchor_q(12, 12, 3))

# Q13: Official Q13 (2.0 K) - Identical
predicted_questions.append(anchor_q(13, 13, 3))

# Q14: Official Q14 (2.0 P) - Identical
predicted_questions.append(anchor_q(14, 14, 3))

# Q15: Official Q15 (1.0 A) - Identical
predicted_questions.append(anchor_q(15, 15, 3))

# Q16: Official Q16 (2.0 K) - Identical
predicted_questions.append(anchor_q(16, 16, 3))

# Q17: Official Q17 (1.0 A) - Identical
predicted_questions.append(anchor_q(17, 17, 3))

# Q18: Predicted Diagram 1 (UML Class Diagram - Order, Customer, OrderItem, Product) 2.0 K
predicted_questions.append({
  "id": 18,
  "code": "G0311",
  "type": "K",
  "pts": 2.0,
  "eo": "3.4.6",
  "euNo": 3,
  "title": "UML Class Diagram: B2B Order & Customer Multiplicities",
  "question": "The following UML class diagram models a B2B retail ordering system:\n\nWhich of the following statements are true and which are false based on this diagram?",
  "diagramHtml": f'<div class="diagram-wrapper"><img src="{img_predicted_q18}" alt="Predicted UML Class Diagram Q18" class="diagram-img" /></div>',
  "options": [
    { "id": "A", "text": "A Customer can exist in the system without having placed any Order.", "truth": True },
    { "id": "B", "text": "An Order can contain zero OrderItem elements.", "truth": False },
    { "id": "C", "text": "An OrderItem can be associated with multiple Products simultaneously.", "truth": False },
    { "id": "D", "text": "Each Order must be associated with exactly one Customer.", "truth": True }
  ],
  "correctDisplay": "A=True, B=False, C=False, D=True",
  "whyCorrect": "• A: True. Multiplicity di hujung Order ialah 0..* (Customer boleh mempunyai 0 atau lebih Order).\n• D: True. Multiplicity di hujung Customer ialah 1 (Setiap Order mesti dimiliki tepat seorang Customer).",
  "whyWrong": "• B: False. Multiplicity di hujung OrderItem ialah 1..* (Order wajib ada sekurang-kurangnya 1 OrderItem).\n• C: False. Multiplicity di hujung Product ialah 1 (Satu baris pesanan merujuk tepat 1 produk).",
  "extra": "Handbook Bab 3.4.6: Multiplicity menentukan had bilangan kejadian objek yang boleh dihubungkan.",
  "mnemonic": "0..* = Pilihan (boleh sifar). 1..* = Wajib ada sekurang-kurangnya satu."
})

# Q19: Official Q19 (1.0 A) - Identical
predicted_questions.append(anchor_q(19, 19, 3))

# Q20: Predicted Diagram 2 (UML State Machine - Order Lifecycle) 2.0 K
predicted_questions.append({
  "id": 20,
  "code": "G0313",
  "type": "K",
  "pts": 2.0,
  "eo": "3.4.5",
  "euNo": 3,
  "title": "UML State Machine: Order Processing Lifecycle",
  "question": "The following UML state machine diagram describes the lifecycle of an online purchase order:\n\nWhich of the following statements are true and which are false based on this diagram?",
  "diagramHtml": f'<div class="diagram-wrapper"><img src="{img_predicted_q20}" alt="Predicted UML State Machine Q20" class="diagram-img" /></div>',
  "options": [
    { "id": "A", "text": "An order can be cancelled directly from the 'Created' state.", "truth": True },
    { "id": "B", "text": "An order can transition from 'Shipped' directly to 'Cancelled'.", "truth": False },
    { "id": "C", "text": "The event 'payment_received' triggers the transition from 'Created' to 'Authorized'.", "truth": True },
    { "id": "D", "text": "'Delivered' and 'Cancelled' are both final states in this state machine.", "truth": True }
  ],
  "correctDisplay": "A=True, B=False, C=True, D=True",
  "whyCorrect": "• A: True. Terdapat transisi 'cancel_order' terus dari 'Created' ke 'Cancelled'.\n• C: True. Event 'payment_received' memacu transisi dari 'Created' ke 'Authorized'.\n• D: True. Kedua-dua keadaan 'Delivered' dan 'Cancelled' mempunyai transisi ke bulatan akhir (final state).",
  "whyWrong": "• B: False. Dari keadaan 'Shipped', tiada transisi terus ke 'Cancelled'; hanya transisi 'delivery_confirmed' ke 'Delivered'.",
  "extra": "Handbook Bab 3.4.5: State Machine memodelkan kitaran hayat tingkah laku objek berasaskan peristiwa (events), guard conditions, dan tindakan.",
  "mnemonic": "State = Keadaan objek. Transition = Anak panah dengan peristiwa [guard] / action."
})

# Q21: Predicted Diagram 3 (UML Activity Diagram - Order Checkout Fork/Join) 2.0 K
predicted_questions.append({
  "id": 21,
  "code": "G0314",
  "type": "K",
  "pts": 2.0,
  "eo": "3.4.7",
  "euNo": 3,
  "title": "UML Activity Diagram: Order Checkout Concurrent Execution",
  "question": "The following UML activity diagram specifies the checkout and fulfillment workflow in an enterprise e-commerce platform:\n\nWhich of the following statements are true and which are false based on this diagram?",
  "diagramHtml": f'<div class="diagram-wrapper"><img src="{img_predicted_q21}" alt="Predicted UML Activity Checkout Q21" class="diagram-img" /></div>',
  "options": [
    { "id": "A", "text": "'Deduct Inventory' and 'Process Payment' are executed concurrently after the fork node.", "truth": True },
    { "id": "B", "text": "'Generate Invoice' can be executed as soon as 'Deduct Inventory' finishes, regardless of 'Process Payment'.", "truth": False },
    { "id": "C", "text": "If 'Validate Customer' fails, the process terminates at the activity final node without initiating concurrent paths.", "truth": True },
    { "id": "D", "text": "The fork node splits a single control flow into multiple concurrent flows.", "truth": True }
  ],
  "correctDisplay": "A=True, B=False, C=True, D=True",
  "whyCorrect": "• A: True. Palang mendatar hitam tebal (fork node) memulakan laluan serentak (concurrent) bagi Deduct Inventory dan Process Payment.\n• C: True. Cabang [invalid] terus membawa aliran kawalan ke bulatan hitam berlingkar (activity final node).\n• D: True. Definisi piawai fork node adalah membahagikan satu token aliran kepada pelbagai token serentak.",
  "whyWrong": "• B: False. Palang join node memerlukan SEMUA aliran masuk (kedua-dua Deduct Inventory dan Process Payment) selesai sebelum Generate Invoice boleh bermula.",
  "extra": "Handbook Bab 3.4.7: Fork = 1 aliran masuk, banyak keluar serentak. Join = Banyak aliran masuk serentak disegerakkan (synchronize) menjadi 1 keluar.",
  "mnemonic": "Fork = Pecah Serentak. Join = Tunggu Semua Selesai."
})

# Q22: Official Q22 (2.0 P) - Identical
predicted_questions.append(anchor_q(22, 22, 3))

# Q23: Predicted Diagram 4 (UML Activity Diagram - Logistics Shipping Decision/Merge) 2.0 K
predicted_questions.append({
  "id": 23,
  "code": "G0316",
  "type": "K",
  "pts": 2.0,
  "eo": "3.4.7",
  "euNo": 3,
  "title": "UML Activity Diagram: Logistics Routing Decision & Merge",
  "question": "The following UML activity diagram models the parcel shipping dispatch logic at a logistics hub:\n\nWhich of the following statements are true and which are false based on this diagram?",
  "diagramHtml": f'<div class="diagram-wrapper"><img src="{img_predicted_q23}" alt="Predicted UML Activity Logistics Q23" class="diagram-img" /></div>',
  "options": [
    { "id": "A", "text": "Parcels with weight > 30 kg are routed to 'Assign Heavy Freight Carrier'.", "truth": True },
    { "id": "B", "text": "A parcel can be routed to both 'Standard Courier' and 'Assign Heavy Freight Carrier' simultaneously.", "truth": False },
    { "id": "C", "text": "The merge diamond brings together alternative flows before 'Print Dispatch Label' is executed.", "truth": True },
    { "id": "D", "text": "If documentation is missing during parcel inspection, the workflow is aborted.", "truth": True }
  ],
  "correctDisplay": "A=True, B=False, C=True, D=True",
  "whyCorrect": "• A: True. Guard condition [weight > 30kg] menghala tepat ke aktiviti 'Assign Heavy Freight Carrier'.\n• C: True. Simbol berlian (merge diamond) menggabungkan laluan alternatif tanpa menunggu kedua-duanya selesai.\n• D: True. Guard [documentation missing] terus menamatkan aliran kerja di activity final node.",
  "whyWrong": "• B: False. Simbol berlian membuat keputusan (decision diamond) adalah mutually exclusive (saling eksklusif); hanya SATU laluan sahaja dipilih berdasarkan guard condition.",
  "extra": "Handbook Bab 3.4.7: Decision/Merge diamond menggunakan syarat [guard] untuk memilih 1 daripada laluan alternatif.",
  "mnemonic": "Diamond = Keputusan saling eksklusif (pilih SATU sahaja)."
})

# =========================================================================
# EU4: Practices for Requirements Elaboration (Q24–Q34, 15.0 Pts, 11 Qs)
# =========================================================================
# Q24: Official Q26 (1.0 A) - Identical
predicted_questions.append(anchor_q(26, 24, 4))

# Q25: Official Q27 (1.0 P) - Identical
predicted_questions.append(anchor_q(27, 25, 4))

# Q26: Official Q28 (1.0 A) - Identical
predicted_questions.append(anchor_q(28, 26, 4))

# Q27: Official Q29 (2.0 P) - Identical
predicted_questions.append(anchor_q(29, 27, 4))

# Q28: Official Q30 (1.0 A) - Identical
predicted_questions.append(anchor_q(30, 28, 4))

# Q29: Official Q31 (2.0 P) - Identical
predicted_questions.append(anchor_q(31, 29, 4))

# Q30: Official Q32 (1.0 P) - Identical
predicted_questions.append(anchor_q(32, 30, 4))

# Q31: Official Q34 (1.0 A) - Identical
predicted_questions.append(anchor_q(34, 31, 4))

# Q32: Predicted 2.0 K (Kano Model Delighters & Habituation)
predicted_questions.append({
  "id": 32,
  "code": "G0409",
  "type": "K",
  "pts": 2.0,
  "eo": "4.2.2",
  "euNo": 4,
  "title": "Kano Model: Dynamics of Delighters and Basic Factors",
  "question": "According to the Kano Model, requirements can be classified into basic factors (dissatisfiers), performance factors (satisfiers), and excitement factors (delighters). Which of the following statements are true and which are false?",
  "options": [
    { "id": "A", "text": "Excitement factors are explicitly expected by customers and cause extreme dissatisfaction if absent.", "truth": False },
    { "id": "B", "text": "Basic factors are taken for granted; fulfilling them does not actively increase customer satisfaction, but failing to fulfill them causes strong dissatisfaction.", "truth": True },
    { "id": "C", "text": "Over time, excitement factors gradually turn into performance factors and eventually into basic factors due to habituation.", "truth": True },
    { "id": "D", "text": "Performance factors show a linear relationship between the degree of requirement fulfillment and customer satisfaction.", "truth": True }
  ],
  "correctDisplay": "A=False, B=True, C=True, D=True",
  "whyCorrect": "• B: True. Basic factors (dissatisfiers) dianggap tabii/wajib ada; jika tiada, pelanggan sangat marah.\n• C: True. Kesan pembiasaan (habituation): ciri hebat (delighter) lama-kelamaan menjadi kebiasaan pasaran (basic factor).\n• D: True. Ciri prestasi (performance factor) berkadar terus secara linear dengan kepuasan pengguna.",
  "whyWrong": "• A: False. Excitement factors TIDAK dijangka oleh pelanggan secara sedar; ketiadaannya tidak menyebabkan ketidakpuasan hati.",
  "extra": "Handbook Bab 4.2.2: Kano Model mengklasifikasikan 3 faktor utama: Basic, Performance, Excitement.",
  "mnemonic": "Basic = Wajib ada. Performance = Linear. Excitement = Bonus wow!"
})

# Q33: Official Q35 (2.0 A) - Identical
predicted_questions.append(anchor_q(35, 33, 4))

# Q34: Predicted 1.0 A (Requirements Negotiation Strategy)
predicted_questions.append({
  "id": 34,
  "code": "G0411",
  "type": "A",
  "pts": 1.0,
  "eo": "4.3.2",
  "euNo": 4,
  "title": "Requirements Negotiation: Resolving Conflicting Stakeholder Interests",
  "question": "During requirements negotiation between the Marketing department and the Security team regarding user registration, a conflict arises. The marketing manager insists on '1-click social login without password', while the security officer requires 'mandatory 2-factor authentication with hardware tokens'. Which technique is the most appropriate collaborative negotiation strategy according to IREB to achieve a sustainable solution? (1 answer)",
  "options": [
    { "id": "A", "text": "Dominance by the Project Manager without consulting either party", "truth": False },
    { "id": "B", "text": "Integrative bargaining (win-win negotiation) exploring underlying goals to formulate an alternative solution", "truth": True },
    { "id": "C", "text": "Postponing the decision indefinitely until after system deployment", "truth": False },
    { "id": "D", "text": "Asking the development team to secretly implement both variants without informing stakeholders", "truth": False }
  ],
  "correctDisplay": "B (Integrative bargaining (win-win negotiation)...)",
  "whyCorrect": "• Pilihan B adalah tepat. Integrative bargaining menyiasat motif/matlamat sebenar di sebalik tuntutan kedua-dua pihak untuk mencari penyelesaian menang-menang (contohnya: biometric biometric login yang pantas dan selamat).",
  "whyWrong": "• A: Dominance (memaksa) mewujudkan rasa tidak puas hati.\n• C: Menangguhkan keputusan tidak menyelesaikan konflik.\n• D: Melaksana secara rahsia melanggar etika dan ketelusan RE.",
  "extra": "Handbook Bab 4.3.2: Strategi resolusi konflik: Agreement, Compromise, Voting, Dominance, Integrative bargaining.",
  "mnemonic": "Konflik berkualiti diselesaikan dengan Integrative Bargaining (Win-Win)."
})

# =========================================================================
# EU5: Process and Working Structure (Q35–Q37, 5.0 Pts, 3 Qs)
# =========================================================================
# Q35: Predicted 2.0 K (Process Facets & Configuration)
predicted_questions.append({
  "id": 35,
  "code": "G0501",
  "type": "K",
  "pts": 2.0,
  "eo": "5.2.1",
  "euNo": 5,
  "title": "RE Process Facets: Time, Purpose, Target, Interaction",
  "question": "IREB distinguishes several facets that configure an appropriate Requirements Engineering process. Which of the following statements regarding the 'Process Facets' (Time, Purpose, Target, Interaction) are true and which are false?",
  "options": [
    { "id": "A", "text": "In a plan-driven, linear RE process, requirements for the entire system are comprehensively documented before development starts.", "truth": True },
    { "id": "B", "text": "In an agile, iterative RE process, requirements are elicited, documented, and refined continuously in short feedback loops (sprints).", "truth": True },
    { "id": "C", "text": "An iterative RE process completely eliminates the need for any requirements documentation or models.", "truth": False },
    { "id": "D", "text": "The 'Customer/Supplier' interaction facet determines whether the project is developed for a specific customer or for a broad, anonymous market (product development).", "truth": True }
  ],
  "correctDisplay": "A=True, B=True, C=False, D=True",
  "whyCorrect": "• A: True. Linear process mendokumentasikan spesifikasi penuh sebelum fasa pembinaan.\n• B: True. Iterative process memperhalusi keperluan secara berterusan dalam sprint.\n• D: True. Aspek Customer/Supplier menentukan sama ada bina untuk pelanggan khusus (contract) atau pasaran terbuka (market).",
  "whyWrong": "• C: False. Pendekatan tangkas (agile) tetap memerlukan dokumentasi (seperti user stories, acceptance criteria, dan model konsep) yang mencukupi untuk shared understanding.",
  "extra": "Handbook Bab 5.2: 4 Facets proses RE: 1. Time (linear vs iterative), 2. Purpose (prescriptive vs exploratory), 3. Target (customer-specific vs market-oriented), 4. Interaction (tight vs loose).",
  "mnemonic": "4 Facet RE: Time, Purpose, Target, Interaction."
})

# Q36: Official Q36 (2.0 P) - Identical
predicted_questions.append(anchor_q(36, 36, 5))

# Q37: Official Q37 (1.0 A) - Identical
predicted_questions.append(anchor_q(37, 37, 5))

# =========================================================================
# EU6: Management Practices for Requirements (Q38–Q43, 10.0 Pts, 6 Qs)
# =========================================================================
# Q38: Official Q38 (2.0 K) - Identical
predicted_questions.append(anchor_q(38, 38, 6))

# Q39: Official Q39 (1.0 A) - Identical
predicted_questions.append(anchor_q(39, 39, 6))

# Q40: Official Q40 (2.0 K) - Identical
predicted_questions.append(anchor_q(40, 40, 6))

# Q41: Predicted 2.0 P (Change Management & Impact Analysis)
predicted_questions.append({
  "id": 41,
  "code": "G0604",
  "type": "P",
  "pts": 2.0,
  "eo": "6.4.1",
  "euNo": 6,
  "title": "Requirements Change Management: Impact Analysis & CCB",
  "question": "A change request is submitted to modify an existing requirements baseline of an operational banking application. According to IREB change management best practices, which two of the following tasks should be performed before the Change Control Board (CCB) makes a decision? (2 answers)",
  "options": [
    { "id": "A", "text": "Assessing the technical feasibility and cost/effort impact of the proposed change", "truth": True },
    { "id": "B", "text": "Immediately rewriting all existing requirements in the database to match the requested change before review", "truth": False },
    { "id": "C", "text": "Analyzing dependencies and risks for related system components and requirements", "truth": True },
    { "id": "D", "text": "Rejecting the change request automatically if it requires more than 1 day of development work", "truth": False },
    { "id": "E", "text": "Committing the change directly to the production branch without stakeholder consultation", "truth": False }
  ],
  "correctDisplay": "A, C",
  "whyCorrect": "• A (Assessing feasibility & cost): Betul. Analisis impak mesti menilai kos, usaha dan kebolehlaksanaan teknikal.\n• C (Analyzing dependencies & risks): Betul. Mesti mengenal pasti keperluan atau modul lain yang terjejas sebelum kelulusan.",
  "whyWrong": "• B & E: Tidak boleh mengubah dokumen/kod sebelum CCB membuat keputusan rasmi.\n• D: Had masa 1 hari adalah rekaan dan bukan kriteria penolakan automatik IREB.",
  "extra": "Handbook Bab 6.4: Aliran kerja Change Request: Submit -> Log -> Analyze Impact -> CCB Decision -> Implement & Verify.",
  "mnemonic": "Ubah Keperluan: Buat Analisis Impak (Kos, Risiko, Kesan) DAHULU sebelum CCB buat keputusan."
})

# Q42: Predicted 2.0 K (Requirements Prioritization Techniques)
predicted_questions.append({
  "id": 42,
  "code": "G0605",
  "type": "K",
  "pts": 2.0,
  "eo": "6.8.1",
  "euNo": 6,
  "title": "Techniques for Requirements Prioritization (Wiegers, AHP, Kano)",
  "question": "Prioritization of requirements is essential when project resources and time constraints prevent implementing all requirements at once. Which of the following statements about prioritization techniques and criteria are true and which are false?",
  "options": [
    { "id": "A", "text": "Requirements can be prioritized based on multiple criteria, such as business value, risk, penalty for non-implementation, and implementation cost.", "truth": True },
    { "id": "B", "text": "In the Analytic Hierarchy Process (AHP), requirements are compared pairwise against each other by stakeholders.", "truth": True },
    { "id": "C", "text": "Top-ten ranking is an ad-hoc prioritization technique suitable when there are thousands of highly complex requirements.", "truth": False },
    { "id": "D", "text": "Wiegers' prioritization method calculates priority using a formula incorporating relative benefit, relative penalty, cost, and technical risk.", "truth": True }
  ],
  "correctDisplay": "A=True, B=True, C=False, D=True",
  "whyCorrect": "• A: True. Kriteria pengutamaan boleh merangkumi nilai perniagaan, kos, risiko, dan implikasi denda.\n• B: True. AHP menggunakan perbandingan berpasangan (pairwise comparison) antara dua keperluan secara sistematik.\n• D: True. Kaedah Karl Wiegers menggunakan formula berbobot (Benefit + Penalty) / (Cost + Risk).",
  "whyWrong": "• C: False. Top-ten ranking hanya sesuai untuk kumpulan keperluan yang sangat kecil, bukan beribu-ribu keperluan kompleks.",
  "extra": "Handbook Bab 6.8: Teknik keutamaan: Ranking, Top-ten, Single-criterion (Kano), Multi-criteria (Wiegers, AHP).",
  "mnemonic": "AHP = Pairwise. Wiegers = Benefit & Penalty vs Cost & Risk."
})

# Q43: Official Q43 (1.0 A) - Identical
predicted_questions.append(anchor_q(43, 43, 6))

# =========================================================================
# EU7: Tool Support (Q44–Q45, 3.0 Pts, 2 Qs)
# =========================================================================
# Q44: Official Q44 (2.0 K) - Identical
predicted_questions.append(anchor_q(44, 44, 7))

# Q45: Official Q45 (1.0 A) - Identical
predicted_questions.append(anchor_q(45, 45, 7))

# Combine both sets into one master structure
combined_data = {
  "eus": eus_official,
  "sets": {
    "official": {
      "id": "official",
      "name": "Set Latihan Rasmi (IREB Practice Exam)",
      "badge": "Set Rasmi",
      "maxPoints": 70.0,
      "passPoints": 49.0,
      "passPct": 70.0,
      "totalQuestions": 45,
      "eus": eus_official,
      "questions": official_questions
    },
    "predicted": {
      "id": "predicted",
      "name": "Set Ramalan Peperiksaan G (Slip Sebenar)",
      "badge": "Set Ramalan G",
      "maxPoints": 72.0,
      "passPoints": 50.4,
      "passPct": 70.0,
      "totalQuestions": 45,
      "eus": eus_predicted,
      "questions": predicted_questions
    }
  },
  "questions": official_questions
}

with open(DATA_PATH, 'w', encoding='utf-8') as f:
    json.dump(combined_data, f, indent=2, ensure_ascii=False)

print("Generated master data with both sets successfully!")
print(f"Official Set: {len(official_questions)} questions, {sum(q['pts'] for q in official_questions)} pts")
print(f"Predicted Set G: {len(predicted_questions)} questions, {sum(q['pts'] for q in predicted_questions)} pts")
