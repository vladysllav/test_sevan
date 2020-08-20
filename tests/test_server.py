from pytest_mock import mocker

from tests.tests_base import test_client


def test_server(test_client, mocker):
    mock_get_backends = mocker.patch("server.get_backends")
    mock_get_backends.return_value = [
        mocker.Mock(get_target_name=mocker.Mock(return_value="email")),
        mocker.Mock(get_target_name=mocker.Mock(return_value="http")),
    ]

    test_data = "test data"
    res = test_client.post("/redispatch/", data=test_data)
    assert res.status_code == 200
    assert "email" in res.json
    assert "http" in res.json

    for mock_backend in mock_get_backends.return_value:
        mock_backend.redispatch.assert_called_once_with(test_data.encode())
        mock_backend.get_target_name.assert_called_once()
