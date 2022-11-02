from  pydantic import BaseModel, validator, Field


class Post(BaseModel):
    id: int
    title: str

    # @validator("id")
    # def asser_id_more_two(cls, v):
    #     if v > 2:
    #         raise ValueError("ID больше двух")
    #     else:
    #         return v

