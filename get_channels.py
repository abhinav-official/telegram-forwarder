#!/usr/bin/env python3
"""
Temporary script to get channel information and user details
Run this to find channel IDs and your user ID
"""

import asyncio
from telethon import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

# Your API credentials
API_ID = 24390163
API_HASH = "5ac2a3551509d703074db3c6862c5bb0"
SESSION_NAME = "temp_session"

async def get_channels_and_user():
    """Get all channels and user information"""
    print("🔍 Connecting to Telegram...")
    
    client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
    await client.start()
    
    # Get user info
    me = await client.get_me()
    print("✅ Connected successfully!")
    print(f"👤 Your user ID: {me.id}")
    print(f"👤 Your username: @{me.username}")
    
    print("\n📢 Fetching all dialogs (chats, channels, groups)...")
    
    # Get all dialogs
    dialogs = await client.get_dialogs()
    
    print(f"\n📋 Found {len(dialogs)} dialogs:")
    print("=" * 80)
    
    channels = []
    groups = []
    chats = []
    
    for dialog in dialogs:
        entity = dialog.entity
        
        # Get entity type and details
        if hasattr(entity, 'megagroup') and entity.megagroup:
            entity_type = "Supergroup"
            groups.append({
                'id': entity.id,
                'title': entity.title,
                'username': getattr(entity, 'username', None),
                'type': entity_type
            })
        elif hasattr(entity, 'broadcast') and entity.broadcast:
            entity_type = "Channel"
            channels.append({
                'id': entity.id,
                'title': entity.title,
                'username': getattr(entity, 'username', None),
                'type': entity_type
            })
        else:
            entity_type = "Chat"
            chats.append({
                'id': entity.id,
                'title': entity.title,
                'username': getattr(entity, 'username', None),
                'type': entity_type
            })
    
    print("📺 CHANNELS:")
    print("-" * 40)
    for i, channel in enumerate(channels, 1):
        username_str = f"@{channel['username']}" if channel['username'] else "No username"
        print(f"{i:2d}. {channel['title']}")
        print(f"    ID: {channel['id']}")
        print(f"    Username: {username_str}")
        print(f"    Type: {channel['type']}")
        print()
    
    print("👥 GROUPS:")
    print("-" * 40)
    for i, group in enumerate(groups, 1):
        username_str = f"@{group['username']}" if group['username'] else "No username"
        print(f"{i:2d}. {group['title']}")
        print(f"    ID: {group['id']}")
        print(f"    Username: {username_str}")
        print(f"    Type: {group['type']}")
        print()
    
    print("💬 CHATS:")
    print("-" * 40)
    for i, chat in enumerate(chats, 1):
        username_str = f"@{chat['username']}" if chat['username'] else "No username"
        print(f"{i:2d}. {chat['title']}")
        print(f"    ID: {chat['id']}")
        print(f"    Username: {username_str}")
        print(f"    Type: {chat['type']}")
        print()
    
    # Save to file for easy reference
    with open('channel_info.txt', 'w') as f:
        f.write("TELEGRAM CHANNEL INFORMATION\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Your User ID: {me.id}\n")
        f.write(f"Your Username: @{me.username}\n\n")
        
        f.write("CHANNELS:\n")
        f.write("-" * 20 + "\n")
        for channel in channels:
            username_str = f"@{channel['username']}" if channel['username'] else "No username"
            f.write(f"Title: {channel['title']}\n")
            f.write(f"ID: {channel['id']}\n")
            f.write(f"Username: {username_str}\n")
            f.write(f"Type: {channel['type']}\n\n")
        
        f.write("GROUPS:\n")
        f.write("-" * 20 + "\n")
        for group in groups:
            username_str = f"@{group['username']}" if group['username'] else "No username"
            f.write(f"Title: {group['title']}\n")
            f.write(f"ID: {group['id']}\n")
            f.write(f"Username: {username_str}\n")
            f.write(f"Type: {group['type']}\n\n")
    
    print(f"💾 Channel information saved to 'channel_info.txt'")
    print("\n🎯 To use in your bot:")
    print("   - For source channel: Use the channel ID")
    print("   - For target (your DM): Use your user ID")
    print("   - Example: SOURCE_CHANNEL_ID = -1001234567890")
    print("   - Example: TARGET_USER_ID = 123456789")
    
    await client.disconnect()

if __name__ == "__main__":
    print("🚀 Telegram Channel Information Fetcher")
    print("=" * 50)
    asyncio.run(get_channels_and_user()) 