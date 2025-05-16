import asyncio
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID
from userbot.forwarder import trigger_forward
from logger import logger

# Inisialisasi bot
bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Debug handler untuk log semua pesan masuk
@bot.on_message()
async def debug_all(client, message):
    from_user = message.from_user.id if message.from_user else "N/A"
    logger.info(f"[DEBUG] Menerima pesan dari: {from_user}, forward: {bool(message.forward_from_chat)}")

# Handler untuk pesan private dari owner
@bot.on_message(filters.private & filters.user(OWNER_ID))
async def handle_any_msg(client, message):
    logger.info(f"[OWNER] Menerima pesan dari owner: {message.text or 'non-text'}")

    if message.forward_from_chat:
        logger.info(f"[FORWARD] Detected forward from: {message.forward_from_chat.title}")
        await message.reply("Pesan diterima, mulai sebar ke grup...")

        await trigger_forward(message.forward_from_chat.id, message.forward_from_message_id)

        await message.reply("Forward selesai.")
        logger.info("[FORWARD] Forwarding selesai untuk satu pesan.")
    else:
        logger.warning("[FORWARD] Tidak ada asal channel terdeteksi.")
        await message.reply("Ini bukan pesan yang diforward dari channel.")

# Fungsi untuk menjalankan bot
async def start_bot():
    await bot.start()
    logger.info("[BOT] Aktif")
    logger.info("[BOT] Masuk idle")
    await asyncio.Event().wait()