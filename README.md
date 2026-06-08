# Telegram Gemini Bot 🤖✨

<div align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZqejd3bWhrZzZqZzZqZzZqZzZqZzZqZzZqZzZqZzZqZzZqJmVwPXY9aW50ZXJuYWxfZ2lmX2J5X2lkJmN0PWc/3o7TKMGpxxHOGTdzJC/giphy.gif" width="200" />
</div>

A powerful Telegram bot powered by **Google Gemini AI**.

## 🚀 Features
- 🤖 **AI-Powered Replies:** Uses Google Gemini (Flash model) for intelligent responses.
- ⚡ **Real-time Webhook:** Built with Flask for fast webhook interactions with Telegram.
- 🐳 **Dockerized:** Easy deployment with Docker and Docker Compose.

## 📋 Prerequisites
- Python 3.11+
- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)
- Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- Google Gemini API Key (from [Google AI Studio](https://aistudio.google.com/))
- A public URL (e.g., Render, ngrok)

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd telegram-gemini-bot
   ```

2. **Configure environment variables:**
   Create a `.env` file based on the `docker-compose.yaml` requirements:
   ```bash
   BOT_TOKEN=your_bot_token
   GEMINI_API_KEY=your_gemini_api_key
   PUBLIC_URL=your_public_url
   ```

3. **Run with Docker:**
   ```bash
   docker-compose up --build
   ```

## ⚙️ Configuration
The bot uses the following environment variables:
| Variable | Description |
| :--- | :--- |
| `BOT_TOKEN` | Your Telegram Bot Token |
| `GEMINI_API_KEY` | Your Google Gemini API Key |
| `PUBLIC_URL` | Your publicly accessible URL for the webhook |

---
*Built with ❤️ and AI.*
