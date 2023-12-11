from api import routes
import requests

API_URL = "localhost:8080"


def get_info(**kwargs):
    return requests.get(API_URL + routes.Routes.INFO, **kwargs)


def post_add_action(**kwargs):
    return requests.post(API_URL + routes.Routes.ADD_ACTION, **kwargs)


def get_user_actions(**kwargs):
    return requests.get(API_URL + routes.Routes.GET_USER_ACTION, **kwargs)


def post_replenish_balance(**kwargs):
    return requests.post(API_URL + routes.Routes.REPLENISH_BALANCE, **kwargs)


def get_actions(**kwargs):
    return requests.get(API_URL + routes.Routes.GET_ACTIONS, **kwargs)


def post_sell_action(**kwargs):
    return requests.post(API_URL + routes.Routes.SELL_ACTION, **kwargs)


def post_auth(**kwargs):
    return requests.post(API_URL + routes.Routes.AUTH, **kwargs)


def post_reg(**kwargs):
    return requests.post(API_URL + routes.Routes.REG, **kwargs)
