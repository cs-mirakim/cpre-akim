import json
import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(ROOT_DIR, 'data', 'app_data.json')
TEMPLATE_PATH = os.path.join(ROOT_DIR, 'scripts', 'template.html')
OUT_HTML_PATH = os.path.join(ROOT_DIR, 'index.html')

with open(DATA_PATH, 'r', encoding='utf-8') as f:
    app_data = json.load(f)

def extract_img_src(html):
    m = re.search(r'src=["\']([^"\']+)["\']', html)
    return m.group(1) if m else ''

def wrap_diagrams(questions_list, prefix=""):
    for q in questions_list:
        diag = q.get('diagramHtml', '')
        if diag and '<img' in diag:
            img_src = extract_img_src(diag)
            qid = q['id']
            img_elem_id = f"diag-img-{prefix}{qid}" if prefix else f"diag-img-{qid}"
            q['diagramHtml'] = f'''
            <div class="my-4 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-950 p-3 sm:p-4 shadow-sm">
              <div class="flex items-center justify-between pb-2 mb-2 border-b border-zinc-100 dark:border-zinc-800/80 text-xs">
                <span class="font-bold text-zinc-700 dark:text-zinc-300 flex items-center gap-1.5">
                  <svg class="w-3.5 h-3.5 text-zinc-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
                  Gambar Rajah Soalan Q{qid}
                </span>
                <button onclick="openImageModal('{img_elem_id}')" class="text-[11px] font-medium text-zinc-500 hover:text-zinc-900 dark:hover:text-zinc-100 flex items-center gap-1 transition-colors">
                  <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0zM10 7v6m3-3H7"/></svg>
                  Besarkan
                </button>
              </div>
              <div class="bg-white rounded-lg p-2 sm:p-4 flex items-center justify-center overflow-x-auto">
                <img id="{img_elem_id}" src="{img_src}" alt="Diagram Q{qid}" class="max-w-full h-auto max-h-[380px] object-contain rounded cursor-zoom-in transition-transform duration-200 hover:scale-[1.01]" onclick="openImageModal('{img_elem_id}')" />
              </div>
            </div>
            '''

# Wrap diagrams for both sets
if 'sets' in app_data:
    wrap_diagrams(app_data['sets']['official']['questions'], prefix="off-")
    wrap_diagrams(app_data['sets']['predicted']['questions'], prefix="pred-")
    # default questions point to official or predicted
    app_data['questions'] = app_data['sets']['official']['questions']
else:
    wrap_diagrams(app_data['questions'])

app_data_json_str = json.dumps(app_data, ensure_ascii=False)

with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
    template_content = f.read()

rendered = template_content.replace('/* APP_DATA_PLACEHOLDER */ null', app_data_json_str)

with open(OUT_HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(rendered)

print(f"Generated {OUT_HTML_PATH} successfully! Size: {len(rendered)} bytes")
