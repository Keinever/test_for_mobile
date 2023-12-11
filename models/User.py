from pydantic import BaseModel
from utils import generate_random_string


class User(BaseModel):
    username: str = generate_random_string(8)
    firstname: str = "test"
    lastname: str = "test"
    email: str = generate_random_string(8) + "@mail.ru"
    password: str = "test"
    confirm_password: str = "test"
