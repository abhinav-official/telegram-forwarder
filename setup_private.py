#!/usr/bin/env python3
"""
Setup script for private channel to DM forwarding
This script helps you configure the forwarder to forward from private channels to your DM using your personal account
"""

import os
import asyncio
from telethon import TelegramClient
from config import *

async def setup_private_forwarding():
    """Setup private channel forwarding to DM using personal account"""
    print("🔍 Setting up Private Channel to DM Forwarding (using your account)...")
    
    # Check API credentials
    if not API_ID or not API_HASH:
        print("❌ API_ID and API_HASH must be set")
        print("Run: source setup_env.sh")
        return False
    
    # Create client
    client = TelegramClient(SESSION_NAME, int(API_ID), API_HASH)
    
    try:
        print("\n🔗 Connecting to Telegram...")
        await client.start()
        
        # Get user info
        me = await client.get_me()
        print(f"✅ Logged in as: {me.first_name} (@{me.username})")
        print(f"📱 Your user ID: {me.id}")
        
        # Test source channel access
        if not SOURCE_CHANNEL:
            print("\n❌ SOURCE_CHANNEL not set")
            print("Please set it to the private channel you want to monitor:")
            print("export SOURCE_CHANNEL=\"@channel_name\" or channel ID")
            return False
        
        print(f"\n📢 Testing access to source channel: {SOURCE_CHANNEL}")
        try:
            source_entity = await client.get_entity(SOURCE_CHANNEL)
            print(f"✅ Can access source channel: {source_entity.title}")
            
            # Check if it's a private channel
            if hasattr(source_entity, 'username') and source_entity.username:
                print("ℹ️  This appears to be a public channel")
            else:
                print("ℹ️  This appears to be a private channel")
                
        except Exception as e:
            print(f"❌ Cannot access source channel: {e}")
            print("\n💡 For private channels, you need:")
            print("   1. Be a member of the channel")
            print("   2. Use the channel ID instead of username")
            print("   3. Or use the channel invite link")
            return False
        
        # Test DM access
        print(f"\n💬 Testing DM access...")
        try:
            test_message = "🤖 Test message from Telegram Auto-Forwarder"
            await client.send_message(me, test_message)
            print("✅ Successfully sent test message to your DM")
            print("💡 You can delete this test message from your DM")
        except Exception as e:
            print(f"❌ Cannot send message to DM: {e}")
            return False
        
        print("\n✅ Setup complete! Your configuration:")
        print(f"   Source Channel: {SOURCE_CHANNEL}")
        print(f"   Target: Your DM (User ID: {me.id})")
        
        print("\n🚀 To start the forwarder:")
        print("   source venv/bin/activate")
        print("   python main_private.py")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    finally:
        await client.disconnect()

def get_channel_info():
    """Helper to get channel information"""
    print("\n📋 How to find private channel information:")
    print("1. For private channels, you need the channel ID")
    print("2. You can get this by:")
    print("   - Forwarding a message from the channel to @userinfobot")
    print("   - Or using the channel invite link")
    print("   - Or asking the channel admin for the channel ID")
    print("\n3. Set the environment variable:")
    print("   export SOURCE_CHANNEL=\"@channel_name\"  # for public channels")
    print("   export SOURCE_CHANNEL=\"-1001234567890\"  # for private channels")

if __name__ == "__main__":
    print("🚀 Private Channel to DM Setup")
    print("=" * 40)
    
    # Show channel info help
    get_channel_info()
    
    # Run setup
    success = asyncio.run(setup_private_forwarding())
    
    if success:
        print("\n🎉 Setup completed successfully!")
    else:
        print("\n❌ Setup failed. Please check the errors above.") 