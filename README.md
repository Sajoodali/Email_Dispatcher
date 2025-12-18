# 📧 Email Dispatcher Pro

Professional email marketing platform built with Streamlit.

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Credentials

Edit `.env` file with your details:

```env
SENDER_NAME=Marketing Team
SENDER_EMAIL=your-email@gmail.com
SENDER_APP_PASSWORD=your-app-password-here

COMPANY_NAME=Globium Clouds
COMPANY_ADDRESS=123 Business Street, City, Country
COMPANY_WEBSITE=www.globiumclouds.com
```

### 3. Run the App

```bash
streamlit run email_dispatcher.py
```

---

## 🔐 Gmail App Password Setup

1. Go to: https://myaccount.google.com/security
2. Enable **2-Step Verification**
3. Go to: https://myaccount.google.com/apppasswords
4. Generate App Password for "Mail"
5. Copy 16-character password (remove spaces)
6. Add to `.env` file

---

## ✨ Features

- ✅ Secure credential storage (.env file)
- ✅ Professional HTML email templates
- ✅ Company branding
- ✅ Real-time email validation
- ✅ Preview before sending
- ✅ Dual SMTP methods (SSL + STARTTLS)
- ✅ Modern dashboard UI

---

## 📁 Files

```
Email_Dispatcher/
├── .env                    # Your credentials (NEVER commit!)
├── .env.example            # Template file
├── .gitignore              # Git ignore rules
├── email_dispatcher.py     # Main application
├── email_template.py       # Email HTML template
├── requirements.txt        # Python dependencies
├── README.md               # This file
└── SECURITY_SETUP.md       # Detailed security guide
```

---

## 🎯 Usage

1. **Configure `.env`** - One time setup
2. **Run app** - `streamlit run email_dispatcher.py`
3. **Compose email** - Fill receiver, subject, message
4. **Send** - Click send button
5. **Done!** ✅

---

## 🛡️ Security

- `.env` file is **automatically ignored by Git**
- Never commit credentials to version control
- Use Gmail App Passwords (not regular password)
- Keep `.env` file secure

---

## 📧 Email Format

Recipients see:

```
From: Globium Clouds <yourmail@gmail.com>
Subject: Your Subject

┌─────────────────────────┐
│   GLOBIUM CLOUDS        │
│   Official Communication│
├─────────────────────────┤
│   Your message here     │
├─────────────────────────┤
│ 📍 123 Business St...   │
│ 🌐 www.globiumclouds.com│
│ © 2025 Globium Clouds   │
└─────────────────────────┘
```

---

## 🔧 Troubleshooting

**Problem:** "⚠️ Configure .env file"

- **Solution:** Edit `.env` file with your credentials

**Problem:** "Authentication Failed"

- **Solution:** Generate new App Password, update `.env`

**Problem:** Values not loading

- **Solution:** Check `.env` format, restart app

---

## 📝 Requirements

- Python 3.7+
- streamlit
- python-dotenv
- Gmail account with App Password

---

**Made with ❤️ for Professional Email Marketing**
