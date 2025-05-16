import asyncio
from bot.handler import start_bot
from userbot.forwarder import start_userbot

async def main():
    await asyncio.gather(
        start_userbot(),
        start_bot(),
    )

if __name__ == "__main__":
    asyncio.run(main())