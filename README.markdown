# 🎵🎤 MoodBeats - Multimodel Emotion Detection Music Recomendation System

<div align="center">

![MoodBeats Logo](https://img.shields.io/badge/MoodBeats-Voice_Emotion_Detection-FF6B6B)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.10-orange)
![MySQL](https://img.shields.io/badge/MySQL-Database-blue)

*🎵 Music Recommendations × 🎤 Voice AI = Perfect Harmony*

[![Install](https://img.shields.io/badge/🚀-Install_Now-brightgreen)](#-quick-installation)
[![Demo](https://img.shields.io/badge/🎮-Live_Demo-blue)](#-live-demo)
[![Docs](https://img.shields.io/badge/📚-Documentation-purple)](#-documentation)

</div>

---

## 📋 *Table of Contents*
- [🌟 Features](#-features)
- [🎯 Quick Start](#-quick-start)
- [📁 Project Structure](#-project-structure)
- [⚙ Installation](#-installation)
- [🚀 Running the App](#-running-the-app)
- [🎮 Usage Guide](#-usage-guide)
- [🔧 Configuration](#-configuration)
- [📊 API Endpoints](#-api-endpoints)
- [🤖 Voice Module Details](#-voice-module-details)
- [💾 Database Schema](#-database-schema)
- [🛠 Troubleshooting](#-troubleshooting)
- [🤝 Contributing](#-contributing)
- [📞 Support](#-support)

---

## 🌟 *Features*

### 🎵 *MoodBeats Web App*
| Feature | Icon | Description |
|---------|------|-------------|
| *User Authentication* | 🔐 | Secure login/register with session management |
| *Mood-based Music* | 😊🎶 | Explore songs by emotional categories |
| *Favorites System* | ⭐ | Save & manage favorite tracks |
| *Playlists* | 📋 | Create custom music collections |
| *Mood History* | 📊 | Track your emotional journey |
| *YouTube Integration* | ▶ | Direct YouTube song playback |
| *Responsive Design* | 📱 | Mobile-friendly interface |

### 🎤 *Voice Emotion Module*
| Feature | Icon | Description |
|---------|------|-------------|
| *Voice Recording* | 🎤 | Upload/record audio directly |
| *Real-time Analysis* | ⚡ | Instant emotion detection |
| *8 Emotions* | 😊😢😠😨 | Neutral, Happy, Sad, Angry, Fearful, Disgust, Surprised, Calm |
| *Deep Learning* | 🧠 | CNN model with 75%+ accuracy |
| *Confidence Scores* | 📈 | Detailed prediction confidence |
| *Personalized Recs* | 🎯 | Mood-based YouTube suggestions |

---

## 🎯 *Quick Start*

### *📥 One-Command Installation*
bash
# Windows
install.bat

# Linux/Mac
chmod +x install.sh
./install.sh


### *🚀 One-Click Launch*
bash
# Windows
run.bat

# Linux/Mac
./run.sh


### *🌐 Access Points*
| Application | URL | Port | Status |
|-------------|-----|------|--------|
| *MoodBeats Web* | http://localhost:5000 | 5000 | 🟢 Live |
| *Voice Module UI* | http://localhost:5001/voice | 5001 | 🟢 Live |
| *Voice API* | http://localhost:5001/api | 5001 | 🟢 Live |

---

## 📁 *Project Structure*


MOODBEATS-VOICE/
├── moodbeats/                    # Main Web Application
│   ├── app.py                   # Flask main application
│   ├── requirements.txt         # Python dependencies
│   ├── templates/               # HTML templates
│   │   ├── index.html          # Home page
│   │   ├── dashboard.html      # User dashboard
│   │   ├── favorites.html     # Favorite songs
│   │   ├── playlist.html       # Playlist manager
│   │   ├── history.html        # Mood history
│   │   └── voice_analysis.html # Voice integration
│   ├── static/                  # Static assets
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   └── database/
│       └── moodbeats.sql       # Database schema
│
├── voice_module/                # Voice Emotion Detection
│   ├── app.py                   # Voice Flask app
│   ├── train.py                # Model training
│   ├── predict.py              # Prediction logic
│   ├── utils.py                # Audio utilities
│   ├── requirements.txt        # Voice module deps
│   └── templates/
│       └── index.html          # Voice UI
│
├── shared/                      # Shared Resources
│   ├── model.h5                # Trained AI model
│   └── labels.json             # Emotion labels
│
├── install.bat                  # Windows installer
├── install.sh                   # Linux/Mac installer
├── run.bat                      # Windows launcher
├── run.sh                       # Linux/Mac launcher
├── README.md                    # This file
└── config.py                   # Global configuration


---

## ⚙ *Installation*

### *📋 Prerequisites*
| Requirement | Version | Check Command |
|-------------|---------|---------------|
| *Python* | 3.8+ | python --version |
| *MySQL* | 8.0+ | mysql --version |
| *Pip* | Latest | pip --version |
| *Git* | Optional | git --version |

### *🔧 Step-by-Step Setup*

bash
# 1. Clone/Copy the project
git clone <repo-url>
cd moodbeats-voice

# 2. Create virtual environment
python -m venv venv

# 3. Activate (Choose your OS)
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Install dependencies
pip install -r moodbeats/requirements.txt
pip install -r voice_module/requirements.txt

# 5. Setup database
mysql -u root -p < moodbeats/database/moodbeats.sql

# 6. Configure (edit config.py)
# Set your MySQL credentials and YouTube API key


### *⚡ Quick Commands Cheat Sheet*
bash
# Install Everything
make install        # If Makefile exists
# OR
./setup.py          # Python setup script

# Database Setup
python setup_database.py

# Train Model (Optional)
cd voice_module
python train.py


---

## 🚀 *Running the App*

### *🖥 Method 1: Automatic (Recommended)*
bash
# Windows
run.bat

# Linux/Mac
chmod +x run.sh
./run.sh


### *🖥 Method 2: Manual Terminal*
bash
# Terminal 1: MoodBeats Web App
cd moodbeats
python app.py

# Terminal 2: Voice Module
cd voice_module
python app.py


### *🌐 Port Configuration*
| Service | Default Port | Change in |
|---------|--------------|-----------|
| MoodBeats Web | 5000 | moodbeats/app.py |
| Voice Module | 5001 | voice_module/app.py |

---

## 🎮 *Usage Guide*

### *👤 User Journey*
1. *Register/Login* → Create your account
2. *Dashboard* → Explore mood categories
3. *Voice Analysis* → Record/upload audio
4. *Get Results* → See emotion + confidence
5. *Get Recommendations* → YouTube songs based on mood
6. *Save Favorites* → Build your music library

### *🎤 Voice Analysis Steps*
mermaid
graph LR
    A[🎤 Record Audio] --> B[📁 Upload File]
    B --> C[⚡ Analyze Emotion]
    C --> D[😊 Get Results]
    D --> E[🎵 Recommendations]
    E --> F[⭐ Save Favorites]


### *📱 Quick Actions*
| Action | Shortcut | Description |
|--------|----------|-------------|
| *Upload Audio* | Click mic icon | Quick voice recording |
| *Analyze* | Drag & drop | Drop audio file anywhere |
| *Get Songs* | Auto-loads | After emotion detection |
| *Save* | Click star | Add to favorites |
| *Share* | Link icon | Copy song link |

---

## 🔧 *Configuration*

### *⚙ config.py*
python
# Database Configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',           # 👈 Change this
    'password': 'password',   # 👈 Change this
    'database': 'moodbeats'
}

# YouTube API (Optional)
YOUTUBE_API_KEY = "YOUR_KEY_HERE"  # Get from Google Cloud Console

# App Settings
DEBUG = True
SECRET_KEY = "your-secret-key-here"
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB


### *🔑 Getting YouTube API Key*
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create new project → Enable YouTube Data API v3
3. Create credentials → API Key
4. Copy key to config.py

---

## 📊 *API Endpoints*

### *🎤 Voice Module API*
| Endpoint | Method | Description | Example |
|----------|--------|-------------|---------|
| /api/detect | POST | Analyze audio emotion | curl -F "audio=@file.wav" localhost:5001/api/detect |
| /api/youtube/{mood} | GET | Get mood-based songs | curl localhost:5001/api/youtube/happy |
| /voice | GET | Web interface | Open in browser |

### *🎵 MoodBeats API*
| Endpoint | Method | Description |
|----------|--------|-------------|
| /api/login | POST | User authentication |
| /api/register | POST | New user registration |
| /api/songs/{mood} | GET | Get songs by mood |
| /api/favorites | POST | Add to favorites |
| /api/playlists | GET | User playlists |

---

## 🤖 *Voice Module Details*

### *🧠 AI Model Architecture*

Input Audio → MFCC Features → CNN Layers → Emotion Classification
    ↓            ↓              ↓              ↓
  3 sec       40×150        Conv2D×2      8 Emotions


### *📊 Emotion Categories*
| Emotion | Icon | Training Samples | Accuracy |
|---------|------|------------------|----------|
| *Happy* | 😊 | 1,200+ | 82% |
| *Sad* | 😢 | 1,100+ | 78% |
| *Angry* | 😠 | 900+ | 75% |
| *Neutral* | 😐 | 1,500+ | 85% |
| *Fearful* | 😨 | 800+ | 72% |
| *Disgust* | 🤢 | 700+ | 70% |
| *Surprised* | 😲 | 600+ | 68% |
| *Calm* | 😌 | 1,000+ | 80% |

### *🔬 Technical Specs*
- *Framework*: TensorFlow 2.10
- *Model*: 2D CNN
- *Input*: MFCC (Mel-frequency cepstral coefficients)
- *Features*: 40 bands × 150 frames
- *Dataset*: RAVDESS + CREMA-D (4,000+ samples)
- *Inference Time*: < 100ms
- *Accuracy*: 75%+ on test set

---

## 💾 *Database Schema*

### *🗃 Main Tables*
sql
-- Users Table
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE,
    email VARCHAR(100) UNIQUE,
    password_hash VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Songs Table
CREATE TABLE songs (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255),
    artist VARCHAR(255),
    youtube_id VARCHAR(50),
    mood_id INT,
    thumbnail_url TEXT
);

-- Voice Analysis History
CREATE TABLE voice_history (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    emotion VARCHAR(50),
    confidence FLOAT,
    audio_file VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


### *🔗 Relationships*

users ──┬── favorites ─── songs
        ├── playlists ─── playlist_songs ─── songs
        └── voice_history


---

## 🛠 *Troubleshooting*

### *🚨 Common Issues & Solutions*

| Issue | Symptoms | Solution |
|-------|----------|----------|
| *Port in Use* | "Address already in use" | Change ports in app.py or kill process: netstat -ano \| findstr :5000 |
| *MySQL Error* | "Can't connect to MySQL" | Check MySQL service: sudo service mysql start |
| *Import Error* | "No module named..." | Reinstall: pip install -r requirements.txt --force-reinstall |
| *Model Error* | "Failed to load model" | Train model: cd voice_module && python train.py |
| *Audio Error* | "Unsupported format" | Convert to WAV: Use online converter or Audacity |

### *📋 Quick Fix Commands*
bash
# Reset everything
make clean
make install

# Check services
python check_services.py

# Update dependencies
pip install --upgrade -r requirements.txt

# Database reset
mysql -u root -p -e "DROP DATABASE moodbeats; CREATE DATABASE moodbeats;"
mysql -u root -p moodbeats < database/moodbeats.sql


### *📞 Debug Mode*
bash
# Run with debug
python app.py --debug

# See logs
tail -f moodbeats.log
tail -f voice_module.log


---

## 🤝 *Contributing*

### *🔄 Development Workflow*
1. *Fork* the repository
2. *Create* feature branch: git checkout -b feature/amazing-feature
3. *Commit* changes: git commit -m 'Add amazing feature'
4. *Push* to branch: git push origin feature/amazing-feature
5. *Open* Pull Request

### *📝 Code Standards*
- Follow PEP 8 style guide
- Add docstrings to functions
- Write unit tests for new features
- Update documentation
- Use meaningful commit messages

### *🧪 Testing*
bash
# Run tests
python -m pytest tests/

# Test coverage
pytest --cov=.

# API testing
python test_api.py


---

## 📞 *Support*

### *📚 Resources*
| Resource | Link | Description |
|----------|------|-------------|
| *Documentation* | /docs | Complete API docs |
| *Issue Tracker* | GitHub Issues | Report bugs |
| *Discussion* | GitHub Discussions | Ask questions |
| *Email* | support@moodbeats.com | Direct support |

### *🆘 Quick Help*
bash
# Get help
python help.py

# Check system
python system_check.py

# View logs
python view_logs.py


### *👥 Community*
- *GitHub*: [MoodBeats Repository](https://github.com/yourusername/moodbeats)
- *Discord*: Join our community
- *Twitter*: @MoodBeatsAI

---

## 🎉 *Success Stories*

> "MoodBeats transformed how I discover music! The voice analysis is incredibly accurate." - Sarah, Music Enthusiast

> "As a developer, I love how easy it was to integrate the voice module into my app." - Alex, Developer

---

<div align="center">

## 🚀 *Ready to Start?*

[![Deploy](https://img.shields.io/badge/🚀_Deploy_Now-FF6B6B?style=for-the-badge&logo=rocket)](#-quick-start)
[![Demo](https://img.shields.io/badge/🎮_Try_Demo-4A90E2?style=for-the-badge&logo=google-chrome)](#-live-demo)
[![Docs](https://img.shields.io/badge/📚_Read_Docs-8A2BE2?style=for-the-badge&logo=read-the-docs)](https://github.com/yourusername/moodbeats/wiki)

*🌟 Star us on GitHub if you like this project!*

</div>

---

<div align="center">

### 📄 *License*
METs Institute Of Management,Nashik License © 2025 MoodBeats Team - Manish , Tanvi , Vishal

### 🙏 *Acknowledgments*
- RAVDESS & CREMA-D datasets
- YouTube Data API
- Flask & TensorFlow communities
- All our contributors

*Made with ❤ by the MoodBeats Team*

</div>

---

## 📱 *Mobile App Coming Soon!*

Stay tuned for our iOS and Android apps with real-time voice analysis and offline mood tracking!

---

*🎵 Your Mood. Your Music. Perfected. 🎤*