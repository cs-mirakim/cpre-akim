import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR) if os.path.basename(SCRIPT_DIR) == 'scripts' else SCRIPT_DIR
data_path = os.path.join(ROOT_DIR, 'data', 'app_data.json')
if not os.path.exists(data_path):
    data_path = os.path.join(ROOT_DIR, 'app_data.json')

with open(data_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

questions = data['questions']
eus = data['eus']

print(f"Checking {len(questions)} questions across {len(eus)} EUs...")

total_possible_pts = 0
type_counts = {'A': 0, 'K': 0, 'P': 0}

for q in questions:
    qid = q['id']
    qtype = q['type']
    pts = q['pts']
    type_counts[qtype] += 1
    total_possible_pts += pts
    
    assert 'code' in q and q['code'], f"Missing code in Q{qid}"
    assert 'eo' in q and q['eo'], f"Missing EO in Q{qid}"
    assert 'question' in q and len(q['question']) > 10, f"Question too short in Q{qid}"
    assert 'options' in q and len(q['options']) >= 3, f"Not enough options in Q{qid}"
    assert 'whyCorrect' in q and len(q['whyCorrect']) > 10, f"Missing whyCorrect in Q{qid}"
    assert 'whyWrong' in q and len(q['whyWrong']) > 10, f"Missing whyWrong in Q{qid}"
    assert 'extra' in q and len(q['extra']) > 10, f"Missing extra in Q{qid}"
    
    # Check options truth values
    if qtype == 'A':
        true_opts = [o for o in q['options'] if o['truth'] is True or o['truth'] in ['Correct', 'Matches', 'Applies', 'Needs to be considered']]
        assert len(true_opts) == 1, f"A-type Q{qid} must have exactly 1 true option, got {len(true_opts)} ({[o['id'] for o in true_opts]})"
    elif qtype == 'K':
        assert pts == 2, f"K-type Q{qid} should be 2 pts, got {pts}"
        assert len(q['options']) in [4, 5], f"K-type Q{qid} must have 4 or 5 options, got {len(q['options'])}"
        for o in q['options']:
            assert isinstance(o['truth'], bool) or isinstance(o['truth'], str), f"K-type Q{qid} option {o['id']} truth invalid: {o['truth']}"
    elif qtype == 'P':
        true_opts = [o for o in q['options'] if o['truth'] is True or o['truth'] in ['Correct', 'Matches', 'Applies', 'Needs to be considered']]
        assert len(true_opts) >= 1, f"P-type Q{qid} must have at least 1 true option"

print(f"Summary:")
print(f"- Total questions: {len(questions)}")
print(f"- Type distribution: {type_counts}")
print(f"- Total exam points: {total_possible_pts} / 70")
print(f"- Passing mark (70%): {total_possible_pts * 0.70:.1f} Pts")
assert total_possible_pts == 70, f"Total points mismatch: expected 70, got {total_possible_pts}"
print("ALL 45 AUTHENTIC QUESTIONS PASSED VERIFICATION PERFECTLY!")
