from app.schemas import BlockData
import hashlib

class Block:
    def __init__(self, data_block: BlockData):
        self.data_block = data_block

    def __call__(self):
        hash_block = self.calculate_hash()
        return hash_block

    def calculate_hash(self):
        header_string: str = self.generate_header(self.data_block)
        hash_block = hashlib.sha256(header_string.encode('utf-8'))
        return hash_block.hexdigest()
    
    def get_hash(self) -> str:
        return self.hash_block

    def generate_header(self, data_block: BlockData) -> str:
        return data_block.hash_block + data_block.prev_hash + str(data_block.date_create)

