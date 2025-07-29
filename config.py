"""
Configuration file for Telegram Auto-Forwarder
Modify these settings to customize the bot's behavior
"""

# Telegram API credentials


# Madhava's Account
API_ID = 25918991
API_HASH = "a0c40f9091e814a7c2Bafa597218b0c0"


# Channel configuration - Channel to Channel forwarding using usernames
SOURCE_CHANNEL = "@binancekillers"  # Binance Killers® (main channel)
TARGET_CHANNEL = "@earnksro4"      # EarnKsro

# Message filtering configuration
# Keywords to look for in messages (case-insensitive)
KEYWORDS = ['buy', 'sell', 'signal', 'alert', 'trade', 'long', 'short', 'entry', 'exit', 'target', 'stop']

# Alternative: forward all messages
FORWARD_ALL_MESSAGES = False

# Alternative: custom filter function
def custom_filter(message):
    """
    Custom filter function for messages.
    Return True to forward the message, False to ignore it.
    
    Args:
        message (str): The message text
        
    Returns:
        bool: True to forward, False to ignore
    """
    # Example: forward messages containing keywords
    keywords = ['alert', 'signal', 'trade', 'crypto', 'buy', 'sell', 'long', 'short', 'entry', 'exit', 'target', 'stop', 'vip']
    return any(keyword in message.lower() for keyword in keywords)

# Logging configuration
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Session file name
SESSION_NAME = "session"

# Connection settings
CONNECTION_TIMEOUT = 30  # seconds
RETRY_DELAY = 5  # seconds between retries
MAX_RETRIES = 3  # maximum number of retries 