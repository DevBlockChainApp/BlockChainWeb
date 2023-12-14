from fastapi import APIRouter, Depends, HTTPException
from app.api.deps import get_db
from app.schemas import AddNewBlock, AddChainBlock
from app.service import AddBlock, ChainBlock
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.block import block as crud_block

router = APIRouter()


@router.post('/create')
async def create_block(data_block: AddNewBlock, db: AsyncSession = Depends(get_db)):
    new_block = AddBlock(data_block.data)
    return await new_block.save_to_db(db)


@router.post('/create_chain')
async def create_chain(data_block: AddChainBlock, db: AsyncSession = Depends(get_db)):
    new_chain = ChainBlock(data_block)
    if not await new_chain.check_block(db):
        return HTTPException(404, 'Not prev hash in db')
    return await new_chain.save_to_db(db)
