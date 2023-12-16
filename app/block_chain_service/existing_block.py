from app.block_chain_service.block_base import BlockBase


class ExistingBlock(BlockBase):
    def __init__(self, hash_block: str):
        self.hash_block = hash_block
