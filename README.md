# 🤖 Telegram Auto-Forwarder

Automatically forward messages from Telegram channels to your DM based on keywords.

## ✨ Features

- 🔍 **Smart Filtering**: Forward messages containing specific keywords
- 📱 **DM Forwarding**: Send filtered messages directly to your Telegram DM
- 🚀 **Easy Setup**: Simple configuration with channel IDs
- 🔄 **24/7 Operation**: Can run continuously on Fly.io's free tier
- 🎛️ **Customizable**: Easy to modify keywords and filtering logic

## 🚀 Quick Start

### 1. Get Your Channel IDs

```bash
# Run the channel fetcher script
python get_channels.py
```

This will show you all your channels and your user ID. Note down:

- Your **User ID** (for target DM)
- The **Channel ID** you want to monitor (for source)

### 2. Configure the Bot

Edit `config.py` and set your channel IDs:

```python
SOURCE_CHANNEL_ID = -1001234567890  # Your source channel ID
TARGET_USER_ID = 123456789          # Your user ID (for DM)
```

### 3. Test Your Setup

```bash
python test_setup.py
```

### 4. Run the Bot

```bash
python main.py
```

## 🔧 Configuration

Edit `config.py` to customize:

- **Keywords**: `KEYWORDS = ['buy', 'sell', 'signal', 'alert', 'trade']`
- **Forward all**: `FORWARD_ALL_MESSAGES = True`
- **Custom filter**: Modify the `custom_filter()` function

## 🚀 Deploy to Fly.io (Optional)

For 24/7 operation:

```bash
# Install Fly.io CLI
brew install flyctl

# Deploy
./deploy.sh
```

## 📁 Project Structure

```
telegram-forwarder/
├── main.py              # Main bot logic
├── config.py            # Configuration settings
├── get_channels.py      # Channel ID fetcher
├── test_setup.py        # Setup testing
├── requirements.txt      # Python dependencies
├── deploy.sh            # Fly.io deployment
├── Dockerfile           # Container configuration
├── fly.toml            # Fly.io configuration
└── README.md           # This file
```

## 🔐 Security

- API credentials are hardcoded in `config.py`
- Session files are excluded from git
- Channel IDs are used instead of usernames for better privacy

## 🐛 Troubleshooting

- **"Cannot access channel"**: Make sure you're a member of the source channel
- **"Cannot send message"**: Check your user ID is correct
- **"API credentials invalid"**: Verify your API_ID and API_HASH

## 📝 License

MIT License - feel free to use and modify!
