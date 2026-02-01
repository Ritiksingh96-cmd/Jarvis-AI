# 🚀 JARVIS Quick Start Guide

## 🎯 What You Have

You now have **TWO versions** of JARVIS:

### 1. **JARVIS Lite** (Recommended for Python 3.13+)
- ✅ Works with Python 3.13
- ✅ Voice recognition and text-to-speech
- ✅ Conversational AI powered by GPT-4
- ✅ Easy to use and setup
- ❌ Cannot execute code on your computer

**File:** `jarvis_lite.py`

### 2. **JARVIS Enhanced** (Requires Python 3.9-3.12)
- ✅ Full Open Interpreter integration
- ✅ Can execute code on your computer
- ✅ Voice recognition and text-to-speech
- ✅ More powerful capabilities
- ❌ Requires Python 3.9-3.12 (not 3.13)

**File:** `jarvis_enhanced.py`

---

## 🏃 Quick Start - JARVIS Lite

### Step 1: Install Dependencies

```bash
pip install SpeechRecognition pyttsx3 rich openai
```

### Step 2: Get OpenAI API Key

1. Go to https://platform.openai.com/api-keys
2. Create a new API key
3. Copy it (you'll need it in the next step)

### Step 3: Run JARVIS

```bash
python jarvis_lite.py
```

### Step 4: Enter Your API Key

When prompted, paste your OpenAI API key.

### Step 5: Choose Mode

- Type `1` for Text Mode (type your commands)
- Type `2` for Voice Mode (speak your commands)

---

## 💬 Using Text Mode

1. Type your questions or commands
2. Press Enter
3. JARVIS will respond

**Example Commands:**
```
> Hello JARVIS
> What's the weather like today?
> Tell me a joke
> Explain quantum computing in simple terms
> What can you help me with?
```

**Special Commands:**
- `voice` - Switch to voice mode
- `clear` - Clear conversation history
- `exit` or `quit` - Exit JARVIS

---

## 🎙️ Using Voice Mode

1. Say "Jarvis" or "Hey Jarvis" to activate
2. Speak your command
3. JARVIS will respond with voice

**Example Voice Commands:**
```
"Hey Jarvis, what time is it?"
"Jarvis, tell me about artificial intelligence"
"Jarvis, what's the capital of France?"
"Jarvis, goodbye"
```

**To Exit:**
- Say "exit", "quit", or "goodbye"
- Press Ctrl+C

---

## ⚙️ Configuration

### Set API Key as Environment Variable (Optional)

**Windows:**
```bash
set OPENAI_API_KEY=your_api_key_here
```

**Linux/Mac:**
```bash
export OPENAI_API_KEY=your_api_key_here
```

### Change AI Model

Edit `jarvis_lite.py` and find this line:
```python
model="gpt-4",  # or "gpt-3.5-turbo" for faster/cheaper
```

Change to:
```python
model="gpt-3.5-turbo",  # Faster and cheaper
```

---

## 🛠️ Troubleshooting

### "No module named 'speech_recognition'"

```bash
pip install SpeechRecognition
```

### "No module named 'pyttsx3'"

```bash
pip install pyttsx3
```

### "No module named 'openai'"

```bash
pip install openai
```

### Microphone Not Working

1. Check microphone is connected
2. Grant microphone permissions to Python/Terminal
3. Test microphone in other apps first

### "Invalid API Key"

1. Check your API key is correct
2. Make sure you have credits in your OpenAI account
3. Visit https://platform.openai.com/account/billing

---

## 🎨 Customization Ideas

### Change JARVIS Voice

Edit `jarvis_lite.py` and modify the voice selection:

```python
# List available voices
voices = self.tts_engine.getProperty('voices')
for voice in voices:
    print(voice.name, voice.id)

# Set your preferred voice
self.tts_engine.setProperty('voice', voices[0].id)  # Change index
```

### Change Speaking Speed

```python
self.tts_engine.setProperty('rate', 175)  # Increase or decrease
```

### Modify Personality

Edit the `system_message` in `jarvis_lite.py` to change how JARVIS behaves.

---

## 📊 What JARVIS Can Do

### Current Capabilities (JARVIS Lite):
- ✅ Answer questions
- ✅ Have conversations
- ✅ Provide information
- ✅ Explain concepts
- ✅ Tell jokes and stories
- ✅ Help with ideas and brainstorming
- ✅ Translate languages
- ✅ Write content
- ✅ And much more!

### What It CANNOT Do (Lite Version):
- ❌ Execute code on your computer
- ❌ Create/edit files
- ❌ Control applications
- ❌ Access your files directly

**For these features, you need JARVIS Enhanced with Python 3.9-3.12**

---

## 🔒 Privacy & Safety

- Your conversations are sent to OpenAI's servers
- OpenAI may store conversations for improvement
- Don't share sensitive personal information
- Your API key should be kept secret

---

## 💡 Tips for Best Results

1. **Be Specific**: Clear questions get better answers
2. **Use Context**: JARVIS remembers the conversation
3. **Experiment**: Try different types of questions
4. **Be Patient**: Voice recognition needs a quiet environment
5. **Have Fun**: JARVIS is here to help and entertain!

---

## 🆘 Need Help?

### Check Python Version
```bash
python --version
```

### Check Installed Packages
```bash
pip list | findstr "openai speech rich pyttsx3"
```

### Reinstall Everything
```bash
pip uninstall SpeechRecognition pyttsx3 rich openai -y
pip install SpeechRecognition pyttsx3 rich openai
```

---

## 🎯 Next Steps

1. ✅ Run JARVIS Lite and test it
2. ✅ Try both text and voice modes
3. ✅ Experiment with different commands
4. ✅ Customize the personality
5. ✅ Consider upgrading to JARVIS Enhanced (requires Python 3.9-3.12)

---

## 📝 Example Session

```
$ python jarvis_lite.py

JARVIS Lite - AI Assistant

Select Mode:
1. 💬 Text Mode (type commands)
2. 🎙️  Voice Mode (speak commands)

Enter choice (1 or 2): 1

[You] > Hello JARVIS

JARVIS: Good day, Sir! I'm JARVIS, your AI assistant. How may I be of service today?

[You] > What can you help me with?

JARVIS: I can assist you with a wide variety of tasks, Sir:
- Answer questions on virtually any topic
- Help with research and information gathering
- Explain complex concepts in simple terms
- Assist with writing and content creation
- Provide recommendations and suggestions
- Engage in meaningful conversations
- And much more!

What would you like to explore today?

[You] > Tell me a joke about AI

JARVIS: Certainly, Sir. Here's one for you:

Why did the AI go to therapy?
Because it had too many unresolved issues!

I hope that brought a smile to your face, Sir.

[You] > exit

JARVIS shutting down. Goodbye, Sir!
```

---

**"Sometimes you gotta run before you can walk."** - Tony Stark

Enjoy your JARVIS AI Assistant! 🚀
