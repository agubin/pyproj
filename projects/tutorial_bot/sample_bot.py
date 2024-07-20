import logging
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, InlineQueryHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a bot, please talk to me!"
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=update.message.text
    )

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    caps_text = ' '.join(context.args).upper()
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=caps_text
    )

async def inline_caps(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, results)

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Sorry, I didn't understand that command."
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token("7050051633:AAEAnPC0TWt3TchgC0KRPO2TV-_vnbx-jls").build()

    start_handler = CommandHandler('start', start)
    app.add_handler(start_handler)

    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    app.add_handler(message_handler)

    caps_handler = CommandHandler('caps', caps)
    app.add_handler(caps_handler)

    inline_caps_handler = InlineQueryHandler(inline_caps)
    app.add_handler(inline_caps_handler)

    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    app.add_handler(unknown_handler)

    app.run_polling()
    