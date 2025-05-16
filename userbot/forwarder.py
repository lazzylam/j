import asyncio
from telethon import TelegramClient
from config import API_ID, API_HASH, FORWARD_DELAY
from logger import logger

userbot = TelegramClient("userbot", API_ID, API_HASH)

async def trigger_forward(from_chat_id, message_id):
    logger.info("Mengambil daftar grup...")
    groups = [dialog async for dialog in userbot.iter_dialogs() if dialog.is_group]

    batch_size = 5
    for i in range(0, len(groups), batch_size):
        batch = groups[i:i + batch_size]
        tasks = [forward_to_group(dialog, from_chat_id, message_id) for dialog in batch]

        await asyncio.gather(*tasks)

        if i + batch_size < len(groups):
            logger.info(f"Menunggu {FORWARD_DELAY} detik sebelum batch berikutnya...")
            await asyncio.sleep(FORWARD_DELAY)

    logger.info("Forward selesai.")

async def forward_to_group(dialog, from_chat_id, message_id):
    try:
        await userbot.forward_messages(
            entity=dialog.id,
            messages=message_id,
            from_peer=from_chat_id
        )
        logger.info(f"[FORWARD] Berhasil ke {dialog.name}")
    except Exception as e:
        logger.error(f"[ERROR] Gagal ke {dialog.name}: {e}")

async def start_userbot():
    await userbot.start()
    logger.info("[USERBOT] Aktif")