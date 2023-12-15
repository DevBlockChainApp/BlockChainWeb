from fastapi import APIRouter, Depends, HTTPException
from app.api.deps import get_db
from app.schemas import AddNewBlock, AddChainBlock, BlockData
from app.service import CreateBlock, ChainBlock
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.block import Block
from app.crud.block import block as crud_block

router = APIRouter()


@router.get('/{block_hash}', response_model=list[BlockData])
async def get_block(block_hash: str, db: AsyncSession = Depends(get_db)):
    tst = await crud_block.get_multi(db, Block.hash_block == block_hash)
    return tst

@router.post('/create')
async def create_block(data_block: AddNewBlock, db: AsyncSession = Depends(get_db)):
    new_block = CreateBlock(data_block.data)
    return await new_block.save_to_db(db)


@router.post('/create_chain')
async def create_chain(data_block: AddChainBlock, db: AsyncSession = Depends(get_db)):
    new_chain = ChainBlock(data_block)
    if not await new_chain.check_block(db):
        return HTTPException(404, 'Not prev hash in db')
    return await new_chain.save_to_db(db)
