import hashlib

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.block_chain_service.block_db import BlockDB
from app.models import Block
from app.schemas import BlockData


class BlockBase(BlockDB):
    def calculate_hash(self):
        header_string: str = self.generate_header()
        hash_block = hashlib.sha256(header_string.encode('utf-8'))
        self.hash_block = str(hash_block.hexdigest())
    
    def generate_header(self) -> str: ...

    async def save_to_db(self, db: AsyncSession):
        self.calculate_hash()
        new_item = self.get_block_info()
        if not await self.check_new_block(db):
            raise HTTPException(404, 'Invalid Block')
        return await self._save_to_db(db, new_item)
    
    def get_block_info(self) -> dict: ...
    
    async def check_new_block(self, db: AsyncSession) -> bool: ...
    
    async def get_block(self, db: AsyncSession) -> BlockData:
        return self._get_block(db, Block.hash_block == self.hash_block)
        