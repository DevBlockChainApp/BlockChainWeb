from fastapi import HTTPException

from app.block_chain_service.create_block import CreateBlock
from app.block_chain_service.create_chain_block import CreateChainBlock
from app.block_chain_service.existing_block import ExistingBlock
from app.schemas import AddNewBlock, AddNewChainBlock


class BlockInterfaceClass:
    def __call__(self, data_block: AddNewBlock | AddNewChainBlock | str = None):
        if isinstance(data_block, str):
            return ExistingBlock(data_block)
        elif isinstance(data_block, AddNewBlock):
            return CreateBlock(data_block)
        elif isinstance(data_block, AddNewChainBlock):
            return CreateChainBlock(data_block)

        raise HTTPException(405, 'Invalid information')


BlockInterface = BlockInterfaceClass()
