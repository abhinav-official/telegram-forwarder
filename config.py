"""
Configuration file for Telegram Auto-Forwarder
Modify these settings to customize the bot's behavior
"""

# Telegram API credentials

# Abhinav's Account
# API_ID = 24390163
# API_HASH = "5ac2a3551509d703074db3c6862c5bb0"

# Aman Dad's Account
API_ID = 21669680
API_HASH = "380f5c49dcd5a214a4b0e0922323ae8d"

# Channel configuration - Update these with actual IDs from get_channels.py
SOURCE_CHANNEL_ID = None  # Will be set after running get_channels.py
TARGET_USER_ID = None     # Will be set after running get_channels.py

# Message filtering configuration
# Keywords to look for in messages (case-insensitive)
KEYWORDS = ['buy', 'sell', 'signal', 'alert', 'trade']

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
    keywords = ['alert', 'signal', 'trade', 'crypto', 'buy', 'sell']
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