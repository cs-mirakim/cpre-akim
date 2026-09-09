const fs = require('fs');
const path = require('path');

const rootDir = path.basename(__dirname) === 'scripts' ? path.resolve(__dirname, '..') : __dirname;
const dataFile = fs.existsSync(path.join(rootDir, 'data', 'app_data.json')) 
  ? path.join(rootDir, 'data', 'app_data.json') 
  : path.join(rootDir, 'app_data.json');

const { eus, questions } = JSON.parse(fs.readFileSync(dataFile, 'utf8'));

// Calculate question counts by type
const kCount = questions.filter(q => q.type === 'K').length;
const aCount = questions.filter(q => q.type === 'A').length;
const pCount = questions.filter(q => q.type === 'P').length;

// Clean and enhance diagrams to ensure high contrast, rounded containers and interactive zoom trigger
questions.forEach(q => {
  if (q.diagramHtml) {
    // If it contains an <img> tag with Base64, wrap it cleanly with light container & click-to-zoom
    if (q.diagramHtml.includes('<img')) {
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
            <img id="diag-img-${q.id}" src="${extractImgSrc(q.diagramHtml)}" alt="Diagram Q${q.id}" class="max-w-full h-auto max-h-[380px] object-contain rounded cursor-zoom-in transition-transform duration-200 hover:scale-[1.01]" onclick="openImageModal('diag-img-${q.id}')" />
          </div>
        </div>
      `;
    }
  }
});

function extractImgSrc(html) {
  const match = html.match(/src=["']([^"']+)["']/);
  return match ? match[1] : '';
}

const htmlContent = `<!DOCTYPE html>
<html lang="ms" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>CPRE FL 3.3.2 Study Master • IREB Exam Hub</title>
  <meta name="description" content="Platform Pembelajaran IREB CPRE Foundation Level 3.3.2 - 45 Soalan Peperiksaan Lengkap, Huraian Mendalam, dan Formula Target Lulus.">
  
  <!-- Inter & JetBrains Mono Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            sans: ['"Inter"', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'ui-monospace', 'monospace'],
          },
          colors: {
            zinc: {
              850: '#141417',
              900: '#101014',
              925: '#0c0c0f',
              950: '#070709',
            },
            brand: {
              50: '#eef2ff',
              100: '#e0e7ff',
              500: '#6366f1',
              600: '#4f46e5',
              700: '#4338ca',
            }
          },
          boxShadow: {
            'card-dark': '0 1px 3px 0 rgba(0, 0, 0, 0.4), 0 1px 2px -1px rgba(0, 0, 0, 0.4)',
            'subtle': '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
          }
        }
      }
    }
  </script>
  
  <style>
    /* Custom Scrollbars */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    .dark ::-webkit-scrollbar-track { background: #070709; }
    .dark ::-webkit-scrollbar-thumb { background: #27272a; border-radius: 9999px; }
    .dark ::-webkit-scrollbar-thumb:hover { background: #3f3f46; }
    ::-webkit-scrollbar-track { background: #f4f4f5; }
    ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 9999px; }
    ::-webkit-scrollbar-thumb:hover { background: #94a3b8; }

    /* Native View Transitions (Titisan Air yang Tenang) */
    ::view-transition-old(root),
    ::view-transition-new(root) {
      animation: none;
      mix-blend-mode: normal;
    }
    ::view-transition-old(root) {
      z-index: 1;
    }
    ::view-transition-new(root) {
      z-index: 999999;
    }

    /* Tactile theme icon rotation */
    #themeToggleBtn svg {
      transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.3s ease;
    }
    #themeToggleBtn:hover svg {
      transform: rotate(25deg) scale(1.1);
    }
    #themeToggleBtn:active svg {
      transform: scale(0.9);
    }

    /* Touch targets and smoothness */
    button, a { -webkit-tap-highlight-color: transparent; }

    @media print {
      .no-print { display: none !important; }
      body { background: #fff !important; color: #000 !important; }
      .q-card { break-inside: avoid; border-color: #e2e8f0 !important; }
    }
  </style>
</head>

<body class="bg-slate-50 dark:bg-zinc-950 text-slate-800 dark:text-zinc-100 font-sans antialiased min-h-screen pb-24 md:pb-12 selection:bg-indigo-500/20">

  <!-- TOP STICKY NAVIGATION BAR (shadcn header style) -->
  <header class="sticky top-0 z-40 bg-white/90 dark:bg-zinc-950/90 backdrop-blur-md border-b border-slate-200 dark:border-zinc-800/90">
    <div class="max-w-5xl mx-auto px-4 h-14 flex items-center justify-between gap-2">
      
      <!-- Brand & Version Info -->
      <div class="flex items-center space-x-3">
        <div class="w-8 h-8 rounded-lg bg-zinc-900 dark:bg-white text-white dark:text-zinc-950 flex items-center justify-center font-bold text-xs tracking-tight shadow-sm">
          RE
        </div>
        <div>
          <div class="flex items-center space-x-2">
            <span class="font-bold text-sm tracking-tight text-slate-900 dark:text-white">CPRE FL 3.3.2</span>
            <span class="inline-flex items-center px-1.5 py-0.5 rounded text-[10px] font-mono font-medium bg-slate-100 dark:bg-zinc-800 text-slate-600 dark:text-zinc-400 border border-slate-200 dark:border-zinc-700/60 hidden sm:inline-flex">
              IREB Standard
            </span>
          </div>
        </div>
      </div>

      <!-- Center / Right Controls -->
      <div class="flex items-center space-x-2">
        
        <!-- Mode Switch Segmented Control -->
        <div class="flex items-center p-0.5 rounded-lg bg-slate-100 dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800">
          <button 
            id="modeStudyBtn" 
            onclick="setMode('study')" 
            class="px-3 py-1 rounded-md text-xs font-semibold bg-white dark:bg-zinc-800 text-slate-900 dark:text-white shadow-xs transition-all"
          >
            Study Mode
          </button>
          <button 
            id="modeQuizBtn" 
            onclick="setMode('quiz')" 
            class="px-3 py-1 rounded-md text-xs font-medium text-slate-600 dark:text-zinc-400 hover:text-slate-900 dark:hover:text-white transition-all"
          >
            Quiz Mode
          </button>
        </div>

        <!-- Bookmarks Filter Button -->
        <button 
          onclick="toggleBookmarkFilter()" 
          id="bookmarkFilterBtn" 
          class="h-8 px-2.5 rounded-lg bg-white dark:bg-zinc-900 hover:bg-slate-100 dark:hover:bg-zinc-800 border border-slate-200 dark:border-zinc-800 text-slate-700 dark:text-zinc-300 flex items-center space-x-1.5 transition-all text-xs font-semibold shadow-xs"
          title="Tapis soalan bertanda bintang"
        >
          <svg class="w-3.5 h-3.5 text-amber-500 fill-amber-500 shrink-0" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M11.48 3.499a.562.562 0 011.04 0l2.125 5.111a.563.563 0 00.475.345l5.518.442c.499.04.701.663.321.988l-4.204 3.602a.563.563 0 00-.182.557l1.285 5.385a.562.562 0 01-.84.61l-4.725-2.885a.563.563 0 00-.586 0L6.982 20.54a.562.562 0 01-.84-.61l1.285-5.386a.562.562 0 00-.182-.557l-4.204-3.602a.563.563 0 01.321-.988l5.518-.442a.563.563 0 00.475-.345L11.48 3.5z" />
          </svg>
          <span id="bookmarkCountText" class="font-mono text-xs text-slate-800 dark:text-zinc-200">0</span>
        </button>

        <!-- Theme Toggle Button -->
        <button 
          onclick="toggleTheme(event)" 
          id="themeToggleBtn" 
          class="w-8 h-8 rounded-lg bg-white dark:bg-zinc-900 hover:bg-slate-100 dark:hover:bg-zinc-800 border border-slate-200 dark:border-zinc-800 text-slate-600 dark:text-zinc-400 flex items-center justify-center transition-all shadow-xs"
          title="Tukar Mod Tema"
        >
          <svg id="moonIcon" class="w-4 h-4 hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M21.752 15.002A9.718 9.718 0 0118 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 003 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 009.002-5.998z" />
          </svg>
          <svg id="sunIcon" class="w-4 h-4 hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 3v2.25m6.364.386l-1.591 1.591M21 12h-2.25m-.386 6.364l-1.591-1.591M12 18.75V21m-4.773-4.227l-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0z" />
          </svg>
        </button>

      </div>
    </div>
  </header>

  <!-- LIVE QUIZ HUD (Visible only when in Quiz Mode) -->
  <div id="quizScoreHud" class="hidden sticky top-14 z-30 bg-indigo-950/90 text-white backdrop-blur-md border-b border-indigo-800/80 shadow-md">
    <div class="max-w-5xl mx-auto px-4 py-2 flex flex-wrap items-center justify-between gap-3 text-xs">
      <div class="flex items-center space-x-3">
        <span class="inline-flex items-center px-2 py-0.5 rounded bg-indigo-500/30 text-indigo-200 font-mono font-bold text-[11px] border border-indigo-400/30">
          LIVE QUIZ HUD
        </span>
        <span class="text-slate-300">Dijawab: <strong id="hudAnsweredCount" class="text-white font-mono">0</strong>/45</span>
        <span class="text-slate-300">Skor Semasa: <strong id="hudScoreDisplay" class="text-emerald-400 font-mono">0 Pts</strong> (<span id="hudPercentage">0%</span>)</span>
      </div>
      <div class="flex items-center space-x-2">
        <button onclick="revealAllQuizAnswers()" class="px-2.5 py-1 rounded bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-xs transition-colors shadow-xs">
          Semak Semua Jawapan
        </button>
        <button onclick="resetQuizAnswers()" class="px-2.5 py-1 rounded bg-zinc-800 hover:bg-zinc-700 text-zinc-300 font-medium text-xs transition-colors">
          Reset Kuiz
        </button>
      </div>
    </div>
  </div>

  <!-- EXAM TARGET & STRATEGY DASHBOARD (Linear / shadcn Card Style) -->
  <section class="max-w-5xl mx-auto px-4 pt-3 sm:pt-5 pb-2">
    
    <!-- Mobile Compact Strategy Bar (Collapsible to save vertical screen space) -->
    <button onclick="toggleStrategyDashboard()" class="w-full sm:hidden mb-3 p-3.5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/90 flex items-center justify-between shadow-xs text-left transition-colors hover:bg-slate-50 dark:hover:bg-zinc-850">
      <div class="flex items-center space-x-2.5">
        <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-emerald-50 dark:bg-emerald-950/60 text-emerald-700 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-800">
          Pass: 70.0%
        </span>
        <span class="text-xs font-bold text-slate-900 dark:text-white">Pelan Kelayakan: 69.02% ➔ 75%+</span>
      </div>
      <span id="stratToggleArrow" class="text-xs font-mono text-slate-500 dark:text-zinc-400">Tutup ▴</span>
    </button>

    <div id="strategyCardsGrid" class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-3 sm:!grid">
      
      <!-- Target Score Math Card -->
      <div class="bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/90 rounded-xl p-4 shadow-sm flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-2">
            <span class="text-[11px] font-bold text-slate-500 dark:text-zinc-400 uppercase tracking-wider">Formula Kelayakan</span>
            <span class="text-[10px] font-mono font-bold px-2 py-0.5 rounded bg-emerald-50 dark:bg-emerald-950/60 text-emerald-700 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-800">
              Lulus: 70.0% (49.0 Pts)
            </span>
          </div>
          <div class="text-base sm:text-lg font-bold tracking-tight text-slate-900 dark:text-white">69.02% ➔ 75%+ Target Push</div>
          <p class="text-xs text-slate-600 dark:text-zinc-400 mt-1.5 leading-relaxed">
            Sebelum ini anda capai <strong>69.02%</strong>. Beza hanya <strong>0.98%</strong> (hanya 1 soalan K-type 2-markah sahaja lagi untuk lulus selamat).
          </p>
        </div>
        
        <!-- Progress bar visualization -->
        <div class="mt-3.5 pt-3 border-t border-slate-100 dark:border-zinc-800/80">
          <div class="flex justify-between text-[11px] font-mono text-slate-500 mb-1">
            <span>Terdahulu: 69.0%</span>
            <span class="text-emerald-600 dark:text-emerald-400 font-bold">Target: 75%+</span>
          </div>
          <div class="w-full bg-slate-100 dark:bg-zinc-800 h-2 rounded-full overflow-hidden flex">
            <div class="bg-slate-400 dark:bg-zinc-500 h-full" style="width: 69%"></div>
            <div class="bg-emerald-500 h-full animate-pulse" style="width: 10%"></div>
          </div>
        </div>
      </div>

      <!-- Strategy Card: Focus on EU5 & EU6 -->
      <div class="bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/90 rounded-xl p-4 shadow-sm flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-2">
            <span class="text-[11px] font-bold text-rose-600 dark:text-rose-400 uppercase tracking-wider">Topik Kritikal (Exam Boost)</span>
            <span class="text-[10px] font-mono font-bold px-2 py-0.5 rounded bg-rose-50 dark:bg-rose-950/60 text-rose-700 dark:text-rose-300 border border-rose-200 dark:border-rose-800">
              8 Soalan (12 Pts)
            </span>
          </div>
          <div class="text-sm font-bold tracking-tight text-slate-900 dark:text-white">EU5 (Process) + EU6 (Management)</div>
          <p class="text-xs text-slate-600 dark:text-zinc-400 mt-1.5 leading-relaxed">
            Kelemahan sebelum ini pada EU5 & EU6 (dapat 3/8). Jika capai <strong>6/8 betul</strong>, markah anda automatik melonjak dari <strong>69% ke 76%+</strong>.
          </p>
        </div>
        <div class="mt-3.5 pt-3 border-t border-slate-100 dark:border-zinc-800/80 flex items-center gap-1.5 overflow-x-auto text-[10px] font-mono text-slate-600 dark:text-zinc-400">
          <span class="px-1.5 py-0.5 bg-slate-100 dark:bg-zinc-800 rounded border border-slate-200 dark:border-zinc-700/60">Time+Purpose</span>
          <span class="px-1.5 py-0.5 bg-slate-100 dark:bg-zinc-800 rounded border border-slate-200 dark:border-zinc-700/60">Future Baseline</span>
          <span class="px-1.5 py-0.5 bg-slate-100 dark:bg-zinc-800 rounded border border-slate-200 dark:border-zinc-700/60">Kano/MoSCoW</span>
        </div>
      </div>

      <!-- Navigation & Mode Selector Card -->
      <div class="bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/90 rounded-xl p-4 shadow-sm flex flex-col justify-between">
        <div>
          <span class="text-[11px] font-bold text-slate-500 dark:text-zinc-400 uppercase tracking-wider">Paparan Utama</span>
          <div class="text-sm font-bold tracking-tight text-slate-900 dark:text-white mt-1">Struktur Silibus Rasmi IREB</div>
          <p class="text-xs text-slate-600 dark:text-zinc-400 mt-1.5 leading-relaxed">
            Tukar antara bank soalan lengkap (Q1–Q45) atau ringkasan nota padat 1-muka surat.
          </p>
        </div>
        <div class="grid grid-cols-2 gap-2 mt-3.5 pt-3 border-t border-slate-100 dark:border-zinc-800/80">
          <button onclick="switchTab('questions')" id="tabQuestionsBtn" class="h-8 px-3 rounded-lg bg-zinc-900 dark:bg-white text-white dark:text-zinc-950 font-bold text-xs shadow-xs transition-all flex items-center justify-center">
            Bank Soalan
          </button>
          <button onclick="switchTab('cheatsheet')" id="tabCheatsheetBtn" class="h-8 px-3 rounded-lg bg-slate-100 dark:bg-zinc-800 hover:bg-slate-200 dark:hover:bg-zinc-700 text-slate-700 dark:text-zinc-300 font-semibold text-xs border border-slate-200 dark:border-zinc-700 transition-all flex items-center justify-center">
            Cheat Sheet
          </button>
        </div>
      </div>

    </div>
  </section>

  <!-- PANDUAN FORMAT SOALAN (A-TYPE, P-TYPE, K-TYPE) ACCORDION -->
  <section class="max-w-5xl mx-auto px-4 py-1.5">
    <div class="bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/90 rounded-xl p-3.5 shadow-sm">
      <button onclick="toggleTypeGuide()" class="w-full flex items-center justify-between text-left group">
        <div class="flex items-center space-x-2.5">
          <span class="px-2 py-0.5 rounded-md bg-blue-50 dark:bg-blue-950/60 text-blue-700 dark:text-blue-300 text-xs font-bold border border-blue-200 dark:border-blue-900/60">
            INFO FORMAT
          </span>
          <span class="text-xs font-bold text-slate-900 dark:text-white group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors">
            Fahami Format Soalan IREB: A-Type, P-Type, dan K-Type
          </span>
        </div>
        <span id="typeGuideArrow" class="text-xs font-mono text-slate-500 dark:text-zinc-400">Buka ▾</span>
      </button>

      <div id="typeGuideBody" class="hidden mt-3.5 pt-3.5 border-t border-slate-100 dark:border-zinc-800/80 grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
        
        <!-- A-Type -->
        <div class="p-3.5 rounded-xl bg-slate-50 dark:bg-zinc-950/80 border border-slate-200 dark:border-zinc-800">
          <div class="font-bold text-slate-900 dark:text-white mb-1.5 flex items-center justify-between">
            <span class="flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-blue-500"></span>
              A-Type (Single Choice)
            </span>
            <span class="text-[10px] font-mono px-1.5 py-0.5 rounded bg-blue-100 dark:bg-blue-950/70 text-blue-700 dark:text-blue-300 font-bold">1 Pt</span>
          </div>
          <p class="text-slate-600 dark:text-zinc-400 leading-relaxed text-[12px]">
            Pilih <strong>HANYA SATU (1)</strong> jawapan yang betul daripada 4 pilihan. Betul = 1 markah. Salah = 0 markah.
          </p>
        </div>

        <!-- P-Type -->
        <div class="p-3.5 rounded-xl bg-slate-50 dark:bg-zinc-950/80 border border-slate-200 dark:border-zinc-800">
          <div class="font-bold text-slate-900 dark:text-white mb-1.5 flex items-center justify-between">
            <span class="flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-amber-500"></span>
              P-Type (Multiple Choice)
            </span>
            <span class="text-[10px] font-mono px-1.5 py-0.5 rounded bg-amber-100 dark:bg-amber-950/70 text-amber-700 dark:text-amber-300 font-bold">1–3 Pts</span>
          </div>
          <p class="text-slate-600 dark:text-zinc-400 leading-relaxed text-[12px]">
            Soalan menyatakan berapa pilihan wajib ditanda (cth: <em>Pick 2 answers</em>). Markah diberi berkadar dengan bilangan jawapan betul yang ditanda.
          </p>
        </div>

        <!-- K-Type -->
        <div class="p-3.5 rounded-xl bg-slate-50 dark:bg-zinc-950/80 border border-slate-200 dark:border-zinc-800">
          <div class="font-bold text-slate-900 dark:text-white mb-1.5 flex items-center justify-between">
            <span class="flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-purple-500"></span>
              K-Type (True/False Matrix)
            </span>
            <span class="text-[10px] font-mono px-1.5 py-0.5 rounded bg-purple-100 dark:bg-purple-950/70 text-purple-700 dark:text-purple-300 font-bold">2 Pts</span>
          </div>
          <p class="text-slate-600 dark:text-zinc-400 leading-relaxed text-[12px]">
            Setiap baris (A, B, C, D) dinilai <strong>True atau False</strong>.<br/>
            • 4/4 betul = <strong>2 markah</strong><br/>
            • 3/4 betul = <strong>1 markah</strong><br/>
            • &le;2 betul = <strong>0 markah</strong>
          </p>
        </div>

      </div>
    </div>
  </section>

  <!-- MAIN TAB 1: QUESTIONS BANK -->
  <main id="questionsTab" class="max-w-5xl mx-auto px-4 py-3">
    
    <!-- Active Bookmark Banner -->
    <div id="bookmarkFilterBanner" class="hidden mb-3.5 p-3 rounded-xl bg-amber-50 dark:bg-amber-950/40 border border-amber-300 dark:border-amber-800 flex items-center justify-between text-xs shadow-xs">
      <div class="flex items-center space-x-2">
        <svg class="w-4 h-4 text-amber-500 fill-amber-500 shrink-0" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
        <span class="text-amber-900 dark:text-amber-200 font-semibold">Menunjukkan soalan bertanda bintang sahaja</span>
      </div>
      <button onclick="toggleBookmarkFilter()" class="px-2.5 py-1 rounded bg-amber-200 dark:bg-amber-900 text-amber-900 dark:text-amber-100 font-bold text-[11px] hover:underline">
        Tunjuk Semua Soalan ✕
      </button>
    </div>

    <!-- Filter & Search Toolbar (shadcn style) -->
    <div class="bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/90 rounded-xl p-3.5 mb-4 space-y-3 shadow-sm">
      
      <!-- Search Box with Clear Button & Shortcut Hint -->
      <div class="relative">
        <svg class="w-4 h-4 text-slate-400 dark:text-zinc-500 absolute left-3 top-1/2 -translate-y-1/2" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
        </svg>
        <input 
          type="text" 
          id="searchInput" 
          oninput="handleSearch(this.value)" 
          placeholder="Cari soalan, kod (cth: K0111, Q15), atau kata kunci (cth: Kano, DFD, Nominalization, Diagram)..." 
          class="w-full pl-9 pr-14 py-2 rounded-lg bg-slate-50 dark:bg-zinc-950 border border-slate-200 dark:border-zinc-800 text-xs text-slate-900 dark:text-white placeholder-slate-400 dark:placeholder-zinc-500 focus:outline-none focus:ring-1 focus:ring-indigo-500 dark:focus:ring-zinc-600 transition-all font-sans"
        >
        <div class="absolute right-2.5 top-1/2 -translate-y-1/2 flex items-center space-x-1">
          <button onclick="clearSearch()" id="clearSearchBtn" class="hidden text-slate-400 hover:text-slate-700 dark:hover:text-zinc-200 text-xs p-1">
            ✕
          </button>
          <span class="hidden sm:inline-block text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-200/70 dark:bg-zinc-800 text-slate-500 dark:text-zinc-400">/</span>
        </div>
      </div>

      <!-- Filters Row: Question Type & Global Expand/Collapse -->
      <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2 pt-1 border-t border-slate-100 dark:border-zinc-800/80">
        
        <!-- Type Filter Chips with Counts -->
        <div class="flex items-center gap-1 overflow-x-auto w-full sm:w-auto pb-1 sm:pb-0 scrollbar-none">
          <span class="text-[11px] font-bold text-slate-500 dark:text-zinc-400 mr-1 shrink-0">Jenis:</span>
          <button onclick="filterByType('all')" class="type-btn active px-2.5 py-1 rounded-md text-xs font-semibold bg-zinc-900 dark:bg-white text-white dark:text-zinc-950 shadow-xs" data-type="all">
            Semua (${questions.length})
          </button>
          <button onclick="filterByType('K')" class="type-btn px-2.5 py-1 rounded-md text-xs font-medium bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300 hover:bg-slate-200 dark:hover:bg-zinc-700 border border-slate-200 dark:border-zinc-700/60" data-type="K">
            K-Type (${kCount})
          </button>
          <button onclick="filterByType('A')" class="type-btn px-2.5 py-1 rounded-md text-xs font-medium bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300 hover:bg-slate-200 dark:hover:bg-zinc-700 border border-slate-200 dark:border-zinc-700/60" data-type="A">
            A-Type (${aCount})
          </button>
          <button onclick="filterByType('P')" class="type-btn px-2.5 py-1 rounded-md text-xs font-medium bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300 hover:bg-slate-200 dark:hover:bg-zinc-700 border border-slate-200 dark:border-zinc-700/60" data-type="P">
            P-Type (${pCount})
          </button>
        </div>

        <!-- Global Action: Toggle all explanations -->
        <div class="flex items-center space-x-2 text-[11px] text-slate-500 dark:text-zinc-400 self-end sm:self-auto">
          <button onclick="expandAllExplanations()" class="hover:text-slate-900 dark:hover:text-white font-medium transition-colors">Buka Semua</button>
          <span>•</span>
          <button onclick="collapseAllExplanations()" class="hover:text-slate-900 dark:hover:text-white font-medium transition-colors">Tutup Semua</button>
        </div>

      </div>

      <!-- EU Selector Pills -->
      <div class="flex items-center gap-1.5 overflow-x-auto pt-1 pb-0.5 scrollbar-none">
        <span class="text-[11px] font-bold text-slate-500 dark:text-zinc-400 mr-1 shrink-0">EU:</span>
        <button onclick="filterByEU(0)" class="eu-btn active px-2.5 py-1 rounded-md text-xs font-semibold bg-zinc-900 dark:bg-white text-white dark:text-zinc-950 shrink-0 shadow-xs" data-eu="0">
          Semua (EU1–7)
        </button>
        ${eus.map(eu => `
          <button onclick="filterByEU(${eu.no})" class="eu-btn px-2.5 py-1 rounded-md text-xs font-medium bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300 hover:bg-slate-200 dark:hover:bg-zinc-700 shrink-0 flex items-center gap-1.5 border border-slate-200 dark:border-zinc-700/60" data-eu="${eu.no}">
            <span class="w-1.5 h-1.5 rounded-full ${eu.no === 5 || eu.no === 6 ? 'bg-rose-500' : 'bg-slate-400 dark:bg-zinc-500'}"></span>
            EU${eu.no} (${eu.range})
          </button>
        `).join('')}
      </div>

    </div>

    <!-- Questions Counter Header -->
    <div class="flex items-center justify-between text-xs text-slate-500 dark:text-zinc-400 mb-3 px-1">
      <div>Menunjukkan <span id="visibleCount" class="font-bold font-mono text-slate-900 dark:text-white">${questions.length}</span> daripada ${questions.length} soalan</div>
      <div id="activeFilterLabel" class="text-[11px]"></div>
    </div>

    <!-- Question Cards Stream -->
    <div id="questionsContainer" class="space-y-4">
      <!-- Dynamically Rendered by JS -->
    </div>

  </main>

  <!-- MAIN TAB 2: CHEAT SHEETS (Structured High-Yield Reference) -->
  <section id="cheatsheetTab" class="max-w-5xl mx-auto px-4 py-4 hidden">
    
    <div class="mb-5 pb-3 border-b border-slate-200 dark:border-zinc-800">
      <h2 class="text-base font-bold text-slate-900 dark:text-white">CPRE FL 3.3.2 Reference & Core Guidelines</h2>
      <p class="text-xs text-slate-500 dark:text-zinc-400 mt-0.5">Nota padat untuk rujukan pantas konsep asas, peraturan pemodelan, dan topik kritikal peperiksaan.</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      
      <!-- 1. Natural Language Defects -->
      <div class="bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800 rounded-xl p-4 shadow-sm">
        <div class="flex items-center justify-between pb-2.5 mb-3 border-b border-slate-100 dark:border-zinc-800">
          <h3 class="text-xs font-bold text-slate-900 dark:text-white uppercase tracking-wider">1. Natural Language Defects (Chapter 5)</h3>
          <span class="text-[10px] font-mono font-bold px-2 py-0.5 rounded bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300 border border-slate-200 dark:border-zinc-700">EU3 / Ch 5</span>
        </div>
        
        <div class="space-y-2.5 text-xs leading-relaxed text-slate-700 dark:text-zinc-300">
          <div class="p-3 rounded-lg bg-slate-50 dark:bg-zinc-950 border border-slate-200 dark:border-zinc-800/80">
            <strong class="text-slate-900 dark:text-zinc-100 block mb-0.5 font-bold">1. Nominalization (-tion, -ment, -ance)</strong>
            <span>Kata kerja bertukar menjadi kata nama. Menyembunyikan pelaku sebenar proses.</span>
            <div class="mt-1 text-[11px] font-mono text-slate-500 dark:text-zinc-400">Contoh: "Data loading occurs" ➔ Tukar ke: "System shall load data"</div>
          </div>

          <div class="p-3 rounded-lg bg-slate-50 dark:bg-zinc-950 border border-slate-200 dark:border-zinc-800/80">
            <strong class="text-slate-900 dark:text-zinc-100 block mb-0.5 font-bold">2. Universal Quantifiers (All, Always, Never)</strong>
            <span>Mengitlakkan keadaan tanpa mengambil kira syarat kekecualian (exceptions).</span>
          </div>

          <div class="p-3 rounded-lg bg-slate-50 dark:bg-zinc-950 border border-slate-200 dark:border-zinc-800/80">
            <strong class="text-slate-900 dark:text-zinc-100 block mb-0.5 font-bold">3. Incompletely Specified Conditions (If...)</strong>
            <span>Menyatakan syarat 'IF' tanpa menjelaskan apa berlaku sekiranya syarat gagal dipenuhi.</span>
          </div>

          <div class="p-3 rounded-lg bg-slate-50 dark:bg-zinc-950 border border-slate-200 dark:border-zinc-800/80">
            <strong class="text-slate-900 dark:text-zinc-100 block mb-0.5 font-bold">4. Passive Voice (Ayat Pasif)</strong>
            <span>Pelaku (agent) yang bertanggungjawab tidak dinyatakan dalam ayat spesifikasi.</span>
          </div>
        </div>
      </div>

      <!-- 2. Model-Based Requirements Rules -->
      <div class="bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800 rounded-xl p-4 shadow-sm">
        <div class="flex items-center justify-between pb-2.5 mb-3 border-b border-slate-100 dark:border-zinc-800">
          <h3 class="text-xs font-bold text-slate-900 dark:text-white uppercase tracking-wider">2. Model-Based RE Rules (Chapter 6)</h3>
          <span class="text-[10px] font-mono font-bold px-2 py-0.5 rounded bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300 border border-slate-200 dark:border-zinc-700">EU3 / Ch 6</span>
        </div>

        <div class="space-y-2.5 text-xs leading-relaxed text-slate-700 dark:text-zinc-300">
          <div class="p-3 rounded-lg bg-slate-50 dark:bg-zinc-950 border border-slate-200 dark:border-zinc-800/80">
            <strong class="text-slate-900 dark:text-zinc-100 block mb-0.5 font-bold">Use Case Diagram</strong>
            <ul class="list-disc pl-4 space-y-0.5 text-slate-600 dark:text-zinc-400">
              <li>Actor ke Actor: Hanya <strong>Generalization</strong> dibenarkan.</li>
              <li>Use Case ke Use Case: Wajib menggunakan <strong>&lt;&lt;include&gt;&gt;</strong> atau <strong>&lt;&lt;extend&gt;&gt;</strong>.</li>
            </ul>
          </div>

          <div class="p-3 rounded-lg bg-slate-50 dark:bg-zinc-950 border border-slate-200 dark:border-zinc-800/80">
            <strong class="text-slate-900 dark:text-zinc-100 block mb-0.5 font-bold">Data Flow Diagram (DFD)</strong>
            <ul class="list-disc pl-4 space-y-0.5 text-slate-600 dark:text-zinc-400">
              <li>Data Store ke Data Store tidak boleh bersambung secara terus (mesti melalui Process).</li>
              <li>External Entity ke Data Store mesti melalui Process.</li>
            </ul>
          </div>

          <div class="p-3 rounded-lg bg-slate-50 dark:bg-zinc-950 border border-slate-200 dark:border-zinc-800/80">
            <strong class="text-slate-900 dark:text-zinc-100 block mb-0.5 font-bold">3 Perspektif IREB</strong>
            <div class="grid grid-cols-3 gap-1.5 text-center mt-1.5 text-[11px]">
              <div class="p-1.5 bg-white dark:bg-zinc-900 rounded font-medium border border-slate-200 dark:border-zinc-800">Structure (Class/ERD)</div>
              <div class="p-1.5 bg-white dark:bg-zinc-900 rounded font-medium border border-slate-200 dark:border-zinc-800">Function (DFD/Activity)</div>
              <div class="p-1.5 bg-white dark:bg-zinc-900 rounded font-medium border border-slate-200 dark:border-zinc-800">Behavior (State)</div>
            </div>
          </div>
        </div>
      </div>

      <!-- 3. EU5 Process & Facets -->
      <div class="bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800 rounded-xl p-4 shadow-sm">
        <div class="flex items-center justify-between pb-2.5 mb-3 border-b border-slate-100 dark:border-zinc-800">
          <h3 class="text-xs font-bold text-slate-900 dark:text-white uppercase tracking-wider">3. Process Facets (EU5)</h3>
          <span class="text-[10px] font-mono font-bold px-2 py-0.5 rounded bg-rose-50 dark:bg-rose-950 text-rose-700 dark:text-rose-300 border border-rose-200 dark:border-rose-800">EU5 Core</span>
        </div>

        <div class="space-y-2 text-xs leading-relaxed text-slate-700 dark:text-zinc-300">
          <p><strong>Time Facet:</strong> Linear (Prescriptive) vs Iterative (Explorative).</p>
          <p><strong>Purpose Facet:</strong> Prescriptive (Contractual) vs Explorative (Product/Market).</p>
          <p><strong>Target Facet:</strong> Specific Customer vs Market-driven (Standard product).</p>
          <p><strong>Format Facet:</strong> Document-centric vs Item-centric.</p>
          <div class="p-2.5 bg-slate-50 dark:bg-zinc-950 rounded-lg border border-slate-200 dark:border-zinc-800 text-[11px] text-slate-800 dark:text-zinc-200 font-medium">
            Kunci soalan: Dua facet paling utama menentukan bentuk proses ialah <strong>Time Facet</strong> dan <strong>Purpose Facet</strong>.
          </div>
        </div>
      </div>

      <!-- 4. EU6 Management Practices -->
      <div class="bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800 rounded-xl p-4 shadow-sm">
        <div class="flex items-center justify-between pb-2.5 mb-3 border-b border-slate-100 dark:border-zinc-800">
          <h3 class="text-xs font-bold text-slate-900 dark:text-white uppercase tracking-wider">4. Management & Baseline (EU6)</h3>
          <span class="text-[10px] font-mono font-bold px-2 py-0.5 rounded bg-rose-50 dark:bg-rose-950 text-rose-700 dark:text-rose-300 border border-rose-200 dark:border-rose-800">EU6 Core</span>
        </div>

        <div class="space-y-2 text-xs leading-relaxed text-slate-700 dark:text-zinc-300">
          <p><strong>Prioritization:</strong> Tujuan utama adalah untuk <strong>Release Planning</strong> dan <strong>Test Focus</strong> (bukan untuk menganggar kos projek).</p>
          <p><strong>Techniques:</strong> Kano (Must-be, Performance, Attractive), MoSCoW, Wiegers Matrix.</p>
          <p><strong>Baselines:</strong> Baseline yang telah diluluskan tidak boleh diubah secara terus; perubahan diserap ke dalam <strong>Future Baseline</strong> melalui proses Change Control.</p>
          <p><strong>Views:</strong> Berfungsi menapis maklumat untuk mengurangkan beban kognitif pembaca.</p>
        </div>
      </div>

    </div>

  </section>

  <!-- FULLSCREEN IMAGE MODAL -->
  <div id="imageModal" onclick="closeImageModal()" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4 transition-opacity duration-200">
    <div class="relative max-w-4xl max-h-[90vh] bg-white dark:bg-zinc-900 rounded-2xl p-4 shadow-2xl overflow-auto border border-zinc-700" onclick="event.stopPropagation()">
      <div class="flex items-center justify-between pb-2 mb-2 border-b border-zinc-200 dark:border-zinc-800">
        <span id="modalImgTitle" class="text-xs font-bold text-zinc-900 dark:text-white">Paparan Penuh Gambar Rajah</span>
        <button onclick="closeImageModal()" class="text-xs font-mono font-bold px-2 py-1 rounded bg-zinc-100 dark:bg-zinc-800 text-zinc-600 dark:text-zinc-300 hover:bg-zinc-200 dark:hover:bg-zinc-700">
          Tutup ✕
        </button>
      </div>
      <div class="flex items-center justify-center p-2 bg-white rounded-lg">
        <img id="modalImgTag" src="" alt="Diagram Fullscreen" class="max-w-full max-h-[75vh] object-contain" />
      </div>
    </div>
  </div>

  <!-- CUSTOM CONFIRMATION DIALOG (shadcn AlertDialog style) -->
  <div id="confirmModal" onclick="closeConfirmModal()" class="fixed inset-0 bg-black/70 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4 transition-opacity duration-200">
    <div class="relative w-full max-w-md bg-white dark:bg-zinc-900 rounded-2xl p-5 sm:p-6 shadow-2xl border border-slate-200 dark:border-zinc-800" onclick="event.stopPropagation()">
      <div class="flex items-start space-x-3.5 mb-4">
        <div class="w-10 h-10 rounded-full bg-rose-50 dark:bg-rose-950/60 border border-rose-200 dark:border-rose-900/60 flex items-center justify-center text-rose-600 dark:text-rose-400 shrink-0">
          <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126zM12 15.75h.007v.008H12v-.008z" />
          </svg>
        </div>
        <div>
          <h3 id="confirmTitle" class="text-sm sm:text-base font-bold text-slate-900 dark:text-white">Set Semula Jawapan Kuiz?</h3>
          <p id="confirmDesc" class="text-xs text-slate-500 dark:text-zinc-400 mt-1 leading-relaxed">
            Semua jawapan yang telah anda tanda dan semakan markah dalam Quiz Mode akan dipadamkan. Tindakan ini tidak boleh diundur.
          </p>
        </div>
      </div>
      
      <div class="flex items-center justify-end space-x-2 pt-3 border-t border-slate-100 dark:border-zinc-800">
        <button onclick="closeConfirmModal()" class="h-8 px-3.5 rounded-lg bg-slate-100 hover:bg-slate-200 dark:bg-zinc-800 dark:hover:bg-zinc-700 text-slate-700 dark:text-zinc-300 text-xs font-semibold transition-colors">
          Batal
        </button>
        <button id="confirmActionBtn" onclick="executeConfirmAction()" class="h-8 px-3.5 rounded-lg bg-rose-600 hover:bg-rose-500 text-white text-xs font-bold shadow-xs transition-colors">
          Ya, Set Semula
        </button>
      </div>
    </div>
  </div>

  <!-- Mobile Quick Jump Drawer (Q1–45 Grid - iOS Sheet Style) -->
  <div id="drawerOverlay" onclick="toggleDrawer()" class="fixed inset-0 bg-black/60 backdrop-blur-sm z-50 hidden transition-opacity duration-200"></div>
  
  <div id="jumpDrawer" class="fixed bottom-0 inset-x-0 bg-white dark:bg-zinc-900 border-t border-slate-200 dark:border-zinc-800 rounded-t-3xl p-4 sm:p-5 z-50 max-h-[85vh] overflow-y-auto transform translate-y-full transition-transform duration-200 ease-out hidden shadow-2xl">
    
    <!-- iOS Drag Handle Bar -->
    <div class="w-10 h-1 bg-slate-300 dark:bg-zinc-700 rounded-full mx-auto mb-3.5 shrink-0"></div>

    <div class="flex items-center justify-between pb-3 mb-3 border-b border-slate-100 dark:border-zinc-800">
      <div>
        <div class="font-bold text-sm text-slate-900 dark:text-white">Lompat Ke Soalan (Q1–45)</div>
        <div class="text-[11px] text-slate-500 dark:text-zinc-400">Pilih nombor soalan mengikut Unit Silibus (EU)</div>
      </div>
      <button onclick="toggleDrawer()" class="w-7 h-7 rounded-full bg-slate-100 dark:bg-zinc-800 text-slate-500 hover:text-slate-900 dark:hover:text-white flex items-center justify-center font-bold text-xs">
        ✕
      </button>
    </div>

    <div class="space-y-3.5 pb-8">
      ${eus.map(eu => {
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
      }).join('')}
    </div>
  </div>

  <!-- Mobile Native Bottom Navigation Bar (iOS / Android App Style) -->
  <nav aria-label="Mobile Navigation" class="fixed bottom-0 inset-x-0 bg-white/95 dark:bg-zinc-950/95 backdrop-blur-xl border-t border-slate-200/90 dark:border-zinc-800/90 h-16 z-30 md:hidden flex items-center justify-around px-2 shadow-lg">
    
    <!-- Tab 1: Soalan -->
    <button onclick="switchTab('questions')" id="mobTabQ" class="flex flex-1 flex-col items-center justify-center py-1 text-slate-900 dark:text-white font-bold transition-all active:scale-95">
      <svg class="w-5 h-5 mb-0.5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
        <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z"/>
      </svg>
      <span class="text-[10px] tracking-tight">Soalan</span>
      <span id="mobDotQ" class="w-1 h-1 rounded-full bg-indigo-600 dark:bg-white mt-0.5 transition-opacity"></span>
    </button>

    <!-- Tab 2: Nota / Cheat Sheet -->
    <button onclick="switchTab('cheatsheet')" id="mobTabCs" class="flex flex-1 flex-col items-center justify-center py-1 text-slate-400 dark:text-zinc-500 hover:text-slate-700 dark:hover:text-zinc-300 font-medium transition-all active:scale-95">
      <svg class="w-5 h-5 mb-0.5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
        <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.042A8.967 8.967 0 006 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 016 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 016-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0018 18a8.967 8.967 0 00-6 2.292m0-14.25v14.25"/>
      </svg>
      <span class="text-[10px] tracking-tight">Cheat Sheet</span>
      <span id="mobDotCs" class="w-1 h-1 rounded-full bg-indigo-600 dark:bg-white mt-0.5 opacity-0 transition-opacity"></span>
    </button>

    <!-- Tab 3: TOC Grid Drawer Trigger -->
    <button onclick="toggleDrawer()" id="mobTabDrawer" class="flex flex-1 flex-col items-center justify-center py-1 text-slate-400 dark:text-zinc-500 hover:text-slate-700 dark:hover:text-zinc-300 font-medium transition-all active:scale-95">
      <svg class="w-5 h-5 mb-0.5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
        <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6A2.25 2.25 0 016 3.75h2.25A2.25 2.25 0 0110.5 6v2.25a2.25 2.25 0 01-2.25 2.25H6a2.25 2.25 0 01-2.25-2.25V6zM3.75 15.75A2.25 2.25 0 016 13.5h2.25a2.25 2.25 0 012.25 2.25V18a2.25 2.25 0 01-2.25 2.25H6A2.25 2.25 0 013.75 18v-2.25zM13.5 6a2.25 2.25 0 012.25-2.25H18A2.25 2.25 0 0120.25 6v2.25A2.25 2.25 0 0118 10.5h-2.25a2.25 2.25 0 01-2.25-2.25V6zM13.5 15.75a2.25 2.25 0 012.25-2.25H18a2.25 2.25 0 012.25 2.25V18A2.25 2.25 0 0118 20.25h-2.25A2.25 2.25 0 0113.5 18v-2.25z"/>
      </svg>
      <span class="text-[10px] tracking-tight">TOC Grid</span>
      <span class="w-1 h-1 rounded-full opacity-0 mt-0.5"></span>
    </button>

  </nav>

  <!-- JAVASCRIPT APPLICATION CORE -->
  <script>
    const appData = ${JSON.stringify({ eus, questions })};
    const questions = appData.questions;
    const eus = appData.eus;

    // State Variables
    let currentTheme = localStorage.getItem('cpre_theme') || (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
    let currentMode = 'study'; // 'study' | 'quiz'
    let currentEU = 0; // 0 = all
    let currentType = 'all'; // 'all' | 'K' | 'A' | 'P'
    let searchQuery = '';
    let filterBookmarkedOnly = false;
    let bookmarkedIds = new Set(JSON.parse(localStorage.getItem('cpre_bookmarks') || '[]'));
    let userQuizAnswers = JSON.parse(localStorage.getItem('cpre_quiz_answers') || '{}');
    let revealedAnswers = new Set();
    let collapsedExplanations = new Set();

    // DOM Elements
    const questionsContainer = document.getElementById('questionsContainer');
    const bookmarkCountText = document.getElementById('bookmarkCountText');
    const visibleCountEl = document.getElementById('visibleCount');
    const searchInput = document.getElementById('searchInput');
    const clearSearchBtn = document.getElementById('clearSearchBtn');
    const bookmarkFilterBanner = document.getElementById('bookmarkFilterBanner');
    const quizScoreHud = document.getElementById('quizScoreHud');

    document.addEventListener('DOMContentLoaded', () => {
      applyTheme(currentTheme);
      updateBookmarkUI();
      renderQuestions();

      // Keyboard Shortcut: '/' to focus search, 'Escape' to close modals/search
      document.addEventListener('keydown', (e) => {
        if (e.key === '/' && document.activeElement !== searchInput) {
          e.preventDefault();
          searchInput.focus();
        } else if (e.key === 'Escape') {
          if (document.activeElement === searchInput) {
            searchInput.blur();
          }
          closeImageModal();
          closeConfirmModal();
        }
      });
    });

    // Theme Switcher with Native View Transitions (Titisan Air yang Tenang)
    function toggleTheme(e) {
      const isDark = document.documentElement.classList.contains('dark');
      const nextTheme = isDark ? 'light' : 'dark';

      // Fallback for browsers without View Transitions
      if (!document.startViewTransition) {
        currentTheme = nextTheme;
        localStorage.setItem('cpre_theme', currentTheme);
        applyTheme(currentTheme);
        return;
      }

      const btn = document.getElementById('themeToggleBtn');
      const rect = btn ? btn.getBoundingClientRect() : { left: window.innerWidth - 48, top: 24, width: 32, height: 32 };
      const x = e && e.clientX ? e.clientX : (rect.left + rect.width / 2);
      const y = e && e.clientY ? e.clientY : (rect.top + rect.height / 2);

      const endRadius = Math.hypot(
        Math.max(x, window.innerWidth - x),
        Math.max(y, window.innerHeight - y)
      );

      const transition = document.startViewTransition(() => {
        currentTheme = nextTheme;
        localStorage.setItem('cpre_theme', currentTheme);
        applyTheme(currentTheme);
      });

      transition.ready.then(() => {
        document.documentElement.animate(
          {
            clipPath: [
              \`circle(0px at \${x}px \${y}px)\`,
              \`circle(\${endRadius}px at \${x}px \${y}px)\`
            ]
          },
          {
            duration: 480,
            easing: 'cubic-bezier(0.22, 1, 0.36, 1)',
            pseudoElement: '::view-transition-new(root)'
          }
        );
      });
    }

    function applyTheme(theme) {
      const html = document.documentElement;
      const moon = document.getElementById('moonIcon');
      const sun = document.getElementById('sunIcon');
      
      if (theme === 'dark') {
        html.classList.add('dark');
        if (moon) moon.classList.remove('hidden');
        if (sun) sun.classList.add('hidden');
      } else {
        html.classList.remove('dark');
        if (sun) sun.classList.remove('hidden');
        if (moon) moon.classList.add('hidden');
      }
    }

    // Toggle Strategy Dashboard (on Mobile)
    function toggleStrategyDashboard() {
      const grid = document.getElementById('strategyCardsGrid');
      const arrow = document.getElementById('stratToggleArrow');
      if (grid.classList.contains('hidden')) {
        grid.classList.remove('hidden');
        arrow.textContent = 'Tutup ▴';
      } else {
        grid.classList.add('hidden');
        arrow.textContent = 'Buka ▾';
      }
    }

    // Toggle Format Guide
    function toggleTypeGuide() {
      const body = document.getElementById('typeGuideBody');
      const arrow = document.getElementById('typeGuideArrow');
      if (body.classList.contains('hidden')) {
        body.classList.remove('hidden');
        arrow.textContent = 'Tutup ▴';
      } else {
        body.classList.add('hidden');
        arrow.textContent = 'Buka ▾';
      }
    }

    // Mode Switcher (Seamlessly switches to questions tab if on cheatsheet)
    function setMode(mode) {
      currentMode = mode;
      const sBtn = document.getElementById('modeStudyBtn');
      const qBtn = document.getElementById('modeQuizBtn');

      if (mode === 'study') {
        sBtn.className = 'px-3 py-1 rounded-md text-xs font-semibold bg-white dark:bg-zinc-800 text-slate-900 dark:text-white shadow-xs transition-all';
        qBtn.className = 'px-3 py-1 rounded-md text-xs font-medium text-slate-600 dark:text-zinc-400 hover:text-slate-900 dark:hover:text-white transition-all';
        quizScoreHud.classList.add('hidden');
      } else {
        qBtn.className = 'px-3 py-1 rounded-md text-xs font-semibold bg-white dark:bg-zinc-800 text-slate-900 dark:text-white shadow-xs transition-all';
        sBtn.className = 'px-3 py-1 rounded-md text-xs font-medium text-slate-600 dark:text-zinc-400 hover:text-slate-900 dark:hover:text-white transition-all';
        quizScoreHud.classList.remove('hidden');
        updateQuizHud();
      }
      
      switchTab('questions');
      renderQuestions();
    }

    // Tab Switcher (Syncs desktop & mobile navigation bars)
    function switchTab(tab) {
      const qTab = document.getElementById('questionsTab');
      const csTab = document.getElementById('cheatsheetTab');
      const qBtn = document.getElementById('tabQuestionsBtn');
      const csBtn = document.getElementById('tabCheatsheetBtn');
      const mobQ = document.getElementById('mobTabQ');
      const mobCs = document.getElementById('mobTabCs');
      const mobDotQ = document.getElementById('mobDotQ');
      const mobDotCs = document.getElementById('mobDotCs');

      if (tab === 'questions') {
        qTab.classList.remove('hidden');
        csTab.classList.add('hidden');
        qBtn.className = 'h-8 px-3 rounded-lg bg-zinc-900 dark:bg-white text-white dark:text-zinc-950 font-bold text-xs shadow-xs transition-all flex items-center justify-center';
        csBtn.className = 'h-8 px-3 rounded-lg bg-slate-100 dark:bg-zinc-800 hover:bg-slate-200 dark:hover:bg-zinc-700 text-slate-700 dark:text-zinc-300 font-semibold text-xs border border-slate-200 dark:border-zinc-700 transition-all flex items-center justify-center';
        
        if (mobQ) mobQ.className = 'flex flex-1 flex-col items-center justify-center py-1 text-slate-900 dark:text-white font-bold transition-all active:scale-95';
        if (mobCs) mobCs.className = 'flex flex-1 flex-col items-center justify-center py-1 text-slate-400 dark:text-zinc-500 hover:text-slate-700 dark:hover:text-zinc-300 font-medium transition-all active:scale-95';
        if (mobDotQ) mobDotQ.classList.remove('opacity-0');
        if (mobDotCs) mobDotCs.classList.add('opacity-0');
      } else {
        qTab.classList.add('hidden');
        csTab.classList.remove('hidden');
        csBtn.className = 'h-8 px-3 rounded-lg bg-zinc-900 dark:bg-white text-white dark:text-zinc-950 font-bold text-xs shadow-xs transition-all flex items-center justify-center';
        qBtn.className = 'h-8 px-3 rounded-lg bg-slate-100 dark:bg-zinc-800 hover:bg-slate-200 dark:hover:bg-zinc-700 text-slate-700 dark:text-zinc-300 font-semibold text-xs border border-slate-200 dark:border-zinc-700 transition-all flex items-center justify-center';
        
        if (mobCs) mobCs.className = 'flex flex-1 flex-col items-center justify-center py-1 text-slate-900 dark:text-white font-bold transition-all active:scale-95';
        if (mobQ) mobQ.className = 'flex flex-1 flex-col items-center justify-center py-1 text-slate-400 dark:text-zinc-500 hover:text-slate-700 dark:hover:text-zinc-300 font-medium transition-all active:scale-95';
        if (mobDotCs) mobDotCs.classList.remove('opacity-0');
        if (mobDotQ) mobDotQ.classList.add('opacity-0');
      }
    }

    // Bookmarking Logic
    function toggleBookmark(qId, e) {
      if (e) e.stopPropagation();
      if (bookmarkedIds.has(qId)) {
        bookmarkedIds.delete(qId);
      } else {
        bookmarkedIds.add(qId);
      }
      localStorage.setItem('cpre_bookmarks', JSON.stringify(Array.from(bookmarkedIds)));
      updateBookmarkUI();
      renderQuestions();
    }

    function updateBookmarkUI() {
      const count = bookmarkedIds.size;
      if (bookmarkCountText) bookmarkCountText.textContent = count;
    }

    // Filter by bookmarks
    function toggleBookmarkFilter() {
      switchTab('questions');
      filterBookmarkedOnly = !filterBookmarkedOnly;
      
      const btn = document.getElementById('bookmarkFilterBtn');
      if (filterBookmarkedOnly) {
        btn.className = 'h-8 px-2.5 rounded-lg bg-amber-50 dark:bg-amber-950/70 border border-amber-400 dark:border-amber-600 text-amber-800 dark:text-amber-200 flex items-center space-x-1.5 shadow-xs transition-all text-xs font-bold';
        bookmarkFilterBanner.classList.remove('hidden');
      } else {
        btn.className = 'h-8 px-2.5 rounded-lg bg-white dark:bg-zinc-900 hover:bg-slate-100 dark:hover:bg-zinc-800 border border-slate-200 dark:border-zinc-800 text-slate-700 dark:text-zinc-300 flex items-center space-x-1.5 transition-all text-xs font-semibold shadow-xs';
        bookmarkFilterBanner.classList.add('hidden');
      }
      renderQuestions();
    }

    // Filter by Type & EU
    function filterByType(type) {
      currentType = type;
      document.querySelectorAll('.type-btn').forEach(b => {
        if (b.getAttribute('data-type') === type) {
          b.className = 'type-btn active px-2.5 py-1 rounded-md text-xs font-semibold bg-zinc-900 dark:bg-white text-white dark:text-zinc-950 shadow-xs';
        } else {
          b.className = 'type-btn px-2.5 py-1 rounded-md text-xs font-medium bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300 hover:bg-slate-200 dark:hover:bg-zinc-700 border border-slate-200 dark:border-zinc-700/60';
        }
      });
      renderQuestions();
    }

    function filterByEU(euNo) {
      currentEU = euNo;
      document.querySelectorAll('.eu-btn').forEach(b => {
        if (parseInt(b.getAttribute('data-eu')) === euNo) {
          b.className = 'eu-btn active px-2.5 py-1 rounded-md text-xs font-semibold bg-zinc-900 dark:bg-white text-white dark:text-zinc-950 shrink-0 shadow-xs';
        } else {
          b.className = 'eu-btn px-2.5 py-1 rounded-md text-xs font-medium bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300 hover:bg-slate-200 dark:hover:bg-zinc-700 shrink-0 flex items-center gap-1.5 border border-slate-200 dark:border-zinc-700/60';
        }
      });
      renderQuestions();
    }

    // Search Handlers
    function handleSearch(val) {
      searchQuery = val.trim().toLowerCase();
      if (searchQuery.length > 0) {
        clearSearchBtn.classList.remove('hidden');
      } else {
        clearSearchBtn.classList.add('hidden');
      }
      renderQuestions();
    }

    function clearSearch() {
      searchInput.value = '';
      searchQuery = '';
      clearSearchBtn.classList.add('hidden');
      renderQuestions();
    }

    // Image Modal Logic
    function openImageModal(imgId) {
      const img = document.getElementById(imgId);
      if (!img) return;
      const modal = document.getElementById('imageModal');
      const modalImg = document.getElementById('modalImgTag');
      modalImg.src = img.src;
      modal.classList.remove('hidden');
    }

    function closeImageModal() {
      const modal = document.getElementById('imageModal');
      modal.classList.add('hidden');
    }

    // Mobile Jump Drawer
    function toggleDrawer() {
      const drawer = document.getElementById('jumpDrawer');
      const overlay = document.getElementById('drawerOverlay');
      if (drawer.classList.contains('hidden')) {
        drawer.classList.remove('hidden');
        overlay.classList.remove('hidden');
        setTimeout(() => drawer.classList.remove('translate-y-full'), 10);
      } else {
        drawer.classList.add('translate-y-full');
        setTimeout(() => {
          drawer.classList.add('hidden');
          overlay.classList.add('hidden');
        }, 200);
      }
    }

    function jumpToQuestion(qId) {
      toggleDrawer();
      switchTab('questions');
      
      if (currentEU !== 0 || currentType !== 'all' || filterBookmarkedOnly || searchQuery !== '') {
        currentEU = 0;
        currentType = 'all';
        filterBookmarkedOnly = false;
        searchQuery = '';
        searchInput.value = '';
        clearSearchBtn.classList.add('hidden');
        bookmarkFilterBanner.classList.add('hidden');
        filterByEU(0);
        filterByType('all');
        renderQuestions();
      }

      setTimeout(() => {
        const el = document.getElementById('q-card-' + qId);
        if (el) {
          el.scrollIntoView({ behavior: 'smooth', block: 'center' });
          el.classList.add('ring-2', 'ring-indigo-500', 'dark:ring-white');
          setTimeout(() => el.classList.remove('ring-2', 'ring-indigo-500', 'dark:ring-white'), 1500);
        }
      }, 50);
    }

    // Explanation Visibility Controls
    function expandAllExplanations() {
      // In Quiz Mode, ensure answers are revealed so explanations are generated
      if (currentMode === 'quiz') {
        questions.forEach(q => revealedAnswers.add(q.id));
      }
      collapsedExplanations.clear();
      renderQuestions();
    }

    function collapseAllExplanations() {
      questions.forEach(q => collapsedExplanations.add(q.id));
      renderQuestions();
    }

    function toggleExplanation(qId) {
      if (collapsedExplanations.has(qId)) {
        collapsedExplanations.delete(qId);
      } else {
        collapsedExplanations.add(qId);
      }
      const el = document.getElementById('exp-body-' + qId);
      const btn = document.getElementById('exp-toggle-btn-' + qId);
      if (el) {
        const isCollapsed = collapsedExplanations.has(qId);
        if (isCollapsed) {
          el.classList.add('hidden');
          if (btn) btn.textContent = 'Huraian Penuh ▾';
        } else {
          el.classList.remove('hidden');
          if (btn) btn.textContent = 'Tutup Huraian ▴';
        }
      }
    }

    // Quiz Mode Selection & Scoring
    function handleOptionSelect(qId, optId, type) {
      if (currentMode !== 'quiz') return;
      if (!userQuizAnswers[qId]) userQuizAnswers[qId] = [];
      
      if (type === 'A') {
        userQuizAnswers[qId] = [optId];
      } else {
        const idx = userQuizAnswers[qId].indexOf(optId);
        if (idx > -1) {
          userQuizAnswers[qId].splice(idx, 1);
        } else {
          userQuizAnswers[qId].push(optId);
        }
      }
      localStorage.setItem('cpre_quiz_answers', JSON.stringify(userQuizAnswers));
      updateQuizHud();
      renderQuestions();
    }

    function revealAnswer(qId) {
      revealedAnswers.add(qId);
      renderQuestions();
      updateQuizHud();
    }

    function revealAllQuizAnswers() {
      questions.forEach(q => revealedAnswers.add(q.id));
      renderQuestions();
      updateQuizHud();
    }

    // Confirmation Modal System
    let pendingConfirmAction = null;

    function openConfirmModal(title, desc, actionFn) {
      document.getElementById('confirmTitle').textContent = title || 'Pengesahan';
      document.getElementById('confirmDesc').textContent = desc || 'Adakah anda pasti untuk meneruskan tindakan ini?';
      pendingConfirmAction = actionFn;
      document.getElementById('confirmModal').classList.remove('hidden');
    }

    function closeConfirmModal() {
      pendingConfirmAction = null;
      document.getElementById('confirmModal').classList.add('hidden');
    }

    function executeConfirmAction() {
      if (typeof pendingConfirmAction === 'function') {
        pendingConfirmAction();
      }
      closeConfirmModal();
    }

    function resetQuizAnswers() {
      openConfirmModal(
        'Set Semula Semua Jawapan Kuiz?',
        'Semua pilihan jawapan yang anda telah tanda dan semakan markah dalam Quiz Mode akan dipadamkan. Anda boleh memulakan ujian semula dari awal.',
        () => {
          userQuizAnswers = {};
          revealedAnswers.clear();
          localStorage.removeItem('cpre_quiz_answers');
          updateQuizHud();
          renderQuestions();
        }
      );
    }

    function updateQuizHud() {
      const answeredQIds = Object.keys(userQuizAnswers).filter(id => userQuizAnswers[id] && userQuizAnswers[id].length > 0);
      const answeredCount = answeredQIds.length;
      let totalEarnedPts = 0;
      const totalPossiblePts = 70;

      answeredQIds.forEach(id => {
        const q = questions.find(x => x.id === parseInt(id));
        if (!q) return;
        const userAns = userQuizAnswers[id] || [];

        if (q.type === 'A') {
          const correctOpt = (q.options || []).find(o => isOptionCorrect(o, q));
          if (correctOpt && userAns.includes(correctOpt.id)) {
            totalEarnedPts += (q.pts || 1);
          }
        } else if (q.type === 'P') {
          const correctOpts = (q.options || []).filter(o => isOptionCorrect(o, q)).map(o => o.id);
          const correctSelected = userAns.filter(a => correctOpts.includes(a)).length;
          const incorrectSelected = userAns.filter(a => !correctOpts.includes(a)).length;
          const score = Math.max(0, correctSelected - incorrectSelected);
          totalEarnedPts += Math.min(score, q.pts || 2);
        } else if (q.type === 'K') {
          let matches = 0;
          const totalOpts = (q.options || []).length;
          (q.options || []).forEach(o => {
            const isCorr = isOptionCorrect(o, q);
            const userSaysTrue = userAns.includes(o.id);
            if ((isCorr && userSaysTrue) || (!isCorr && !userSaysTrue)) {
              matches++;
            }
          });
          if (totalOpts === 5) {
            if (matches === 5) totalEarnedPts += 2;
            else if (matches === 4) totalEarnedPts += 1;
          } else {
            if (matches === 4) totalEarnedPts += 2;
            else if (matches === 3) totalEarnedPts += 1;
          }
        }
      });

      const percentage = ((totalEarnedPts / totalPossiblePts) * 100).toFixed(1);
      
      const hudAns = document.getElementById('hudAnsweredCount');
      const hudScore = document.getElementById('hudScoreDisplay');
      const hudPct = document.getElementById('hudPercentage');

      if (hudAns) hudAns.textContent = answeredCount;
      if (hudScore) hudScore.textContent = totalEarnedPts + ' Pts';
      if (hudPct) hudPct.textContent = percentage + '%';
    }

    function isOptionCorrect(opt, q) {
      if (typeof opt.truth === 'boolean') return opt.truth;
      if (typeof opt.truth === 'string') {
        const s = opt.truth.trim().toLowerCase();
        if (s.startsWith('does not') || s.includes('false') || s.includes('incorrect')) return false;
        if (s === 'matches' || s === 'applies' || s.includes('needs to be considered') || s === 'true' || s === 'correct') return true;
      }
      if (q.correctDisplay) {
        return q.correctDisplay.includes(opt.id + '=True') || q.correctDisplay.includes(opt.id + '=Matches') || q.correctDisplay.includes(opt.id + '=Applies') || q.correctDisplay.includes(opt.id + '=Needs to be considered') || q.correctDisplay.includes(opt.id + '=Correct') || q.correctDisplay.includes(opt.id + ' (Only') || q.correctDisplay.startsWith(opt.id);
      }
      return false;
    }

    // Smart Reader Formatter (Zero-slop, clean paragraphs and bullets)
    function formatText(text) {
      if (!text) return '';
      const paragraphs = text.split(/\\n\\n+/);
      return paragraphs.map(p => {
        const trimmed = p.trim();
        if (!trimmed) return '';
        
        let formatted = trimmed
          .replace(/\\*\\*(.*?)\\*\\*/g, '<strong class="font-bold text-slate-900 dark:text-white">$1</strong>')
          .replace(/\\\`([^\\\`]+)\\\`/g, '<code class="px-1.5 py-0.5 rounded bg-slate-200 dark:bg-zinc-800 text-slate-900 dark:text-zinc-100 font-mono text-[11px]">$1</code>')
          .replace(/\\n/g, '<br/>');

        if (formatted.startsWith('• ') || formatted.startsWith('- ')) {
          return \`<div class="flex items-start space-x-2 my-1.5"><span class="text-slate-400 dark:text-zinc-500 font-bold shrink-0 leading-relaxed">•</span><span class="leading-relaxed">\${formatted.replace(/^[•\\-]\\s*/, '')}</span></div>\`;
        }
        return \`<p class="leading-relaxed mb-2 last:mb-0">\${formatted}</p>\`;
      }).join('');
    }

    // Render Question Cards
    function renderQuestions() {
      const filtered = questions.filter(q => {
        if (currentEU !== 0 && q.euNo !== currentEU) return false;
        if (currentType !== 'all' && q.type !== currentType) return false;
        if (filterBookmarkedOnly && !bookmarkedIds.has(q.id)) return false;
        if (searchQuery) {
          const matchQ = (q.question || '').toLowerCase().includes(searchQuery);
          const matchCode = (q.code || '').toLowerCase().includes(searchQuery);
          const matchTitle = (q.title || '').toLowerCase().includes(searchQuery);
          const matchWhy = (q.whyCorrect || '').toLowerCase().includes(searchQuery);
          const matchOpts = (q.options || []).some(o => (o.text || '').toLowerCase().includes(searchQuery));
          const matchId = ('q' + q.id).includes(searchQuery);
          if (!matchQ && !matchCode && !matchTitle && !matchWhy && !matchOpts && !matchId) return false;
        }
        return true;
      });

      visibleCountEl.textContent = filtered.length;

      if (filtered.length === 0) {
        if (filterBookmarkedOnly) {
          questionsContainer.innerHTML = \`
            <div class="bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800 rounded-xl p-10 text-center shadow-sm">
              <div class="w-10 h-10 mx-auto mb-3 rounded-full bg-amber-50 dark:bg-amber-950/60 flex items-center justify-center text-amber-500">
                <svg class="w-5 h-5 fill-amber-500" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              </div>
              <div class="text-sm font-bold text-slate-900 dark:text-white mb-1">Tiada soalan bertanda bintang</div>
              <div class="text-xs text-slate-500 dark:text-zinc-400 max-w-sm mx-auto mb-4">Tekan ikon bintang pada mana-mana soalan untuk simpan ke senarai ulangkaji fokus anda.</div>
              <button onclick="toggleBookmarkFilter()" class="h-8 px-3 rounded-lg bg-zinc-900 dark:bg-white text-white dark:text-zinc-950 text-xs font-bold shadow-xs">
                Tunjuk Semua Soalan
              </button>
            </div>
          \`;
        } else {
          questionsContainer.innerHTML = \`
            <div class="bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800 rounded-xl p-10 text-center shadow-sm">
              <div class="text-sm font-bold text-slate-900 dark:text-white mb-1">Tiada soalan sepadan</div>
              <div class="text-xs text-slate-500 dark:text-zinc-400 mb-3">Sila ubah carian kata kunci atau tetapan penapis.</div>
              <button onclick="clearSearch(); filterByEU(0); filterByType('all');" class="h-8 px-3 rounded-lg bg-zinc-900 dark:bg-white text-white dark:text-zinc-950 text-xs font-bold shadow-xs">
                Reset Penapis
              </button>
            </div>
          \`;
        }
        return;
      }

      questionsContainer.innerHTML = filtered.map(q => {
        const isBookmarked = bookmarkedIds.has(q.id);
        const isRevealed = currentMode === 'study' || revealedAnswers.has(q.id);
        const userSelections = userQuizAnswers[q.id] || [];
        const isExpCollapsed = collapsedExplanations.has(q.id);

        // Type Badge styling (Clean shadcn style badge)
        let typeBadgeColor = 'bg-blue-50 dark:bg-blue-950/60 text-blue-700 dark:text-blue-300 border-blue-200 dark:border-blue-900/60';
        if (q.type === 'K') typeBadgeColor = 'bg-purple-50 dark:bg-purple-950/60 text-purple-700 dark:text-purple-300 border-purple-200 dark:border-purple-900/60';
        if (q.type === 'P') typeBadgeColor = 'bg-amber-50 dark:bg-amber-950/60 text-amber-700 dark:text-amber-300 border-amber-200 dark:border-amber-900/60';

        return \`
          <article id="q-card-\${q.id}" class="q-card bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/90 rounded-xl p-4 sm:p-5 shadow-sm transition-all hover:border-slate-300 dark:hover:border-zinc-700">
            
            <!-- Card Header Meta -->
            <div class="flex items-center justify-between gap-2 mb-3">
              <div class="flex flex-wrap items-center gap-1.5 sm:gap-2">
                <span class="inline-flex items-center justify-center h-6 px-2.5 rounded-md bg-zinc-900 dark:bg-white font-mono font-extrabold text-xs text-white dark:text-zinc-950 shadow-xs">
                  Q\${q.id}
                </span>
                <span class="font-mono text-xs text-slate-600 dark:text-zinc-400 font-bold">\${q.code}</span>
                <span class="text-[11px] font-bold px-2 py-0.5 rounded-md border \${typeBadgeColor}">
                  \${q.type}-Type • \${q.pts} \${q.pts > 1 ? 'Pts' : 'Pt'}
                </span>
                <span class="text-[11px] font-medium px-2 py-0.5 rounded-md bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300 border border-slate-200 dark:border-zinc-700/60">
                  EU\${q.euNo}
                </span>
              </div>

              <!-- Bookmark Star Button -->
              <button 
                onclick="toggleBookmark(\${q.id}, event)" 
                class="w-7 h-7 rounded-lg flex items-center justify-center text-slate-400 hover:text-amber-500 bg-slate-50 dark:bg-zinc-800/60 hover:bg-slate-100 dark:hover:bg-zinc-700 border border-slate-200 dark:border-zinc-700/60 transition-all"
                title="Tanda soalan"
              >
                <svg class="w-3.5 h-3.5 \${isBookmarked ? 'fill-amber-400 text-amber-400' : 'text-slate-400 dark:text-zinc-500'}" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M11.48 3.499a.562.562 0 011.04 0l2.125 5.111a.563.563 0 00.475.345l5.518.442c.499.04.701.663.321.988l-4.204 3.602a.563.563 0 00-.182.557l1.285 5.385a.562.562 0 01-.84.61l-4.725-2.885a.563.563 0 00-.586 0L6.982 20.54a.562.562 0 01-.84-.61l1.285-5.386a.562.562 0 00-.182-.557l-4.204-3.602a.563.563 0 01.321-.988l5.518-.442a.563.563 0 00.475-.345L11.48 3.5z" />
                </svg>
              </button>
            </div>

            <!-- Question Statement -->
            <div class="mb-3.5">
              <div class="text-[11px] font-bold text-slate-500 dark:text-zinc-400 uppercase tracking-wider mb-1">\${q.title}</div>
              <div class="text-xs sm:text-[13.5px] font-semibold text-slate-900 dark:text-zinc-100 leading-relaxed">
                \${formatText(q.question)}
              </div>
              \${q.eo ? \`<div class="inline-flex items-center text-[10.5px] text-slate-500 dark:text-zinc-400 font-mono mt-1.5 font-medium px-2 py-0.5 rounded bg-slate-100 dark:bg-zinc-800 border border-slate-200 dark:border-zinc-700/60">EO: \${q.eo}</div>\` : ''}
            </div>

            <!-- Embedded Diagram Illustration (High Contrast PDF Extract) -->
            \${q.diagramHtml || ''}

            <!-- Options List (shadcn Card style) -->
            <div class="space-y-2 mb-3.5">
              \${(q.options || []).map(opt => {
                const optId = opt.id;
                const isSelected = userSelections.includes(optId);
                
                let optStyle = 'bg-slate-50 dark:bg-zinc-950 border-slate-200 dark:border-zinc-800 text-slate-800 dark:text-zinc-200 hover:border-slate-300 dark:hover:border-zinc-700';
                let indicator = '';

                if (isRevealed) {
                  const isCorrect = isOptionCorrect(opt, q);

                  if (isCorrect) {
                    optStyle = 'bg-emerald-50/80 dark:bg-emerald-950/40 border-2 border-emerald-500 dark:border-emerald-600 text-emerald-950 dark:text-emerald-100 font-medium shadow-xs';
                    indicator = \`
                      <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-600 text-white shadow-xs">
                        \${typeof opt.truth === 'boolean' || typeof opt.truth === 'string' ? (opt.truth === true ? 'TRUE' : String(opt.truth).toUpperCase()) : 'CORRECT'}
                      </span>
                    \`;
                  } else {
                    optStyle = 'bg-slate-50/40 dark:bg-zinc-950/40 border border-slate-200 dark:border-zinc-800/80 text-slate-500 dark:text-zinc-400';
                    indicator = \`
                      <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-slate-200 dark:bg-zinc-800 text-slate-600 dark:text-zinc-400">
                        \${typeof opt.truth === 'boolean' || typeof opt.truth === 'string' ? (opt.truth === false ? 'FALSE' : String(opt.truth).toUpperCase()) : 'INCORRECT'}
                      </span>
                    \`;
                  }
                } else if (isSelected) {
                  optStyle = 'bg-indigo-50 dark:bg-indigo-950/50 border-2 border-indigo-500 text-indigo-950 dark:text-indigo-100 font-semibold shadow-xs';
                }

                return \`
                  <div 
                    onclick="handleOptionSelect(\${q.id}, '\${optId}', '\${q.type}')" 
                    class="p-3 rounded-lg border text-xs leading-relaxed flex items-start justify-between gap-3 transition-all cursor-pointer \${optStyle}"
                  >
                    <div class="flex items-start space-x-2.5">
                      <span class="w-5 h-5 rounded-md flex items-center justify-center font-mono font-bold text-[11px] bg-slate-200 dark:bg-zinc-800 text-slate-800 dark:text-zinc-200 shrink-0 mt-0.5">
                        \${optId}
                      </span>
                      <span class="mt-0.5">\${opt.text}</span>
                    </div>
                    <div class="shrink-0 mt-0.5">
                      \${indicator}
                    </div>
                  </div>
                \`;
              }).join('')}
            </div>

            <!-- Quiz Reveal Button -->
            \${!isRevealed ? \`
              <div class="pt-1 flex justify-end">
                <button onclick="revealAnswer(\${q.id})" class="h-8 px-3 rounded-lg bg-zinc-900 dark:bg-white text-white dark:text-zinc-950 text-xs font-bold shadow-xs transition-all hover:opacity-90">
                  Semak Jawapan & Huraian
                </button>
              </div>
            \` : ''}

            <!-- Deep Explanations Section with Clean Callout Cards -->
            \${isRevealed ? \`
              <div class="mt-4 pt-3.5 border-t border-slate-100 dark:border-zinc-800 space-y-3">
                
                <!-- Official Answer Strip (Uniform Header + Dedicated Response Container) -->
                <div class="rounded-xl bg-slate-100/90 dark:bg-zinc-850 border border-slate-200 dark:border-zinc-700/80 p-3 shadow-2xs">
                  <div class="flex items-center justify-between gap-2 pb-2 mb-2 border-b border-slate-200/80 dark:border-zinc-700/60">
                    <div class="flex items-center gap-2">
                      <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-mono font-extrabold bg-zinc-900 dark:bg-white text-white dark:text-zinc-950 uppercase tracking-wider shadow-2xs">
                        Jawapan Rasmi
                      </span>
                      <span class="text-[11px] font-medium text-slate-500 dark:text-zinc-400 hidden sm:inline">Skema Peperiksaan IREB</span>
                    </div>
                    <button 
                      id="exp-toggle-btn-\${q.id}" 
                      onclick="toggleExplanation(\${q.id})" 
                      class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md text-[11.5px] font-bold bg-white dark:bg-zinc-800 hover:bg-slate-50 dark:hover:bg-zinc-700 text-indigo-600 dark:text-indigo-400 border border-slate-200 dark:border-zinc-700 shadow-2xs transition-all shrink-0"
                    >
                      \${isExpCollapsed ? 'Huraian Penuh ▾' : 'Tutup Huraian ▴'}
                    </button>
                  </div>
                  <div class="font-mono text-xs sm:text-[13px] font-bold text-slate-900 dark:text-zinc-100 leading-relaxed break-words bg-white/80 dark:bg-zinc-900/90 p-2.5 rounded-lg border border-slate-200/60 dark:border-zinc-800 shadow-2xs">
                    \${q.correctDisplay || 'Rujuk Pilihan di Atas'}
                  </div>
                </div>

                <div id="exp-body-\${q.id}" class="exp-body space-y-3 text-xs pt-1 \${isExpCollapsed ? 'hidden' : ''}">
                  
                  <!-- Why Correct: Emerald Callout -->
                  \${q.whyCorrect ? \`
                    <div class="p-3.5 rounded-xl border border-emerald-300 dark:border-emerald-800/80 bg-emerald-50/80 dark:bg-emerald-950/40 text-emerald-950 dark:text-emerald-100 shadow-xs">
                      <div class="font-bold text-emerald-800 dark:text-emerald-300 text-xs uppercase tracking-wider mb-2 flex items-center gap-1.5">
                        <svg class="w-4 h-4 text-emerald-600 dark:text-emerald-400 shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path></svg>
                        Penerangan & Logik Betul
                      </div>
                      <div class="space-y-1.5 text-xs font-normal">
                        \${formatText(q.whyCorrect)}
                      </div>
                    </div>
                  \` : ''}

                  <!-- Trap Alert / Why Wrong: Rose Callout -->
                  \${q.whyWrong ? \`
                    <div class="p-3.5 rounded-xl border border-rose-300 dark:border-rose-800/80 bg-rose-50/80 dark:bg-rose-950/40 text-rose-950 dark:text-rose-100 shadow-xs">
                      <div class="font-bold text-rose-800 dark:text-rose-300 text-xs uppercase tracking-wider mb-2 flex items-center gap-1.5">
                        <svg class="w-4 h-4 text-rose-600 dark:text-rose-400 shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd"></path></svg>
                        Perangkap Soalan (Trap Alert) & Pilihan Salah
                      </div>
                      <div class="space-y-1.5 text-xs font-normal">
                        \${formatText(q.whyWrong)}
                      </div>
                    </div>
                  \` : ''}

                  <!-- Handbook Notes: Blue Callout -->
                  \${q.extra ? \`
                    <div class="p-3.5 rounded-xl border border-blue-300 dark:border-blue-800/80 bg-blue-50/80 dark:bg-blue-950/40 text-blue-950 dark:text-blue-100 shadow-xs">
                      <div class="font-bold text-blue-800 dark:text-blue-300 text-xs uppercase tracking-wider mb-2 flex items-center gap-1.5">
                        <svg class="w-4 h-4 text-blue-600 dark:text-blue-400 shrink-0" fill="currentColor" viewBox="0 0 20 20"><path d="M9 4.804A7.968 7.968 0 005.5 4c-1.255 0-2.443.29-3.5.804v10A7.969 7.969 0 015.5 14c1.669 0 3.218.51 4.5 1.385A7.962 7.962 0 0114.5 14c1.255 0 2.443.29 3.5.804v-10A7.968 7.968 0 0014.5 4c-1.255 0-2.443.29-3.5.804V12a1 1 0 11-2 0V4.804z"></path></svg>
                        Rujukan Sukatan & Konsep IREB
                      </div>
                      <div class="space-y-1.5 text-xs font-normal">
                        \${formatText(q.extra)}
                      </div>
                    </div>
                  \` : ''}

                  <!-- Mnemonic: Amber Callout -->
                  \${q.mnemonic ? \`
                    <div class="p-3.5 rounded-xl border border-amber-300 dark:border-amber-800/80 bg-amber-50/80 dark:bg-amber-950/40 text-amber-950 dark:text-amber-100 shadow-xs">
                      <strong class="text-amber-800 dark:text-amber-300 block mb-1.5 text-xs font-bold uppercase tracking-wider">Formula Hafalan (Mnemonic Anchor):</strong>
                      <div class="space-y-1 text-xs font-normal">
                        \${formatText(q.mnemonic)}
                      </div>
                    </div>
                  \` : ''}

                </div>

              </div>
            \` : ''}

          </article>
        \`;
      }).join('');
    }
  </script>
</body>
</html>`;

const outHtmlPath = path.join(rootDir, 'index.html');
fs.writeFileSync(outHtmlPath, htmlContent, 'utf8');
console.log(`Generated upgraded ${outHtmlPath} with Shadcn clean UI & zero AI-slop! Size: ${htmlContent.length} bytes`);
