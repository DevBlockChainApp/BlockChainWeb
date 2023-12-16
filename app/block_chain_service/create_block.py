from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from app.block_chain_service.block_base import BlockBase
from app.models import Block
from app.schemas import AddNewBlock


class CreateBlock(BlockBase):
    def __init__(self, block_data: AddNewBlock):
        self.data = block_data.data
        self.date_create = datetime.now()

    def generate_header(self):
        return self.data + str(self.date_create)

    def get_block_info(self):
        return {
            'data': self.data,
            'date_create': self.date_create,
            'hash_block': self.hash_block,
            'prev_hash': None
        }
    
    async def check_new_block(self, db: AsyncSession) -> bool:
        objs = await self._get_check_info(db, Block.hash_block == self.hash_block)
        return not objs
