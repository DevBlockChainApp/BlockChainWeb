from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BlockData(BaseModel):
    data: str
    date_create: datetime = datetime.now()
    hash_block: Optional[str]
    prev_hash: Optional[str]

    class Config:
        orm_mode = True


class AddNewBlock(BaseModel):
    data: str


class AddNewChainBlock(BaseModel):
    data: str
    prev_hash: str
