<h1>🎮 Tic Tac Toe (Python + Tkinter)</h1>

<p>
  A simple <strong>Tic Tac Toe</strong> game built with
  <strong>Python’s Tkinter GUI toolkit</strong>. Play against another human or the built-in
  <em>Computer AI</em> that tries to block your moves and win strategically.
</p>


<h2>🚀 Features</h2>
<ul>
  <li>Play <strong>Human vs Human</strong> or <strong>Human vs Computer</strong></li>
  <li>Computer AI with a <strong>basic strategy</strong> (win → block → center → corners)</li>
  <li><strong>Play Again</strong> (reset) option</li>
  <li>Clean and minimal <strong>Tkinter GUI</strong></li>
</ul>

<h2>📂 Repository Structure</h2>
<pre><code>tic-tac-toe/
│── Game.py     
│── ui.py      
│── board.py   
│── logic.py    
│── ai.py    
│── README.md  
│── NOTICE
└── LICENSE
</code></pre>

<h2>📝 File Descriptions</h2>
<ul>
  <li>
    <a href="https://github.com/SupratikB23/Tic-Tac-Toe-Game/blob/main/Game.py"><code>Game.py</code></a> — Entry point. Initializes the Tkinter root window and starts the game loop.
  </li>
  <li>
    <a href="https://github.com/SupratikB23/Tic-Tac-Toe-Game/blob/main/ui.py"><code>ui.py</code></a> — UI setup (title, status label, buttons, play area). Handles switching between
    “Play with Human” and “Play with Computer”.
  </li>
  <li>
    <a href="https://github.com/SupratikB23/Tic-Tac-Toe-Game/blob/main/board.py"><code>board.py</code></a> — Defines the <code>XOPoint</code> class representing each grid cell and
    tracks moves made by <code>X</code> and <code>O</code>.
  </li>
  <li>
    <a href="https://github.com/SupratikB23/Tic-Tac-Toe-Game/blob/main/logic.py"><code>logic.py</code></a> — Declares winning lines, checks for a winner/draw, and disables input when the game ends.
  </li>
  <li>
    <a href="https://github.com/SupratikB23/Tic-Tac-Toe-Game/blob/main/ai.py"><code>ai.py</code></a> — Computer opponent logic (<code>auto_play</code>): try to win, otherwise block, otherwise take center or corners.
  </li>
</ul>

<h2>🖥️ How to Run</h2>
<ol>
  <li>
    <p><strong>Clone</strong> the repository:</p>
    <pre><code>git clone https://github.com/SupratikB23/tic-tac-toe.git
cd tic-tac-toe
</code></pre>
  </li>
  <li>
    <p><strong>Run</strong> the app:</p>
    <pre><code>python main.py
</code></pre>
  </li>
  <li>
    <p><strong>Play</strong>:</p>
    <ul>
      <li>Click <em>“Play with Human”</em> to face another person.</li>
      <li>Click <em>“Play with Computer”</em> to face the AI.</li>
    </ul>
  </li>
</ol>

<h2>📜 License</h2>
<p>
  This project is licensed under the Apache-2.0 license.
</p>
