from dataclasses import dataclass

from pyrogram.types import Message
from urlextract import URLExtract

# Test object message
# Message: {
#     "_": "Message",
#     "id": 2323,
#     "sender_chat": {
#         "_": "Chat",
#         "id": -1001289166992,
#         "type": "ChatType.CHANNEL",
#         "is_verified": false,
#         "is_restricted": false,
#         "is_creator": false,
#         "is_scam": false,
#         "is_fake": false,
#         "title": "Open Source",
#         "username": "open_source_friend",
#         "photo": {
#             "_": "ChatPhoto",
#             "small_file_id": "AQADAgADf68xGzs70UgAEAIAA3DPg94W____-dWVZvYx79gABB4E",
#             "small_photo_unique_id": "AgADf68xGzs70Ug",
#             "big_file_id": "AQADAgADf68xGzs70UgAEAMAA3DPg94W____-dWVZvYx79gABB4E",
#             "big_photo_unique_id": "AgADf68xGzs70Ug"
#         },
#         "dc_id": 2,
#         "has_protected_content": false
#     },
#     "date": "2023-04-25 16:43:50",
#     "chat": {
#         "_": "Chat",
#         "id": -1001289166992,
#         "type": "ChatType.CHANNEL",
#         "is_verified": false,
#         "is_restricted": false,
#         "is_creator": false,
#         "is_scam": false,
#         "is_fake": false,
#         "title": "Open Source",
#         "username": "open_source_friend",
#         "photo": {
#             "_": "ChatPhoto",
#             "small_file_id": "AQADAgADf68xGzs70UgAEAIAA3DPg94W____-dWVZvYx79gABB4E",
#             "small_photo_unique_id": "AgADf68xGzs70Ug",
#             "big_file_id": "AQADAgADf68xGzs70UgAEAMAA3DPg94W____-dWVZvYx79gABB4E",
#             "big_photo_unique_id": "AgADf68xGzs70Ug"
#         },
#         "dc_id": 2,
#         "has_protected_content": false
#     },
#     "mentioned": false,
#     "scheduled": false,
#     "from_scheduled": false,
#     "media": "MessageMediaType.VIDEO",
#     "edit_date": "2024-07-11 17:38:39",
#     "has_protected_content": false,
#     "has_media_spoiler": false,
#     "caption_entities": [
#         {
#             "_": "MessageEntity",
#             "type": "MessageEntityType.BOLD",
#             "offset": 0,
#             "length": 12
#         },
#         {
#             "_": "MessageEntity",
#             "type": "MessageEntityType.TEXT_LINK",
#             "offset": 91,
#             "length": 1,
#             "url": "https://t.me/open_source_friend"
#         },
#         {
#             "_": "MessageEntity",
#             "type": "MessageEntityType.TEXT_LINK",
#             "offset": 200,
#             "length": 1,
#             "url": "https://t.me/open_source_friend"
#         },
#         {
#             "_": "MessageEntity",
#             "type": "MessageEntityType.TEXT_LINK",
#             "offset": 266,
#             "length": 1,
#             "url": "https://t.me/open_source_friend"
#         },
#         {
#             "_": "MessageEntity",
#             "type": "MessageEntityType.TEXT_LINK",
#             "offset": 296,
#             "length": 1,
#             "url": "https://t.me/open_source_friend"
#         },
#         {
#             "_": "MessageEntity",
#             "type": "MessageEntityType.TEXT_LINK",
#             "offset": 381,
#             "length": 1,
#             "url": "https://t.me/open_source_friend"
#         },
#         {
#             "_": "MessageEntity",
#             "type": "MessageEntityType.URL",
#             "offset": 384,
#             "length": 37
#         }
#     ],
#     "video": {
#         "_": "Video",
#         "file_id": "BAACAgIAAx0CTNcgkAACCRNnK-q2PStsbuUxLZnHp2I-Rs1nCQACaCkAA_ZASk2eS28HTfnaHgQ",
#         "file_unique_id": "AgADaCkAA_ZASg",
#         "width": 1280,
#         "height": 720,
#         "duration": 156,
#         "file_name": "PentestGPT.mp4",
#         "mime_type": "video/mp4",
#         "file_size": 9570312,
#         "supports_streaming": true,
#         "date": "2023-04-25 16:43:42",
#         "thumbs": [
#             {
#                 "_": "Thumbnail",
#                 "file_id": "AAMCAgADHQJM1yCQAAIJE2cr6rY9K2xu5TEtmcenYj5GzWcJAAJoKQAD9kBKTZ5LbwdN-doACAEAB20ABx4E",
#                 "file_unique_id": "AgADaCkAA_ZASg",
#                 "width": 320,
#                 "height": 180,
#                 "file_size": 1166
#             }
#         ]
#     },
#     "caption": "PentestGPT\n\nPentestGPT — это инструмент для тестирования на проникновение на основе ChatGPT.\n\nОн предназначен для автоматизации процесса тестирования на проникновение и работает в интерактивном режиме, чтобы направлять тестеров на проникновение как в общем прогрессе, так и в конкретных операциях.\n\nPentestGPT способен решать простые и средние машины HackTheBox и другие задачи CTF.\n\nhttps://github.com/GreyDGL/PentestGPT",
#     "views": 22590,
#     "forwards": 979,
#     "outgoing": false,
#     "reply_markup": {
#         "_": "InlineKeyboardMarkup",
#         "inline_keyboard": [
#             [
#                 {
#                     "_": "InlineKeyboardButton",
#                     "text": "👍🏻 178",
#                     "callback_data": "send_reaction_0"
#                 },
#                 {
#                     "_": "InlineKeyboardButton",
#                     "text": "👎🏻 14",
#                     "callback_data": "send_reaction_1"
#                 }
#             ]
#         ]
#     }
# }
#


@dataclass
class MessageOpenSource:
    id: int
    name: str
    text: str
    links: list[str]
    likes_count: int
    dislikes_count: int
    ratio: float
    date_created: str
    date_updated: str


@dataclass
class MessageToSend:
    id: int
    text: str

    def to_dict(self):
        return {"id": self.id, "text": self.text}


@dataclass
class MessagesToSend:
    messages: list[MessageToSend]

    def to_dict(self):
        return [message.to_dict() for message in self.messages]


class Messages:
    def __init__(self):
        self.extractor_urls = URLExtract()
        self.messages: list[MessageOpenSource] = []
        self.errors: set[int] = set()

    async def add(self, message: MessageOpenSource):
        print(f"Added {message.name} {message.id}")
        self.messages.append(message)

    def get_ten_messages(self):
        return self.messages[:10]

    def get_errors(self):
        return self.errors

    async def handle(self, message: Message):
        try:
            likes_count = (
                int(message.reply_markup.inline_keyboard[0][0].text.split(" ")[1])
                if message.reply_markup
                else 0
            )
            dislikes_count = (
                int(message.reply_markup.inline_keyboard[0][1].text.split(" ")[1])
                if message.reply_markup
                else 0
            )
        except IndexError as e:
            print(f"Ошибка взятия количества лайков и дизлайков: {e}")
            self.errors.add(message.id)
            likes_count = 0
            dislikes_count = 0

        caption = message.caption
        if not caption:
            print(f"Caption is empty for {message.id}")
            self.errors.add(message.id)
            return
        message_open_source = MessageOpenSource(
            id=message.id,
            name=caption.split("\n\n")[0],
            text=caption.split("\n\n")[1],
            links=self.extractor_urls.find_urls(message.caption),
            likes_count=likes_count,
            dislikes_count=dislikes_count,
            ratio=likes_count / dislikes_count if dislikes_count else 0,
            date_created=message.date.strftime("%Y-%m-%d %H:%M:%S"),
            date_updated=message.edit_date.strftime("%Y-%m-%d %H:%M:%S")
            if message.edit_date
            else "",
        )

        await self.add(message_open_source)
