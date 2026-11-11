from pydantic import BaseModel


class EventCreateSchema(BaseModel):
    page: str
    description: str | None = ""


class EventUpdateSchema(BaseModel):
    page: str | None = ""
    description: str


class EventSchema(BaseModel):
    id: int
    page: str | None = ""
    description: str | None = ""


class EventListSchema(BaseModel):
    results: list[EventSchema]
    count: int
