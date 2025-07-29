# 📦 Telegram Auto-Forwarder with Telethon on Fly.io

A lightweight, 24/7 bot to automatically forward messages from one Telegram channel to another using your personal account (Telethon). Runs on **Fly.io's free tier**.

---

## 🔧 Requirements

- Python 3.10+
- Fly.io account ([https://fly.io](https://fly.io))
- Telegram API credentials
- Basic Git and CLI knowledge

---

## 📌 Step 1: Get Telegram API Credentials

1. Go to [https://my.telegram.org](https://my.telegram.org)
2. Log in with your Telegram phone number
3. Click **API Development Tools**
4. Create a new app (name doesn't matter)
5. Save:
   - `api_id`
   - `api_hash`

---

## 📌 Step 2: Create and Clone Your Repo

```bash
git init telegram-forwarder
cd telegram-forwarder
```

---

## 📌 Step 3: Create Project Files

### `main.py`

```python
from telethon import TelegramClient, events
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
source_channel = os.getenv("SOURCE_CHANNEL")
target_channel = os.getenv("TARGET_CHANNEL")

client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    msg = event.message.message
    if msg and ('buy' in msg.lower() or 'sell' in msg.lower()):
        await client.send_message(target_channel, msg)

client.start()
client.run_until_disconnected()
```

### `requirements.txt`

```
telethon==1.34.0
```

### `Dockerfile`

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
```

### `fly.toml`

```toml
app = "telegram-forwarder-bot"

[env]
PYTHONUNBUFFERED = "1"

[[services]]
  internal_port = 8080
  protocol = "tcp"

  [[services.ports]]
    handlers = ["http"]
    port = 80
```

---

## 📌 Step 4: Install Fly.io CLI

```bash
# macOS
brew install flyctl

# Linux
curl -L https://fly.io/install.sh | sh

# Windows
iwr https://fly.io/install.ps1 -useb | iex
```

---

## 📌 Step 5: Deploy to Fly.io

```bash
# Login to Fly.io
fly auth login

# Create app (replace with your app name)
fly apps create telegram-forwarder-bot

# Set environment variables
fly secrets set API_ID="your_api_id"
fly secrets set API_HASH="your_api_hash"
fly secrets set SOURCE_CHANNEL="@source_channel_username"
fly secrets set TARGET_CHANNEL="@target_channel_username"

# Deploy
fly deploy
```

---

## 📌 Step 6: First Run Authentication

After deployment, you'll need to authenticate with Telegram:

```bash
# Connect to your app
fly ssh console

# Run the bot (this will prompt for phone number)
python main.py
```

Follow the prompts to enter your phone number and verification code.

---

## ✅ Done! Your bot now runs 24/7 on Fly.io's free tier.

---

## 🔧 Customization

### Change Message Filter

Edit the condition in `main.py`:

```python
# Current: forwards messages containing 'buy' or 'sell'
if msg and ('buy' in msg.lower() or 'sell' in msg.lower()):

# Example: forward all messages
if msg:

# Example: forward messages with specific keywords
if msg and any(word in msg.lower() for word in ['alert', 'signal', 'trade']):
```

### Add More Channels

Add multiple source channels:

```python
source_channels = [os.getenv("SOURCE_CHANNEL_1"), os.getenv("SOURCE_CHANNEL_2")]

@client.on(events.NewMessage(chats=source_channels))
```

---

## 🚨 Important Notes

- **Rate Limits**: Be mindful of Telegram's rate limits
- **Session File**: The session file is stored in Fly.io's ephemeral storage
- **Re-authentication**: You may need to re-authenticate after app restarts
- **Free Tier**: Fly.io free tier includes 3 shared-cpu-1x 256mb VMs

---

## 🐛 Troubleshooting

### Bot not forwarding messages?

1. Check if you're a member of both channels
2. Verify channel usernames in environment variables
3. Check Fly.io logs: `fly logs`

### Authentication issues?

1. Ensure your phone number is correct
2. Check if you have 2FA enabled
3. Try re-authenticating: `fly ssh console` then `python main.py`

### Deployment issues?

1. Check Fly.io status: `fly status`
2. View logs: `fly logs`
3. Restart app: `fly apps restart telegram-forwarder-bot`
