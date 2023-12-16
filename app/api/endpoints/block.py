from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.block_chain_service.block_interface import BlockInterface
from app.schemas import AddNewBlock, AddNewChainBlock, BlockData

router = APIRouter()


@router.get('/{block_hash}', response_model=list[BlockData])
async def get_block(block_hash: str, db: AsyncSession = Depends(get_db)):
    block = BlockInterface(block_hash)
    return await block.get_block(db)


@router.post('/create_block')
async def create_block(data_block: AddNewBlock, db: AsyncSession = Depends(get_db)):
    new_block = BlockInterface(data_block)
    return await new_block.save_to_db(db)


@router.post('/create_chain')
async def create_chain(data_block: AddNewChainBlock, db: AsyncSession = Depends(get_db)):
    new_chain = BlockInterface(data_block)
    return await new_chain.save_to_db(db)
