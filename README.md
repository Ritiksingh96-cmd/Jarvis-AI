# 🤖 JARVIS AI - Personal Assistant & OS Controller

Welcome to the **JARVIS AI Core**, a powerful, premium-themed AI assistant designed to control your Windows system, manage tasks, and provide a high-end interface inspired by Tony Stark's legendary AI.

---

## 🛠️ Tech Stack

### Backend (System Logic)
- **Language**: Python 3.11+
- **AI Engine**: OpenAI GPT-4 / OpenRouter (supporting GPT-4o, Claude 3, etc.)
- **Voice Recognition**: `SpeechRecognition` (Google Speech API)
- **Text-to-Speech (TTS)**: `pyttsx3` (Offline SAPI5 support)
- **Automation**: `pyautogui`, `AppOpener`
- **Internet Services**: `requests`, `webbrowser`

### Frontend (Dashboard)
- **Core**: HTML5, Vanilla JavaScript (ES6+)
- **Styling**: CSS3 (Glassmorphism, Arc Reactor animations)
- **Framework**: Flask (Python) for the Backend-to-Dashboard bridge
- **Real-time Data**: WebSockets/JSON API

---

## 📚 Required Python Libraries

To run the full JARVIS experience, ensure these libraries are installed:

```bash
# Core Dependencies
pip install openai python-dotenv SpeechRecognition pyttsx3 rich requests AppOpener

# Dashboard & Automation Dependencies
pip install flask flask-cors pyautogui
```

---

## 🚀 Run Commands

### 1. The Ultimate Mode (Voice Controller)
The primary desktop version with system control and voice interaction.
```bash
python jarvis_ultimate.py
```

### 2. The Web Dashboard (Best Visuals)
Launches the Flask server and the Arc Reactor dashboard.
```bash
python dashboard_server.py
```
*Access the dashboard at `http://localhost:5000`*

### 3. Siri-Lite Mode (Direct App Control)
A lighter version optimized for quick app launching and searches.
```bash
python jarvis_siri.py
```

### 4. Pro Mode (Research & Search)
Optimized for complex web searches and deep queries.
```bash
python jarvis_pro.py
```

### 5. Utilities
```bash
# Check if your system is ready
python check_system.py

# Test your OpenRouter API key
python check_key.py
```

---

## ⚙️ Configuration (.env)

Create a `.env` file in the root directory and add your credentials:

```text
OPENAI_API_KEY=your_openrouter_or_openai_key
GITHUB_TOKEN=your_github_token_for_backups
```

---

## 🌟 Features Breakdown

- **Arc Reactor Dashboard**: Real-time visual feedback of AI activity.
- **System Commands**: Volume control, PC locking, and application launching.
- **GitHub Backup**: Integrated private repo creation to save your code.
- **Multi-Mode**: Switch between Text-only, Voice-active, and Web-based control.
- **Context Awareness**: Remembers previous commands for fluid conversation.

---

**"I am JARVIS, Sir. At your service."** 🦾✨
