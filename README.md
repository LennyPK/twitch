# Twitch Streaming Tools

A collection of tools and integrations for Twitch streaming, including overlays, channel points, chat integration, and Discord bot functionality.

## Project Structure

### Alert Box
Custom CSS and HTML implementations for various Twitch alerts:
- Subscriber alerts (New, Resub, Gifted, Community Gifted)
- Follower alerts
- Cheer alerts
- Tip alerts
- Raid alerts

### Channel Points
Python-based channel point redemptions integrated with Streamer.bot:
- Kiss
- Smack
- Timer-based actions:
  - Action Ban
  - Word Ban
  - Voice Ban
  - Cursing Ban
  - No Timer

### Chatbox
Custom chat overlay implementation for stream display

### Counters
Various counter implementations:
- Bit Counter
- Bully Counter
- First Counter
- Kiss Counter

### Discord Bot
Discord bot implementation with:
- Guild integration
- Slash command support
- Environment-based configuration
- Member tracking

### Goals (Meters)
Progress tracking implementations:
- Bit Meter
- Sub Meter
- Sub Goal (in development)

### StreamElements
StreamElements-specific integrations and customizations

### Games
Game-specific integrations and overlays

## Technical Implementation

### Alert System
- HTML/CSS-based alert designs
- JavaScript event handling
- Custom styling and animations
- Responsive layouts

### Channel Points
- Python-based automation
- Streamer.bot integration
- Timer-based action system
- Custom redemption handling

### Discord Integration
- Discord.py implementation
- Slash command support
- Environment variable configuration
- Guild-specific commands

### OBS Integration
- Lua-based autostarter script
- Program launch automation
- OBS scene management
- Auto-quit functionality

## Setup and Configuration

### Alert Box Setup
1. Configure alert sources in Twitch dashboard
2. Upload HTML/CSS files to your streaming software
3. Customize alert designs as needed

### Channel Points Setup
1. Install required Python dependencies
2. Configure Streamer.bot
3. Set up channel point rewards in Twitch
4. Link rewards to corresponding Python scripts

### Discord Bot Setup
1. Create Discord application and bot
2. Configure .env file with:
   - DISCORD_TOKEN
   - DISCORD_GUILD
3. Run bot.py to start the bot

### OBS Setup
1. Install the autostarter.lua script
2. Configure executable paths
3. Set auto-quit preferences

## Requirements

- OBS Studio
- Python 3.x
- Streamer.bot
- Discord.py
- Node.js (for some alert implementations)
- Twitch account with affiliate/partner status

## Development Tools

- Visual Studio Code (recommended)
- OBS Studio
- Streamer.bot
- Discord Developer Portal
- Twitch Developer Console
