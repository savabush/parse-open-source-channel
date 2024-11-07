import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = str(os.environ.get("API_HASH"))
    BOT_TOKEN = os.environ.get("BOT_TOKEN")

    CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))


class Prompts:
    FORMAT_MESSAGE = """
        [
            {"id": 123, "text": "Текст 1"},
            {"id": 456, "text": "Текст 2"},
            ...
        ]
    """
    FORMAT_OUTPUT = """
        [
            {"id": 123},
            {"id": 456},
            ...
        ]
    """
    PROMPT = "Я {}. Сейчас я отправлю тебе датасет с инофрмацией о разных проектах для разных IT специальностей в таком формате: \n{}\n\nПожалуйста, отсортируй его в порядке убывания по полезности для меня. \n\n Отправь мне только этот список cостоящий из id в формате json в формате \n\n{}\n\n. Твоя задача - просто отсортировать. Ценность каждого объекта ты выбираешь сам, в зависимости от своей роли. Вот сам датасет:\n\n{}"

    SYSTEM_PROMPT = "Ты {}, являющийся экспертом в этой области"


config = Config()
