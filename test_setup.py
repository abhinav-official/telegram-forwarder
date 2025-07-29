#!/usr/bin/env python3
"""
Test script for Telegram Auto-Forwarder
Run this to verify your configuration before deployment
"""

import asyncio
from telethon import TelegramClient
from config import *

async def test_connection():
    """Test the Telegram connection and channel access"""
    print("🔍 Testing Telegram Auto-Forwarder setup...")
    
    # Check configuration
    print("\n📋 Checking configuration:")
    required_config = {
        "API_ID": API_ID,
        "API_HASH": API_HASH,
        "SOURCE_CHANNEL_ID": SOURCE_CHANNEL_ID,
        "TARGET_USER_ID": TARGET_USER_ID
    }
    
    missing_config = []
    for var_name, var_value in required_config.items():
        if var_value:
            if var_name == "API_HASH":
                print(f"  ✅ {var_name}: {'*' * len(str(var_value))} (hidden)")
            else:
                print(f"  ✅ {var_name}: {var_value}")
        else:
            print(f"  ❌ {var_name}: Not set")
            missing_config.append(var_name)
    
    if missing_config:
        print(f"\n❌ Missing configuration: {', '.join(missing_config)}")
        print("Please run get_channels.py first and update config.py with the channel IDs.")
        return False
    
    # Test Telegram connection
    print("\n🔗 Testing Telegram connection...")
    try:
        client = TelegramClient(SESSION_NAME, int(API_ID), API_HASH)
        await client.start()
        print("  ✅ Successfully connected to Telegram")
        
        # Test channel access
        print("\n📢 Testing channel access...")
        
        # Test source channel
        try:
            source_entity = await client.get_entity(SOURCE_CHANNEL_ID)
            print(f"  ✅ Source channel accessible: {source_entity.title}")
        except Exception as e:
            print(f"  ❌ Cannot access source channel {SOURCE_CHANNEL_ID}: {e}")
            print("  💡 Make sure you're a member of the source channel")
            return False
        
        # Test target user
        try:
            target_entity = await client.get_entity(TARGET_USER_ID)
            print(f"  ✅ Target user accessible: {target_entity.first_name} {target_entity.last_name or ''}")
        except Exception as e:
            print(f"  ❌ Cannot access target user {TARGET_USER_ID}: {e}")
            print("  💡 Make sure the user ID is correct")
            return False
        
        # Test message sending (optional)
        print("\n📤 Testing message sending...")
        try:
            test_message = "🤖 Test message from Telegram Auto-Forwarder"
            await client.send_message(TARGET_USER_ID, test_message)
            print("  ✅ Successfully sent test message to target user")
            print("  💡 You can delete this test message from your DM")
        except Exception as e:
            print(f"  ❌ Cannot send message to target user: {e}")
            print("  💡 Make sure you have permission to send messages")
            return False
        
        await client.disconnect()
        print("\n✅ All tests passed! Your setup is ready for deployment.")
        return True
        
    except Exception as e:
        print(f"  ❌ Failed to connect to Telegram: {e}")
        print("  💡 Check your API_ID and API_HASH")
        return False

async def test_filtering():
    """Test the message filtering logic"""
    print("\n🔍 Testing message filtering...")
    
    test_messages = [
        "Buy signal for BTC",
        "Sell recommendation for ETH",
        "Just a regular message",
        "Alert: New trading opportunity",
        "Hello world"
    ]
    
    for msg in test_messages:
        from main import should_forward_message
        result = should_forward_message(msg)
        status = "✅" if result else "❌"
        print(f"  {status} '{msg}' -> {'Forward' if result else 'Ignore'}")

if __name__ == "__main__":
    print("🚀 Telegram Auto-Forwarder Setup Test")
    print("=" * 50)
    
    # Test connection
    success = asyncio.run(test_connection())
    
    if success:
        # Test filtering
        asyncio.run(test_filtering())
        
        print("\n🎉 Setup test completed successfully!")
        print("\n📝 Next steps:")
        print("  1. Run the bot: python main.py")
        print("  2. Deploy to Fly.io: ./deploy.sh (optional)")
        print("  3. Monitor logs: fly logs (if deployed)")
    else:
        print("\n❌ Setup test failed. Please fix the issues above.")
        print("\n💡 To get channel IDs, run: python get_channels.py") 