import openpyxl
import json

wb = openpyxl.load_workbook('docs/CorrectionAidForThePracticeExam_EN_2025-09-11.xlsx', data_only=True)
ws = wb.active

with open('data/app_data.json', 'r', encoding='utf-8') as f:
    app_data = json.load(f)

app_questions = {q['id']: q for q in app_data['questions']}

col_idx = 2
excel_data = {}
letters = ['A', 'B', 'C', 'D', 'E', 'F']

while col_idx <= ws.max_column:
    val = ws.cell(row=1, column=col_idx).value
    if isinstance(val, int):
        q_num = val
        q_id = ws.cell(row=2, column=col_idx).value
        q_type = q_id[0]
        q_pts = ws.cell(row=4, column=col_idx).value
        q_num_ans = ws.cell(row=5, column=col_idx).value
        
        answers = {}
        if q_type == 'K':
            num_rows = q_num_ans
            for i in range(num_rows):
                r = 7 + i
                key1 = ws.cell(row=r, column=col_idx+2).value
                answers[letters[i]] = True if key1 == 1 else False
            excel_data[q_num] = {
                'id': q_id, 'type': q_type, 'pts': q_pts, 'num_ans': q_num_ans, 'answers': answers
            }
            col_idx += 5
        else:
            correct_opts = []
            for i in range(6):
                r = 7 + i
                key = ws.cell(row=r, column=col_idx+1).value
                if key == 1:
                    correct_opts.append(letters[i])
            excel_data[q_num] = {
                'id': q_id, 'type': q_type, 'pts': q_pts, 'num_ans': q_num_ans, 'answers': correct_opts
            }
            col_idx += 3
    else:
        col_idx += 1

print(f'Parsed {len(excel_data)} questions from Excel.\n')

mismatches = []
pts_total_excel = sum(q['pts'] for q in excel_data.values())
pts_total_app = sum(q['pts'] for q in app_data['questions'])

print(f"Total Points: Excel = {pts_total_excel}, App = {pts_total_app}")

for q_num, ex in excel_data.items():
    app_q = app_questions.get(q_num)
    if not app_q:
        mismatches.append(f"Q{q_num} missing in app_data.json")
        continue
    if app_q['type'] != ex['type']:
        mismatches.append(f"Q{q_num} type mismatch: app={app_q['type']}, ex={ex['type']}")
    if app_q['pts'] != ex['pts']:
        mismatches.append(f"Q{q_num} pts mismatch: app={app_q['pts']}, ex={ex['pts']}")
    
    if ex['type'] == 'K':
        for opt in app_q['options']:
            opt_id = opt['id']
            expected_truth = ex['answers'].get(opt_id)
            actual_truth = opt.get('truth')
            if isinstance(actual_truth, str):
                s = actual_truth.strip().lower()
                if s.startswith('does not') or 'false' in s or 'incorrect' in s:
                    actual_truth = False
                elif s in ['matches', 'applies', 'true', 'correct'] or 'needs to be considered' in s:
                    actual_truth = True
            if actual_truth != expected_truth:
                mismatches.append(f"Q{q_num} ({ex['id']}) Option {opt_id} truth: app={opt.get('truth')} ({actual_truth}), Excel={expected_truth}")
    else:
        # For A and P type:
        app_correct = []
        for o in app_q['options']:
            t = o.get('truth')
            if t is True or t == 'correct':
                app_correct.append(o['id'])
            elif isinstance(t, str) and 'correct' in t.lower() and 'incorrect' not in t.lower():
                app_correct.append(o['id'])
        
        if set(app_correct) != set(ex['answers']):
            mismatches.append(f"Q{q_num} ({ex['id']}) type {ex['type']}: app={app_correct}, Excel={ex['answers']}")

print(f"\nTotal mismatches found: {len(mismatches)}")
for m in mismatches:
    print(" -", m)

if len(mismatches) == 0:
    print("\n>>> ALL 45 QUESTIONS, TYPES, POINTS, AND ANSWER KEYS ARE 100% IN FULL TALLY WITH EXCEL CORRECTION AID! <<<")
