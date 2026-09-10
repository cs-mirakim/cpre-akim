import json
import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(ROOT_DIR, 'data', 'app_data.json')
SCRATCH_DIR = os.path.join(ROOT_DIR, 'scripts', 'scratch')

import sys
sys.path.append(SCRATCH_DIR)

# Load the drafted official explanations
from draft_official_explanations_1 import OFFICIAL_EXPLANATIONS as OFF_1
from draft_official_explanations_2 import OFFICIAL_EXPLANATIONS_2 as OFF_2
from draft_official_explanations_3 import OFFICIAL_EXPLANATIONS_3 as OFF_3

ALL_OFFICIAL_EXP = {}
ALL_OFFICIAL_EXP.update(OFF_1)
ALL_OFFICIAL_EXP.update(OFF_2)
ALL_OFFICIAL_EXP.update(OFF_3)

with open(DATA_PATH, 'r', encoding='utf-8') as f:
    app_data = json.load(f)

# ==============================================================================
# 1. UPDATE SET LATIHAN RASMI (OFFICIAL SET)
# ==============================================================================
print("Updating official practice exam set...")
for q in app_data['sets']['official']['questions']:
    qid = q['id']
    if qid in ALL_OFFICIAL_EXP:
        exp = ALL_OFFICIAL_EXP[qid]
        q['correctDisplay'] = exp['correctDisplay']
        q['whyCorrect'] = exp['whyCorrect']
        q['whyWrong'] = exp['whyWrong']

# ==============================================================================
# 2. UPDATE SET RAMALAN G (PREDICTED SET)
# ==============================================================================
print("Updating predicted Set G...")
# Custom explanations for Set G's custom questions
SET_G_CUSTOM = {
    18: {
        "correctDisplay": "A=False, B=True, C=True, D=True, E=False",
        "whyCorrect": (
            "• B (A customer can place multiple orders over time): True. Penggandaan pada peranan Order dari Customer ialah 0..*, bermakna seorang pelanggan boleh membuat sifar, satu, atau banyak pesanan.\n"
            "• C (Each invoice belongs to exactly one order): True. Hubungan Invoice ke Order mempunyai multiplicity 1..1 (setiap invois merujuk kepada tepat satu pesanan).\n"
            "• D (An order can exist without an invoice initially): True. Multiplicity pada Invoice dari Order ialah 0..1 (pesanan boleh wujud sebelum invois dijana)."
        ),
        "whyWrong": (
            "• A (An order can exist without an associated customer): False. Multiplicity pada Customer ialah 1..1 (setiap pesanan wajib dimiliki oleh seorang pelanggan berdaftar).\n"
            "• E (An invoice can combine multiple separate orders into one line item): False. Hubungan komposisi tegas 1..1 menghalang penyatuan pelbagai pesanan berbeza ke dalam satu invois yang sama."
        )
    },
    20: {
        "correctDisplay": "A=False, B=True, C=True, D=False",
        "whyCorrect": (
            "• B (An order transitions to 'Cancelled' if payment authorization fails): True. Terdapat transisi jelas dengan peristiwa 'payment_failed' yang mengalihkan pesanan terus ke status 'Cancelled'.\n"
            "• C (An order can only be 'Shipped' after it has successfully reached 'Payment Authorized'): True. Aliran proses mengikut urutan bersyarat di mana barangan hanya boleh dihantar selepas pembayaran disahkan."
        ),
        "whyWrong": (
            "• A (An order can transition from 'Pending' directly to 'Delivered' in one step): False. Tiada transisi melangkau status; pesanan mesti melalui fasa pembayaran dan penghantaran terlebih dahulu.\n"
            "• D (Once in 'Cancelled' state, an order can be reopened to 'Pending'): False. Status 'Cancelled' ialah status penamat (tiada anak panah keluar kembali ke 'Pending')."
        )
    },
    21: {
        "correctDisplay": "A=False, B=False, C=False, D=True",
        "whyCorrect": (
            "• D (Confirmation email is sent only after both payment processing and inventory reservation are complete): Matches. Join Node (bar tebal penyatu) menunggu KEDUA-DUA cabang selesai sebelum menghantar emel pengesahan."
        ),
        "whyWrong": (
            "• A (Payment processing must strictly precede inventory reservation): Does not match. Kedua-dua aktiviti bermula serentak selepas Fork Node (cabang selari), jadi tiada urutan tetap.\n"
            "• B (Inventory reservation starts only after payment is completely confirmed): Does not match. Fork Node memulakan kedua-dua aktiviti secara serentak (concurrently).\n"
            "• C (Payment processing and inventory reservation must terminate at the exact same millisecond): Does not match. Join Node menunggu kedua-duanya selesai, tetapi tidak mewajibkan ia tamat serentak."
        )
    },
    23: {
        "correctDisplay": "A=True, B=True, C=False, D=True",
        "whyCorrect": (
            "• A (A package can follow the 'Express Delivery' route when express guard is true): True. Decision Node membenarkan aliran melalui laluan ekspres apabila syarat [express == true] dipenuhi.\n"
            "• B (A package can follow the 'Standard Freight' route when express guard is false): True. Terdapat cabang alternatif untuk penghantaran biasa apabila syarat [express == false].\n"
            "• D (The destination address verification is performed before routing logic evaluates dispatch options): True. Aliran berturutan menunjukkan pengesahan alamat diselesaikan sebelum cabang keputusan dibuat."
        ),
        "whyWrong": (
            "• C (Express and Standard routes are executed simultaneously in parallel for every package): False. Simbol rombus ialah Decision Node (memilih salah satu laluan alternatif sahaja), bukannya Fork Node yang menjalankan kedua-duanya serentak."
        )
    },
    35: {
        "correctDisplay": "A=True, B=False, C=True, D=True",
        "whyCorrect": (
            "• A (Safety-critical sub-systems mandate a more prescriptive and rigorously validated documentation process): True. Sistem berisiko keselamatan memerlukan spesifikasi bertulis yang formal dan validasi ketat.\n"
            "• C (In a customer-specific project setting, requirements are primarily elicited from designated customer representatives): True. Projek pelanggan khusus berurusan terus dengan wakil pelanggan tertentu.\n"
            "• D (The time facet dictates whether requirements are defined upfront in one pass or evolved continuously): True. Faset masa membahagikan proses kepada Linear (sekali harung) atau Iterative (berperingkat)."
        ),
        "whyWrong": (
            "• B (An exploratory RE process is selected when requirements are completely fixed and legally binding): False. Proses eksploratori dipilih apabila keperluan masih kabur atau inovatif; jika keperluan telah tetap dan mengikat, proses preskriptif yang digunakan."
        )
    },
    42: {
        "correctDisplay": "A=True, B=False, C=True, D=False",
        "whyCorrect": (
            "• A (The Analytic Hierarchy Process evaluates requirements by performing systematic pairwise comparisons): True. AHP menggunakan matriks perbandingan berpasangan (pairwise comparison) secara matematik.\n"
            "• C (MoSCoW categorization is an example of an absolute, single-criterion ranking technique): True. MoSCoW (Must, Should, Could, Won't) mengelaskan keperluan mengikut tahap kepentingan segera."
        ),
        "whyWrong": (
            "• B (In Wiegers' method, the priority score increases when estimated implementation cost and risk increase): False. Dalam formula Wiegers: Keutamaan = Nilai / (Kos + Risiko). Kos dan risiko berada di bahagian pembahagi (denominator); kos/risiko tinggi akan MENURUNKAN skor keutamaan.\n"
            "• D (Prioritization should only consider business value to the customer, completely ignoring penalties and risks): False. IREB menegaskan pengutamaan mesti menyeimbangkan pelbagai kriteria termasuk denda undang-undang, kos pelaksanaan, dan risiko teknikal."
        )
    }
}

for q in app_data['sets']['predicted']['questions']:
    qid = q['id']
    if qid in SET_G_CUSTOM:
        exp = SET_G_CUSTOM[qid]
        q['correctDisplay'] = exp['correctDisplay']
        q['whyCorrect'] = exp['whyCorrect']
        q['whyWrong'] = exp['whyWrong']
    elif qid in ALL_OFFICIAL_EXP:
        exp = ALL_OFFICIAL_EXP[qid]
        q['correctDisplay'] = exp['correctDisplay']
        q['whyCorrect'] = exp['whyCorrect']
        q['whyWrong'] = exp['whyWrong']

# ==============================================================================
# 3. UPDATE SET RAMALAN G+ (MARITIME & AUTHENTIC LEAK SET)
# ==============================================================================
print("Updating predicted Set G+ (Maritime & Leak Set)...")
SET_G_PLUS_CUSTOM = {
    1: {
        "correctDisplay": "A=True, B=True, C=False, D=True",
        "whyCorrect": (
            "• A ('The system shall encrypt all telematics using AES-256-GCM' is a technical constraint): True. Menetapkan algoritma enkripsi khusus (AES-256) mengehadkan kebebasan reka bentuk teknikal pembangun, menjadikannya Technical Constraint.\n"
            "• B ('The port dispatcher shall be able to filter arriving vessels by gross tonnage' is a functional requirement): True. Fungsi menapis kapal mengikut tan ialah tingkah laku/fungsi sistem (Functional Requirement).\n"
            "• D ('The dashboard shall render updated radar coordinates within 800 milliseconds' is a quality requirement regarding performance): True. Had masa pemaparan (< 800ms) ialah keperluan kualiti prestasi (Quality Requirement: Performance Efficiency)."
        ),
        "whyWrong": (
            "• C ('The database backup routine must execute daily at 03:00 AM UTC' is a quality requirement regarding usability): False. Ini adalah kekangan operasi (Operational Constraint), bukannya kualiti kebolehgunaan (Usability)."
        )
    },
    6: {
        "correctDisplay": "A=True, B=True, C=False, D=True",
        "whyCorrect": (
            "• A (The system boundary separates what will be designed and implemented inside the software from the operational environment): True. Sempadan sistem mentakrifkan apa yang dibina di dalam perisian berbanding dunia luar.\n"
            "• B (The context boundary delineates the relevant operational context from the irrelevant environment): True. Sempadan konteks memisahkan konteks relevan daripada persekitaran yang tidak berkaitan.\n"
            "• D (Aspects situated within the grey zone must be clarified during requirements analysis so they are assigned either inside the system, into the context, or into the irrelevant environment): True. Zon kelabu wajib diselesaikan semasa analisis supaya setiap elemen mendapat sempadan yang jelas."
        ),
        "whyWrong": (
            "• C (The grey zone consists of aspects where the requirements engineer has conclusively confirmed that no stakeholder cares about them): False. Zon kelabu mengandungi aspek yang belum diputuskan, bukannya aspek yang sah diabaikan."
        )
    },
    13: {
        "correctDisplay": "A=True, B=False, C=True, D=True",
        "whyCorrect": (
            "• A (A requirement is 'Verifiable' if a practical test or inspection procedure can be devised to prove whether the requirement has been met): True. Boleh diuji/disahkan (Verifiable) bermaksud ada cara objektif untuk membuktikan pematuhan.\n"
            "• C (A requirement is 'Traceable' if it can be tracked back to its originating stakeholder rationale and forward to its design and verification artifacts): True. Boleh dijejak (Traceable) membolehkan jejak ke punca asal (backward) dan ke artifak hiliran (forward).\n"
            "• D (A requirement containing the phrase 'The system should be as fast as reasonably possible' violates the verifiability criterion): True. Frasa kabur 'as fast as reasonably possible' tidak mempunyai metrik berangka yang boleh diuji."
        ),
        "whyWrong": (
            "• B (A requirement is 'Unambiguous' only if it is expressed purely in formal mathematical logic and contains no natural language): False. Tidak kabur (Unambiguous) bermaksud hanya mempunyai satu tafsiran sahaja; ia tidak mewajibkan notasi matematik formal semata-mata."
        )
    },
    14: {
        "correctDisplay": "A, B",
        "whyCorrect": (
            "• A (The modal verb 'shall' indicates a strictly mandatory requirement with full legal binding commitment): Betul. 'Shall' menetapkan kewajipan undang-undang yang mengikat secara mutlak (legally mandatory).\n"
            "• B (The modal verb 'should' indicates a desirable or future goal that carries no legal necessity under contract): Betul. 'Should' menyatakan cadangan atau matlamat yang wajar tetapi tidak membawa liabiliti undang-undang mutlak."
        ),
        "whyWrong": (
            "• C (Passive voice constructions are recommended by SOPHIST because they keep sentences concise): Salah. Ayat pasif dilarang keras dalam SOPHIST kerana ia menyembunyikan pelaku/ejen yang bertanggungjawab.\n"
            "• D (The modal verb 'will' represents the highest level of legal necessity in IREB contractual requirements specifications): Salah. 'Will' hanya menyatakan niat masa depan atau kenyataan maklumat; 'shall' ialah tahap kewajipan tertinggi."
        )
    },
    15: {
        "correctDisplay": "A (Nominalization)",
        "whyCorrect": (
            "• Pilihan A (Nominalization) adalah jawapan yang betul. "
            "Penggunaan kata nama 'authentication' (daripada kata kerja proses 'authenticate') ialah kecacatan Nominalization. Ia menyembunyikan siapa yang mengesahkan, bagaimana pengesahan berlaku, dan urutan tindakan sebenar."
        ),
        "whyWrong": (
            "• B (Universal quantifier): Tiada perkataan kuantiti sejagat seperti 'all/always/never' dalam ayat soalan.\n"
            "• C (Synonym collision): Tiada pertembungan dua istilah berbeza yang bermaksud perkara yang sama.\n"
            "• D (Structural grammar inversion): Bukan kecacatan utama yang diterangkan dalam teori transformasi bahasa IREB."
        )
    },
    20: {
        "correctDisplay": "A=True, B=True, C=False, D=False",
        "whyCorrect": (
            "• A (A vessel can transition from 'At Sea' directly to 'Entering Harbor' without waiting at anchorage if the berth is not busy): True. Rajah memaparkan transisi 'approach_port [berth_busy == false]' yang membenarkan kapal masuk terus ke fasa 'Entering Harbor' tanpa perlu berlabuh sauh.\n"
            "• B (If a storm warning with wind > 40 knots occurs while entering the harbor, the vessel returns to 'Waiting at Anchorage'): True. Transisi kecemasan 'storm_warning [wind > 40kn]' mengarahkan kapal yang sedang memasuki alur pelabuhan kembali berlabuh selamat di 'Waiting at Anchorage'."
        ),
        "whyWrong": (
            "• C (A vessel can transition directly from 'At Sea' to 'Cargo Operations' in a single step): False. Tiada anak panah terus dari 'At Sea' ke 'Cargo Operations'; kapal wajib merapat di dermaga (Moored at Berth) terlebih dahulu.\n"
            "• D ('Moored at Berth' and 'Cargo Operations' are executed concurrently as parallel states in this diagram): False. Kedua-dua keadaan ini berlaku secara berurutan (sequential), bukan serentak (tiada garis putus-putus atau composite orthogonal states)."
        )
    },
    24: {
        "correctDisplay": "A (Field Observation / Apprenticeship)",
        "whyCorrect": (
            "• Pilihan A (Field Observation / Apprenticeship) adalah jawapan yang betul. "
            "Pakar navigasi pelabuhan mempunyai pengetahuan tersirat (tacit knowledge) yang sukar diungkapkan secara lisan semasa mesyuarat. Pemerhatian lapangan secara langsung (Field Observation / Apprenticeship) adalah satu-satunya teknik yang membolehkan jurutera keperluan melihat tindakan dan keputusan sebenar pakar dalam konteks kerja."
        ),
        "whyWrong": (
            "• B (Distributing a standardized multiple-choice questionnaire): Soal selidik tidak dapat menangkap nuansa tindakan tersirat yang tidak disedari oleh responden.\n"
            "• C (Conducting a formal structured interview in an off-site conference room): Temu bual bergantung kepada keupayaan pakar untuk menyatakan proses secara lisan; pakar tidak dapat menerangkan keputusan intuitif.\n"
            "• D (Performing keyword frequency analysis on archived terminal log reports): Log teks hanya merekodkan hasil data akhir, bukan proses pemikiran dan interaksi manusia."
        )
    },
    26: {
        "correctDisplay": "A (Excitement factors gradually transition into Performance factors and eventually become Basic factors)",
        "whyCorrect": (
            "• Pilihan A adalah jawapan yang betul mengikut Model Kano. "
            "Seiring dengan kematangan pasaran dan jangkaan pengguna yang meningkat, ciri produk yang asalnya merupakan faktor keterujaan (Delighters) lama-kelamaan akan dianggap perkara biasa (Performance factors) dan akhirnya menjadi faktor asas mandatori (Basic factors / Must-be)."
        ),
        "whyWrong": (
            "• B (Basic factors migrate into Delighters as customers appreciate their enduring reliability): Faktor asas tidak pernah bertukar menjadi faktor keterujaan kerana pengguna menganggapnya sebagai kewajipan lumrah.\n"
            "• C (Reverse factors spontaneously convert into One-dimensional Performance factors without user redesign): Faktor terbalik (reverse factors) menyebabkan ketidakpuasan hati apabila wujud; ia tidak bertukar sendiri tanpa reka bentuk semula.\n"
            "• D (Classifications remain completely static throughout the entire product lifecycle): Salah. Model Kano menekankan dinamik masa di mana jangkaan pelanggan sentiasa berevolusi."
        )
    },
    28: {
        "correctDisplay": "A (Unilateral avoidance / Disregard)",
        "whyCorrect": (
            "• Pilihan A (Unilateral avoidance / Disregard) adalah jawapan yang betul (ia BUKAN teknik resolusi konflik yang sah). "
            "Mengabaikan konflik atau memadamkan keperluan yang dipertikaikan secara senyap tanpa persetujuan pihak berkepentingan (Disregard / Avoidance) bukanlah penyelesaian profesional dan boleh menggagalkan projek."
        ),
        "whyWrong": (
            "• B (Consensus building through moderated stakeholder dialogue): Teknik sah penyelesaian konflik mengikut IREB melalui rundingan konsensus.\n"
            "• C (Compromise): Teknik sah di mana setiap pihak bertolak ansur untuk mencapai titik tengah yang dipersetujui.\n"
            "• D (Hierarchical Escalation): Teknik sah penyelesaian konflik melalui keputusan pemutus oleh jawatankuasa tadbir urus atau pihak atasan."
        )
    },
    31: {
        "correctDisplay": "A (Interest Conflict)",
        "whyCorrect": (
            "• Pilihan A (Interest Conflict) adalah jawapan yang betul. "
            "Kedua-dua pihak bersetuju mengenai data teknikal pergerakan kontena, tetapi mempunyai matlamat organisasi yang bercanggah (Keselamatan maksimum vs Kepantasan throughput). Percanggahan matlamat ini merupakan takrifan tepat bagi Konflik Kepentingan (Interest Conflict)."
        ),
        "whyWrong": (
            "• B (Data / Subject-matter Conflict): Percanggahan mengenai kesahihan data, fakta, atau tafsiran maklumat teknikal (dalam senario ini kedua-dua pihak bersetuju tentang fakta).\n"
            "• C (Structural Conflict): Percanggahan yang disebabkan oleh ketidakseimbangan kuasa hierarki atau kekangan sumber organisasi.\n"
            "• D (Relationship Conflict): Percanggahan emosi peribadi atau permusuhan interpersonal antara individu."
        )
    },
    33: {
        "correctDisplay": "A (The Moderator)",
        "whyCorrect": (
            "• Pilihan A (The Moderator) adalah jawapan yang betul mengikut kaedah Fagan Inspection. "
            "Moderator bertanggungjawab memimpin sesi semakan, menguatkuasakan peraturan proses, mengawal masa, dan mengekalkan tumpuan objektif sepanjang mesyuarat semakan."
        ),
        "whyWrong": (
            "• B (The Author): Pengarang dokumen yang diperiksa; pengarang tidak boleh memoderasi mesyuarat sendiri bagi mengelakkan bias dan konflik kepentingan.\n"
            "• C (The Scribe / Recorder): Bertanggungjawab merekodkan setiap kecacatan dan isu yang dikenal pasti semasa mesyuarat.\n"
            "• D (The Lead Architect): Bertindak sebagai salah seorang Reviewer/Inspector yang menyemak dokumen dari perspektif seni bina."
        )
    },
    35: {
        "correctDisplay": "A=True, B=False, C=True, D=True",
        "whyCorrect": (
            "• A (Safety-critical sub-systems mandate a more prescriptive and rigorously validated documentation process): True. Sistem berisiko tinggi (seperti radar pengelakan perlanggaran kapal) memerlukan spesifikasi preskriptif dan semakan formal yang ketat.\n"
            "• C (In a customer-specific project setting, requirements are primarily elicited from designated customer representatives): True. Projek pelanggan khusus mendapatkan keperluan secara langsung daripada wakil pelanggan yang dikenal pasti.\n"
            "• D (The time facet dictates whether requirements are defined upfront in one pass or evolved continuously across increments): True. Faset masa menentukan sama ada proses adalah Linear (sekali harung) atau Iterative (berterusan)."
        ),
        "whyWrong": (
            "• B (An exploratory RE process is selected when requirements and stakeholder goals are completely fixed and legally binding): False. Proses eksploratori digunakan apabila keperluan inovatif atau masih kabur; jika keperluan telah tetap dan mengikat, proses preskriptif yang digunakan."
        )
    },
    36: {
        "correctDisplay": "A, B",
        "whyCorrect": (
            "• A (Time Facet: Linear vs. Iterative): Betul. Faset Masa rasmi IREB membahagikan proses kepada pelaksanaan linear atau berperingkat.\n"
            "• B (Purpose Facet: Prescriptive vs. Explorative): Betul. Faset Tujuan rasmi IREB membahagikan proses kepada tujuan preskriptif kontrak atau penerokaan inovatif."
        ),
        "whyWrong": (
            "• C (Budget Facet: Fixed-Price vs. Time-and-Materials): Salah. Model perniagaan/bajet bukan salah satu daripada 4 faset proses rasmi IREB.\n"
            "• D (Architecture Facet: Monolithic vs. Microservices): Salah. Seni bina teknikal bukan faset proses konfigurasi RE piawai IREB (4 Faset: Time, Purpose, Target, Interaction)."
        )
    },
    39: {
        "correctDisplay": "A (Tracing a requirement backward to the stakeholder statement, business goal, or regulatory standard that originated it)",
        "whyCorrect": (
            "• Pilihan A adalah jawapan yang betul mengikut takrifan IREB. "
            "Pre-RS Traceability membolehkan keperluan dijejak ke belakang (backward) kepada sumber asalnya sebelum spesifikasi ditulis—seperti kenyataan pihak berkepentingan, matlamat perniagaan, minit mesyuarat, atau dokumen piawaian perundangan."
        ),
        "whyWrong": (
            "• B (Tracing a requirement forward to the source code classes and automated regression test scripts): Ini adalah takrifan untuk Post-RS Traceability (jejak ke hadapan ke artifak pembangunan dan ujian).\n"
            "• C (Tracing dependencies exclusively between requirements within the same specification document): Ini merujuk kepada Inter-Requirements Traceability.\n"
            "• D (Tracing historical defect tickets recorded during user acceptance testing): Ini adalah penjejakan kecacatan (defect traceability), bukan Pre-RS traceability."
        )
    },
    41: {
        "correctDisplay": "A, B",
        "whyCorrect": (
            "• A (Conducting an Impact Analysis to evaluate technical effort, budget variance, and ripple effects): Betul. Analisis Impak wajib dilaksanakan untuk menilai kesan teknikal, peruntukan bajet, dan kesan rantaian sebelum kelulusan diberikan.\n"
            "• B (Submitting the change request and impact evaluation to the Change Control Board for formal approval): Betul. Lembaga Kawalan Perubahan (CCB) adalah badan tadbir urus yang diberi kuasa meluluskan, menolak, atau menangguhkan permohonan perubahan."
        ),
        "whyWrong": (
            "• C (Immediately altering source code repositories before documenting the change request): Salah. Mengubah kod tanpa kelulusan formal dan dokumentasi (uncontrolled change) memusnahkan kestabilan sistem.\n"
            "• D (Discarding previously approved test cases without creating an updated baseline): Salah. Membuang kes ujian tanpa jejak audit melanggar piawaian jaminan kualiti kejuruteraan perisian."
        )
    },
    42: {
        "correctDisplay": "A=True, B=False, C=True, D=False",
        "whyCorrect": (
            "• A (The Analytic Hierarchy Process evaluates requirements by performing systematic pairwise comparisons): True. AHP menggunakan perbandingan berpasangan (pairwise comparison) yang berstruktur dan berasaskan matematik.\n"
            "• C (MoSCoW categorization is an example of an absolute, single-criterion ranking technique): True. Kaedah MoSCoW membahagikan keperluan kepada 4 bakul keutamaan mutlak (Must, Should, Could, Won't)."
        ),
        "whyWrong": (
            "• B (In Wiegers' method, the priority score increases when the estimated implementation cost and technical risk increase): False. Dalam formula Karl Wiegers: Keutamaan = Nilai / (Kos + Risiko). Kos dan risiko berada di bahagian pembahagi; jika kos atau risiko meningkat, skor keutamaan akan MENURUN, bukannya meningkat.\n"
            "• D (Prioritization should only consider business value to the customer, completely ignoring penalties and risks): False. IREB menegaskan bahawa pengutamaan yang baik mesti menyeimbangkan nilai perniagaan dengan risiko teknikal dan penalti ketidakpatuhan undang-undang."
        )
    },
    43: {
        "correctDisplay": "A (A stable, internally consistent, and formally approved set of requirements frozen at a specific milestone)",
        "whyCorrect": (
            "• Pilihan A adalah takrifan tepat bagi Requirements Baseline mengikut IREB. "
            "Baseline ialah konfigurasi sekumpulan artifak keperluan yang stabil, lengkap, bebas percanggahan, dan diluluskan secara rasmi (frozen/signed off) pada sesuatu peristiwa penting projek untuk dijadikan penanda aras kawalan perubahan."
        ),
        "whyWrong": (
            "• B (An informal scratchpad list of ideas brainstormed during initial elicitation): Nota draf awal tidak stabil dan belum diluluskan, maka ia bukan baseline.\n"
            "• C (The minimum number of test cases required to achieve 100% statement coverage): Ini metrik ujian perisian, bukan baseline keperluan.\n"
            "• D (A live, unversioned database where requirements are continually overwritten): Pangkalan data tanpa kawalan versi bercanggah secara langsung dengan konsep integriti baseline."
        )
    },
    44: {
        "correctDisplay": "A=True, B=True, C=False, D=True",
        "whyCorrect": (
            "• A (A suitable RE tool must support bidirectional traceability between requirements and verification artifacts): True. Kebolehkesanan dwiarah (bidirectional traceability) adalah ciri teras yang mesti disokong oleh alatan RE moden.\n"
            "• B (Role-based access control and comprehensive version history are essential capabilities): True. Kawalan akses berasaskan peranan (RBAC) dan sejarah versi lengkap diperlukan untuk kerjasama berpasukan yang selamat.\n"
            "• D (Tool integration interfaces are vital to connect RE data with test management and bug tracking systems): True. Antara muka integrasi (seperti REST API atau piawaian OSLC) membolehkan pertukaran data yang lancar dengan alatan pembangunan lain."
        ),
        "whyWrong": (
            "• C (Introducing a sophisticated RE tool automatically corrects poorly phrased or missing requirements): False. Alatan perisian tidak boleh membetulkan keperluan yang kabur atau mencari keperluan yang hilang secara ajaib tanpa kepakaran jurutera manusia ('A fool with a tool is still a fool')."
        )
    }
}

for q in app_data['sets']['predicted_maritime']['questions']:
    qid = q['id']
    if qid in SET_G_PLUS_CUSTOM:
        exp = SET_G_PLUS_CUSTOM[qid]
        q['correctDisplay'] = exp['correctDisplay']
        q['whyCorrect'] = exp['whyCorrect']
        q['whyWrong'] = exp['whyWrong']
    elif qid in SET_G_CUSTOM:
        exp = SET_G_CUSTOM[qid]
        q['correctDisplay'] = exp['correctDisplay']
        q['whyCorrect'] = exp['whyCorrect']
        q['whyWrong'] = exp['whyWrong']
    elif qid in ALL_OFFICIAL_EXP:
        exp = ALL_OFFICIAL_EXP[qid]
        q['correctDisplay'] = exp['correctDisplay']
        q['whyCorrect'] = exp['whyCorrect']
        q['whyWrong'] = exp['whyWrong']

# Save updated dataset
with open(DATA_PATH, 'w', encoding='utf-8') as f:
    json.dump(app_data, f, indent=2, ensure_ascii=False)

print("Saved all updated explanations to data/app_data.json successfully!")
