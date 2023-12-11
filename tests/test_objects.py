import random
from http import HTTPStatus
import pytest

from models import User, TestData, Action, Actions

from api import (
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
    def test_user(self):
        return User()

    @pytest.fixture(scope='class')
    def test_data(self):
        return TestData()

    @pytest.fixture(scope='class')
    def test_actions(self):
        return Actions()

    def test_post_reg_and_post_auth(self, test_user, test_data):
        response = post_reg(json={
            "username": test_user.username,
            "firstname": test_user.firstname,
            "lastname": test_user.lastname,
            "email": test_user.email,
            "password": test_user.password,
            "confirm_password": test_user.confirm_password
        })
        assert response.status_code == HTTPStatus.OK
        response = post_auth(json={"username": test_user.username, "password": test_user.password})
        assert response.status_code == HTTPStatus.OK
        test_data.token = response.json().get("token")

    def test_get_info(self, test_user, test_data):
        if not test_data.token:
            self.test_post_reg_and_post_auth(test_user, test_data)
        response = get_info(headers={"Authorization": f"Bearer {test_data.token}"})
        assert response.status_code == HTTPStatus.OK

    def test_get_actions(self, test_actions):
        response = get_actions()
        data = response.json()
        test_actions.list_of_actions = [Action(name=item.get("name")) for item in data]
        assert response.status_code == HTTPStatus.OK

    def test_get_user_actions(self, test_user, test_data):
        if not test_data.token:
            self.test_post_reg_and_post_auth(test_user, test_data)
        response = get_user_actions(headers={"Authorization": f"Bearer {test_data.token}"})
        assert response.status_code == HTTPStatus.OK

    def test_post_replenish_balance(self, test_user, test_data):
        if not test_data.token:
            self.test_post_reg_and_post_auth(test_user, test_data)
        response = get_user_actions(headers={"Authorization": f"Bearer {test_data.token}"}, json={"money": 1000000000})
        assert response.status_code == HTTPStatus.OK

    def test_post_buy_action(self, test_user, test_data, test_actions):
        if not test_data.token:
            self.test_post_reg_and_post_auth(test_user, test_data)
        if not test_actions.list_of_actions:
            self.test_get_actions(test_actions)
        stock_name = random.choice(test_actions.list_of_actions).name
        response = post_add_action(
            headers={"Authorization": f"Bearer {test_data.token}"},
            json={"name": stock_name}
        )
        assert response.status_code == HTTPStatus.OK
        test_data.stonk_name = stock_name

    def test_post_sell_action(self, test_user, test_data, test_actions):
        if not test_data.token:
            self.test_post_reg_and_post_auth(test_user, test_data)
        if not test_actions.list_of_actions:
            self.test_get_actions(test_actions)
        if not test_data.stonk_name:
            self.test_post_buy_action(test_user, test_data, test_actions)
        response = post_add_action(
            headers={"Authorization": f"Bearer {test_data.token}"},
            json={"name": test_data.stonk_name}
        )
        assert response.status_code == HTTPStatus.OK
        test_data.stonk_name = None


