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
├── main.py                          # Entry point
├── config.yaml                      # User settings (wake word, paths, profiles)
├── requirements.txt                 # Python dependencies
├── README.md                        # Project overview
├── ollama_setup.md                  # Local LLM (Ollama) installation guide
│
├── core/                            # Core AI & orchestration
│   ├── __init__.py
│   ├── brain.py                     # Ollama interface & prompt management
│   ├── llm_manager.py               # Model loader/switcher
│   ├── listener.py                  # Wake-word & speech‑to‑text
│   ├── speaker.py                   # Text‑to‑speech engine
│   ├── intent_parser.py             # Map LLM output → actions
│   ├── memory.py                    # Session/history manager
│   └── utils.py                     # Core helpers (logging, config)
│
├── modules/                         # Functional capability packs
│   ├── file_operations/             # File system tasks
│   │   ├── __init__.py
│   │   ├── operations.py            # CRUD: create, delete, rename, move
│   │   ├── search.py                # Filename & content search
│   │   └── organizer.py             # Smart folder structuring
│   │
│   ├── system_control/              # OS & app controls
│   │   ├── __init__.py
│   │   ├── power.py                 # Shutdown, restart, lock screen
│   │   ├── applications.py          # Launch/close programs
│   │   ├── hardware.py              # Volume/brightness adjustments
│   │   └── security.py              # Authentication gates
│   │
│   ├── web_operations/              # Internet‑enabled tasks
│   │   ├── __init__.py
│   │   ├── browser.py               # Open URLs, bookmarks
│   │   └── youtube.py               # Search/play videos
│   │
│   ├── communication/               # Email & messaging
│   │   ├── __init__.py
│   │   ├── email_sender.py          # SMTP/gmail automation
│   │   └── whatsapp.py              # WhatsApp Web via Selenium
│   │
│   └── knowledge_engine/            # Local knowledge & summaries
│       ├── __init__.py
│       ├── queries.py               # Ask LLM questions
│       ├── summarization.py         # Text condensation
│       └── documents.py             # PDF/txt parsing
│
├── experiments/                     # Prototype & cutting‑edge
│   ├── vision/                      # Screen OCR & gesture
│   │   ├── screen_parser.py
│   │   └── gesture_control.py
│   │
│   └── llm_plugins/                 # Custom skill builders
│       ├── live_coder.py            # Voice-driven code editing
│       └── skill_compiler.py        # NL→new module scaffolds
│
├── utils/                           # Shared utilities
│   ├── __init__.py
│   ├── auth.py                      # Voice‑print user auth
│   ├── logger.py                    # Structured logs
│   └── error_handler.py             # Graceful recovery
│
├── assets/                          # Static resources
│   ├── icons/                       # Tray & notification icons
│   ├── sounds/                      # Audio feedback clips
│   └── models/                      # Cached LLM weights (optional)
│
├── tests/                           # Automated tests
│   ├── unit/
│   │   ├── test_listener.py
│   │   ├── test_brain.py
│   │   └── test_file_ops.py
│   └── integration/
│       ├── test_full_flow.py
│       └── test_system_control.py
│
└── docs/                            # Developer & user docs
    ├── ARCHITECTURE.md              # System design overview
    ├── API_REFERENCE.md             # Module interfaces
    └── CONTRIBUTING.md              # How to contribute  

```
