# Don't Remove Credit Tg - @Tushar0125
# Ask Doubt on telegram @Tushar0125

import os
import re
import sys
import json
import time
import m3u8
import aiohttp
import asyncio
import requests
import subprocess
import urllib.parse
import cloudscraper
import datetime
import random
import ffmpeg
import logging 
import yt_dlp
from subprocess import getstatusoutput
from aiohttp import web
from core import *
from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup
from yt_dlp import YoutubeDL
import yt_dlp as youtube_dl
import cloudscraper
import m3u8
import core as helper
from utils import progress_bar
from vars import API_ID, API_HASH, BOT_TOKEN
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput
from pytube import YouTube

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
cookies_file_path = os.getenv("COOKIES_FILE_PATH", "youtube_cookies.txt")

cpimg = "https://graph.org/file/5ed50675df0faf833efef-e102210eb72c1d5a17.jpg"  

async def show_random_emojis(message):
    emojis = ['🎊', '🔮', '😎', '⚡️', '🚀', '✨', '💥', '🎉', '🥂', '🍾', '🦠', '🤖', '❤️‍🔥', '🕊️', '💃', '🥳','🐅','🦁']
    emoji_message = await message.reply_text(' '.join(random.choices(emojis, k=1)))
    return emoji_message
    
# Define the owner's user ID
OWNER_ID = 1169394017 # Your user ID as the new owner (positive number)

# List of sudo users (initially empty or pre-populated)
SUDO_USERS = [5840594311,7856557198,6303334633,1169394017]

AUTH_CHANNEL = -1002572301679

# Function to check if a user is authorized
def is_authorized(user_id: int) -> bool:
    return user_id == OWNER_ID or user_id in SUDO_USERS or user_id == AUTH_CHANNEL

bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN)

# Sudo command to add/remove sudo users
@bot.on_message(filters.command("sudo"))
async def sudo_command(bot: Client, message: Message):
    user_id = message.chat.id
    if user_id != OWNER_ID:
        await message.reply_text("**🚫 You are not authorized to use this command.**")
        return

    try:
        args = message.text.split(" ", 2)
        if len(args) < 2:
            await message.reply_text("**Usage:** `/sudo add <user_id>` or `/sudo remove <user_id>`")
            return

        action = args[1].lower()
        target_user_id = int(args[2])

        if action == "add":
            if target_user_id not in SUDO_USERS:
                SUDO_USERS.append(target_user_id)
                await message.reply_text(f"**✅ User {target_user_id} added to sudo list.**")
            else:
                await message.reply_text(f"**⚠️ User {target_user_id} is already in the sudo list.**")
        elif action == "remove":
            if target_user_id == OWNER_ID:
                await message.reply_text("**🚫 The owner cannot be removed from the sudo list.**")
            elif target_user_id in SUDO_USERS:
                SUDO_USERS.remove(target_user_id)
                await message.reply_text(f"**✅ User {target_user_id} removed from sudo list.**")
            else:
                await message.reply_text(f"**⚠️ User {target_user_id} is not in the sudo list.**")
        else:
            await message.reply_text("**Usage:** `/sudo add <user_id>` or `/sudo remove <user_id>`")
    except Exception as e:
        await message.reply_text(f"**Error:** {str(e)}")

# Inline keyboard for start command
keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🇮🇳ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ🇮🇳" ,url=f"https://t.me/Tushar0125") ],
                    [
                    InlineKeyboardButton("🔔ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ🔔" ,url="https://t.me/TxtToVideoUpdateChannel") ],
                    [
                    InlineKeyboardButton("🦋ғᴏʟʟᴏᴡ ᴜs🦋" ,url="https://t.me/TxtToVideoUpdateChannel")                              
                ],           
            ]
      )

# Start command handler
@bot.on_message(filters.command(["start"]))
async def start_command(bot: Client, message: Message):
    welcome_text = """**🎉 Welcome to DRM Uploader Bot!**

➠ **I am a txt to video uploader bot**
➠ **For using me send /tushar**
➠ **For guide send /help**
➠ **Now running on Render platform!**

🤖 **Bot made by ➤ Tushar**
📢 **Updates:** @TxtToVideoUpdateChannel"""
    
    await message.reply_text(welcome_text, reply_markup=keyboard)

# Help command
@bot.on_message(filters.command("help"))
async def help_command(bot: Client, message: Message):
    help_text = """
**🤖 DRM Uploader Bot - Commands Help**

**📋 Available Commands:**

🔥 **Basic Commands:**
• `/start` - Start the bot
• `/help` - Show this help message
• `/stop` - Stop ongoing process
• `/restart` - Restart the bot (sudo only)

🎬 **Main Features:**
• `/tushar` - Upload txt file for processing
• `/cookies` - Upload YouTube cookies file (sudo only)
• `/e2t` - Edit and sort txt files

📊 **Admin Commands:**
• `/sudo add <user_id>` - Add sudo user (owner only)
• `/sudo remove <user_id>` - Remove sudo user (owner only)
• `/userlist` - List all sudo users (sudo only)
• `/yt2txt` - Create txt from YouTube playlist (sudo only)

**🏗️ Platform:** Now running on Render!
**👨‍💻 Developer:** @Tushar0125
**📢 Updates:** @TxtToVideoUpdateChannel

**💡 Note:** Some commands require sudo privileges.
"""
    await message.reply_text(help_text)

if __name__ == "__main__":
    print("🚀 Starting DRM Uploader Bot on Render...")
    print("✅ Bot initialized successfully")
    bot.run()
