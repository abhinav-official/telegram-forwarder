#!/bin/bash

# Telegram Auto-Forwarder Environment Setup
echo "🚀 Setting up Telegram Auto-Forwarder environment..."

# Set API credentials
export API_ID="24390163"
export API_HASH="5ac2a3551509d703074db3c6862c5bb0"

echo "✅ API credentials set:"
echo "  API_ID: $API_ID"
echo "  API_HASH: $API_HASH"

# Check if source and target channels are set
if [ -z "$SOURCE_CHANNEL" ]; then
    echo "⚠️  SOURCE_CHANNEL not set. Please set it to your source channel (e.g., @channel_name)"
    echo "   export SOURCE_CHANNEL=\"@your_source_channel\""
fi

if [ -z "$TARGET_CHANNEL" ]; then
    echo "⚠️  TARGET_CHANNEL not set. Please set it to your target channel (e.g., @channel_name)"
    echo "   export TARGET_CHANNEL=\"@your_target_channel\""
fi

echo ""
echo "🔧 To set channels, run:"
echo "   export SOURCE_CHANNEL=\"@your_source_channel\""
echo "   export TARGET_CHANNEL=\"@your_target_channel\""
echo ""
echo "🧪 To test your setup, run:"
echo "   python test_setup.py"
echo ""
echo "🚀 To deploy to Fly.io, run:"
echo "   ./deploy.sh" 