import json
import redis
from typing import Dict, Any

# התחברות ל-Redis
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def set_user_state(user_id: str, state: Dict[str, Any]):
    """שמור את מצב המשתמש ב-Redis"""
    r.set(user_id, json.dumps(state))

def get_user_state(user_id: str) -> Dict[str, Any]:
    """קרא את מצב המשתמש מ-Redis"""
    state = r.get(user_id)
    if state:
        return json.loads(state)
    return {}

def delete_user_state(user_id: str):
    """מחק מצב משתמש"""
    r.delete(user_id)
