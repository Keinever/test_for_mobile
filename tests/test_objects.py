from http import HTTPStatus

import pytest

from api import (
    ApiClient,
    get_info,
    post_add_action,
    get_user_actions,
    post_replenish_balance,
    get_actions,
    post_sell_action,
    post_auth,
    post_reg
)


class TestApi:
    """
    Тесты для эндпоинтов api
    """

    @pytest.fixture(scope='class')
    def client(self):
        return ApiClient()

    def test_post_auth(self, client):
        response = post_auth(client)
        assert response.status_code == HTTPStatus.OK
