import asyncio

from pyrogram import Client

from config import config
from models import Messages, MessagesToSend, MessageToSend
from services.xlsx import OpenSourceXLSXService

app = Client(
    "my_account",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
)


async def main():
    await app.start()

    messages = Messages()

    try:
        async for message in app.get_chat_history(config.CHANNEL_ID):
            await messages.handle(message)
    except KeyboardInterrupt:
        await app.stop()

    print(f"Количество сообщений: {len(messages.messages)}")
    print(f"Количество ошибок: {len(messages.errors)}")

    messages_to_send = MessagesToSend(
        messages=[
            MessageToSend(id=message.id, text=message.text)
            for message in messages.messages
        ]
    )
    # TODO: добавить LLM
    # all_ollama_service = AllOllama(messages_to_send)
    # await all_ollama_service.sort_messages()
    # messages_from_llm = await all_ollama_service.get_messages()
    # print(messages_from_llm)
    messages_from_llm = MessagesToSend(messages=[])
    open_source_xlsx_service = OpenSourceXLSXService(messages, messages_from_llm)
    await open_source_xlsx_service.create_xlsx("messages.xlsx")


if __name__ == "__main__":
    asyncio.run(main())
