import os
import re
import requests
from flask import Flask, request
import google.generativeai as genai

from telegram import Bot, Update
from telegram.ext import Dispatcher, MessageHandler, filters

# ------------- CONFIG -----------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
PUBLIC_URL = os.environ.get("PUBLIC_URL")  # Render / hosting URL
WEBHOOK_PATH = "/bot"
# --------------------------------------

app = Flask(__name__)
bot = Bot(token=BOT_TOKEN)

# Dispatcher (sync)
dispatcher = Dispatcher(bot, None, workers=1)

# Gemini config
genai.configure(api_key=GEMINI_API_KEY)

# Updated Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash")


# ------------------ HANDLER ------------------
def reply_handler(update, context):
    text = update.message.text

    try:
        ai_output = model.generate_content(text).text

        # Remove code blocks and markdown/HTML
        ai_output = re.sub(r"```.*?```", "", ai_output, flags=re.DOTALL)
        ai_output = re.sub(r"\*\*(.*?)\*\*", r"\1", ai_output)
        ai_output = re.sub(r"__(.*?)__", r"\1", ai_output)
        ai_output = re.sub(r"`(.*?)`", r"\1", ai_output)
        ai_output = re.sub(r"#+\s*(.*)", r"\1", ai_output)
        ai_output = re.sub(r"---", "", ai_output)

        ai_output = ai_output.strip()

    except Exception as e:
        ai_output = f"Gemini Error: {str(e)}"

    bot.send_message(
        chat_id=update.message.chat.id,
        text=ai_output
    )


dispatcher.add_handler(MessageHandler(filters.TEXT, reply_handler))


# ------------------ WEBHOOK ------------------
@app.route(WEBHOOK_PATH, methods=["POST"])
def webhook():
    json_data = request.get_json(force=True)
    update = Update.de_json(json_data, bot)
    dispatcher.process_update(update)
    return "OK"


@app.route("/")
def home():
    return "Telegram Gemini Bot Running!"


# ------------------ SET WEBHOOK --------------
def set_webhook():
    url = f"{PUBLIC_URL}{WEBHOOK_PATH}"
    print("Setting webhook:", url)

    response = requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={url}"
    )

    print("Webhook response:", response.text)


# ------------------ MAIN ---------------------
if __name__ == "__main__":
    print("🚀 Starting Flask...")
    set_webhook()
    app.run(host="0.0.0.0", port=5000)
