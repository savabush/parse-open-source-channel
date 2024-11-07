from openpyxl import Workbook

from models import Messages, MessagesToSend


class OpenSourceXLSXService:
    def __init__(self, messages: Messages, messages_from_llm: MessagesToSend):
        self.messages = messages
        self.messages_from_llm = messages_from_llm

    async def create_xlsx(self, filename: str):
        wb = Workbook()
        ws_messages = wb.active
        ws_messages.title = "Messages"
        ws_errors = wb.create_sheet("Errors")

        # Set header row for messages worksheet
        ws_messages["A1"] = "ID"
        ws_messages["B1"] = "Name"
        ws_messages["C1"] = "Text"
        ws_messages["D1"] = "Links"
        ws_messages["E1"] = "Likes Count"
        ws_messages["F1"] = "Dislikes Count"
        ws_messages["G1"] = "Ratio"
        ws_messages["H1"] = "Date Created"
        ws_messages["I1"] = "Date Updated"

        # Set header row for errors worksheet
        ws_errors["A1"] = "Message ID"

        # Iterate over messages and write data to rows
        row_num = 2
        for message in self.messages.messages:
            ws_messages[f"A{row_num}"] = message.id
            ws_messages[f"B{row_num}"] = message.name
            ws_messages[f"C{row_num}"] = message.text
            ws_messages[f"D{row_num}"] = ", ".join(message.links)
            ws_messages[f"E{row_num}"] = message.likes_count
            ws_messages[f"F{row_num}"] = message.dislikes_count
            ws_messages[f"G{row_num}"] = message.ratio
            ws_messages[f"H{row_num}"] = message.date_created
            ws_messages[f"I{row_num}"] = message.date_updated
            row_num += 1

        # Iterate over errors and write data to rows
        error_row_num = 2
        for message_id in self.messages.errors:
            ws_errors[f"A{error_row_num}"] = message_id
            error_row_num += 1

        # Save workbook to file
        wb.save(filename)
