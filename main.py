from telethon import TelegramClient, events
import os
import logging
import asyncio
from datetime import datetime
from config import *

# Configure logging
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format=LOG_FORMAT
)
logger = logging.getLogger(__name__)

# Validate environment variables
if not all([API_ID, API_HASH, SOURCE_CHANNEL, TARGET_CHANNEL]):
    logger.error("Missing required environment variables. Please set API_ID, API_HASH, SOURCE_CHANNEL, and TARGET_CHANNEL")
    exit(1)

client = TelegramClient(SESSION_NAME, int(API_ID), API_HASH)

def should_forward_message(message):
    """
    Determine if a message should be forwarded based on configuration
    """
    if not message:
        return False
    
    if FORWARD_ALL_MESSAGES:
        return True
    
    # Use custom filter if available
    try:
        return custom_filter(message)
    except NameError:
        # Fall back to keyword-based filtering
        return any(keyword in message.lower() for keyword in KEYWORDS)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    try:
        msg = event.message.message
        if should_forward_message(msg):
            logger.info(f"Forwarding message: {msg[:50]}...")
            await client.send_message(TARGET_CHANNEL, msg)
            logger.info("Message forwarded successfully")
        else:
            logger.debug(f"Message filtered out: {msg[:30]}...")
    except Exception as e:
        logger.error(f"Error forwarding message: {e}")

async def main():
    retry_count = 0
    while retry_count < MAX_RETRIES:
        try:
            logger.info("Starting Telegram Auto-Forwarder...")
            await client.start()
            logger.info("Client started successfully")
            
            # Keep the client running
            await client.run_until_disconnected()
        except Exception as e:
            logger.error(f"Error in main: {e}")
            retry_count += 1
            if retry_count < MAX_RETRIES:
                logger.info(f"Retrying in {RETRY_DELAY} seconds... (attempt {retry_count}/{MAX_RETRIES})")
                await asyncio.sleep(RETRY_DELAY)
            else:
                logger.error("Max retries reached. Exiting.")
        finally:
            await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
