# Handling Errors
from pydantic import BaseModel, ValidationError

class User(BaseModel):
    username: str
    uid: int
    email: str

try:
    user = User(
        username=None,
        uid=123,
        email=145,
    )
    print(user)
except ValidationError as e:
    print(e)


