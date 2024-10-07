from __future__ import annotations

from datetime import datetime
from pydantic import (
    BaseModel as BaseSchema,
    UUID4,
)


# ! CHATS
class ChatSchema(BaseSchema):
    uuid: UUID4
    name: str
    tokens: int
    project_uuid: UUID4 | None = None


class ChatSaveSchema(ChatSchema):
    pass

class ChatResponseSchema(ChatSaveSchema):
    pass


# ! MESSAGES
class MessageSchema(BaseSchema):
    uuid: UUID4
    role: str
    content: str
    tokens: int
    date: datetime
    chat_uuid: UUID4


class MessagesDeleteSchema(BaseSchema):
    uuids: list[UUID4]


class MessageResponseSchema(MessageSchema):
    pass
