from fastapi import APIRouter, Depends
from app.api.deps import get_db
from app.schemas import BlockData
from app.schemas import AddNewBlock
from app.service import Block
from app.crud.block import block as crud_block
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.post('/create')
async def create_block(data_block: AddNewBlock, db: AsyncSession = Depends(get_db)):
    new_block = Block(data_block.data)
    return await new_block.save_to_db(db)