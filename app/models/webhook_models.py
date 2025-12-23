from pydantic import BaseModel
from typing import List, Optional


class Text(BaseModel):
    body: str


class Message(BaseModel):
    from_: str
    id: str
    timestamp: str
    type: str
    text: Optional[Text] = None

    class Config:
        fields = {"from_": "from"}


class Profile(BaseModel):
    name: str


class Contact(BaseModel):
    wa_id: str
    profile: Profile


class Metadata(BaseModel):
    display_phone_number: str
    phone_number_id: str


class Value(BaseModel):
    messaging_product: str
    metadata: Metadata
    contacts: Optional[List[Contact]] = None
    messages: Optional[List[Message]] = None


class Change(BaseModel):
    field: str
    value: Value


class Entry(BaseModel):
    id: str
    changes: List[Change]


class WebhookPayload(BaseModel):
    object: str
    entry: List[Entry]
