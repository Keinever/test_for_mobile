from api import routes


def get_info(client, ):
    return client.get(routes.Routes.INFO, params={})


def post_add_action(client, **kwargs):
    return client.post(routes.Routes.ADD_ACTION, **kwargs)


def get_user_actions(client, ):
    return client.get(routes.Routes.GET_USER_ACTION, params={})


def post_replenish_balance(client, **kwargs):
    return client.post(routes.Routes.REPLENISH_BALANCE, **kwargs)


def get_actions(client, ):
    return client.get(routes.Routes.GET_ACTIONS, params={})


def post_sell_action(client, **kwargs):
    return client.post(routes.Routes.SELL_ACTION, **kwargs)


def post_auth(client, **kwargs):
    return client.post(routes.Routes.AUTH, **kwargs)


def post_reg(client, **kwargs):
    return client.post(routes.Routes.REG, **kwargs)


def get_objects(client, *ids):
    return client.get(routes.Routes.OBJECTS, params={'id': ids} if ids else None)
