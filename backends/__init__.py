from .email_backend import EmailTargetBackend
from .http_backend import HTTPTargetBackend


def get_backends(app):
    """Initialize and return backends if they have been configured"""
    # Passing config would be better, but flask mail required the app object
    # At least this way backends are decoupled from everything else
    return [
        backend
        for backend in (EmailTargetBackend(app), HTTPTargetBackend(app))
        if backend.is_ready()
    ]
