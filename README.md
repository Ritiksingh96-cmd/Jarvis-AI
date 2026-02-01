# 🤖 JARVIS AI Agent - Complete Package

Welcome to your personal JARVIS AI Assistant, inspired by Tony Stark's AI from Iron Man!

## 📦 What's Included

This package contains **THREE versions** of JARVIS:

### 1. 🎯 JARVIS Lite (Recommended)
**File:** `jarvis_lite.py`

- ✅ Works with Python 3.13+
- ✅ Voice recognition with wake word detection
- ✅ Text-to-speech responses
- ✅ GPT-4 powered conversations
- ✅ Both text and voice modes
- ✅ Conversation memory
- ❌ Cannot execute code

**Best for:** General use, conversations, information, and assistance

### 2. 🚀 JARVIS Enhanced
**File:** `jarvis_enhanced.py`

- ✅ Full Open Interpreter integration
- ✅ Can execute code on your computer
- ✅ Voice and text modes
- ✅ System control capabilities
- ❌ Requires Python 3.9-3.12 (not 3.13)

**Best for:** Advanced users who need code execution

### 3. 🎮 JARVIS Demo
**File:** `jarvis_demo.py`

- ✅ No API key required
- ✅ Pre-programmed responses
- ✅ Test the interface
- ❌ Limited capabilities

**Best for:** Testing before getting an API key

---

## 🚀 Quick Start (3 Steps)

### Step 1: Install Dependencies

**Option A - Automatic (Windows):**
```bash
setup_jarvis.bat
```

**Option B - Manual:**
```bash
pip install SpeechRecognition pyttsx3 rich openai
```

### Step 2: Get OpenAI API Key

1. Visit: https://platform.openai.com/api-keys
2. Create account or sign in
3. Click "Create new secret key"
4. Copy the key (starts with `sk-`)

### Step 3: Run JARVIS

**Easiest Way:**
```bash
run_jarvis.bat
```
(Double-click the file)

**Or via command line:**
```bash
python jarvis_lite.py
```

**Or try demo first:**
```bash
python jarvis_demo.py
```
(No API key needed)

---

## 📖 Documentation

- **`SETUP_COMPLETE.md`** - Setup summary and status
- **`QUICK_START.md`** - Detailed quick start guide
- **`JARVIS_README.md`** - Full documentation
- **`README.md`** - This file

---

## 🎮 Usage Examples

### Text Mode
```
$ python jarvis_lite.py

Select Mode:
1. 💬 Text Mode
2. 🎙️  Voice Mode

Enter choice: 1

[You] > Hello JARVIS
JARVIS: Good day, Sir! How may I assist you today?

[You] > What's 25 * 34?
JARVIS: 25 multiplied by 34 equals 850, Sir.

[You] > Tell me about quantum computing
JARVIS: Quantum computing is a revolutionary approach to computation...
```

### Voice Mode
```
$ python jarvis_lite.py

Select Mode: 2

🎙️ Voice Mode Active
Say 'Jarvis' or 'Hey Jarvis' to activate

🎤 Listening...
You said: Hey Jarvis, what time is it?

JARVIS: [speaks] It's currently 3:45 PM, Sir.

🎤 Listening...
You said: Jarvis, goodbye

JARVIS: [speaks] Shutting down. Goodbye, Sir.
```

---

## 🛠️ Utilities

### System Check
```bash
python check_system.py
```
Verifies all dependencies and configuration.

### Demo Mode
```bash
python jarvis_demo.py
```
Test the interface without an API key.

---

## ⚙️ Configuration

### Set API Key (Recommended)

**Windows:**
```bash
set OPENAI_API_KEY=sk-your-key-here
```

**Linux/Mac:**
```bash
export OPENAI_API_KEY=sk-your-key-here
```

### Change AI Model

Edit `jarvis_lite.py`, line ~95:
```python
model="gpt-4",  # Change to "gpt-3.5-turbo"
```

**Models:**
- `gpt-4` - Most capable, slower, more expensive
- `gpt-3.5-turbo` - Fast, cheaper, good quality

---

## 💡 Features

### What JARVIS Can Do:

- ✅ Answer questions on any topic
- ✅ Have natural conversations
- ✅ Explain complex concepts
- ✅ Help with brainstorming
- ✅ Provide recommendations
- ✅ Tell jokes and stories
- ✅ Translate languages
- ✅ Write content
- ✅ Math calculations
- ✅ General knowledge
- ✅ And much more!

### Voice Features:

- ✅ Wake word detection ("Hey Jarvis")
- ✅ Natural speech recognition
- ✅ Text-to-speech responses
- ✅ Conversational memory
- ✅ Multiple microphone support

---

## 🎯 Commands Reference

### Text Mode Commands:
- `voice` - Switch to voice mode
- `clear` - Clear conversation history
- `exit` or `quit` - Exit JARVIS

### Voice Mode:
- "Hey Jarvis" or "Jarvis" - Activate listening
- "exit", "quit", "goodbye" - Exit JARVIS

### Keyboard:
- `Ctrl+C` - Force quit
- `Enter` - Submit (text mode)

---

## 🐛 Troubleshooting

### "No API key found"
**Solution:** Enter your OpenAI API key when prompted

### "Module not found"
**Solution:** Run `setup_jarvis.bat` or install manually:
```bash
pip install SpeechRecognition pyttsx3 rich openai
```

### "Could not understand audio"
**Solution:**
- Speak clearly
- Reduce background noise
- Check microphone permissions
- Try adjusting microphone volume

### "API Error"
**Solution:**
- Verify API key is correct
- Check you have credits in OpenAI account
- Ensure internet connection

---

## 💰 Cost Information

### GPT-4:
- ~$0.03 per 1K input tokens
- ~$0.06 per 1K output tokens
- Typical conversation: $0.01-0.05 per exchange

### GPT-3.5-turbo:
- ~$0.0005 per 1K input tokens
- ~$0.0015 per 1K output tokens
- Typical conversation: $0.001-0.005 per exchange

**Tip:** Use GPT-3.5-turbo for most tasks to save money!

---

## 🔒 Privacy & Security

- Conversations are sent to OpenAI's servers
- OpenAI may store data for improvement
- Don't share sensitive personal information
- Keep your API key secret
- Never commit API keys to version control

---

## 🎨 Customization

### Change Personality

Edit `system_message` in `jarvis_lite.py` to modify JARVIS's personality and behavior.

### Adjust Voice

```python
# Speed
self.tts_engine.setProperty('rate', 175)  # Adjust number

# Volume
self.tts_engine.setProperty('volume', 0.9)  # 0.0 to 1.0

# Voice
voices = self.tts_engine.getProperty('voices')
self.tts_engine.setProperty('voice', voices[0].id)  # Change index
```

### Wake Words

Modify the wake word detection in `jarvis_lite.py`:
```python
if 'jarvis' in command_lower or 'hey jarvis' in command_lower:
    # Add more wake words here
```

---

## 📊 File Structure

```
open-interpreter/
├── jarvis_lite.py          # Main JARVIS (Python 3.13+)
├── jarvis_enhanced.py      # Advanced version (Python 3.9-3.12)
├── jarvis_demo.py          # Demo mode (no API key)
├── check_system.py         # System verification
├── run_jarvis.bat          # Windows launcher
├── setup_jarvis.bat        # Dependency installer
├── requirements_jarvis.txt # Dependency list
├── SETUP_COMPLETE.md       # Setup summary
├── QUICK_START.md          # Quick start guide
├── JARVIS_README.md        # Full documentation
└── README.md               # This file
```

---

## 🎓 Tips for Best Results

1. **Be Specific:** Clear questions get better answers
2. **Use Context:** JARVIS remembers the conversation
3. **Experiment:** Try different types of questions
4. **Be Patient:** Voice recognition needs quiet environment
5. **Save Money:** Use GPT-3.5-turbo for routine tasks
6. **Clear History:** Type `clear` to start fresh conversations

---

## 🚀 Advanced Usage

### Use Local Models (No API costs)

Instead of OpenAI, use local models with JARVIS Enhanced:

```python
interpreter.offline = True
interpreter.llm.model = "openai/x"
interpreter.llm.api_base = "http://localhost:1234/v1"  # LM Studio
interpreter.llm.api_key = "fake_key"
```

Requires:
- Python 3.9-3.12
- LM Studio or similar
- Local model downloaded

---

## 📚 Learning Resources

- [OpenAI API Docs](https://platform.openai.com/docs)
- [Open Interpreter](https://github.com/OpenInterpreter/open-interpreter)
- [Speech Recognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3 Docs](https://pyttsx3.readthedocs.io/)

---

## 🤝 Support

### Check System Status
```bash
python check_system.py
```

### Verify Installation
```bash
pip list | findstr "openai speech rich pyttsx3"
```

### Reinstall Dependencies
```bash
pip uninstall SpeechRecognition pyttsx3 rich openai -y
pip install SpeechRecognition pyttsx3 rich openai
```

---

## 🎉 Quick Test

### 1. Test Demo (No API key needed)
```bash
python jarvis_demo.py
```

### 2. Check System
```bash
python check_system.py
```

### 3. Run JARVIS
```bash
python jarvis_lite.py
```

---

## 📝 Version Comparison

| Feature | Demo | Lite | Enhanced |
|---------|------|------|----------|
| No API Key | ✅ | ❌ | ❌ |
| Voice Input | ❌ | ✅ | ✅ |
| Voice Output | ❌ | ✅ | ✅ |
| AI Responses | ❌ | ✅ | ✅ |
| Code Execution | ❌ | ❌ | ✅ |
| Python 3.13 | ✅ | ✅ | ❌ |
| Free to Use | ✅ | ❌* | ❌* |

*Requires OpenAI API credits

---

## 🎯 Recommended Workflow

1. **Start with Demo:** Test the interface
   ```bash
   python jarvis_demo.py
   ```

2. **Check System:** Verify everything is installed
   ```bash
   python check_system.py
   ```

3. **Get API Key:** Sign up at OpenAI

4. **Run JARVIS Lite:** Start with text mode
   ```bash
   python jarvis_lite.py
   ```

5. **Try Voice Mode:** Once comfortable with text

6. **Customize:** Adjust settings to your preference

---

## 🌟 Example Conversations

### Information Query
```
You: What is machine learning?
JARVIS: Machine learning is a subset of artificial intelligence...
```

### Math Help
```
You: What's the square root of 144?
JARVIS: The square root of 144 is 12, Sir.
```

### Creative Writing
```
You: Write a haiku about AI
JARVIS: Silicon minds think
      Processing endless data
      Future now unfolds
```

### Translation
```
You: Translate "Hello, how are you?" to Spanish
JARVIS: "Hola, ¿cómo estás?" is the Spanish translation, Sir.
```

---

## 🎊 You're Ready!

Everything is set up and ready to go. Choose your starting point:

**🎮 Just Testing?**
```bash
python jarvis_demo.py
```

**✅ Ready to Go?**
```bash
python jarvis_lite.py
```

**🔧 Want to Check First?**
```bash
python check_system.py
```

---

**"Sometimes you gotta run before you can walk."** - Tony Stark

**Enjoy your personal JARVIS AI Assistant!** 🦾✨

---

*Made with ❤️ for AI enthusiasts and Iron Man fans*
