const fs = require('fs');
const path = require('path');

const rootDir = path.basename(__dirname) === 'scripts' ? path.resolve(__dirname, '..') : __dirname;
const dataFile = fs.existsSync(path.join(rootDir, 'data', 'app_data.json')) 
  ? path.join(rootDir, 'data', 'app_data.json') 
  : path.join(rootDir, 'app_data.json');
const templateFile = path.join(rootDir, 'scripts', 'template.html');
const outHtmlPath = path.join(rootDir, 'index.html');

const { eus, questions } = JSON.parse(fs.readFileSync(dataFile, 'utf8'));

// Counts
const kCount = questions.filter(q => q.type === 'K').length;
const aCount = questions.filter(q => q.type === 'A').length;
const pCount = questions.filter(q => q.type === 'P').length;

function extractImgSrc(html) {
  const match = html.match(/src=["']([^"']+)["']/);
  return match ? match[1] : '';
}

// Enhance diagrams
questions.forEach(q => {
  if (q.diagramHtml && q.diagramHtml.includes('<img')) {
    const imgSrc = extractImgSrc(q.diagramHtml);
    q.diagramHtml = `
      <div class="my-4 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-950 p-3 sm:p-4 shadow-sm">
        <div class="flex items-center justify-between pb-2 mb-2 border-b border-zinc-100 dark:border-zinc-800/80 text-xs">
          <span class="font-bold text-zinc-700 dark:text-zinc-300 flex items-center gap-1.5">
            <svg class="w-3.5 h-3.5 text-zinc-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
            Gambar Rajah Rasmi Soalan Q${q.id}
          </span>
          <button onclick="openImageModal('diag-img-${q.id}')" class="text-[11px] font-medium text-zinc-500 hover:text-zinc-900 dark:hover:text-zinc-100 flex items-center gap-1 transition-colors">
            <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0zM10 7v6m3-3H7"/></svg>
            Besarkan
          </button>
        </div>
        <div class="bg-white rounded-lg p-2 sm:p-4 flex items-center justify-center overflow-x-auto">
          <img id="diag-img-${q.id}" src="${imgSrc}" alt="Diagram Q${q.id}" class="max-w-full h-auto max-h-[380px] object-contain rounded cursor-zoom-in transition-transform duration-200 hover:scale-[1.01]" onclick="openImageModal('diag-img-${q.id}')" />
        </div>
      </div>
    `;
  }
});

const euButtonsHtml = eus.map(eu => `
  <button onclick="filterByEU(${eu.no})" class="eu-btn px-2.5 py-1 rounded-md text-xs font-medium bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300 hover:bg-slate-200 dark:hover:bg-zinc-700 shrink-0 flex items-center gap-1.5 border border-slate-200 dark:border-zinc-700/60" data-eu="${eu.no}">
    <span class="w-1.5 h-1.5 rounded-full ${eu.no === 5 || eu.no === 6 ? 'bg-rose-500' : 'bg-slate-400 dark:bg-zinc-500'}"></span>
    EU${eu.no} (${eu.range})
  </button>
`).join('');

const tocDrawerHtml = eus.map(eu => {
  const qList = questions.filter(q => q.euNo === eu.no);
  return `
    <div>
      <div class="text-[11px] font-bold text-slate-600 dark:text-zinc-400 mb-1.5 flex items-center justify-between">
        <span class="flex items-center gap-1.5">
          <span class="w-1.5 h-1.5 rounded-full ${eu.no === 5 || eu.no === 6 ? 'bg-rose-500' : 'bg-indigo-500'}"></span>
          EU${eu.no}: ${eu.name}
        </span>
        <span class="font-mono text-[10px] font-medium text-slate-400">${eu.range}</span>
      </div>
      <div class="grid grid-cols-6 sm:grid-cols-9 gap-1.5">
        ${qList.map(q => `
          <button 
            onclick="jumpToQuestion(${q.id})" 
            id="drawerBtnQ${q.id}" 
            class="h-8 rounded-lg text-xs font-mono font-bold border text-center flex items-center justify-center transition-all bg-slate-50 dark:bg-zinc-950 border-slate-200 dark:border-zinc-800 text-slate-800 dark:text-zinc-200 hover:bg-zinc-900 hover:text-white dark:hover:bg-white dark:hover:text-zinc-950 active:scale-95"
          >
            Q${q.id}
          </button>
        `).join('')}
      </div>
    </div>
  `;
}).join('');

let template = fs.readFileSync(templateFile, 'utf8');
template = template.replace('/* APP_DATA_PLACEHOLDER */ null', JSON.stringify({ eus, questions }));
template = template.replace('<!-- EU_BUTTONS_PLACEHOLDER -->', euButtonsHtml);
template = template.replace('<!-- TOC_DRAWER_PLACEHOLDER -->', tocDrawerHtml);
template = template.replace(/<!-- QUESTIONS_COUNT -->/g, questions.length);
template = template.replace(/<!-- K_COUNT -->/g, kCount);
template = template.replace(/<!-- A_COUNT -->/g, aCount);
template = template.replace(/<!-- P_COUNT -->/g, pCount);

fs.writeFileSync(outHtmlPath, template, 'utf8');
console.log(`Generated upgraded ${outHtmlPath} with template substitution! Size: ${template.length} bytes`);
