#!/bin/bash

# Telegram Auto-Forwarder Deployment Script
# Usage: ./deploy.sh

set -e

echo "🚀 Starting Telegram Auto-Forwarder deployment..."

# Check if flyctl is installed
if ! command -v flyctl &> /dev/null; then
    echo "❌ flyctl is not installed. Please install it first:"
    echo "   macOS: brew install flyctl"
    echo "   Linux: curl -L https://fly.io/install.sh | sh"
    echo "   Windows: iwr https://fly.io/install.ps1 -useb | iex"
    exit 1
fi

# Check if user is logged in
if ! flyctl auth whoami &> /dev/null; then
    echo "🔐 Please log in to Fly.io first:"
    echo "   flyctl auth login"
    exit 1
fi

# Get app name from fly.toml or prompt user
APP_NAME=$(grep '^app =' fly.toml | cut -d'"' -f2 2>/dev/null || echo "")

if [ -z "$APP_NAME" ]; then
    echo "📝 Enter your Fly.io app name:"
    read -r APP_NAME
fi

echo "📦 App name: $APP_NAME"

# Check if app exists, create if not
if ! flyctl apps list | grep -q "$APP_NAME"; then
    echo "🆕 Creating new Fly.io app: $APP_NAME"
    flyctl apps create "$APP_NAME" --org personal
else
    echo "✅ App $APP_NAME already exists"
fi

# Set environment variables if not already set
echo "🔧 Setting environment variables..."

# Check if secrets are already set
if ! flyctl secrets list | grep -q "API_ID"; then
    echo "📝 Enter your Telegram API ID:"
    read -r API_ID
    flyctl secrets set "API_ID=$API_ID"
fi

if ! flyctl secrets list | grep -q "API_HASH"; then
    echo "📝 Enter your Telegram API Hash:"
    read -r API_HASH
    flyctl secrets set "API_HASH=$API_HASH"
fi

if ! flyctl secrets list | grep -q "SOURCE_CHANNEL"; then
    echo "📝 Enter source channel username (e.g., @channel_name):"
    read -r SOURCE_CHANNEL
    flyctl secrets set "SOURCE_CHANNEL=$SOURCE_CHANNEL"
fi

if ! flyctl secrets list | grep -q "TARGET_CHANNEL"; then
    echo "📝 Enter target channel username (e.g., @channel_name):"
    read -r TARGET_CHANNEL
    flyctl secrets set "TARGET_CHANNEL=$TARGET_CHANNEL"
fi

# Deploy the app
echo "🚀 Deploying to Fly.io..."
flyctl deploy

echo "✅ Deployment complete!"
echo ""
echo "🔐 To authenticate with Telegram, run:"
echo "   flyctl ssh console"
echo "   python main.py"
echo ""
echo "📊 To view logs:"
echo "   flyctl logs"
echo ""
echo "🔄 To restart the app:"
echo "   flyctl apps restart $APP_NAME" 