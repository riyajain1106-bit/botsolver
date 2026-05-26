# Botsolver 🤖

> *A sleek, intelligent chat interface powered by one of the world's fastest AI inference engines — built for the terminal generation, redesigned for the web.*

Botsolver brings conversational AI to your browser with a clean, minimal UI inspired by ChatGPT. Ask anything. Get answers instantly.

---

## ✨ Features

- **Real-time AI chat** — powered by Groq's ultra-fast LLaMA 3.3 70B model
- **ChatGPT-style UI** — dark theme, typing indicators, smooth auto-scroll
- **Serverless backend** — API key stays server-side, never exposed to the browser
- **Zero dependencies on the frontend** — pure HTML, CSS, and JavaScript
- **Vercel-ready** — deploy in under a minute

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Backend | Node.js (Vercel Serverless Function) |
| AI Model | LLaMA 3.3 70B via Groq API |
| Deployment | Vercel |

---

## 📸 Screenshots

> *Coming soon — add your screenshots here.*

<!-- Replace with actual screenshots -->
```
[ Screenshot of chat interface ]
[ Screenshot of a response ]
```

---

## 🚀 Live Demo

🔗 **[botsolver.vercel.app](https://botsolver.vercel.app/)**

---

## ⚙️ Setup & Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/riyajain1106-bit/botsolver.git
cd botsolver
```

### 2. Add your API key

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key_here
```

Get your free API key at [console.groq.com](https://console.groq.com).

### 3. Run the dev server

```bash
npm run dev
```

Open **http://localhost:3000** in your browser.

---

## 🔐 Environment Variables

| Variable | Description |
|----------|-------------|
| `GROQ_API_KEY` | Your Groq API key — never commit this |

For Vercel deployment, add this in:
**Project Settings → Environment Variables**

---

## 📁 Project Structure

```
botsolver/
├── index.html        # Frontend UI
├── api/
│   └── chat.js       # Vercel serverless function (Groq proxy)
├── server.js         # Local dev server
├── package.json      # npm scripts
├── vercel.json       # Vercel deployment config
├── .env              # Local env vars (not committed)
└── .gitignore
```

---

## 🌐 Deploy to Vercel

1. Push this repo to GitHub
2. Import it at [vercel.com/new](https://vercel.com/new)
3. Add `GROQ_API_KEY` under **Settings → Environment Variables**
4. Hit **Deploy**

---

<p align="center">Built with curiosity · Powered by Groq · Deployed on Vercel</p>
