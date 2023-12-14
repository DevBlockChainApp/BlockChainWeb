from app.schemas import AddChainBlock
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.block import block as crud_block
import hashlib

class ChainBlock:
    def __init__(self, block: AddChainBlock):
        self.data = block.data
        self.prev_hash = block.prev_hash
        self.date_create = datetime.now()
        self.calculate_hash()

    def calculate_hash(self):
        header_string: str = self.generate_header()
        hash_block = hashlib.sha256(header_string.encode('utf-8'))
        self.hash_block = str(hash_block.hexdigest())
    
    def generate_header(self):
        return self.data + self.prev_hash + str(self.date_create)

    def get_block_info(self):
        return {
            'data': self.data,
            'date_create': self.date_create,
            'hash_block': self.hash_block,
            'prev_hash': self.prev_hash
        }
    
    async def save_to_db(self, db: AsyncSession):
        return await crud_block.create(db, obj_in=self.get_block_info())
    
    async def check_block(self, db):
        return await crud_block.get(db, self.prev_hash)
    
