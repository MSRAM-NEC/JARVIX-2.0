# 🎙️ Voice Assistant for Windows 
# JARVIX 2.0

An always-on, voice-controlled AI assistant that can:
- Handle file tasks
- Automate system actions
- Send emails and WhatsApp messages
- Play YouTube videos
- Search the internet
- Run silently in the background
- Understand your commands via voice or natural text

---

## 👥 Team Members

- MSRAM(Lead)
- GOWSIKAN(Member)



---

## 🧠 Features

| Feature                     | Description                                |
|----------------------------|--------------------------------------------|
| 🎤 Voice Wake-Up            | Listens for wake word (like "Hey Nova")    |
| 📂 File Operations          | Create, delete, move, rename files/folders |
| 🖥️ System Commands          | Lock screen, screenshot, mute, battery     |
| 📨 Email Automation         | Send emails with attachments via voice     |
| 💬 WhatsApp Automation      | Open WhatsApp Web and send messages        |
| 📺 YouTube + Search         | Play videos, search Google                 |
| 🧠 GPT Integration          | Understand smart natural language          |
| 🔕 Silent Background Mode   | Runs in tray, never disturbs UI            |

## 📁 Project Structure

<pre lang="markdown"> ``` JARVIX_2.0/ │ ├── main.py # Main assistant script ├── requirements.txt # Python dependencies ├── README.md # Project documentation │ ├── modules/ # Optional: Additional feature modules │ ├── file_ops.py # File operations (create, delete, rename) │ ├── system_control.py # System commands (shutdown, lock, etc.) │ └── voice_commands.py # Speech recognition logic │ ├── utils/ # Utility functions/helpers (optional) │ └── logger.py # Custom logger (if needed) │ ├── assets/ # Images, icons, etc. (if used in UI/voice) │ └── tests/ # Unit tests for modules (optional) └── test_file_ops.py ``` </pre>