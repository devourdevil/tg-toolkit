


from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, CallbackContext
import random
import time
import os

# Replace 'YOUR_TOKEN' with your actual bot token
TOKEN = os.getenv('TOKEN')

def start(update: Update, context: CallbackContext) -> None:
    username = update.message.from_user.username
    reply_text = f"Hello {username}, I am a Toolkit for Telegram. What can I do for you?"
    keyboard = [[InlineKeyboardButton("Insta Hack", callback_data='insta_hack')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(reply_text, reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if query.data == 'insta_hack':
        query.edit_message_text(text="Please enter the Instagram username:")
        context.user_data['next'] = 'ask_action'

def message_handler(update: Update, context: CallbackContext) -> None:
    if 'next' in context.user_data and context.user_data['next'] == 'ask_action':
        insta_username = update.message.text
        context.user_data['insta_username'] = insta_username
        reply_text = f"What can I do with this username {insta_username}?"
        keyboard = [
            [InlineKeyboardButton("Hack", callback_data='hack')],
            [InlineKeyboardButton("Phone Number", callback_data='phone_number')],
            [InlineKeyboardButton("Go to Page", callback_data='goto_page')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(reply_text, reply_markup=reply_markup)
        context.user_data['next'] = None

def process_action(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    insta_username = context.user_data.get('insta_username', 'unknown')

    if query.data == 'hack':
        query.edit_message_text(text="Processing hack...")
        time.sleep(2)  # Simulate a delay for processing
        random_password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890', k=8))
        query.edit_message_text(text=f"Hacked Insta successfully!\nUsername: {insta_username}\nPassword: {random_password}")

    elif query.data == 'phone_number':
        query.edit_message_text(text="Fetching phone number...")
        time.sleep(2)  # Simulate a delay for processing
        random_phone_number = '+91' + ''.join(random.choices('1234567890', k=10))
        query.edit_message_text(text=f"Phone Number: {random_phone_number}")

    elif query.data == 'goto_page':
        query.edit_message_text(text=f"Go to Instagram page: https://instagram.com/{insta_username}")

def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button, pattern='^insta_hack$'))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))
    dispatcher.add_handler(CallbackQueryHandler(process_action, pattern='^(hack|phone_number|goto_page)$'))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
