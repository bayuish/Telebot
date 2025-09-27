import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Token dari BotFather (jangan commit ke GitHub langsung, pakai ENV variable di Render)
import os
TOKEN = "8355523461:AAG2mNsdFfnAP_V7UtgoW9j8GcEg9Te6Rx8"

# Command /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo 👋, saya Belbot321_bot!\n\n"
        "Ketik /help untuk lihat menu."
    )

# Command /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Daftar perintah:\n"
        "/start - Mulai bot\n"
        "/setarea - Atur area geofencing\n"
        "/status - Cek lokasi sekarang"
    )

# Command /setarea
async def setarea(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 2:
        await update.message.reply_text("Gunakan format: /setarea <lat> <lon>")
        return

    lat, lon = context.args
    with open("geofence.txt", "w") as f:
        f.write(f"{lat},{lon}")

    await update.message.reply_text(f"✅ Area diset ke: {lat}, {lon}")

# Runner
async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("setarea", setarea))

    print("Bot jalan di Render...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
