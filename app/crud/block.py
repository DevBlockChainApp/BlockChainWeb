from app.crud.base import CRUDBase
from app.models import Block
from app.schemas import BlockCreate, BlockUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, Optional
from sqlalchemy import select


class CRUDBlock(CRUDBase[Block, BlockCreate, BlockUpdate]):
    async def get(self, db: AsyncSession, *args) -> Optional[Block]:
        return (await db.execute(select(self.model).filter(*args))).all()
        


block = CRUDBlock(Block)
