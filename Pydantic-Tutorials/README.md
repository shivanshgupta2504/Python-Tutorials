# Pydantic Tutorials

Welcome to the Pydantic tutorials! This directory contains code examples and explanations to help you master **Pydantic**, a powerful data validation and settings management library in Python that utilizes Python type annotations.

## What is Pydantic?

**Pydantic** enforces type hints at runtime, providing user-friendly errors when data is invalid. It is widely used in modern Python frameworks like FastAPI and for general data validation, parsing, and serialization tasks.

Key features of Pydantic:
- **Type Validation**: Validates that data matches the defined Python type annotations.
- **Data Parsing**: Automatically converts data to the correct type when safely possible (e.g., parsing a string `"123"` to an integer `123`).
- **Clear Errors**: Generates highly informative and structured error messages when validation fails.
- **JSON Serialization**: Easily convert Pydantic models to and from JSON (dictionaries).
- **Custom Validators**: Apply complex validation rules logic that stretches far beyond simple type checks.

---

## Best Practices

1. **Use `BaseModel` for Data Structures**: Inherit from `pydantic.BaseModel` to create your data classes. It automatically acts as the engine for your validation and serialization.
2. **Leverage Type Hints**: Use Python's standard `typing` module (`list`, `dict`, `Literal`) to describe your data accurately.
3. **Use `Annotated` and `Field` for Constraints**: Use `typing.Annotated` along with `pydantic.Field` to enforce constraints like `min_length`, `max_length`, `ge` (greater than or equal to), and `le` (less than or equal to). This keeps your type signatures clean.
4. **Prefer Custom Validators for Complex Logic**: Use `@field_validator` and `@model_validator` instead of writing validation code randomly scattered throughout your application. This guarantees the checks run automatically during every model instantiation.
5. **Use Specific Types for Specialized Data**: Pydantic provides specialized types like `EmailStr`, `HttpUrl`, `UUID`, and `SecretStr` for strict, complex validation immediately out-of-the-box.
6. **Alias and Populate by Name**: Use the `alias` parameter in `Field` to handle cases where incoming data has a different naming convention (e.g., handling `"id"` in JSON but mapping it to `"uid"` in the model). Configure `populate_by_name=True` to allow your application to flexibly accept either name.
7. **Protect Sensitive Data**: Always handle passwords, keys, and tokens with `SecretStr` to prevent accidental logging or exposure in standard print statements or server logs.

---

## Code Examples

### Example 1: Basic Model and Serialization (`example1.py`)

This example demonstrates how to create a simple model, instantiate it, and export the data.

```python
from pydantic import BaseModel

class User(BaseModel):
    # Attributes with no default values are strictly required
    username: str
    uid: int
    email: str

    full_name: str | None = None
    bio: str = ""
    is_active: bool = True

user = User(username="Shivansh", uid=1234567890, email="test@example.com")

print(user)
print(user.model_dump()) # Exports a Python dictionary
print(user.model_dump_json(indent=2)) # Exports a JSON string

# Accessing Attributes
print(user.username)

# All Attribute values are mutable unless defined otherwise in model_config
user.username = 123
print(user.username)
```

**Key Points & Method Parameters:**
- **`BaseModel`**: The core class to inherit from when creating Pydantic models.
- **Required vs Optional Fields**: `username`, `uid`, and `email` are required because they lack a default value. `full_name`, `bio`, and `is_active` are optional.
- **`model_dump()`**: Serializes the model into a standard Python dictionary mappings.
- **`model_dump_json(indent=2)`**: Serializes the model into a JSON-formatted string. `indent=2` is an argument that specifies the indentation level for readable, pretty-printing of the JSON output.

---

### Example 2: Handling Validation Errors (`example2.py`)

This example shows how Pydantic handles fundamentally invalid incoming data and how to catch the errors correctly.

```python
from pydantic import BaseModel, ValidationError

class User(BaseModel):
    username: str
    uid: int
    email: str

try:
    user = User(
        username=None, # Invalid type, expects a string
        uid=123,
        email=145, # Invalid type, expects a string
    )
    print(user)
except ValidationError as e:
    print(e)
```

**Key Points:**
- Data type coercion only works if it's safe and standard. Sometimes values fundamentally violate the required type (e.g. `None` instead of `str`).
- **`ValidationError`**: Pydantic throws this standard exception when model instantiation fails due to bad data. Catching it in a try-except block gives you access to a rich object containing detailed information on exactly *which* fields failed and *why*.

---

### Example 3: Advanced Validations, Fields, and Nested Models (`example3.py`)

This example dives into complex real-world use cases involving constraints, custom types, multiple validators, computed fields, and model configuration.

```python
from datetime import datetime, UTC
from typing import Literal, Annotated
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, ValidationError, EmailStr, HttpUrl, SecretStr, field_validator, model_validator, computed_field, ConfigDict

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

    @field_validator("username")
    @classmethod
    def validate_username(cls, v: str) -> str:
        if not v.replace("_", "").isalnum():
            raise ValueError("Username must be Alphanumeric (underscores allowed)")
        return v.lower()
    
    @field_validator("website", mode="before")
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
```

**Key Features & Method Parameter Meanings:**

- **`ConfigDict` (`model_config`)**: Configuration dictionary to fine-tune a model's underlying rules.
  - `populate_by_name=True`: Allows creating the model using either the field's real code name (`uid`) or its alias string (`id`).
  - `strict=True`: Prevents automatic type coercion (e.g., throwing a validation error if `"123"` is provided for an `int` instead of silently converting it).
  - `extra="allow"`: Allows extra, unknown attributes not defined in the original model to be attached to the instance without failing validation.
  - `validate_assignment=True`: Ensures validation logically runs again anytime you assign a new value to an attribute *after* it's already instantiated.

- **`Field(...)`**: Specifically customizes field validations and structural metadata.
  - `min_length`/`max_length`: Enforces strict character limit bounds on strings.
  - `ge`/`le`: Enforces numeric minimum (`ge`: "greater than or equal to") and maximum (`le`: "less than or equal to") bounds.
  - `default_factory`: Uses a callable function (like `uuid4` or `list`) to dynamically generate fresh default values at the exact time of instantiation, instead of sharing a mutated default list among instances.
  - `alias`: Defines an alternative external name for initialization and serialization (widely used for reading external JSON containing keys like `id` which you want intuitively named `uid` natively).

- **Specialized Complex Types**:
  - `EmailStr`: Strictly validates whether a string matches a correct email pattern.
  - `HttpUrl`: Validates fully formed URLs.
  - `SecretStr`: Avoids passwords being logged, exposed, or printed directly in cleartext. You must explicitly call `.get_secret_value()` to extract the raw string.

- **`@field_validator("field_name", mode="...")`**: Custom function to independently validate a specific field.
  - `mode="before"`: Modifies logic to run the function *before* Pydantic performs its default rigid type checking. Extremely useful for quick data cleanup (e.g., prepending `https://` if it was forgotten).
  - Normal validator functions check logic and intentionally raise a standard `ValueError` to feed back bad data states to the overall validation engine.

- **`@computed_field`**: Enables you to quickly wrap dynamic `@property` functions to expose them as pseudo-fields, meaning they get seamlessly bundled into JSON serialization output via `model_dump()`.

- **`@model_validator(mode="after")`**: Enforces system validation checking the entire model context as a cohesive whole.
  - `mode="after"` means it runs only after all individual fields have already passed validation. It's often required when complex business logic depends on dynamically checking *multiple* fields interactively against each other (e.g., verifying a `password` perfectly matches a `confirm_password` during a `UserRegistration`).

- **Nested Models Architecture**: Using `BlogPost` cleanly includes another model `User` cleanly as its internal `author` attribute, and features a `list` iteratively filled with inner `Comment` models. Pydantic handles the complex burden of nested recursive JSON parsing entirely behind the scenes structure data beautifully and deeply into your Python objects layer by layer.

---

## Core Concepts in Depth

To master Pydantic, it's crucial to understand how data flows in (Deserialization) and out (Serialization), as well as how to enforce custom rules at the specific field level vs the model level.

### 1. Deserialization (Input Parsing)

Deserialization is the process of taking raw data (like JSON strings, dictionaries, or keyword arguments) and parsing it into a validated Pydantic model instance.

```python
from pydantic import BaseModel, ValidationError

class Product(BaseModel):
    id: int
    name: str
    price: float

# Method A: Using Keyword Arguments (Standard)
p1 = Product(id=1, name="Laptop", price=999.99)

# Method B: Using Unpacking (From a Dictionary)
data_dict = {"id": 2, "name": "Mouse", "price": "49.50"} # price is string, but parsed to float
p2 = Product(**data_dict)

# Method C: Using model_validate (Better for validating dicts directly)
p3 = Product.model_validate({"id": 3, "name": "Keyboard", "price": 100})

# Method D: Using model_validate_json (Directly from a JSON string)
json_data = '{"id": 4, "name": "Monitor", "price": 250.0}'
p4 = Product.model_validate_json(json_data)

print(p1, p2, p3, p4, sep="\n")
```

### 2. Serialization (Output Formatting)

Serialization is the process of converting your Pydantic model back into standard Python data types (like dictionaries) or JSON strings for APIs and storage.

```python
from pydantic import BaseModel, Field

class Employee(BaseModel):
    emp_id: int = Field(alias="id")
    name: str
    salary: float
    password: str = Field(exclude=True) # Exclude from serialization by default

employee = Employee(id=101, name="Alice", salary=85000.0, password="supersecret")

# 1. model_dump(): Returns a Python Dictionary
print(employee.model_dump())
# Output: {'emp_id': 101, 'name': 'Alice', 'salary': 85000.0}
# Notice 'password' is excluded!

# 2. Customizing Output (Include/Exclude overriding)
print(employee.model_dump(include={'name', 'salary'}))
# Output: {'name': 'Alice', 'salary': 85000.0}

# 3. Serializing with Aliases
print(employee.model_dump(by_alias=True))
# Output: {'id': 101, 'name': 'Alice', 'salary': 85000.0}

# 4. model_dump_json(): Returns a JSON string
print(employee.model_dump_json(indent=2))
```

### 3. Field Validation

Field validators run *per field* when the model is instantiated. They can cleanly format data or reject it based on custom rules.

```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    email: str
    role: str
    
    # 1. mode="before" - Runs BEFORE Pydantic attempts standard type matching
    @field_validator('role', mode='before')
    @classmethod
    def default_to_user(cls, v):
        if v is None or v == "":
            return "user"
        return v.lower()
        
    # 2. mode="after" (default) - Runs AFTER Pydantic has validated the type
    @field_validator('email')
    @classmethod
    def validate_email_domain(cls, v):
        if not v.endswith("@company.com"):
            raise ValueError("Only company emails are allowed")
        return v

user1 = User(email="john@company.com", role="ADMIN")
print(user1.role) # Output: admin

# Will raise ValueError
# User(email="john@gmail.com", role="user")
```

### 4. Model Validation

Model validators validate the entire object at once. Use them when the validity of one field depends on the value of another field.

```python
from pydantic import BaseModel, model_validator

class Event(BaseModel):
    start_date: str
    end_date: str
    
    @model_validator(mode='after')
    def check_dates(self) -> 'Event':
        # Now we have access to the entire validated object
        if self.end_date < self.start_date:
            raise ValueError("end_date cannot be before start_date")
        return self

# Valid
e1 = Event(start_date="2026-01-01", end_date="2026-01-10")

# Raises ValidationError
# e2 = Event(start_date="2026-01-10", end_date="2026-01-01")
```

### 5. Settings Management (Extra Concept)

Pydantic's `BaseSettings` (via the `pydantic-settings` package) is the modern Python standard for handling application configuration and environment variables safely.

```python
# Note: requires `pip install pydantic-settings`
from pydantic_settings import BaseSettings, SettingsConfigDict

class AppConfig(BaseSettings):
    app_name: str = "My Application"
    admin_email: str
    db_url: str
    
    # Automatically reads from a .env file if it exists, matching the field names
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

# config = AppConfig() # Will read os.environ and `.env` to populate admin_email and db_url
```
