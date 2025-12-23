from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class Text(BaseModel):
    body: str

class ButtonReply(BaseModel):
    id: str
    title: str

class Interactive(BaseModel):
    type: str
    button_reply: Optional[ButtonReply] = None
    
class Message(BaseModel):
    from_: str = Field(..., alias="from")
    id: str
    timestamp: str
    type: str
    text: Optional[Text] = None
    interactive: Optional[Interactive] = None

    model_config = {
        "populate_by_name": True,      
        "extra": "allow",              
        "alias_generator": None,
    }
    from_: str = Field(..., alias="from")


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



# {"object": "whatsapp_business_account", "entry": [{"id": "1356781342363049", "changes": [{"value": {"messaging_product": "whatsapp", "metadata": {"display_phone_number": "15551863822", "phone_number_id": "828587440348208"}, "contacts": [{"profile": {"name": "איטה הקשר"}, "wa_id": "972532229369"}], "messages": [{"from": "972532229369", "id": "wamid.HBgMOTcyNTMyMjI5MzY5FQIAEhggQUNGMDk5ODVGQjhEQjhENDZFRDY2RTM2NTcyOTVGNjQA", "timestamp": "1766428006", "text": {"body": "שלום מה נשמע"}, "type": "text"}]}, "field": "messages"}]}]}
# לחיצת כפתור 
# {"object": "whatsapp_business_account", "entry": [{"id": "1356781342363049", "changes": [{"value": {"messaging_product": "whatsapp", "metadata": {"display_phone_number": "15551863822", "phone_number_id": "828587440348208"}, "contacts": [{"profile": {"name": "איטה הקשר"}, "wa_id": "972532229369"}], "messages": [{"context": {"from": "15551863822", "id": "wamid.HBgMOTcyNTMyMjI5MzY5FQIAERgSNjU2NkU1MTE4NEU5NjJEQTA1AA=="}, "from": "972532229369", "id": "wamid.HBgMOTcyNTMyMjI5MzY5FQIAEhggQUMyNDE0M0YwNzc2OUZBRDY2RUY1OTIyQTUzRDdGOTAA", "timestamp": "1766430219", "type": "interactive", "interactive": {"type": "button_reply", "button_reply": {"id": "MAIN_1", "title": "אפשרות 1"}}}]}, "field": "messages"}]}]}