#!/bin/bash

# Discord Bot Setup Script
# Works on Linux, Termux, and similar environments

echo "🤖 Discord Bot Setup"
echo "===================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install it first."
    exit 1
fi

echo "✅ Python 3 found"

# Install pip dependencies
echo ""
echo "📦 Installing dependencies..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

# Create config.json if it doesn't exist
if [ ! -f "config.json" ]; then
    echo ""
    echo "📝 Creating config.json..."
    cp config.json.example config.json
    echo "✅ config.json created from example"
    echo ""
    echo "⚠️  Please edit config.json with your bot token:"
    echo "   - Get your token from: https://discord.com/developers/applications"
    echo "   - Add your user ID as owner_id"
else
    echo "✅ config.json already exists"
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "To start the bot, run:"
echo "  python3 main.py"
