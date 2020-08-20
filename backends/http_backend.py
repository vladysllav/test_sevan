import requests

from .base import BaseTargetBackend


class HTTPTargetBackend(BaseTargetBackend):
    target = "http"

    def __init__(self, app):
        self.url = app.config.get("HTTP_TARGET_ENDPOINT")

    def redispatch(self, data):
        """Redispatch to http endpoint"""
        requests.post(self.url, data)

    def get_target_name(self):
        """Get target name"""
        return f"{self.target} ({self.url})"

    def is_ready(self):
        """Backend initialized properly"""
        return self.url is not None
