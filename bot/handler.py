from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID
from userbot.forwarder import trigger_forward
from logger import logger

bot = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.private & filters.user(OWNER_ID) & filters.forwarded)
async def handle_forwarded_msg(client, message):
    if not message.forward_from_chat:
        await message.reply("Gagal deteksi asal pesan.")
        logger.warning("Forward gagal: Tidak ditemukan asal channel.")
        return

    await message.reply("Pesan diterima, mulai sebar ke grup...")
    logger.info(f"Trigger forward: Pesan dari {message.forward_from_chat.title}")
    
    await trigger_forward(message.forward_from_chat.id, message.forward_from_message_id)

    await message.reply("Forward selesai.")
    logger.info("Forwarding selesai untuk satu pesan.")

async def start_bot():
    await bot.start()
    logger.info("[BOT] Aktif")
    await bot.idle()