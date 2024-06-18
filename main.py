import os
import random
import time
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Environment variables
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Initialize the bot
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    username = message.from_user.username
    reply_text = f"Hello {username}, I am a Toolkit for Telegram. What can I do for you?"
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Insta Hack", callback_data='insta_hack')]
        ]
    )
    await message.reply(reply_text, reply_markup=keyboard)

@app.on_callback_query(filters.regex('insta_hack'))
async def insta_hack(client, callback_query):
    await callback_query.message.edit("Please enter the Instagram username:")
    app.set_parse_mode("username", True)

@app.on_message(filters.text & filters.private & filters.create(lambda _, __, msg: msg.parse_mode == "username"))
async def ask_action(client, message):
    insta_username = message.text
    message.parse_mode = None  # Reset the parse mode
    reply_text = f"What can I do with this username {insta_username}?"
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Hack", callback_data=f'hack:{insta_username}')],
            [InlineKeyboardButton("Phone Number", callback_data=f'phone_number:{insta_username}')],
            [InlineKeyboardButton("Go to Page", callback_data=f'goto_page:{insta_username}')]
        ]
    )
    await message.reply(reply_text, reply_markup=keyboard)

@app.on_callback_query(filters.regex(r'^(hack|phone_number|goto_page):'))
async def process_action(client, callback_query):
    action, insta_username = callback_query.data.split(":")
    
    if action == "hack":
        await callback_query.message.edit("Processing hack...")
        time.sleep(2)  # Simulate a delay for processing
        random_password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890', k=8))
        await callback_query.message.edit(f"Hacked Insta successfully!\nUsername: {insta_username}\nPassword: {random_password}")

    elif action == "phone_number":
        await callback_query.message.edit("Fetching phone number...")
        time.sleep(2)  # Simulate a delay for processing
        random_phone_number = '+91' + ''.join(random.choices('1234567890', k=10))
        await callback_query.message.edit(f"Phone Number: {random_phone_number}")

    elif action == "goto_page":
        await callback_query.message.edit(f"Go to Instagram page: https://instagram.com/{insta_username}")

if __name__ == '__main__':
    app.run()
