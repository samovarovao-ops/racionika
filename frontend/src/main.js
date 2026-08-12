const DEMO_MENU = {
  menu_id: "demo_menu_001", version: 1,
  items: [
    { program: "Classic", day: 1, meal: "\u0417\u0430\u0432\u0442\u0440\u0430\u043a", name: "\u041e\u0432\u0441\u044f\u043d\u0430\u044f \u043a\u0430\u0448\u0430 \u0441 \u044f\u0433\u043e\u0434\u0430\u043c\u0438", desc: "\u041e\u0432\u0441\u044f\u043d\u044b\u0435 \u0445\u043b\u043e\u043f\u044c\u044f, \u0441\u0432\u0435\u0436\u0438\u0435 \u044f\u0433\u043e\u0434\u044b, \u043c\u0451\u0434", portions: 1, price: 120, weight: 250 },
    { program: "Classic", day: 1, meal: "\u041e\u0431\u0435\u0434", name: "\u041a\u0443\u0440\u0438\u043d\u044b\u0439 \u0441\u0443\u043f \u0441 \u043b\u0430\u043f\u0448\u043e\u0439", desc: "\u041a\u0443\u0440\u0438\u043d\u044b\u0439 \u0431\u0443\u043b\u044c\u043e\u043d, \u043b\u0430\u043f\u0448\u0430, \u043c\u043e\u0440\u043a\u043e\u0432\u044c, \u0437\u0435\u043b\u0435\u043d\u044c", portions: 1, price: 180, weight: 350 },
    { program: "Classic", day: 1, meal: "\u0423\u0436\u0438\u043d", name: "\u0413\u0440\u0435\u0447\u043a\u0430 \u0441 \u043a\u043e\u0442\u043b\u0435\u0442\u043e\u0439", desc: "\u0413\u0440\u0435\u0447\u043d\u0435\u0432\u0430\u044f \u043a\u0430\u0448\u0430, \u043a\u0443\u0440\u0438\u043d\u0430\u044f \u043a\u043e\u0442\u043b\u0435\u0442\u0430, \u0441\u0430\u043b\u0430\u0442", portions: 1, price: 220, weight: 300 },
    { program: "Classic", day: 1, meal: "\u041f\u0435\u0440\u0435\u043a\u0443\u0441", name: "\u0422\u0432\u043e\u0440\u043e\u0436\u043d\u0430\u044f \u0437\u0430\u043f\u0435\u043a\u0430\u043d\u043a\u0430", desc: "\u0422\u0432\u043e\u0440\u043e\u0433, \u0438\u0437\u044e\u043c, \u0432\u0430\u043d\u0438\u043b\u044c", portions: 1, price: 90, weight: 150 },
    { program: "Classic", day: 2, meal: "\u0417\u0430\u0432\u0442\u0440\u0430\u043a", name: "\u0411\u043b\u0438\u043d\u044b \u0441 \u0442\u0432\u043e\u0440\u043e\u0433\u043e\u043c", desc: "\u0422\u043e\u043d\u043a\u0438\u0435 \u0431\u043b\u0438\u043d\u044b, \u0442\u0432\u043e\u0440\u043e\u0436\u043d\u0430\u044f \u043d\u0430\u0447\u0438\u043d\u043a\u0430", portions: 1, price: 140, weight: 220 },
    { program: "Classic", day: 2, meal: "\u041e\u0431\u0435\u0434", name: "\u0411\u043e\u0440\u0449", desc: "\u0421\u0432\u0435\u043a\u043e\u043b\u044c\u043d\u044b\u0439 \u0441\u0443\u043f, \u0441\u043c\u0435\u0442\u0430\u043d\u0430", portions: 1, price: 190, weight: 350 },
    { program: "Classic", day: 2, meal: "\u0423\u0436\u0438\u043d", name: "\u0420\u044b\u0431\u0430 \u0437\u0430\u043f\u0435\u0447\u0451\u043d\u0430\u044f", desc: "\u0422\u0440\u0435\u0441\u043a\u0430, \u0431\u0440\u043e\u043a\u043a\u043e\u043b\u0438, \u043c\u043e\u0440\u043a\u043e\u0432\u044c", portions: 1, price: 250, weight: 300 },
    { program: "Classic", day: 2, meal: "\u041f\u0435\u0440\u0435\u043a\u0443\u0441", name: "\u0419\u043e\u0433\u0443\u0440\u0442 \u0441 \u043e\u0440\u0435\u0445\u0430\u043c\u0438", desc: "\u041d\u0430\u0442\u0443\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u0439\u043e\u0433\u0443\u0440\u0442, \u0433\u0440\u0435\u0446\u043a\u0438\u0435 \u043e\u0440\u0435\u0445\u0438", portions: 1, price: 80, weight: 150 },
    { program: "Balance", day: 1, meal: "\u0417\u0430\u0432\u0442\u0440\u0430\u043a", name: "\u041e\u043c\u043b\u0435\u0442 \u0441 \u043e\u0432\u043e\u0449\u0430\u043c\u0438", desc: "\u042f\u0439\u0446\u0430, \u043f\u043e\u043c\u0438\u0434\u043e\u0440\u044b, \u0448\u043f\u0438\u043d\u0430\u0442", portions: 1, price: 130, weight: 200 },
    { program: "Balance", day: 1, meal: "\u041e\u0431\u0435\u0434", name: "\u0422\u0451\u043f\u043b\u044b\u0439 \u0441\u0430\u043b\u0430\u0442 \u0441 \u043a\u0443\u0440\u0438\u0446\u0435\u0439", desc: "\u0413\u0440\u0443\u0434\u043a\u0430, \u0430\u0432\u043e\u043a\u0430\u0434\u043e, \u043f\u043e\u043c\u0438\u0434\u043e\u0440\u044b", portions: 1, price: 210, weight: 300 },
    { program: "Balance", day: 1, meal: "\u0423\u0436\u0438\u043d", name: "\u041b\u043e\u0441\u043e\u0441\u044c \u043d\u0430 \u043f\u0430\u0440\u0443", desc: "\u041b\u043e\u0441\u043e\u0441\u044c, \u0441\u043f\u0430\u0440\u0436\u0430, \u0440\u0438\u0441", portions: 1, price: 280, weight: 280 },
    { program: "Balance", day: 1, meal: "\u041f\u0435\u0440\u0435\u043a\u0443\u0441", name: "\u041f\u0440\u043e\u0442\u0435\u0438\u043d\u043e\u0432\u044b\u0439 \u043a\u043e\u043a\u0442\u0435\u0439\u043b\u044c", desc: "\u041f\u0440\u043e\u0442\u0435\u0438\u043d, \u0431\u0430\u043d\u0430\u043d", portions: 1, price: 100, weight: 300 },
    { program: "Vegan", day: 1, meal: "\u0417\u0430\u0432\u0442\u0440\u0430\u043a", name: "\u0413\u0440\u0430\u043d\u043e\u043b\u0430 \u0441 \u043c\u043e\u043b\u043e\u043a\u043e\u043c", desc: "\u0413\u0440\u0430\u043d\u043e\u043b\u0430, \u043c\u0438\u043d\u0434\u0430\u043b\u044c\u043d\u043e\u0435 \u043c\u043e\u043b\u043e\u043a\u043e, \u0431\u0430\u043d\u0430\u043d", portions: 1, price: 110, weight: 250 },
    { program: "Vegan", day: 1, meal: "\u041e\u0431\u0435\u0434", name: "\u0422\u043e\u043c \u044f\u043c \u0441 \u0442\u043e\u0444\u0443", desc: "\u041a\u043e\u043a\u043e\u0441\u043e\u0432\u043e\u0435 \u043c\u043e\u043b\u043e\u043a\u043e, \u0442\u043e\u0444\u0443, \u0433\u0440\u0438\u0431\u044b", portions: 1, price: 200, weight: 350 },
    { program: "Vegan", day: 1, meal: "\u0423\u0436\u0438\u043d", name: "\u0412\u043e\u043a \u0441 \u043e\u0432\u043e\u0449\u0430\u043c\u0438", desc: "\u0411\u0440\u043e\u043a\u043a\u043e\u043b\u0438, \u043c\u043e\u0440\u043a\u043e\u0432\u044c, \u043d\u0443\u0442", portions: 1, price: 190, weight: 300 },
    { program: "Vegan", day: 1, meal: "\u041f\u0435\u0440\u0435\u043a\u0443\u0441", name: "\u0425\u0443\u043c\u0443\u0441", desc: "\u041d\u0443\u0442, \u0442\u0430\u0445\u0438\u043d\u0438, \u043c\u043e\u0440\u043a\u043e\u0432\u044c", portions: 1, price: 85, weight: 180 }
  ],
  tariffs: [
    { program: "Classic", people: 1, weekly_price: 1650 },
    { program: "Classic", people: 2, weekly_price: 3000 },
    { program: "Balance", people: 1, weekly_price: 1950 },
    { program: "Balance", people: 2, weekly_price: 3600 },
    { program: "Vegan", people: 1, weekly_price: 1500 },
    { program: "Vegan", people: 2, weekly_price: 2800 }
  ]
};

function demoCalc(groups, days, startDay) {
  const allResults = [];
  groups.forEach(group => {
    const prog = group.program, adults = group.adults || 0, children = group.children || 0;
    const peopleEquiv = adults + children * 0.5, totalPeople = adults + children;
    const tariff = DEMO_MENU.tariffs.find(t => t.program === prog && t.people === Math.round(peopleEquiv));
    let kitPrice = tariff ? (tariff.weekly_price / 7) * days : DEMO_MENU.items.filter(i => i.program === prog).reduce((s, i) => s + i.price * i.portions * peopleEquiv, 0) * days;
    const plan = [];
    for (let d = 0; d < days; d++) {
      const dayNum = ((startDay - 1 + d) % 7) + 1;
      const items = DEMO_MENU.items.filter(i => i.program === prog);
      const meals = {};
      items.forEach(item => { if (!meals[item.meal]) meals[item.meal] = []; meals[item.meal].push({ "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435_\u0431\u043b\u044e\u0434\u0430": item.name, "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435": item.desc, "\u0426\u0435\u043d\u0430_\u0437\u0430_\u043f\u043e\u0440\u0446\u0438\u044e": item.price, "\u041f\u043e\u0440\u0446\u0438\u0438_\u043d\u0430_\u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0430": item.portions, "\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c_\u0441\u0442\u0440\u043e\u043a\u0438": Math.round(item.price * item.portions * peopleEquiv) }); });
      const mealOrder = ["\u0417\u0430\u0432\u0442\u0440\u0430\u043a", "\u041e\u0431\u0435\u0434", "\u0423\u0436\u0438\u043d", "\u041f\u0435\u0440\u0435\u043a\u0443\u0441"];
      const pr = mealOrder.filter(m => meals[m]).map(m => ({ "\u041f\u0440\u0438\u0451\u043c": m, "\u0431\u043b\u044e\u0434\u0430": meals[m] }));
      const dayCost = pr.reduce((s, m) => s + m["\u0431\u043b\u044e\u0434\u0430"].reduce((bs, b) => bs + b["\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c_\u0441\u0442\u0440\u043e\u043a\u0438"], 0), 0);
      plan.push({ "\u0414\u0435\u043d\u044c": dayNum, "\u043f\u0440\u0438\u0451\u043c\u044b": pr, "\u0434\u043d\u0435\u0432\u043d\u0430\u044f_\u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c": dayCost });
    }
    allResults.push({ program: prog, adults, children, people_equiv: peopleEquiv, kit_price: Math.round(kitPrice), plan });
  });
  const totalKit = allResults.reduce((s, g) => s + g.kit_price, 0);
  const totalPeople = allResults.reduce((s, g) => s + g.adults + g.children, 0);
  const discountPercent = days >= 7 ? 10 : 0;
  const discountAmount = Math.round(totalKit * discountPercent / 100);
  const finalPrice = totalKit - discountAmount;
  return { menu_id: "demo_menu_001", token: "demo_" + Math.random().toString(36).slice(2, 10), groups: allResults, days, start_day: startDay, per_day_cost: Math.round(finalPrice / days), total_kit_price: totalKit, discount_percent: discountPercent, discount_amount: discountAmount, final_price: finalPrice, per_person_per_day: totalPeople > 0 ? Math.round(finalPrice / totalPeople / days) : 0 };
}

const API = '/api';

let currentMenuId = null;
let lastCalcResult = null;
let selectedDayTab = null;
let adminToken = null;
let people = [{ program: 'Classic', type: 'adult' }];
let demoMode = false;

const PROGRAMS = { Classic: '\u041a\u043b\u0430\u0441\u0441\u0438\u043a\u0430', Balance: '\u0411\u0430\u043b\u0430\u043d\u0441', Vegan: '\u0412\u0435\u0433\u0430\u043d' };
const PROGRAM_ICONS = { Classic: '\ud83c\udf5d', Balance: '\ud83e\udd57', Vegan: '\ud83e\udd6c' };
const DAYS_RU = ['', '\u041f\u043d', '\u0412\u0442', '\u0421\u0440', '\u0427\u0442', '\u041f\u0442', '\u0421\u0431', '\u0412\u0441'];
const MEAL_ICONS = { '\u0417\u0430\u0432\u0442\u0440\u0430\u043a': '\u2615', '\u041e\u0431\u0435\u0434': '\ud83c\udf5b', '\u0423\u0436\u0438\u043d': '\ud83c\udf7d', '\u041f\u0435\u0440\u0435\u043a\u0443\u0441': '\ud83c\udf6a' };

const $ = s => document.querySelector(s);
const fmt = v => Math.round(v).toLocaleString('ru-RU');

async function checkBackend() {
  try {
    const r = await fetch(API + '/health', { signal: AbortSignal.timeout(3000) });
    if (r.ok) {
      const ct = r.headers.get('content-type') || '';
      if (ct.includes('application/json')) { demoMode = false; return; }
    }
  } catch {}
  demoMode = true;
  console.log('Backend unavailable, running in demo mode');
}

async function init() {
  await checkBackend();
  handleRoute();
  window.addEventListener('hashchange', handleRoute);
}

function handleRoute() {
  const hash = location.hash || '#/';
  if (hash.startsWith('#/share/')) {
    loadShareResult(hash.split('/')[2]);
  } else if (hash === '#/admin') {
    renderAdminPage();
  } else if (hash === '#/calc') {
    renderCalcPage();
  } else {
    renderWelcomePage();
  }
}

function renderWelcomePage() {
  const app = $('#app');
  const demoBanner = demoMode ? '<div class="demo-banner">Демо-режим: используются тестовые данные</div>' : '';
  app.innerHTML =
    demoBanner +
    '<div class="welcome-page">' +
      '<div class="welcome-card">' +
        '<div class="welcome-emoji">\ud83c\udf7d\ufe0f</div>' +
        '<h1 class="welcome-title">\u0420\u0430\u0446\u0438\u043e\u043d\u0438\u043a\u0430</h1>' +
        '<p class="welcome-tagline">\u0418\u043d\u0442\u0435\u043b\u043b\u0435\u043a\u0442\u0443\u0430\u043b\u044c\u043d\u044b\u0439 \u043a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440 \u0440\u0430\u0446\u0438\u043e\u043d\u043e\u0432</p>' +
        '<p class="welcome-subtitle">\u041f\u043e\u0441\u0447\u0438\u0442\u0430\u0439\u0442\u0435 \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u043f\u0438\u0442\u0430\u043d\u0438\u044f \u043d\u0430 \u043d\u0435\u0434\u0435\u043b\u044e \u0434\u043b\u044f \u0432\u0430\u0448\u0435\u0439 \u0441\u0435\u043c\u044c\u0438</p>' +
        '<div class="welcome-features">' +
          '<div class="welcome-feature"><span class="feature-icon">\ud83d\udcdd</span><span>\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0443 \u043f\u0438\u0442\u0430\u043d\u0438\u044f \u0434\u043b\u044f \u043a\u0430\u0436\u0434\u043e\u0433\u043e</span></div>' +
          '<div class="welcome-feature"><span class="feature-icon">\ud83d\udcb0</span><span>\u0423\u0437\u043d\u0430\u0439\u0442\u0435 \u0446\u0435\u043d\u0443 \u0434\u043e \u0437\u0430\u043a\u0430\u0437\u0430</span></div>' +
          '<div class="welcome-feature"><span class="feature-icon">\ud83d\udcc4</span><span>\u0421\u043a\u0430\u0447\u0430\u0439\u0442\u0435 \u043e\u0442\u0447\u0451\u0442 \u0432 PDF</span></div>' +
        '</div>' +
        '<button class="welcome-btn" onclick="location.hash=\'#/calc\'">\u041d\u0430\u0447\u0430\u0442\u044c \u0440\u0430\u0441\u0447\u0451\u0442 \u2192</button>' +
      '</div>' +
    '</div>';
}

async function loadShareResult(token) {
  const app = $('#app');
  app.innerHTML = '<div class="loading">\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430...</div>';
  try {
    const r = await fetch(API + '/share/' + token);
    if (!r.ok) throw new Error('not found');
    const data = await r.json();
    lastCalcResult = data;
    renderResultView(data);
  } catch {
    app.innerHTML = '<div class="error">\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d</div>';
  }
}

async function loadLatestMenu() {
  if (demoMode) {
    currentMenuId = DEMO_MENU.menu_id;
    return { menu_id: DEMO_MENU.menu_id, version: DEMO_MENU.version };
  }
  try {
    const r = await fetch(API + '/latest-menu');
    if (!r.ok) return null;
    const data = await r.json();
    currentMenuId = data.menu_id;
    return data;
  } catch { return null; }
}

function renderCalcPage() {
  const app = $('#app');
  const demoBanner = demoMode ? '<div class="demo-banner">Демо-режим: используются тестовые данные</div>' : '';
  app.innerHTML = demoBanner + '<header class="header"><h1>\ud83c\udf5d \u0420\u0430\u0446\u0438\u043e\u043d\u0438\u043a\u0430</h1><nav><a href="#/">\u0413\u043b\u0430\u0432\u043d\u0430\u044f</a> <a href="#/admin">\u0410\u0434\u043c\u0438\u043d</a></nav></header><div id="content" class="content"><div class="loading">\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u043c\u0435\u043d\u044e...</div></div>';
  loadLatestMenu().then(menu => {
    if (!menu) { $('#content').innerHTML = '<div class="error">\u041c\u0435\u043d\u044e \u043d\u0435 \u0437\u0430\u0433\u0440\u0443\u0436\u0435\u043d\u043e. \u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u0435 \u0444\u0430\u0439\u043b \u0432 \u0430\u0434\u043c\u0438\u043d\u043a\u0435.</div>'; return; }
    renderCalcForm();
  });
}

function renderCalcForm() {
  const content = $('#content');

  let peopleHtml = people.map((p, i) => {
    let removeBtn = people.length > 1 ? '<button class="btn-remove" onclick="removePerson(' + i + ')">\u00d7</button>' : '';
    return '<div class="person-card"><div class="person-row"><span class="person-num">' + (i + 1) + '</span><select class="program-select" onchange="updatePerson(' + i + ', \'program\', this.value)"><option value="Classic"' + (p.program === 'Classic' ? ' selected' : '') + '>\ud83c\udf5d \u041a\u043b\u0430\u0441\u0441\u0438\u043a\u0430</option><option value="Balance"' + (p.program === 'Balance' ? ' selected' : '') + '>\ud83e\udd57 \u0411\u0430\u043b\u0430\u043d\u0441</option><option value="Vegan"' + (p.program === 'Vegan' ? ' selected' : '') + '>\ud83e\udd6c \u0412\u0435\u0433\u0430\u043d</option></select><select class="type-select" onchange="updatePerson(' + i + ', \'type\', this.value)"><option value="adult"' + (p.type === 'adult' ? ' selected' : '') + '>\u0412\u0437\u0440\u043e\u0441\u043b\u044b\u0439</option><option value="child"' + (p.type === 'child' ? ' selected' : '') + '>\u0420\u0435\u0431\u0451\u043d\u043e\u043a</option></select>' + removeBtn + '</div></div>';
  }).join('');

  content.innerHTML =
    '<form id="calc-form" onsubmit="doCalc(event)">' +
    '<div class="people-container">' +
    '<h3>\u041b\u044e\u0434\u0438</h3>' +
    '<div id="people-list">' + peopleHtml + '</div>' +
    '<button type="button" class="btn-add-person" onclick="addPerson()">+ \u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0430</button>' +
    '</div>' +
    '<div class="params-row">' +
    '<div class="field"><label>\u0414\u043d\u0435\u0439</label><select id="days-select"><option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4</option><option value="5">5</option><option value="6">6</option><option value="7" selected>7 (\u0441\u043a\u0438\u0434\u043a\u0430 -10%)</option></select></div>' +
    '<div class="field"><label>\u0421\u0442\u0430\u0440\u0442</label><select id="start-day-select"><option value="1">\u041f\u043d</option><option value="2">\u0412\u0442</option><option value="3">\u0421\u0440</option><option value="4">\u0427\u0442</option><option value="5">\u041f\u0442</option><option value="6">\u0421\u0431</option><option value="7">\u0412\u0441</option></select></div>' +
    '</div>' +
    '<button type="submit" class="btn-calc">\ud83d\udcca \u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c</button>' +
    '</form>' +
    '<div id="result-area"></div>';

  if (lastCalcResult) renderResult(lastCalcResult, $('#result-area'));
}

function addPerson() {
  people.push({ program: 'Classic', type: 'adult' });
  renderCalcForm();
}

function removePerson(idx) {
  if (people.length <= 1) return;
  people.splice(idx, 1);
  renderCalcForm();
}

function updatePerson(idx, field, value) {
  people[idx][field] = value;
}

async function doCalc(e) {
  e.preventDefault();
  const days = parseInt($('#days-select').value);
  const startDay = parseInt($('#start-day-select').value);
  const groups = people.map(p => p.type === 'child'
    ? { program: p.program, adults: 0, children: 1 }
    : { program: p.program, adults: 1, children: 0 });

  const body = { menu_id: currentMenuId, groups: groups, days: days, start_day: startDay };

  const resultArea = $('#result-area');
  resultArea.innerHTML = '<div class="loading">\u0420\u0430\u0441\u0447\u0451\u0442...</div>';
  try {
    let data;
    if (demoMode) {
      data = demoCalc(groups, days, startDay);
    } else {
      const r = await fetch(API + '/calc', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
      if (!r.ok) { const err = await r.json(); throw new Error(err.detail || '\u041e\u0448\u0438\u0431\u043a\u0430'); }
      data = await r.json();
    }
    lastCalcResult = data;
    selectedDayTab = 0;
    renderResult(data, resultArea);
  } catch (err) {
    resultArea.innerHTML = '<div class="error">\u041e\u0448\u0438\u0431\u043a\u0430: ' + err.message + '</div>';
  }
}

function renderResult(data, container) {
  const hasDiscount = data.discount_percent > 0;

  let peopleSummary = data.groups.map((g, i) => {
    const progName = PROGRAMS[g.program] || g.program;
    const icon = PROGRAM_ICONS[g.program] || '';
    const typeLabel = g.children > 0 ? ' (\u0440\u0435\u0431\u0451\u043d\u043e\u043a)' : '';
    return '<div class="summary-person"><div class="summary-person-icon">' + icon + '</div><div class="summary-person-info"><strong>\u0427\u0435\u043b\u043e\u0432\u0435\u043a ' + (i + 1) + typeLabel + '</strong><span>' + progName + '</span></div><div class="summary-person-price">' + fmt(g.kit_price) + ' \u20bd</div></div>';
  }).join('');

  let discountHtml = '';
  if (hasDiscount) {
    discountHtml = '<div class="discount-panel"><div class="discount-badge">-' + data.discount_percent + '%</div><div class="discount-info"><div class="discount-title">\u0421\u043a\u0438\u0434\u043a\u0430 \u0437\u0430 \u0437\u0430\u043a\u0430\u0437 7 \u0434\u043d\u0435\u0439</div><div class="discount-amount">-' + fmt(data.discount_amount) + ' \u20bd</div></div></div>';
  }

  container.innerHTML =
    '<div class="result-summary"><h3>\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442</h3>' +
    peopleSummary +
    '<div class="summary-totals">' +
    '<div class="total-row"><span>\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0432 \u0434\u0435\u043d\u044c:</span><strong>' + fmt(data.per_day_cost) + ' \u20bd</strong></div>' +
    '<div class="total-row"><span>\u0418\u0442\u043e\u0433\u043e:</span><strong class="final-price">' + fmt(data.total_kit_price) + ' \u20bd</strong></div>' +
    (hasDiscount ? '<div class="total-row discount"><span>\u0421\u043e \u0441\u043a\u0438\u0434\u043a\u043e\u0439:</span><strong class="final-price discount">' + fmt(data.final_price) + ' \u20bd</strong></div>' : '') +
    '<div class="total-row"><span>\u0417\u0430 \u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0430 \u0432 \u0434\u0435\u043d\u044c:</span><strong>' + fmt(data.per_person_per_day) + ' \u20bd</strong></div>' +
    '</div>' + discountHtml + '</div>' +
    '<div class="days-tabs" id="days-tabs"></div>' +
    '<div id="day-detail"></div>' +
    '<div class="actions">' +
    '<button class="btn-pdf" onclick="downloadPDF()">\ud83d\udcc4 \u0421\u043a\u0430\u0447\u0430\u0442\u044c PDF</button>' +
    '<button class="btn-share" onclick="shareToTelegram()">\ud83d\udcf2 \u041f\u043e\u0434\u0435\u043b\u0438\u0442\u044c\u0441\u044f \u0432 Telegram</button>' +
    '<button class="btn-order" onclick="createWebOrder()">\ud83d\uded2 \u041e\u0444\u043e\u0440\u043c\u0438\u0442\u044c \u0437\u0430\u043a\u0430\u0437</button>' +
    '</div>';

  renderDaysTabs(data);
}

function renderDaysTabs(data) {
  const tabsEl = $('#days-tabs');
  if (!tabsEl || !data.groups.length) return;
  const plan = data.groups[0].plan;
  tabsEl.innerHTML = plan.map((day, i) => {
    const dayName = DAYS_RU[day['\u0414\u0435\u043d\u044c']] || '';
    return '<button class="day-tab ' + (selectedDayTab === i ? 'active' : '') + '" onclick="selectDay(' + i + ')">\u0414\u0435\u043d\u044c ' + day['\u0414\u0435\u043d\u044c'] + ' <small>' + dayName + '</small></button>';
  }).join('');
  if (selectedDayTab === null) selectedDayTab = 0;
  renderDayDetail(data, selectedDayTab);
}

function selectDay(idx) {
  selectedDayTab = idx;
  if (!lastCalcResult) return;
  renderDaysTabs(lastCalcResult);
  renderDayDetail(lastCalcResult, idx);
}

function renderDayDetail(data, dayIdx) {
  const detailEl = $('#day-detail');
  if (!detailEl) return;
  let html = '';
  data.groups.forEach((g, gi) => {
    const progName = PROGRAMS[g.program] || g.program;
    const icon = PROGRAM_ICONS[g.program] || '';
    const day = g.plan[dayIdx];
    if (!day) return;
    html += '<div class="group-day-block"><div class="group-day-header">' + icon + ' \u0427\u0435\u043b\u043e\u0432\u0435\u043a ' + (gi + 1) + ' \u2014 ' + progName + '</div>';
    day['\u043f\u0440\u0438\u0451\u043c\u044b'].forEach(meal => {
      const mealIcon = MEAL_ICONS[meal['\u041f\u0440\u0438\u0451\u043c']] || '';
      html += '<div class="meal-block"><div class="meal-title">' + mealIcon + ' ' + meal['\u041f\u0440\u0438\u0451\u043c'] + '</div>';
      meal['\u0431\u043b\u044e\u0434\u0430'].forEach(b => {
        html += '<div class="dish-item"><div class="dish-name">' + b['\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435_\u0431\u043b\u044e\u0434\u0430'] + '</div><div class="dish-desc">' + b['\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'] + '</div><div class="dish-meta"><span>\u0426\u0435\u043d\u0430: ' + fmt(b['\u0426\u0435\u043d\u0430_\u0437\u0430_\u043f\u043e\u0440\u0446\u0438\u044e']) + ' \u20bd</span><span>\u041f\u043e\u0440\u0446\u0438\u0438: ' + b['\u041f\u043e\u0440\u0446\u0438\u0438_\u043d\u0430_\u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0430'] + '</span><span class="dish-cost">' + fmt(b['\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c_\u0441\u0442\u0440\u043e\u043a\u0438']) + ' \u20bd</span></div></div>';
      });
      html += '</div>';
    });
    html += '<div class="day-total">\u0418\u0442\u043e\u0433\u043e \u0437\u0430 \u0434\u0435\u043d\u044c: ' + fmt(day['\u0434\u043d\u0435\u0432\u043d\u0430\u044f_\u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c']) + ' \u20bd</div></div>';
  });
  detailEl.innerHTML = html;
}

async function downloadPDF() {
  if (!lastCalcResult) return;
  if (typeof jsPDF === 'undefined') { alert('PDF library not loaded. Check your internet connection.'); return; }
  const doc = new jsPDF();
  const data = lastCalcResult;
  let y = 15;

  doc.setFontSize(16);
  doc.text('Racionika', 105, y, { align: 'center' });
  y += 8;
  doc.setFontSize(10);
  doc.text('Programs: ' + data.groups.map(g => g.program).join(', '), 105, y, { align: 'center' });
  y += 6;
  doc.text('Days: ' + data.days, 105, y, { align: 'center' });
  y += 12;

  data.groups.forEach((g, i) => {
    if (y > 260) { doc.addPage(); y = 15; }
    doc.setFontSize(12);
    doc.text('#' + (i + 1) + ' ' + g.program + (g.children > 0 ? ' (child)' : ''), 10, y);
    doc.text(g.kit_price + ' RUB', 200, y, { align: 'right' });
    y += 10;

    g.plan.forEach(day => {
      if (y > 260) { doc.addPage(); y = 15; }
      doc.setFontSize(10);
      doc.text('Day ' + day['\u0414\u0435\u043d\u044c'], 14, y);
      y += 7;

      const mealOrder = ['\u0417\u0430\u0432\u0442\u0440\u0430\u043a', '\u041e\u0431\u0435\u0434', '\u0423\u0436\u0438\u043d', '\u041f\u0435\u0440\u0435\u043a\u0443\u0441'];
      day['\u043f\u0440\u0438\u0451\u043c\u044b'].forEach(priem => {
        doc.setFontSize(9);
        doc.text(priem['\u041f\u0440\u0438\u0451\u043c'], 18, y);
        y += 5;
        priem['\u0431\u043b\u044e\u0434\u0430'].forEach(b => {
          if (y > 270) { doc.addPage(); y = 15; }
          doc.setFontSize(8);
          doc.text(b['\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435_\u0431\u043b\u044e\u0434\u0430'] + ' - ' + b['\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c_\u0441\u0442\u0440\u043e\u043a\u0438'] + ' RUB', 22, y);
          y += 4;
        });
        y += 2;
      });
      doc.setFontSize(8);
      doc.text('Day total: ' + day['\u0434\u043d\u0435\u0432\u043d\u0430\u044f_\u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c'] + ' RUB', 180, y, { align: 'right' });
      y += 6;
    });
    y += 4;
  });

  if (y > 250) { doc.addPage(); y = 15; }
  doc.setFontSize(11);
  doc.text('Total: ' + data.total_kit_price + ' RUB', 10, y);
  y += 7;
  if (data.discount_amount > 0) {
    doc.text('Discount (' + data.discount_percent + '%): -' + data.discount_amount + ' RUB', 10, y);
    y += 7;
    doc.text('Final: ' + data.final_price + ' RUB', 10, y);
  }

  doc.save('racionika_report.pdf');
}

function shareToTelegram() {
  if (!lastCalcResult || !lastCalcResult.token) return;
  const url = 'https://t.me/RacionikaBot?start=share_' + lastCalcResult.token;
  window.open(url, '_blank');
}

async function createWebOrder() {
  if (!lastCalcResult) return;
  if (demoMode) {
    alert('Order creation is only available with a connected backend. Run the app locally for full functionality.');
    return;
  }
  const body = {
    menu_id: lastCalcResult.menu_id,
    groups: lastCalcResult.groups.map(g => ({ program: g.program, adults: g.adults, children: g.children })),
    days: lastCalcResult.days,
    start_day: lastCalcResult.start_day,
    user_id: 0,
    user_name: '\u0412\u0435\u0431-\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c',
    source: 'web',
  };
  try {
    const r = await fetch(API + '/orders', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
    if (r.ok) {
      alert('\u2705 \u0417\u0430\u043a\u0430\u0437 \u0441\u043e\u0437\u0434\u0430\u043d! \u041c\u044b \u0441\u0432\u044f\u0436\u0435\u043c\u0441\u044f \u0441 \u0432\u0430\u043c\u0438.');
    } else {
      alert('\u041e\u0448\u0438\u0431\u043a\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0437\u0430\u043a\u0430\u0437\u0430.');
    }
  } catch (err) { alert('\u041e\u0448\u0438\u0431\u043a\u0430: ' + err.message); }
}

function renderResultView(data) {
  const app = $('#app');
  app.innerHTML = '<header class="header"><h1>\ud83c\udf5d \u0420\u0430\u0446\u0438\u043e\u043d\u0438\u043a\u0430</h1><nav><a href="#/">\u0413\u043b\u0430\u0432\u043d\u0430\u044f</a> <a href="#/calc">\u041a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440</a></nav></header><div class="content" id="result-view"></div>';
  renderResult(data, $('#result-view'));
}

function renderAdminPage() {
  const app = $('#app');
  app.innerHTML = '<header class="header"><h1>\ud83d\uded1 \u0410\u0434\u043c\u0438\u043d\u043a\u0430</h1><nav><a href="#/">\u0413\u043b\u0430\u0432\u043d\u0430\u044f</a> <a href="#/calc">\u041a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440</a></nav></header><div class="content">' + (adminToken ? renderAdminPanel() : renderLoginForm()) + '</div>';
  if (adminToken) { loadAdminVersions(); loadAdminOrders(); }
}

function renderLoginForm() {
  return '<form onsubmit="adminLogin(event)" class="login-form"><h3>\u0412\u0445\u043e\u0434</h3><div class="field"><label>\u041f\u0430\u0440\u043e\u043b\u044c</label><input type="password" id="admin-password" placeholder="\u041f\u0430\u0440\u043e\u043b\u044c"></div><button type="submit" class="btn-calc">\u0412\u043e\u0439\u0442\u0438</button></form>';
}

function renderAdminPanel() {
  return '<div class="admin-panel"><h3>\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u043c\u0435\u043d\u044e</h3><form onsubmit="adminUploadFile(event)" class="upload-form"><input type="file" id="menu-file" accept=".xlsx,.xls"><button type="submit" class="btn-calc">\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c</button></form><div id="upload-result"></div><h3>\u0412\u0435\u0440\u0441\u0438\u0438 \u043c\u0435\u043d\u044e</h3><div id="versions-list">\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430...</div><h3>\u0417\u0430\u043a\u0430\u0437\u044b</h3><div id="orders-list">\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430...</div></div>';
}

async function adminLogin(e) {
  e.preventDefault();
  const password = $('#admin-password').value;
  try {
    const r = await fetch(API + '/admin/login', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ password }) });
    if (r.ok) { adminToken = password; renderAdminPage(); loadAdminVersions(); }
    else { alert('\u041d\u0435\u0432\u0435\u0440\u043d\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c'); }
  } catch (err) { alert('\u041e\u0448\u0438\u0431\u043a\u0430: ' + err.message); }
}

async function adminUploadFile(e) {
  e.preventDefault();
  const fileInput = $('#menu-file');
  if (!fileInput.files.length) return;
  const formData = new FormData();
  formData.append('file', fileInput.files[0]);
  try {
    const r = await fetch(API + '/upload-menu', { method: 'POST', headers: { 'X-Admin-Password': adminToken }, body: formData });
    const data = await r.json();
    const resultDiv = $('#upload-result');
    if (data.errors && data.errors.length) {
      resultDiv.innerHTML = '<div class="error">\u041e\u0448\u0438\u0431\u043a\u0438:<br>' + data.errors.map(e => e.message).join('<br>') + '</div>';
    } else {
      currentMenuId = data.menu_id;
      resultDiv.innerHTML = '<div class="success">\u041c\u0435\u043d\u044e \u0437\u0430\u0433\u0440\u0443\u0436\u0435\u043d\u043e: ' + data.row_count + ' \u0441\u0442\u0440\u043e\u043a, \u0432\u0435\u0440\u0441\u0438\u044f ' + data.version + '</div>';
      loadAdminVersions();
    }
  } catch (err) { alert('\u041e\u0448\u0438\u0431\u043a\u0430 \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0438: ' + err.message); }
}

async function loadAdminVersions() {
  try {
    const r = await fetch(API + '/admin/versions', { headers: { 'X-Admin-Password': adminToken } });
    const versions = await r.json();
    const list = $('#versions-list');
    if (!list) return;
    list.innerHTML = versions.map(v => '<div class="version-item"><span>v' + v.version + ' \u2014 ' + v.filename + ' (' + v.row_count + ' \u0441\u0442\u0440\u043e\u043a)</span><span class="version-id">' + v.menu_id + '</span></div>').join('');
  } catch { const list = $('#versions-list'); if (list) list.innerHTML = '\u041d\u0435 \u0443\u0434\u0430\u043b\u043e\u0441\u044c \u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c'; }
}

async function loadAdminOrders() {
  try {
    const r = await fetch(API + '/orders', { headers: { 'X-Admin-Password': adminToken } });
    const orders = await r.json();
    const list = $('#orders-list');
    if (!list) return;
    if (!orders.length) { list.innerHTML = '\u0417\u0430\u043a\u0430\u0437\u043e\u0432 \u043f\u043e\u043a\u0430 \u043d\u0435\u0442'; return; }
    const statusLabels = { pending: '\u23f3 \u041e\u0436\u0438\u0434\u0430\u0435\u0442', confirmed: '\u2705 \u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0451\u043d', cancelled: '\u274c \u041e\u0442\u043c\u0435\u043d\u0451\u043d' };
    list.innerHTML = orders.map(o => {
      const st = statusLabels[o.status] || o.status;
      const src = o.source === 'telegram' ? '\ud83d\udcf2 TG' : '\ud83c\udf10 Web';
      const groups = (o.groups || []).map(g => PROGRAMS[g.program] || g.program).join(', ');
      const btns = o.status === 'pending'
        ? '<button class="btn-sm btn-success" onclick="confirmOrder(\'' + o.order_id + '\')">\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c</button> <button class="btn-sm btn-danger" onclick="cancelOrder(\'' + o.order_id + '\')">\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c</button>'
        : '';
      return '<div class="order-item"><span class="order-id">#' + o.order_id.slice(0, 8) + '</span><span class="order-src">' + src + '</span><span class="order-groups">' + groups + ' (' + o.days + ' \u0434.)</span><span class="order-status">' + st + '</span><span class="order-user">@' + (o.user_name || '?') + '</span>' + btns + '</div>';
    }).join('');
  } catch { const list = $('#orders-list'); if (list) list.innerHTML = '\u041d\u0435 \u0443\u0434\u0430\u043b\u043e\u0441\u044c \u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c'; }
}

async function confirmOrder(orderId) {
  try {
    await fetch(API + '/orders/' + orderId, { method: 'PATCH', headers: { 'Content-Type': 'application/json', 'X-Admin-Password': adminToken }, body: JSON.stringify({ status: 'confirmed' }) });
    loadAdminOrders();
  } catch {}
}

async function cancelOrder(orderId) {
  try {
    await fetch(API + '/orders/' + orderId, { method: 'PATCH', headers: { 'Content-Type': 'application/json', 'X-Admin-Password': adminToken }, body: JSON.stringify({ status: 'cancelled' }) });
    loadAdminOrders();
  } catch {}
}

init();

window.addPerson = addPerson;
window.removePerson = removePerson;
window.updatePerson = updatePerson;
window.doCalc = doCalc;
window.selectDay = selectDay;
window.downloadPDF = downloadPDF;
window.shareToTelegram = shareToTelegram;
window.createWebOrder = createWebOrder;
window.adminLogin = adminLogin;
window.adminUploadFile = adminUploadFile;
window.confirmOrder = confirmOrder;
window.cancelOrder = cancelOrder;
