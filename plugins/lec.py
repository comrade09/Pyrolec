import os
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from bot import Bot
from helper_func import subscribed, encode, decode, get_messages


LEC = f"hi gyus <a href= https://t.me/ath2023> hemlo </a>"

@Bot.on_message(filters.command('lecture') & filters.private )
async def lectue_command(bot: Bot, message: Message):
    await message.reply_text( text = LEC,
    disable_web_page_preview = True
   )

