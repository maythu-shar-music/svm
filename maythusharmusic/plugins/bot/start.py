# -*- coding: utf-8 -*-
import time
import asyncio
from pyrogram import filters
from pyrogram.enums import ChatType, ChatMemberStatus, ParseMode
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from youtubesearchpython.__future__ import VideosSearch

import config
from maythusharmusic import app
from maythusharmusic.misc import _boot_
from maythusharmusic.plugins.sudo.sudoers import sudoers_list
from maythusharmusic.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from maythusharmusic.utils.decorators.language import LanguageStart
from maythusharmusic.utils.formatters import get_readable_time
from maythusharmusic.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS
from strings import get_string


@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    await message.react("❤")
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            await message.reply_sticker("CAACAgUAAxkBAAEP1iZpIbqC1oXAVuwP0n3b9oNnnHRlvQAC0g4AAqVyqVcL00FzQjR1ZjYE")
            return await message.reply_photo(
                photo=config.START_IMG_URL,
                caption=_["help_1"].format(config.SUPPORT_CHAT),
                reply_markup=keyboard,
            )
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>sᴜᴅᴏʟɪsᴛ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                )
            return
        if name[0:3] == "inf":
            m = await message.reply_text("🔎")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = _["start_6"].format(
                title, duration, views, published, channellink, channel, app.mention
            )
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=_["S_B_8"], url=link),
                        InlineKeyboardButton(text=_["S_B_9"], url=config.SUPPORT_CHAT),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                chat_id=message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                reply_markup=key,
            )
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                )
    else:
        try:
            out = private_panel(_)
            lol = await message.reply_text("**ω ᥫ᭡**")
            await asyncio.sleep(0.1)
            await lol.edit_text("**ωє ᥫ᭡**")
            await asyncio.sleep(0.1)
            await lol.edit_text("**ωєℓ ᥫ᭡**")
            await asyncio.sleep(0.1)
            await lol.edit_text("**ωєℓᴄ ᥫ᭡**")
            await asyncio.sleep(0.1)
            await lol.edit_text("**ωєℓᴄᴏᴍ ᥫ᭡**")
            await asyncio.sleep(0.1)
            await lol.edit_text("**ωєℓᴄᴏᴍᴇ ᥫ᭡**")
            await asyncio.sleep(0.1)
            await lol.edit_text("**ωєℓᴄᴏᴍᴇ в ᥫ᭡**")
            await asyncio.sleep(0.1)
            await lol.edit_text("**ωєℓᴄᴏᴍᴇ вα ᥫ᭡**")
            await asyncio.sleep(0.1)
            await lol.edit_text("**ωєℓᴄᴏᴍᴇ вαв ᥫ᭡**")
            await asyncio.sleep(0.1)
            await lol.edit_text("**ωєℓᴄᴏᴍᴇ вαву ᥫ᭡**")
            
            await lol.delete()
            lols = await message.reply_text("**⚡️ѕ**")
            await asyncio.sleep(0.1)
            await lols.edit_text("⚡ѕт")        
            await asyncio.sleep(0.1)
            await lols.edit_text("**⚡ѕтα**")
            await asyncio.sleep(0.1)
            await lols.edit_text("**⚡ѕтαя**")
            await asyncio.sleep(0.1)
            await lols.edit_text("**⚡ѕтαят**")
            await asyncio.sleep(0.1)
            await lols.edit_text("**⚡ѕтαятι**")
            await asyncio.sleep(0.1)
            await lols.edit_text("**⚡ѕтαятιи**")
            await asyncio.sleep(0.1)
            await lols.edit_text("**⚡ѕтαятιиg**")
            await asyncio.sleep(0.1)
            await lols.edit_text("**⚡ѕтαятιиg.**")
            await lols.edit_text("**⚡ѕтαятιиg....**")
            
            m = await message.reply_sticker("CAACAgUAAxkBAAEP0-NpIJZD3PhPH5RITkr21yD7cmlaaQAC4w8AAh7zWVcwgHF1OyOemjYE")
            
            chat_photo = config.START_IMG_URL
            spoiler_needed = False
                
        except Exception as e:
            print(f"Error: {e}")
            chat_photo = config.START_IMG_URL
            spoiler_needed = False
            
        await lols.delete()
        await m.delete()
        
        PREMIUM_EMOJI_1 = "6120465303177533732" 
        PREMIUM_EMOJI_2 = "6120591326107935086" 
        PREMIUM_EMOJI_3 = "6120398056874582504"
        PREMIUM_EMOJI_4 = "6205967094039709231"
        PREMIUM_EMOJI_5 = "6206217069726271155"
        PREMIUM_EMOJI_6 = "6204129896009042249"
        PREMIUM_EMOJI_7 = "6206275004540126842"
        PREMIUM_EMOJI_8 = "6205967094039709231"
        PREMIUM_EMOJI_9 = "6206217069726271155"
        PREMIUM_EMOJI_10 = "6204129896009042249"
        PREMIUM_EMOJI_11 = "6206275004540126842"
        
        START_TEXT = f"""
<emoji id="{PREMIUM_EMOJI_4}">🔴</emoji> ʜᴇʏ ʙᴀʙʏ : {message.from_user.mention} <emoji id="{PREMIUM_EMOJI_1}">🥺</emoji>
<emoji id="{PREMIUM_EMOJI_5}">🔴</emoji> ɪ ᴀᴍ {app.mention}, ʜᴇʀᴇ ᴛᴏ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴡɪᴛʜ ᴀ ꜱᴍᴏᴏᴛʜ ᴍᴜꜱɪᴄ ꜱᴛʀᴇᴀᴍɪɴɢ ᴇxᴘᴇʀɪᴇɴᴄᴇ <emoji id="{PREMIUM_EMOJI_2}">🤩</emoji>.

<emoji id="{PREMIUM_EMOJI_6}">🔴</emoji> ғᴇᴀᴛᴜʀᴇs
<emoji id="{PREMIUM_EMOJI_7}">🔴</emoji> ʜǫ ᴀᴜᴅɪᴏ : 320ᴋʙᴘs sᴛʀᴇᴀᴍɪɴɢ
<emoji id="{PREMIUM_EMOJI_8}">🔴</emoji> sᴛʀᴇᴀᴍ sᴜᴘᴘᴏʀᴛ : ᴀᴜᴅɪᴏ-ᴠɪᴅᴇᴏ
<emoji id="{PREMIUM_EMOJI_9}">🔴</emoji> 24-7 ᴜᴘᴛɪᴍᴇ : ᴇɴᴛᴇʀᴘʀɪsᴇ ʀᴇʟɪᴀʙɪʟɪᴛʏ
<emoji id="{PREMIUM_EMOJI_10}">🔴</emoji> ᴘʟᴀʏ ᴄᴏᴍᴍᴇɴᴛꜱ : ᴘʟᴀʏ, ᴠᴘʟᴀʏ 
<emoji id="{PREMIUM_EMOJI_11}">🔴</emoji> ʙᴀsᴇᴅ ᴏɴ : ʏᴏᴜᴛᴜʙᴇ ᴀᴘɪ

<emoji id="{PREMIUM_EMOJI_4}">🔴</emoji> ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴍᴇ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴛʜᴇ ʙᴜᴛᴛᴏɴꜱ ʙᴇʟᴏᴡ <emoji id="{PREMIUM_EMOJI_3}">😙</emoji>."""

        await message.reply_photo(
            photo=chat_photo,
            caption=START_TEXT,
            reply_markup=InlineKeyboardMarkup(out),
            has_spoiler=spoiler_needed,
            parse_mode=ParseMode.HTML
         )
        
        if await is_on_off(config.LOG):
            sender_id = message.from_user.id
            sender_name = message.from_user.first_name
            return await app.send_message(
                config.LOGGER_ID,
                f"{message.from_user.mention} ʜᴀs sᴛᴀʀᴛᴇᴅ ʙᴏᴛ. \n\n**ᴜsᴇʀ ɪᴅ :** {sender_id}\n**ᴜsᴇʀ ɴᴀᴍᴇ:** {sender_name}",
            )


@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    await message.reply_photo(
        photo=config.START_IMG_URL,
        caption=_["start_1"].format(app.mention, get_readable_time(uptime)),
        reply_markup=InlineKeyboardMarkup(out),
    )
    return await add_served_chat(message.chat.id)


@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except:
                    pass
            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)
                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_5"].format(
                            app.mention,
                            f"https://t.me/{app.username}?start=sudolist",
                            config.SUPPORT_CHAT,
                        ),
                        disable_web_page_preview=True,
                    )
                    return await app.leave_chat(message.chat.id)

                out = start_panel(_)
                await message.reply_photo(
                    photo=config.START_IMG_URL,
                    caption=_["start_3"].format(
                        message.from_user.first_name,
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
                await add_served_chat(message.chat.id)
                await message.stop_propagation()
        except Exception as ex:
            print(ex)
