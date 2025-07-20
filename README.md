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
```
JARVIX-2.0/
│
├── main.py                     # The central entry point. Starts the assistant and runs the main loop.
│
├── requirements.txt            # All project dependencies.
├── README.md                   # Project documentation.
├── config.py                   # Central configuration (e.g., save paths, default settings).
│
├── core/                       # The essential services: the "brain" and "senses".
│   ├── __init__.py
│   ├── listener.py             # Handles all voice input (Speech-to-Text).
│   ├── speaker.py              # Handles all voice output (Text-to-Speech).
│   ├── command_parser.py       # Decides which feature to run based on user's command.
│
└── features/                   # The "hands": All the actions the assistant can perform.
    │
    ├── __init__.py
    │
    ├── system_operations/      # MODULE 1: All tasks related to the OS.
    │   ├── __init__.py
    │   ├── power.py            # --> Shutdown, Restart, Sleep, Lock, Sign Out.
    │   ├── audio.py            # --> Volume controls (mute, set, increase).
    │   ├── display.py          # --> Brightness controls, Screenshot.
    │   ├── network.py          # --> Wi-Fi and Bluetooth controls.
    │   └── applications.py     # --> Open/Close apps, Task Manager, Show Desktop.
    │
    ├── file_operations/        # MODULE 2: (For Later) All file/folder tasks.
    │   ├── __init__.py
    │   └── file_manager.py     # --> Create, Delete, Copy, Move files.
    │
    ├── web_operations/         # MODULE 3: (For Later) All internet-related tasks.
    │   ├── __init__.py
    │   ├── browser.py          # --> Google Search, Open websites.
    │   └── youtube.py          # --> Search and play YouTube videos.
    │
    └── utility_operations/     # MODULE 4: Simple, miscellaneous tasks.
        ├── __init__.py
        ├── clipboard.py        # --> Read/Write to clipboard.
        └── info.py             # --> Tell time, date, battery, IP address.
```
