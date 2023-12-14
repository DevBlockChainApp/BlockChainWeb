from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class BlockData(BaseModel):
    data: str
    date_create: datetime = datetime.now()
    hash_block: Optional[str]
    prev_hash: Optional[str]


class BlockCreate(BaseModel):
    pass


class BlockUpdate(BaseModel):
    pass
