import os
import re
import logging
from dotenv import load_dotenv

import google.generativeai as genai

# ---------------- TELEGRAM ----------------
from telegram.ext import Updater, MessageHandler, Filters

# Load environment variables
load_dotenv()

# ------------- CONFIG -----------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Gemini config
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

# ------------------ HANDLER ------------------
def reply_handler(update, context):
    text = update.message.text
    logging.info(f"Received message: {text}")

    try:
        ai_output = model.generate_content(text).text

        # Clean output
        ai_output = re.sub(r"```.*?```", "", ai_output, flags=re.DOTALL)
        ai_output = re.sub(r"\*\*(.*?)\*\*", r"\1", ai_output)
        ai_output = re.sub(r"__(.*?)__", r"\1", ai_output)
        ai_output = re.sub(r"`(.*?)`", r"\1", ai_output)
        ai_output = re.sub(r"#+\s*(.*)", r"\1", ai_output)
        ai_output = re.sub(r"---", "", ai_output)
        ai_output = ai_output.strip()

    except Exception as e:
        logging.error(f"Gemini Error: {e}")
        ai_output = f"Gemini Error: {str(e)}"

    update.message.reply_text(ai_output)

# ------------------ MAIN ---------------------
if __name__ == "__main__":
    logging.info("🚀 Starting Bot in Polling Mode...")
    
    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Register handler
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_handler))

    # Start polling
    updater.start_polling()
    logging.info("Bot is running. Press Ctrl+C to stop.")
    updater.idle()
