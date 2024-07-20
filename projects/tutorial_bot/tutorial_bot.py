import logging
import asyncio

import telegram

logger = logging.getLogger(__name__)

async def main():
    bot = telegram.Bot("7050051633:AAEAnPC0TWt3TchgC0KRPO2TV-_vnbx-jls")
    async with bot:
        # print(await bot.get_me())
        
        # updates = (await bot.get_updates())[0]
        # print(updates)

        await bot.send_message(text='Привет из разработки', chat_id=959473056)


if __name__ == '__main__':
    asyncio.run(main())