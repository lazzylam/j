from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID
from userbot.forwarder import trigger_forward

bot = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.private & filters.user(OWNER_ID) & filters.forwarded)
async def handle_forwarded_msg(client, message):
    if not message.forward_from_chat:
        await message.reply("Gagal deteksi asal pesan.")
        return
    await message.reply("Pesan diterima, mulai sebar ke grup...")
    await trigger_forward(message.forward_from_chat.id, message.forward_from_message_id)
    await message.reply("Forward selesai.")

async def start_bot():
    await bot.start()
    print("[BOT] Aktif")
    await bot.idle()
