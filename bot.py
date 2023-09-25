from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN: Final = "6247666701:AAGmOFO-RX4x-1cet2Y2ONaf6CI4aoqLlGw"
BOT_USERNAME: Final = "@moonaudioproduction_bot"


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi there! MoonAudioProduction bot welcomes you!")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Great! Please, type anything so I can respond!")


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command")


# Responses

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if processed in ["Hello", "hello", "hi", "Hi", "Привет", "привет"]:
        return "Hi there!"

    if "how are you?" in processed:
        return "Thanks, I'm good!"

    if processed in ["id", "ID", "Id", "iD"]:
        return text
    if processed == "photo":
        photo = open("old_man.jpeg", "rb")
        chat_bot.send_photo(message.chat.id, photo)

    return "I don't understand you...("


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f"User ({update.message.chat.id}) in {message_type}: '{text}'")

    # if message_type == "group":
    #     if BOT_USERNAME in text:
    #         new_text: str = text.replace(BOT_USERNAME, "")
    #         response: str = handle_response(new_text)
    #     else:
    #         return
    #
    # else:
    response: str = handle_response(text)

    print("Bot:", response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} cause the error {context.error}")


if __name__ == '__main__':
    print("Starting bot...")

    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print("Bot is polling...")
    app.run_polling(poll_interval=1)
