from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Block
from app.schemas import BlockData


class BlockDB:
    async def _save_to_db(self, db: AsyncSession, new_item: dict) -> Block:
        db_obj = Block(**new_item)  # type: ignore
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def _get_block(self, db: AsyncSession, *args) -> BlockData:
        return (await db.execute(select(Block).filter(*args))).scalars()

    async def _get_check_info(self, db: AsyncSession, *args):
        return (await db.execute(select(Block).filter(*args))).all()
