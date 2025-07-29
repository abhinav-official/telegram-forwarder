# 🚀 Telegram Auto-Forwarder Setup Guide

Your API credentials have been configured successfully! Here's how to complete the setup:

## ✅ Already Configured

- **API_ID**: 24390163
- **API_HASH**: 5ac2a3551509d703074db3c6862c5bb0
- **Dependencies**: Installed in virtual environment

## 🔧 Next Steps

### 1. Set Your Channels

You need to specify which channels to forward messages between:

```bash
# Set your source channel (where messages come from)
export SOURCE_CHANNEL="@your_source_channel"

# Set your target channel (where messages go to)
export TARGET_CHANNEL="@your_target_channel"
```

**Examples:**

```bash
export SOURCE_CHANNEL="@crypto_signals"
export TARGET_CHANNEL="@my_trading_group"
```

### 2. Test Your Setup

```bash
# Activate virtual environment and test
source venv/bin/activate
python test_setup.py
```

This will:

- ✅ Test your API credentials
- ✅ Verify channel access
- ✅ Send a test message
- ✅ Test message filtering

### 3. Deploy to Fly.io (Optional)

If you want to run this 24/7 on Fly.io's free tier:

```bash
# Install Fly.io CLI
brew install flyctl

# Login and deploy
fly auth login
./deploy.sh
```

### 4. Authenticate

```bash
# For local testing
source venv/bin/activate
python main.py

# For Fly.io deployment
fly ssh console
python main.py
```

You'll be prompted to:

1. Enter your phone number
2. Enter the verification code sent to Telegram

## 🔍 Channel Requirements

**Source Channel:**

- You must be a member of the source channel
- The channel must be public or you must have access

**Target Channel:**

- You must be a member of the target channel
- You must have permission to send messages

## 🎛️ Customization

Edit `config.py` to customize:

- **Keywords**: Change `KEYWORDS = ['buy', 'sell']` to your preferred terms
- **Forward all**: Set `FORWARD_ALL_MESSAGES = True` to forward everything
- **Custom filter**: Modify the `custom_filter()` function for advanced filtering

## 🐛 Troubleshooting

**Common Issues:**

- **"Cannot access channel"**: Make sure you're a member of both channels
- **"Cannot send message"**: Check your permissions in the target channel
- **"API credentials invalid"**: Double-check your API_ID and API_HASH

**Get Help:**

- Check logs: `fly logs` (if deployed)
- Test locally: `python test_setup.py`
- Restart: `fly apps restart your-app-name`

## 🎉 You're Ready!

Once you've set your channels and tested the setup, your Telegram Auto-Forwarder will be ready to run!
