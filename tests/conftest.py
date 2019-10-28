import pytest

from price_searcher_app.flask_app import create_app
from price_searcher_app import setup


@pytest.fixture
def mock_load_data_sources(mocker):
    yield mocker.patch.object(setup, 'load_data_sources')


@pytest.fixture
def flask_app(mock_load_data_sources):
    app = create_app()
    app.debug = True
    yield app
