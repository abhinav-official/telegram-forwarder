"""
Configuration file for Telegram Auto-Forwarder
Modify these settings to customize the bot's behavior
"""

import os

# Telegram API credentials (set via environment variables)
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

# Channel configuration
SOURCE_CHANNEL = os.getenv("SOURCE_CHANNEL")
TARGET_CHANNEL = os.getenv("TARGET_CHANNEL")

# Message filtering configuration
# Keywords to look for in messages (case-insensitive)
KEYWORDS = ['buy', 'sell']

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
    # Example: forward messages containing 'alert' or 'signal'
    keywords = ['alert', 'signal', 'trade', 'crypto']
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