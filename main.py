import asyncio
from bot.handler import start_bot
from userbot.forwarder import start_userbot
from logger import logger

async def main():
    logger.info("[MAIN] Memulai bot dan userbot...")
    await asyncio.gather(
        start_userbot(),
        start_bot(),
    )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logger.exception(f"[FATAL] Terjadi error saat menjalankan: {e}")