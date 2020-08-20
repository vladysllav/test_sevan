from flask_mail import Mail, Message

from .base import BaseTargetBackend


class EmailTargetBackend(BaseTargetBackend):
    target = "email"

    def __init__(self, app):
        self.client = None
        if all(
            (
                app.config.get("MAIL_SERVER"),
                bool(app.config.get("MAIL_USE_TLS"))
                != bool(app.config.get("MAIL_USE_SSL")),
                app.config.get("MAIL_PORT"),
                app.config.get("MAIL_USERNAME"),
                app.config.get("MAIL_PASSWORD"),
                app.config.get("MAIL_DEFAULT_SENDER"),
                app.config.get("MAIL_RECIPIENT"),
            )
        ):
            self.client = Mail(app)
            self.recipient = app.config.get("MAIL_RECIPIENT")

    def redispatch(self, data):
        self.client.send(
            Message(subject="Redispatch", body=data, recipients=[self.recipient])
        )

    def get_target_name(self):
        """Get target name"""
        return f"{self.target} ({self.recipient})"

    def is_ready(self):
        """Backend initialized properly"""
        return self.client is not None
