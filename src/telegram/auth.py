import secrets

from config import BOTFATHER_USER_ID, BOTFATHER_WEBHOOK_SECRET


def get_request_user_id(request_body: dict) -> int:
    return request_body['message']['chat']['id']

def verify_user_id(user_id: int) -> bool:
    return user_id == BOTFATHER_USER_ID

def authenticate_user_id(request_body: dict) -> bool:
    user_id = get_request_user_id(request_body=request_body)
    return verify_user_id(user_id=user_id)

def get_request_header_secret(request_header: dict) -> str:
    return str(request_header.get('x-telegram-bot-api-secret-token'))

def verify_header_secret(header_secret: str) -> bool:
    return secrets.compare_digest(header_secret, BOTFATHER_WEBHOOK_SECRET)

def authenticate_header_secret(request_header: dict) -> bool:
    header_secret = get_request_header_secret(request_header=request_header)
    return verify_header_secret(header_secret=header_secret)
