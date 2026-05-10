import './style.css'

const subjects = [
  { name: 'Algorithms', icon: '🧠', size: 'lg', path: 'Algorithms' },
  { name: 'Machine Learning', icon: '⚡', size: 'md', path: 'Machine Learning' },
  { name: 'Data Structures', icon: '📊', size: 'md', path: 'Data Structure through Python' },
  { name: 'Artificial Intelligence', icon: '🤖', size: 'md', path: 'Artificial Intelligence' },
  { name: 'Linear Algebra', icon: '📈', size: 'lg', path: 'Linear Algebra' },
  { name: 'DBMS', icon: '🗄️', size: 'sm', path: 'Database Management System' },
  { name: 'Calculus', icon: '📐', size: 'sm', path: 'Calculas and Optimization' },
  { name: 'Aptitude', icon: '💡', size: 'sm', path: 'General Aptitude' },
  { name: 'Stats', icon: '📉', size: 'sm', path: 'Probability and Statics' }
];

const app = document.querySelector('#app');

const render = () => {
  app.innerHTML = `
    <nav class="nav">
      <div class="logo">PW-GATE PRO</div>
      <div style="color: var(--text-dim); font-size: 0.875rem;">FREE RESOURCE HUB</div>
    </nav>

    <header class="hero">
      <h1>Master the Gate.</h1>
      <p>Premium curated notes for elite performance. Designed for focus, built for speed.</p>
    </header>

    <div class="grid">
      ${subjects.map((s, i) => `
        <div class="card card-${s.size}" onclick="handleCardClick('${s.path}')">
          <div>
            <div class="tag">SUBJECT // 0${i + 1}</div>
            <h3>${s.name}</h3>
            <p style="color: var(--text-secondary); font-size: 0.875rem;">Access high-quality class notes and problem sets.</p>
          </div>
          <div class="icon">${s.icon}</div>
        </div>
      `).join('')}
    </div>

    <footer class="footer">
      &copy; 2026 PW-GATE PRO • MADE WITH PASSION FOR GATE ASPIRANTS
    </footer>
  `;
};

window.handleCardClick = (path) => {
  // Use absolute path relative to the repository name on GitHub Pages
  const basePath = '/free-pw-notes-for-gate/';
  window.open(window.location.origin + basePath + path, '_blank');
};

// Add mouse-move glow effect
document.addEventListener('mousemove', (e) => {
  const cards = document.querySelectorAll('.card');
  cards.forEach(card => {
    const rect = card.getBoundingClientRect();
    const x = ((e.clientX - rect.left) / rect.width) * 100;
    const y = ((e.clientY - rect.top) / rect.height) * 100;
    card.style.setProperty('--x', `${x}%`);
    card.style.setProperty('--y', `${y}%`);
  });
});

render();
