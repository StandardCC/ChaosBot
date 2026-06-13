# Discord Moderation Bot

A powerful Discord bot with moderation and utility commands. Includes both **slash commands** and **prefix commands**.

## Features

✅ **Moderation Commands**
- `/kick` - Kick members from the server
- `/ban` - Ban members from the server
- `/clear` - Clear messages from a channel (1-100)
- `/purge` - Purge messages from a channel (1-1000)
- `/purge_all_channels` - Purge all messages from all channels

✅ **Information Commands**
- `/userinfo` - Get information about a user
- `/serverinfo` - Get information about the server

✅ **Utility Commands**
- `/ping` - Check bot latency
- `/say` - Make the bot send a message
- `/set_honeypot` - Set a channel as honeypot (auto-kick & delete messages)

✅ **Prefix Commands**
- All commands above available with prefix (default: `!`)
- Example: `!ping`, `!kick @user`, `!say hello`

✅ **Honeypot System**
- Automatically kicks users who message in the honeypot channel
- Deletes honeypot messages
- Sends alert to bot owner

## Installation

### Requirements
- Python 3.8 or higher
- pip

### Setup Steps

1. **Download the bot**
   ```bash
   # If on Termux or Android
   git clone https://github.com/your-username/discord-bot
   cd discord-bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create your config file**
   ```bash
   cp config.json.example config.json
   ```

4. **Edit config.json** with your bot information:
   ```json
   {
       "token": "YOUR_BOT_TOKEN_HERE",
       "prefix": "!",
       "owner_id": 123456789
   }
   ```

   - Get your bot token from [Discord Developer Portal](https://discord.com/developers/applications)
   - Get your owner ID by enabling Developer Mode in Discord and right-clicking your profile

5. **Run the bot**
   ```bash
   python main.py
   ```

## Getting a Bot Token

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application"
3. Go to "Bot" section and click "Add Bot"
4. Copy the token
5. Paste it in `config.json`

## Inviting the Bot to Your Server

1. In Developer Portal, go to "OAuth2" → "URL Generator"
2. Select these scopes:
   - `bot`
   - `applications.commands`
3. Select these permissions:
   - Send Messages
   - Manage Messages
   - Kick Members
   - Ban Members
   - Manage Channels

4. Copy the generated URL and open it in your browser

## Command Examples

### Slash Commands
```
/ping
/say message: Hello everyone!
/kick user: @User reason: Spamming
/ban user: @User reason: Toxicity
/clear amount: 10
/purge amount: 50
/purge_all_channels
/userinfo user: @User
/serverinfo
/set_honeypot channel: #honeypot
```

### Prefix Commands
```
!ping
!say Hello everyone!
!kick @User Spamming
!ban @User Toxicity
!clear 10
!purge 50
!userinfo @User
!serverinfo
!set_honeypot #honeypot
```

## Honeypot System

The honeypot system automatically protects a channel by:
1. Detecting any message sent in the honeypot channel
2. Deleting the message immediately
3. Kicking the user from the server
4. Sending an alert to the bot owner

**Setup:**
```
/set_honeypot channel: #honeypot
```

or with prefix:
```
!set_honeypot #honeypot
```

## Configuration

Edit `config.json`:

```json
{
    "token": "YOUR_DISCORD_BOT_TOKEN",
    "prefix": "!",
    "owner_id": 123456789
}
```

- **token**: Your Discord bot token
- **prefix**: Command prefix (default: `!`)
- **owner_id**: Your Discord user ID (for honeypot alerts)

## Troubleshooting

**Bot won't start**
- Check that `config.json` exists and has a valid token
- Make sure your token is correct
- Check internet connection

**Commands not working**
- Make sure bot has necessary permissions
- Slash commands may take a minute to sync
- Check that you have permission to use the command

**Honeypot not working**
- Make sure bot has permission to kick members
- Make sure bot has higher role than the user
- Check that the channel is correctly set

## Support

For issues or feature requests, open an issue on GitHub.

## License

MIT License - Feel free to use and modify!
