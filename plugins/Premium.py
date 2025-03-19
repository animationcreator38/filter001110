
from datetime import timedelta
import pytz
import datetime, time
from Script import script 
from info import ADMINS, PREMIUM_LOGS,LOG_CHANNEL
from utils import get_seconds, temp
from database.users_chats_db import db 
from pyrogram import Client, filters 
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.command("remove_premium") & filters.user(ADMINS))
async def remove_premium(client, message):
    if len(message.command) == 2:
        user_id = int(message.command[1])  # Convert the user_id to integer
        user = await client.get_users(user_id)
        if await db.remove_premium_access(user_id):
            await message.reply_text("ᴜꜱᴇʀ ʀᴇᴍᴏᴠᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ !")
            await client.send_message(
                chat_id=user_id,
                text=f"<b>Dᴇᴀʀ {user.mention},\n\n ☹️ ʏᴏᴜʀ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ ᴘʟᴀɴ ʜᴀꜱ ᴇxᴘɪʀᴇᴅ, ᴛᴏ ᴇɴᴊᴏʏ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ ꜱᴇʀᴠɪᴄᴇꜱ ᴀɢᴀɪɴ ᴘʟᴇᴀꜱᴇ ʙᴜʏ ᴄɪɴᴇᴡᴏᴏᴅ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ ᴀɢᴀɪɴ ᴀꜱ ᴘᴇʀ ʏᴏᴜʀ ᴘʟᴀɴ ᴛᴏ ᴄʜᴇᴄᴋ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀɴ ᴜꜱᴇ /myplan ᴛᴏ ᴄʜᴇᴄᴋ ᴘʟᴀɴꜱ ʟɪꜱᴛ ᴜꜱᴇ /Plans</b>"
            )
        else:
            await message.reply_text("ᴜɴᴀʙʟᴇ ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴜꜱᴇᴅ !\nᴀʀᴇ ʏᴏᴜ ꜱᴜʀᴇ, ɪᴛ ᴡᴀꜱ ᴀ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ ɪᴅ ?")
    else:
        await message.reply_text("ᴜꜱᴀɢᴇ : /remove_premium user_id") 

@Client.on_message(filters.command("myplan"))
async def myplan(client, message):
    user = message.from_user.mention 
    user_id = message.from_user.id
    data = await db.get_user(message.from_user.id)  # Convert the user_id to integer
    if data and data.get("expiry_time"):
        #expiry_time = datetime.datetime.now() + datetime.timedelta(seconds=data)
        expiry = data.get("expiry_time") 
        expiry_ist = expiry.astimezone(pytz.timezone("Asia/Kolkata"))
        expiry_str_in_ist = expiry.astimezone(pytz.timezone("Asia/Kolkata")).strftime("%d-%m-%Y\n⏱️ ᴇxᴘɪʀʏ ᴛɪᴍᴇ : %I:%M:%S %p")            
        current_time = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
        time_left = expiry_ist - current_time
        days = time_left.days
        hours, remainder = divmod(time_left.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_left_str = f"{days} ᴅᴀʏꜱ, {hours} ʜᴏᴜʀꜱ, {minutes} ᴍɪɴᴜᴛᴇꜱ"
        await message.reply_text(f"ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ ᴜꜱᴇʀ ᴅᴀᴛᴀ :\n\n😎 ᴜꜱᴇʀ : {user}\n⚡ ᴜꜱᴇʀ ɪᴅ : <code>{user_id}</code>\n⏰ ᴛɪᴍᴇ ʟᴇꜰᴛ : {time_left_str}\n✖️ ᴇxᴘɪʀʏ ᴅᴀᴛᴇ : {expiry_str_in_ist}")   
    else:
        await message.reply_text(f"<b>ʜᴇʏ {user},\n\n𝒀𝒐𝒖 𝑫𝒐 𝑵𝒐𝒕 𝑯𝒂𝒗𝒆 𝑨𝒏𝒚 𝑨𝒄𝒕𝒊𝒗𝒆 𝑷𝒓𝒆𝒎𝒊𝒖𝒎 𝒑𝒍𝒂𝒏𝒔, 𝑰𝒇 𝒀𝒐𝒖 𝑾𝒂𝒏𝒕 𝑻𝒐 𝑻𝒂𝒌𝒆 𝑷𝒓𝒆𝒎𝒊𝒖𝒎 𝑻𝒉𝒆𝒏 𝑪𝒍𝒊𝒄𝒌 𝑶𝒏 𝑩𝒆𝒍𝒐𝒘 𝑩𝒖𝒕𝒕𝒐𝒏 👇\n\n<blockquote>आपके पास कोई सक्रिय 𝑷𝒓𝒆𝒎𝒊𝒖𝒎 𝑷𝒍𝒂𝒏𝒔 नहीं है, यदि आप 𝑷𝒓𝒆𝒎𝒊𝒖𝒎 लेना चाहते हैं तो नीचे दिए गए 𝑩𝒖𝒕𝒕𝒐𝒏 पर 𝑪𝒍𝒊𝒄𝒌 करें 👇</blockquote><b>",
	reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🌳 ᴄʜᴇᴄᴋᴏᴜᴛ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴꜱ 🌳", callback_data='seeplans')]]))			 

@Client.on_message(filters.command("get_premium") & filters.user(ADMINS))
async def get_premium(client, message):
    if len(message.command) == 2:
        user_id = int(message.command[1])
        user = await client.get_users(user_id)
        data = await db.get_user(user_id)  
        if data and data.get("expiry_time"):
            #expiry_time = datetime.datetime.now() + datetime.timedelta(seconds=data)
            expiry = data.get("expiry_time") 
            expiry_ist = expiry.astimezone(pytz.timezone("Asia/Kolkata"))
            expiry_str_in_ist = expiry.astimezone(pytz.timezone("Asia/Kolkata")).strftime("%d-%m-%Y\n⏱️ ᴇxᴘɪʀʏ ᴛɪᴍᴇ : %I:%M:%S %p")            
            current_time = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
            time_left = expiry_ist - current_time
            days = time_left.days
            hours, remainder = divmod(time_left.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            time_left_str = f"{days} days, {hours} hours, {minutes} minutes"
            await message.reply_text(f"ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ ᴜꜱᴇʀ ᴅᴀᴛᴀ :\n\n😎 ᴜꜱᴇʀ : {user.mention}\n⚡ ᴜꜱᴇʀ ɪᴅ : <code>{user_id}</code>\n⏰ ᴛɪᴍᴇ ʟᴇꜰᴛ : {time_left_str}\n✖️ ᴇxᴘɪʀʏ ᴅᴀᴛᴇ : {expiry_str_in_ist}")
        else:
            await message.reply_text("ɴᴏ ᴀɴʏ ᴘʀᴇᴍɪᴜᴍ ᴅᴀᴛᴀ ᴏꜰ ᴛʜᴇ ᴡᴀꜱ ꜰᴏᴜɴᴅ ɪɴ ᴅᴀᴛᴀʙᴀꜱᴇ !")
    else:
        await message.reply_text("ᴜꜱᴀɢᴇ : /get_premium user_id")

@Client.on_message(filters.command("add_premium") & filters.user(ADMINS))
async def give_premium_cmd_handler(client, message):
    if len(message.command) == 4:
        time_zone = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
        current_time = time_zone.strftime("%d-%m-%Y\n⏱️ ᴀᴄᴛɪᴠᴀᴛɪᴏɴ ᴛɪᴍᴇ : %I:%M:%S %p") 
        user_id = int(message.command[1])  
        user = await client.get_users(user_id)
        time = message.command[2]+" "+message.command[3]
        seconds = await get_seconds(time)
        if seconds > 0:
            expiry_time = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
            user_data = {"id": user_id, "expiry_time": expiry_time}  
            await db.update_user(user_data) 
            data = await db.get_user(user_id)
            expiry = data.get("expiry_time")   
            expiry_str_in_ist = expiry.astimezone(pytz.timezone("Asia/Kolkata")).strftime("%d-%m-%Y\n⏱️ ᴇxᴘɪʀʏ ᴛɪᴍᴇ : %I:%M:%S %p")         
            await message.reply_text(f"ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ 🥳\n\n😎 ᴜꜱᴇʀ : {user.mention}\n⚡ ᴜꜱᴇʀ ɪᴅ : <code>{user_id}</code>\n🗓 ᴠᴀʟɪᴅɪᴛʏ : <code>{time}</code>\n\n📅 ᴀᴄᴛɪᴠᴀᴛɪᴏɴ ᴅᴀᴛᴇ : {current_time}\n\n✖️ ᴇxᴘɪʀʏ ᴅᴀᴛᴇ : {expiry_str_in_ist}", disable_web_page_preview=True)
            await client.send_message(
                chat_id=user_id,
                text=f"Dᴇᴀʀ {user.mention} 🥰,\n\nᴛʜᴀɴᴋ ʏᴏᴜ ᴠᴇʀʏ ᴍᴜᴄʜ ꜰᴏʀ ᴘᴜʀᴄʜᴀꜱɪɴɢ ᴄɪɴᴇᴡᴏᴏᴅ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ 🥳. ɴᴏᴡ ꜰᴇᴇʟ ᴘʀᴏᴜᴅ ᴏꜰ ʏᴏᴜʀꜱᴇʟꜰ 😎 ᴀꜱ ʏᴏᴜ ᴀʀᴇ ɴᴏᴡ ᴀ ᴍᴇᴍʙᴇʀ ᴏꜰ ᴄɪɴᴇᴡᴏᴅ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ\n\n🗓 ᴠᴀʟɪᴅɪᴛʏ : <code>{time}</code>\n📅 ᴀᴄᴛɪᴠᴀᴛɪᴏɴ ᴅᴀᴛᴇ : {current_time}\n\n✖️ ᴇxᴘɪʀʏ ᴅᴀᴛᴇ : {expiry_str_in_ist}", disable_web_page_preview=True              
            )    
            await client.send_message(PREMIUM_LOGS, text=f"#Added_Premium\n\n😎 ᴜꜱᴇʀ : {user.mention}\n⚡ ᴜꜱᴇʀ ɪᴅ : <code>{user_id}</code>\n🗓 ᴠᴀʟɪᴅɪᴛʏ : <code>{time}</code>\n\n📅 ᴀᴄᴛɪᴠᴀᴛɪᴏɴ ᴅᴀᴛᴇ : {current_time}\n\n✖️ ᴇxᴘɪʀʏ ᴅᴀᴛᴇ : {expiry_str_in_ist}", disable_web_page_preview=True)
                    
        else:
            await message.reply_text("Invalid time format. Please use '1 day for days', '1 hour for hours', or '1 min for minutes', or '1 month for months' or '1 year for year'")
    else:
        await message.reply_text("Usage : /add_premium user_id time (e.g., '1 day for days', '1 hour for hours', or '1 min for minutes', or '1 month for months' or '1 year for year')")

@Client.on_message(filters.command("premium_users") & filters.user(ADMINS))
async def premium_user(client, message):
    aa = await message.reply_text("<i>ꜰᴇᴛᴄʜɪɴɢ...</i>")
    new = f" ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀꜱ ʟɪꜱᴛ :\n\n"
    user_count = 1
    users = await db.get_all_users()
    async for user in users:
        data = await db.get_user(user['id'])
        if data and data.get("expiry_time"):
            expiry = data.get("expiry_time") 
            expiry_ist = expiry.astimezone(pytz.timezone("Asia/Kolkata"))
            expiry_str_in_ist = expiry.astimezone(pytz.timezone("Asia/Kolkata")).strftime("%d-%m-%Y\n⏱️ ᴇxᴘɪʀʏ ᴛɪᴍᴇ : %I:%M:%S %p")            
            current_time = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
            time_left = expiry_ist - current_time
            days = time_left.days
            hours, remainder = divmod(time_left.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            time_left_str = f"{days} days, {hours} hours, {minutes} minutes"	 
            new += f"{user_count}. {(await client.get_users(user['id'])).mention}\n👤 ᴜꜱᴇʀ ɪᴅ : {user['id']}\n⏳ ᴇxᴘɪʀʏ ᴅᴀᴛᴇ : {expiry_str_in_ist}\n⏰ ᴛɪᴍᴇ ʟᴇꜰᴛ : {time_left_str}\n"
            user_count += 1
        else:
            pass
    try:    
        await aa.edit_text(new)
    except MessageTooLong:
        with open('usersplan.txt', 'w+') as outfile:
            outfile.write(new)
        await message.reply_document('usersplan.txt', caption="Paid Users:")



@Client.on_message(filters.command("plans"))
async def plan(client, message):
    user_id = message.from_user.id 
    users = message.from_user.mention
    log_message = f"<b><u>🚫 ᴛʜɪs ᴜsᴇʀs ᴛʀʏ ᴛᴏ ᴄʜᴇᴄᴋ /plan</u> {temp.B_LINK}\n\n- ɪᴅ - `{user_id}`\n- ɴᴀᴍᴇ - {users}</b>" 
    btn = [[
            InlineKeyboardButton('🔹 Tɪɴʏ', callback_data='broze'),
            InlineKeyboardButton('🎉 Sᴛᴀʀᴛᴇʀ', callback_data='silver')
        ],[
            InlineKeyboardButton('🥈 Sɪʟᴠᴇʀ', callback_data='gold'),
            InlineKeyboardButton('🏅 Gᴏʟᴅᴇɴ', callback_data='platinum')
        ],[
            InlineKeyboardButton('🚀 Pʟᴀᴛɪɴᴜᴍ', callback_data='diamond'),
            InlineKeyboardButton('💎 Dɪᴀᴍᴏɴᴅ', callback_data='other')
        ],[            
            InlineKeyboardButton('⭅ Bᴀᴄᴋ Tᴏ Hᴏᴍᴇ ⭆', callback_data='start')
        ]]
    await message.reply_photo(photo="https://envs.sh/Wjj.png", caption=script.PREMIUM_TEXT.format(message.from_user.mention), reply_markup=InlineKeyboardMarkup(btn))
    await client.send_message(LOG_CHANNEL, log_message)

    
