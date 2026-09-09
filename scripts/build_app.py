import json
import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(ROOT_DIR, 'data', 'app_data.json')
TEMPLATE_PATH = os.path.join(ROOT_DIR, 'scripts', 'template.html')
OUT_HTML_PATH = os.path.join(ROOT_DIR, 'index.html')

with open(DATA_PATH, 'r', encoding='utf-8') as f:
    app_data = json.load(f)

eus = app_data['eus']
questions = app_data['questions']

# Counts
k_count = len([q for q in questions if q['type'] == 'K'])
a_count = len([q for q in questions if q['type'] == 'A'])
p_count = len([q for q in questions if q['type'] == 'P'])

def extract_img_src(html):
    m = re.search(r'src=["\']([^"\']+)["\']', html)
    return m.group(1) if m else ''

# Clean and enhance diagrams
for q in questions:
    diag = q.get('diagramHtml', '')
    if diag and '<img' in diag:
        img_src = extract_img_src(diag)
        qid = q['id']
        q['diagramHtml'] = f'''
        <div class="my-4 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-950 p-3 sm:p-4 shadow-sm">
          <div class="flex items-center justify-between pb-2 mb-2 border-b border-zinc-100 dark:border-zinc-800/80 text-xs">
            <span class="font-bold text-zinc-700 dark:text-zinc-300 flex items-center gap-1.5">
              <svg class="w-3.5 h-3.5 text-zinc-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
              Gambar Rajah Rasmi Soalan Q{qid}
            </span>
            <button onclick="openImageModal('diag-img-{qid}')" class="text-[11px] font-medium text-zinc-500 hover:text-zinc-900 dark:hover:text-zinc-100 flex items-center gap-1 transition-colors">
              <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0zM10 7v6m3-3H7"/></svg>
              Besarkan
            </button>
          </div>
          <div class="bg-white rounded-lg p-2 sm:p-4 flex items-center justify-center overflow-x-auto">
            <img id="diag-img-{qid}" src="{img_src}" alt="Diagram Q{qid}" class="max-w-full h-auto max-h-[380px] object-contain rounded cursor-zoom-in transition-transform duration-200 hover:scale-[1.01]" onclick="openImageModal('diag-img-{qid}')" />
          </div>
        </div>
        '''

eu_btn_list = []
for eu in eus:
    no = eu['no']
    rng = eu['range']
    dot_color = 'bg-rose-500' if (no == 5 or no == 6) else 'bg-slate-400 dark:bg-zinc-500'
    eu_btn_list.append(f'''
      <button onclick="filterByEU({no})" class="eu-btn px-2.5 py-1 rounded-md text-xs font-medium bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300 hover:bg-slate-200 dark:hover:bg-zinc-700 shrink-0 flex items-center gap-1.5 border border-slate-200 dark:border-zinc-700/60" data-eu="{no}">
        <span class="w-1.5 h-1.5 rounded-full {dot_color}"></span>
        EU{no} ({rng})
      </button>
    ''')
eu_buttons_html = ''.join(eu_btn_list)

drawer_blocks = []
for eu in eus:
    no = eu['no']
    name = eu['name']
    rng = eu['range']
    dot_color = 'bg-rose-500' if (no == 5 or no == 6) else 'bg-indigo-500'
    
    q_btns = []
    for q in questions:
        if q['euNo'] == no:
            qid = q['id']
            q_btns.append(f'''
              <button 
                onclick="jumpToQuestion({qid})" 
                id="drawerBtnQ{qid}" 
                class="h-8 rounded-lg text-xs font-mono font-bold border text-center flex items-center justify-center transition-all bg-slate-50 dark:bg-zinc-950 border-slate-200 dark:border-zinc-800 text-slate-800 dark:text-zinc-200 hover:bg-zinc-900 hover:text-white dark:hover:bg-white dark:hover:text-zinc-950 active:scale-95"
              >
                Q{qid}
              </button>
            ''')
    
    drawer_blocks.append(f'''
      <div>
        <div class="text-[11px] font-bold text-slate-600 dark:text-zinc-400 mb-1.5 flex items-center justify-between">
          <span class="flex items-center gap-1.5">
            <span class="w-1.5 h-1.5 rounded-full {dot_color}"></span>
            EU{no}: {name}
          </span>
          <span class="font-mono text-[10px] font-medium text-slate-400">{rng}</span>
        </div>
        <div class="grid grid-cols-6 sm:grid-cols-9 gap-1.5">
          {''.join(q_btns)}
        </div>
      </div>
    ''')

toc_drawer_items_html = ''.join(drawer_blocks)

app_data_json_str = json.dumps({'eus': eus, 'questions': questions}, ensure_ascii=False)

with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
    template_content = f.read()

rendered = template_content.replace('/* APP_DATA_PLACEHOLDER */ null', app_data_json_str)
rendered = rendered.replace('<!-- EU_BUTTONS_PLACEHOLDER -->', eu_buttons_html)
rendered = rendered.replace('<!-- TOC_DRAWER_PLACEHOLDER -->', toc_drawer_items_html)
rendered = rendered.replace('<!-- QUESTIONS_COUNT -->', str(len(questions)))
rendered = rendered.replace('<!-- K_COUNT -->', str(k_count))
rendered = rendered.replace('<!-- A_COUNT -->', str(a_count))
rendered = rendered.replace('<!-- P_COUNT -->', str(p_count))

with open(OUT_HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(rendered)

print(f"Generated {OUT_HTML_PATH} successfully! Size: {len(rendered)} bytes")
