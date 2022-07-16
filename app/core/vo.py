from pydantic import BaseModel


class BaseVO(BaseModel):
    class Config:
        allow_mutation = False
        use_enum_values = True
        orm_mode = True


BaseDTO = BaseVO
