from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
import hashlib
from app.crud.block import block as crud_block

class AddBlock:
    def __init__(self, data: str):
        self.data = data
        self.date_create = datetime.now()
        self.calculate_hash()

    def calculate_hash(self):
        header_string: str = self.generate_header()
        hash_block = hashlib.sha256(header_string.encode('utf-8'))
        self.hash_block = str(hash_block.hexdigest())
    
    def generate_header(self):
        return self.data + str(self.date_create)

    def get_block_info(self):
        return {
            'data': self.data,
            'date_create': self.date_create,
            'hash_block': self.hash_block,
            'prev_hash': None
        }

    async def save_to_db(self, db: AsyncSession):
        return await crud_block.create(db, obj_in=self.get_block_info())


    # def __call__(self):
    #     hash_block = self.calculate_hash()
    #     return hash_block

    # def calculate_hash(self):
    #     header_string: str = self.generate_header(self.data_block)
    #     hash_block = hashlib.sha256(header_string.encode('utf-8'))
    #     return hash_block.hexdigest()
    
    # def get_hash(self) -> str:
    #     return self.hash_block

    # def generate_header(self, data_block: BlockData) -> str:
    #     return data_block.hash_block + data_block.prev_hash + str(data_block.date_create)

