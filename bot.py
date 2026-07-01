import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Bienvenido al PHAGY Official Sentinel.\n\nEl bot está en construcción."
    )


def main():
    if not TOKEN:
        raise ValueError("La variable de entorno BOT_TOKEN no está configurada.")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("✅ Bot iniciado correctamente...")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
