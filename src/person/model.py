from pydantic import BaseModel

class Person(BaseModel):
    id: int
    name: str
    phone: str
    email: str
    region: str
    country: str


class PersonUpdateModel(BaseModel):
    name: str
    phone: str
    email: str
    region: str
    country: str