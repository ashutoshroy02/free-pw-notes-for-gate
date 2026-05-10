import './style.css'

const subjects = [
  { name: 'Algorithms', icon: '🧠', count: 12, path: '../Algorithms' },
  { name: 'Artificial Intelligence', icon: '🤖', count: 8, path: '../Artificial Intelligence' },
  { name: 'Calculus & Optimization', icon: '📐', count: 15, path: '../Calculus and Optimization' },
  { name: 'Data Structures', icon: '📊', count: 20, path: '../Data Structure through Python' },
  { name: 'Machine Learning', icon: '⚡', count: 25, path: '../Machine Learning' },
  { name: 'DBMS', icon: '🗄️', count: 10, path: '../Database Management System' },
  { name: 'Linear Algebra', icon: '📈', count: 14, path: '../Linear Algebra' },
  { name: 'General Aptitude', icon: '💡', count: 18, path: '../General Aptitude' }
];

document.querySelector('#app').innerHTML = `
  <header class="header">
    <h1>Free PW Notes for GATE</h1>
    <p>The most premium collection of GATE study materials, organized for deep focus and ultimate performance.</p>
  </header>

  <div class="subject-grid">
    ${subjects.map((s, i) => `
      <div class="card" style="--i: ${i + 1}" onclick="window.open('${s.path}', '_blank')">
        <div>
          <div class="icon">${s.icon}</div>
          <h3>${s.name}</h3>
          <p>Complete class notes, practice sets, and advanced topics.</p>
        </div>
        <div class="stats">
          <span>${s.count} FILES</span>
          <span>•</span>
          <span>UPDATED 2D AGO</span>
        </div>
      </div>
    `).join('')}
  </div>

  <nav class="nav-bottom">
    <a href="#">Dashboard</a>
    <a href="#">Subjects</a>
    <a href="#">Resources</a>
  </nav>
`
