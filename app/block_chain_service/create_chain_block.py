from datetime import datetime

from sqlalchemy import or_

from app.models import Block
from app.schemas import AddNewChainBlock
from app.block_chain_service.block_base import BlockBase


class CreateChainBlock(BlockBase):
    def __init__(self, data_block: AddNewChainBlock):
        self.data = data_block.data
        self.prev_hash = data_block.prev_hash
        self.date_create = datetime.now()
    
    def generate_header(self):
        return self.data + self.prev_hash + str(self.date_create)

    def get_block_info(self):
        return {
            'data': self.data,
            'date_create': self.date_create,
            'hash_block': self.hash_block,
            'prev_hash': self.prev_hash
        }
    
    async def check_new_block(self, db):
        objs = await self._get_check_info(db, or_(Block.hash_block == self.prev_hash,
                                                  Block.prev_hash == self.prev_hash))
        return len(objs) == 1
