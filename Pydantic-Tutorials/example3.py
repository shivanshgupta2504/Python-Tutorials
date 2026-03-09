from datetime import datetime, UTC
from functools import partial
from typing import Literal, Annotated
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, ValidationError, EmailStr, HttpUrl, SecretStr, field_validator, model_validator, ValidationInfo, computed_field, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        strict=True,
        extra="allow",
        validate_assignment=True,
    )

    username: Annotated[str, Field(min_length=3, max_length=20)]
    uid: UUID = Field(default_factory=uuid4, alias="id")
    email: EmailStr
    website: HttpUrl | None = None
    password: SecretStr
    age: Annotated[int, Field(ge=13, le=130)]
    first_name: str = ""
    last_name: str = ""
    follower_count: int = 0
    bio: str = ""
    is_active: bool = True

    # Creating a field validator -> Custon validator for attributes
    @field_validator("username")
    @classmethod
    def validate_username(cls, v: str) -> str:
        if not v.replace("_", "").isalnum():
            raise ValueError("Username must be Alphanumeric (underscores allowed)")
        return v.lower()
    
    @field_validator("website", mode="before") # Modifies the value before validation
    @classmethod
    def add_https(cls, v: str | None) -> str | None:
        if v and not v.startswith(("http://", "https://")):
            return f"https://{v}"
        return v
    
    @computed_field
    @property
    def display_name(self) -> str:
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username
    
    @computed_field
    @property
    def is_influencer(self) -> bool:
        return self.follower_count >= 10000

class Comment(BaseModel):
    content: str
    author_email: EmailStr
    likes: int = 0

class BlogPost(BaseModel):
    title: Annotated[str, Field(min_length=1, max_length=200)]
    content: Annotated[str, Field(min_length=10)]
    author: User
    view_count: int = 0
    is_published: bool = False
    tags: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(tz=UTC))
    # created_at: datetime = Field(default_factory=partial(datetime.now, tz=UTC))
    status: Literal["draft", "published", "archived"] = "draft"
    slug: Annotated[str, Field(pattern=r"^[a-z0-9-]+$")]
    comments: list[Comment] = Field(default_factory=list)

class UserRegistration(BaseModel):
    email: EmailStr
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def passwords_match(self) -> "UserRegistration":
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self

# post = BlogPost(
#     title="Getting Started with Python",
#     content="Here's how to begin...",
#     author_id="12345",
# )

# print(post)

### Invalid User
# try:
#     user = User(
#         uid=0,
#         username="cs",
#         email="CoreyMSchafer@gmail.com",
#         age=12,
#     )
# except ValidationError as e:
#     print(e)

### Valid User
# user = User(
#     username="coreyms",
#     email="CoreyMSchafer@gmail.com",
#     age=39,
#     password="secret123",
# )
# print(user)
# print(user.password.get_secret_value())

### BlogPost Dictionary
post_data = {
    "title": "Understanding Pydantic Models",
    "content": "Pydantic makes data validation easy and intuitive...",
    "slug": "understanding-pydantic",
    "author": {
        "username": "coreyms",
        "email": "CoreyMSchafer@gmail.com",
        "age": 39,
        "password": "secret123",
    },
    "comments": [
        {
            "content": "I think I understand nested models now!",
            "author_email": "student@example.com",
            "likes": 25,
        },
        {
            "content": "Can you cover FastAPI next?",
            "author_email": "viewer@example.com",
            "likes": 15,
        },
    ],
}

post = BlogPost(**post_data)

print(post.model_dump_json(indent=2))

