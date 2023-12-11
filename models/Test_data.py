from pydantic import BaseModel


class TestData(BaseModel):
    stonk_name: str = None
    token: str = None
