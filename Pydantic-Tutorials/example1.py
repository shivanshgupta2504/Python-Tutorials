from pydantic import BaseModel

class User(BaseModel):
    # Attribute with non-default values are required
    username: str
    uid: int
    email: str

    full_name: str | None = None
    bio: str = ""
    is_active: bool = True

user = User(username="Shivansh", uid=1234567890, email="[EMAIL_ADDRESS]")
print(user)
print(user.model_dump()) # Python dictionary
print(user.model_dump_json(indent=2)) # JSON string

# Accessing Attributes
print(user.username)

# All Attribute values are mutable unless configured
user.username = 123
print(user.username)