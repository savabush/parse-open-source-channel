import json

from ollama import AsyncClient

from config import Prompts
from models import MessagesToSend


class BaseOllama:
    ME_AS = ""
    OLLAMA_AS = ""

    def __init__(self, messages: MessagesToSend):
        self._prompt = Prompts.PROMPT.format(
            self.ME_AS,
            Prompts.FORMAT_MESSAGE,
            Prompts.FORMAT_OUTPUT,
            messages.to_dict(),
        )
        self.messages = messages
        self.sorted_messages = None

    def get_prompt(self):
        return self._prompt

    def get_system_prompt(self):
        return Prompts.SYSTEM_PROMPT.format(self.OLLAMA_AS)

    async def sort_messages(self):
        # system_message = {"role": "system", "content": self.get_system_prompt()}
        message = {"role": "user", "content": self.get_prompt()}
        # assistant_message = {
        #     "role": "assistant",
        #     "content": config.Prompts.FORMAT_OUTPUT,
        # }
        response = ""
        async for part in await AsyncClient().chat(
            model="llama3.1",
            messages=[message],
            stream=True,
            format="json",
            options={"temperature": 0.40},
        ):
            part = part["message"]["content"]
            print(part, end="", flush=True)
            response += part
        try:
            response = json.loads(response)
        except json.decoder.JSONDecodeError:
            print(f"Неправильный ответ от LLM: {response}")
        self.sorted_messages = response
        # self.sorted_messages = data


class BackendDeveloperOllama(BaseOllama):
    ME_AS = "Backend Developer"
    OLLAMA_AS = "Профессионал в бэкенд-разработке"


class ArchitectorOllama(BaseOllama):
    ME_AS = "Архитектор ПО"
    OLLAMA_AS = "Профессионал в архитектуре ПО"


class DesignerOllama(BaseOllama):
    ME_AS = "Веб-дизайнер"
    OLLAMA_AS = "Профессионал в веб-дизайне"


class FrontendDeveloperOllama(BaseOllama):
    ME_AS = "Frontend Developer"
    OLLAMA_AS = "Профессионал в frontend-разработке"


class FullstackDeveloperOllama(BaseOllama):
    ME_AS = "Fullstack Developer"
    OLLAMA_AS = "Профессионал в fullstack-разработке"


class MLDeveloperOllama(BaseOllama):
    ME_AS = "ML Developer"
    OLLAMA_AS = "Профессионал в машинном обучении"


class AllOllama:
    def __init__(self, messages: MessagesToSend):
        self.backend_developer = BackendDeveloperOllama(messages)
        self.architector = ArchitectorOllama(messages)
        self.designer = DesignerOllama(messages)
        self.frontend_developer = FrontendDeveloperOllama(messages)
        self.fullstack_developer = FullstackDeveloperOllama(messages)
        self.ml_developer = MLDeveloperOllama(messages)

    async def sort_messages(self):
        await self.backend_developer.sort_messages()
        await self.architector.sort_messages()
        await self.designer.sort_messages()
        await self.frontend_developer.sort_messages()
        await self.fullstack_developer.sort_messages()
        await self.ml_developer.sort_messages()

    async def get_messages(self):
        return {
            self.backend_developer.ME_AS: self.backend_developer.sorted_messages,
            self.architector.ME_AS: self.architector.sorted_messages,
            self.designer.ME_AS: self.designer.sorted_messages,
            self.frontend_developer.ME_AS: self.frontend_developer.sorted_messages,
            self.fullstack_developer.ME_AS: self.fullstack_developer.sorted_messages,
            self.ml_developer.ME_AS: self.ml_developer.sorted_messages,
        }
