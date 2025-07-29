# 🚀 Quick Start Guide

Get your Telegram Auto-Forwarder running in 5 minutes!

## 1️⃣ Get Telegram API Credentials

- Go to [https://my.telegram.org](https://my.telegram.org)
- Log in and create an app
- Save your `api_id` and `api_hash`

## 2️⃣ Test Your Setup

```bash
# Set environment variables
export API_ID="your_api_id"
export API_HASH="your_api_hash"
export SOURCE_CHANNEL="@source_channel"
export TARGET_CHANNEL="@target_channel"

# Test the setup
python test_setup.py
```

## 3️⃣ Deploy to Fly.io

```bash
# Install Fly.io CLI
brew install flyctl  # macOS
# or: curl -L https://fly.io/install.sh | sh  # Linux

# Login and deploy
fly auth login
./deploy.sh
```

## 4️⃣ Authenticate

```bash
fly ssh console
python main.py
# Enter your phone number and verification code
```

## 5️⃣ Monitor

```bash
fly logs  # View logs
fly status  # Check status
```

## ✅ Done! Your bot runs 24/7 on Fly.io's free tier.

---

## 🔧 Customization

Edit `config.py` to change:

- **Keywords**: Modify `KEYWORDS` list
- **Filter**: Use `custom_filter()` function
- **Forward all**: Set `FORWARD_ALL_MESSAGES = True`

## 🐛 Need Help?

- **Test locally**: `python test_setup.py`
- **Check logs**: `fly logs`
- **Restart**: `fly apps restart your-app-name`
- **Full docs**: See `README.md`
