from pydantic import BaseModel


class EventSchema(BaseModel):
    id: int


class EventListSchema(BaseModel):
    results: list[EventSchema]
    count: int
