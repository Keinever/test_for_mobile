from pydantic import BaseModel


class Action(BaseModel):
    name: str


class Actions(BaseModel):
    list_of_actions: list[Action] = []
