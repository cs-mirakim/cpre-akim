import json
import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(ROOT_DIR, 'data', 'app_data.json')
EU_DATA_PATH = os.path.join(ROOT_DIR, 'data', 'eu_study_data.json')

sys.path.append(os.path.join(ROOT_DIR, 'scripts'))
from scratch.build_eu_kb import EU_KNOWLEDGE_BASE
from scratch.build_all_drill_questions import get_additional_drill_questions

with open(DATA_PATH, 'r', encoding='utf-8') as f:
    app_data = json.load(f)

# Standardize options and question fields
def normalize_question(q, default_source="Set Latihan"):
    norm = dict(q)
    
    # 1. Identification & Classification
    norm_id = q.get('id') or q.get('code')
    if default_source.startswith("Set Rasmi") and str(norm_id).isdigit():
        norm['id'] = f"OFF-{int(norm_id):02d}"
        norm['code'] = q.get('code') or f"A{int(norm_id)}"
    elif default_source.startswith("Set Ramalan") and str(norm_id).isdigit():
        norm['id'] = f"PRED-{int(norm_id):02d}"
        norm['code'] = q.get('code') or f"G{int(norm_id)}"
    else:
        norm['id'] = str(norm_id)
        norm['code'] = str(q.get('code') or norm_id)
    
    eu_no = q.get('euNo')
    if not eu_no and 'euId' in q:
        try:
            eu_no = int(q['euId'].replace('EU', '').strip())
        except:
            eu_no = 1
    elif not eu_no:
        eu_no = 1
    norm['euNo'] = int(eu_no)
    norm['euId'] = f"EU{norm['euNo']}"
    
    norm['topic'] = q.get('topic') or q.get('title') or f"Topik EU {norm['euNo']}"
    norm['title'] = norm['topic']
    norm['type'] = q.get('type', 'A').upper()
    norm['pts'] = int(q.get('pts') or q.get('points') or (2 if norm['type'] in ['K', 'P'] else 1))
    
    # 2. Text Content (English Question)
    norm['question'] = q.get('question') or q.get('text') or ""
    
    # 3. Standardize Options Array
    standard_options = []
    if norm['type'] == 'K':
        if 'subQuestions' in q:
            for sq in q['subQuestions']:
                standard_options.append({
                    'id': sq['id'],
                    'text': sq['text'],
                    'truth': bool(sq.get('truth', sq.get('isCorrect', False)))
                })
        elif 'options' in q:
            for opt in q['options']:
                standard_options.append({
                    'id': opt['id'],
                    'text': opt['text'],
                    'truth': bool(opt.get('truth', False))
                })
    else:
        # Single (A) or Multiple (P) Choice
        raw_options = q.get('options', [])
        correct_answers = q.get('correctAnswers', [])
        for opt in raw_options:
            is_truth = False
            if 'truth' in opt:
                is_truth = bool(opt['truth'])
            elif opt['id'] in correct_answers:
                is_truth = True
            standard_options.append({
                'id': opt['id'],
                'text': opt['text'],
                'truth': is_truth
            })
    norm['options'] = standard_options
    
    # 4. Correct Display
    if not norm.get('correctDisplay'):
        if norm['type'] == 'K':
            parts = [f"{o['id']}={'True' if o['truth'] else 'False'}" for o in standard_options]
            norm['correctDisplay'] = ", ".join(parts)
        else:
            correct_ids = [o['id'] for o in standard_options if o['truth']]
            norm['correctDisplay'] = ", ".join(correct_ids)
            
    # 5. Explanations (Bilingual & Technical)
    exp = q.get('explanation', {})
    if isinstance(exp, dict):
        norm['whyCorrect'] = q.get('whyCorrect') or exp.get('whyCorrect') or exp.get('summary') or ""
        norm['whyWrong'] = q.get('whyWrong') or exp.get('whyWrong') or ""
        norm['trapAlert'] = q.get('trapAlert') or q.get('extra') or exp.get('trapAlert') or ""
        norm['handbookRef'] = q.get('handbookRef') or exp.get('handbookRef') or f"CPRE Foundation Level - Handbook V.1.2.0 (Bab {norm['euNo']})"
    else:
        norm['whyCorrect'] = q.get('whyCorrect', '')
        norm['whyWrong'] = q.get('whyWrong', '')
        norm['trapAlert'] = q.get('trapAlert') or q.get('extra', '')
        norm['handbookRef'] = q.get('handbookRef') or f"CPRE Foundation Level - Handbook V.1.2.0 (Bab {norm['euNo']})"
        
    norm['mnemonic'] = q.get('mnemonic', '')
    
    # 6. Diagram HTML
    raw_diag = q.get('diagramHtml')
    if raw_diag and isinstance(raw_diag, str):
        # Ensure clean styling and click-to-zoom
        if 'openImageModal' not in raw_diag and '<img' in raw_diag:
            raw_diag = raw_diag.replace('<img', '<img onclick="openImageModal(this.src)" style="cursor: zoom-in;"')
        norm['diagramHtml'] = raw_diag
    else:
        norm['diagramHtml'] = None
        
    # 7. Source Tag
    norm['sourceSet'] = q.get('sourceSet') or default_source
    
    return norm

# Process Official and Predicted sets
official_raw = app_data['sets']['official']['questions']
predicted_raw = app_data['sets']['predicted']['questions']
additional_raw = get_additional_drill_questions()

official_norm = [normalize_question(q, default_source="Set Rasmi (Official Exam)") for q in official_raw]
predicted_norm = [normalize_question(q, default_source="Set Ramalan G (Exam Pool)") for q in predicted_raw]
additional_norm = [normalize_question(q, default_source="Bank Soalan Latihan & Ekstraksi") for q in additional_raw]

# Update back to app_data sets so everything stays 100% consistent
app_data['sets']['official']['questions'] = official_norm
app_data['sets']['predicted']['questions'] = predicted_norm

# Build Master EU Catalog
eu_drill_catalog = {}

for eu_key, kb in EU_KNOWLEDGE_BASE.items():
    eu_drill_catalog[eu_key] = {
        "id": kb["id"],
        "code": kb["code"],
        "title": kb["title"],
        "titleBm": kb["titleBm"],
        "examWeight": kb["examWeight"],
        "memoryAnchors": kb["memoryAnchors"],
        "deepDiveNotes": kb["deepDiveNotes"],
        "questions": []
    }

def add_questions_to_catalog(q_list):
    for q in q_list:
        eu_key = q['euId']
        if eu_key in eu_drill_catalog:
            existing_ids = [item['id'] for item in eu_drill_catalog[eu_key]['questions']]
            if q['id'] not in existing_ids:
                eu_drill_catalog[eu_key]['questions'].append(q)

# Add all sets into EU catalog
add_questions_to_catalog(official_norm)
add_questions_to_catalog(predicted_norm)
add_questions_to_catalog(additional_norm)

# Sort questions within each EU by source and number
for eu_key in eu_drill_catalog:
    eu_drill_catalog[eu_key]['questions'].sort(key=lambda x: (x.get('sourceSet', ''), x['id']))

print("==================================================")
print("CPRE EU DRILL CATALOG COMPILED SUCCESSFULLY")
print("==================================================")
total_questions = 0
for k, v in eu_drill_catalog.items():
    cnt = len(v['questions'])
    total_questions += cnt
    print(f"  {k} ({v['code']} - {v['title']}): {cnt} soalan")
print("--------------------------------------------------")
print(f"TOTAL SOALAN ULANGKAJI KESELURUHAN: {total_questions}")
print("==================================================")

# Save standalone data/eu_study_data.json
with open(EU_DATA_PATH, 'w', encoding='utf-8') as f:
    json.dump(eu_drill_catalog, f, ensure_ascii=False, indent=2)
print(f"Saved {EU_DATA_PATH}")

# Attach to master app_data.json
app_data['eu_drill'] = eu_drill_catalog

# Also ensure set selection has only 'official' and 'predicted'
app_data['sets']['predicted']['name'] = "Set Ramalan G (Exam Pool)"
app_data['sets']['predicted']['description'] = "45 Soalan Ramalan CPRE FL 3.4 Berasaskan Domain Maritim & Keselamatan Operasi (72 Pts)"

with open(DATA_PATH, 'w', encoding='utf-8') as f:
    json.dump(app_data, f, ensure_ascii=False, indent=2)
print(f"Updated {DATA_PATH} with normalized datasets and eu_drill catalog!")
