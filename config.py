import os

from dotenv import load_dotenv

load_dotenv()

MAIL_SERVER = os.environ.get("MAIL_SERVER", "smtp.gmail.com")
MAIL_USE_TLS = bool(os.environ.get("MAIL_USE_TLS", False))
MAIL_USE_SSL = bool(os.environ.get("MAIL_USE_SSL", True))
MAIL_PORT = os.environ.get("MAIL_PORT", 465)
MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER")
MAIL_RECIPIENT = os.environ.get("MAIL_RECIPIENT")

HTTP_TARGET_ENDPOINT = os.environ.get(
    "HTTP_TARGET_ENDPOINT", "https://postman-echo.com/post"
)
