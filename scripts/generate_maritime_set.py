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

# Take base questions from predicted set G as starting template
base_g = copy.deepcopy(app_data['sets']['predicted']['questions'])
maritime_questions = []

for q in base_g:
    qid = q['id']
    mq = copy.deepcopy(q)
    mq['code'] = mq['code'].replace('G', 'GM')
    
    # Question 20 is the dedicated Vessel/Ship State Machine question
    if qid == 20:
        mq = {
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
            "correctDisplay": "A=True, B=True, C=False, D=True",
            "whyCorrect": "• A: True. Terdapat transisi 'approach_port [berth_busy == false]' yang membenarkan kapal masuk terus ke fasa 'Entering Harbor' tanpa perlu berlabuh sauh.\n• B: True. Transisi kecemasan 'storm_warning [wind > 40kn]' mengarahkan kapal yang sedang memasuki alur pelabuhan kembali berlabuh selamat di 'Waiting at Anchorage'.",
            "whyWrong": "• C: False. Tiada anak panah terus dari 'At Sea' ke 'Cargo Operations'; kapal wajib merapat di dermaga (Moored at Berth) terlebih dahulu.\n• D: False. Kedua-dua keadaan ini berlaku secara berurutan (sequential), bukan serentak (tiada garis putus-putus atau composite orthogonal states).",
            "extra": "Handbook Bab 3.4.5: State Machine Diagram memodelkan kitaran hayat tingkah laku objek dinamik berdasarkan Events, Guard Conditions [syarat], dan Actions /tindakan.",
            "mnemonic": "State Machine Kapal: Semak Guard [syarat] & arah anak panah. Masuk pelabuhan wajib ikut urutan selamat."
        }
    
    # Strengthen EU5 Q35 with focused process configuration insights
    elif qid == 35:
        mq = {
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
        
    # Strengthen EU6 Q42 on prioritization (AHP vs Wiegers)
    elif qid == 42:
        mq = {
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

    maritime_questions.append(mq)

# Check points and counts
eus_predicted = app_data['sets']['predicted']['eus']
pts_total = sum(q['pts'] for q in maritime_questions)
print(f"Constructed maritime questions: {len(maritime_questions)} questions, {pts_total:.2f} Pts")

# Add as third set in app_data
app_data['sets']['predicted_maritime'] = {
    "id": "predicted_maritime",
    "name": "Set Ramalan G+ (Varian Maritim & Arkib Bocor)",
    "shortName": "Ramalan G+ (Maritim)",
    "badge": "Set G+ Maritim",
    "maxPoints": 72.0,
    "passPoints": 50.40,
    "passPct": 70.0,
    "totalQuestions": 45,
    "eus": eus_predicted,
    "questions": maritime_questions
}

with open(DATA_PATH, 'w', encoding='utf-8') as f:
    json.dump(app_data, f, indent=2, ensure_ascii=False)

print("Saved app_data.json with 3 complete sets successfully!")
