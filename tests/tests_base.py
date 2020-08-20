import pytest
from flask import Flask


@pytest.fixture(scope="module")
def test_app():
    app = Flask(__name__)
    app.config.from_object("tests.test_config")

    return app


@pytest.fixture(scope="module")
def test_client():
    from server import app

    app.config.from_object("tests.test_config")
    testing_client = app.test_client()

    ctx = app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()
