from pytest_mock import mocker

from backends import get_backends
from backends.email_backend import EmailTargetBackend
from backends.http_backend import HTTPTargetBackend
from tests.tests_base import test_app


def test_get_backends(test_app, mocker):
    mock_email_backend = mocker.patch("backends.EmailTargetBackend")
    mock_email_backend.return_value.is_ready = mocker.Mock(return_value=False)

    mock_http_backend = mocker.patch("backends.HTTPTargetBackend")
    mock_http_backend.return_value.is_ready = mocker.Mock(return_value=False)

    assert get_backends(test_app) == []

    mock_email_backend.assert_called_once_with(test_app)
    mock_email_backend.return_value.is_ready.assert_called_once()

    mock_http_backend.assert_called_once_with(test_app)
    mock_http_backend.return_value.is_ready.assert_called_once()


def test_email_backend(test_app, mocker):
    backend = EmailTargetBackend(test_app)
    assert backend.is_ready()

    mock_send_mail = mocker.patch.object(backend.client, "send")
    mock_message = mocker.patch("backends.email_backend.Message")

    test_data = "test data"
    backend.redispatch(test_data)

    mock_message.assert_called_once_with(
        subject="Redispatch", body=test_data, recipients=[backend.recipient]
    )
    mock_send_mail.assert_called_once()

    assert backend.target in backend.get_target_name()
    assert backend.recipient in backend.get_target_name()


def test_http_backend(test_app, mocker):
    backend = HTTPTargetBackend(test_app)
    assert backend.is_ready()

    mock_post_request = mocker.patch("backends.http_backend.requests.post")

    test_data = "test data"
    backend.redispatch(test_data)

    mock_post_request.assert_called_once_with(backend.url, test_data)

    assert backend.target in backend.get_target_name()
    assert backend.url in backend.get_target_name()
