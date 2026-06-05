import copy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


default_activities = copy.deepcopy(app_module.activities)


def _reset_activities() -> None:
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(default_activities))


@pytest.fixture
def client():
    _reset_activities()
    with TestClient(app_module.app) as client_instance:
        yield client_instance
    _reset_activities()
