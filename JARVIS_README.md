# 🤖 JARVIS Enhanced - AI Assistant

An advanced AI assistant inspired by Tony Stark's JARVIS from Iron Man, powered by Open Interpreter.

## ✨ Features

- 🎤 **Voice Control**: Speak commands naturally with wake word detection
- 🗣️ **Text-to-Speech**: JARVIS responds with voice
- 💻 **Code Execution**: Run Python, JavaScript, Shell commands, and more
- 🧠 **AI-Powered**: Uses GPT-4 or GPT-3.5 for intelligent responses
- 🎨 **Beautiful Interface**: Rich terminal UI with colors and formatting
- 🔧 **System Control**: Can control your computer, create files, analyze data, and more

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- OpenAI API Key ([Get one here](https://platform.openai.com/api-keys))
- Microphone (for voice mode)

### Installation

#### Windows

1. Run the setup script:
```bash
setup_jarvis.bat
```

#### Manual Installation

```bash
pip install -r requirements_jarvis.txt
```

Or install individually:
```bash
pip install open-interpreter SpeechRecognition pyttsx3 pyautogui rich python-dotenv
```

### Configuration

Set your OpenAI API key as an environment variable:

**Windows:**
```bash
set OPENAI_API_KEY=your_api_key_here
```

**Linux/Mac:**
```bash
export OPENAI_API_KEY=your_api_key_here
```

Or create a `.env` file:
```
OPENAI_API_KEY=your_api_key_here
```

## 🎮 Usage

### Run JARVIS

```bash
python jarvis_enhanced.py
```

### Modes

**Text Mode (Default)**
- Type commands directly
- Type `voice` to switch to voice mode
- Type `exit` or `quit` to stop

**Voice Mode**
- Say "Jarvis" or "Hey Jarvis" to activate
- Speak your command
- Say "exit", "quit", or "goodbye" to stop

### Example Commands

**Text Mode:**
```
> What's the weather like today?
> Create a Python script to analyze this CSV file
> Open my browser and search for AI news
> What files are in my current directory?
```

**Voice Mode:**
```
"Hey Jarvis, what time is it?"
"Jarvis, create a new folder called Projects"
"Jarvis, show me my system information"
"Jarvis, goodbye"
```

## 🎯 Capabilities

JARVIS can:

- 📊 **Data Analysis**: Analyze CSV, Excel, JSON files
- 🖼️ **Image Processing**: Edit, resize, convert images
- 🌐 **Web Automation**: Control browsers, scrape data
- 📝 **File Management**: Create, edit, organize files
- 💻 **System Control**: Run commands, check system info
- 📈 **Visualization**: Create charts and graphs
- 🔍 **Research**: Search the web, summarize information
- And much more!

## ⚙️ Configuration

### Change AI Model

Edit `jarvis_enhanced.py` and modify:

```python
interpreter.llm.model = "gpt-4"  # or "gpt-3.5-turbo"
```

### Auto-Run Mode

**⚠️ Warning: This allows JARVIS to execute code without confirmation!**

Edit `jarvis_enhanced.py`:
```python
interpreter.auto_run = True  # Enable auto-execution
```

### Customize Voice

The script automatically selects the best available voice. To customize:

1. List available voices:
```python
import pyttsx3
engine = pyttsx3.init()
for voice in engine.getProperty('voices'):
    print(voice.name, voice.id)
```

2. Set your preferred voice in `jarvis_enhanced.py`

## 🛡️ Safety

- By default, JARVIS asks for confirmation before executing code
- Review commands carefully before approving
- Don't enable auto-run mode unless you trust the AI completely
- Keep your API key secure

## 🐛 Troubleshooting

### "No module named 'pyaudio'"

**Windows:**
```bash
pip install pipwin
pipwin install pyaudio
```

Or download from: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

**Linux:**
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
pip install pyaudio
```

**Mac:**
```bash
brew install portaudio
pip install pyaudio
```

### "Speech recognition not working"

- Check your microphone is connected and working
- Grant microphone permissions to your terminal/Python
- Try adjusting the `phrase_time_limit` in the code

### "API Key Error"

- Verify your OpenAI API key is correct
- Check you have credits in your OpenAI account
- Ensure the environment variable is set correctly

## 📚 Advanced Usage

### Use Local Models

Instead of OpenAI, you can use local models:

```python
interpreter.offline = True
interpreter.llm.model = "openai/x"
interpreter.llm.api_base = "http://localhost:1234/v1"  # LM Studio
interpreter.llm.api_key = "fake_key"
```

### Custom System Message

Modify the `system_message` in `jarvis_enhanced.py` to change JARVIS's personality.

## 🤝 Contributing

Feel free to enhance JARVIS! Some ideas:

- Add more wake words
- Implement conversation history
- Add GUI interface
- Integrate with smart home devices
- Add more voice options
- Improve error handling

## 📄 License

This project uses Open Interpreter, which is licensed under AGPL-3.0.

## 🙏 Credits

- [Open Interpreter](https://github.com/OpenInterpreter/open-interpreter)
- Inspired by Marvel's Iron Man JARVIS
- Built with ❤️ for AI enthusiasts

## ⚡ Tips

1. **Be Specific**: The more detailed your command, the better the result
2. **Use Context**: JARVIS remembers the conversation
3. **Experiment**: Try different commands to discover capabilities
4. **Stay Safe**: Review code before execution
5. **Have Fun**: JARVIS is here to help and impress!

---

**"Sometimes you gotta run before you can walk."** - Tony Stark
