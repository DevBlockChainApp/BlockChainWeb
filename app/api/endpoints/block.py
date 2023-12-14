from fastapi import APIRouter, Depends
from app.api.deps import get_db
from app.schemas import BlockData
from app.service import Block
from app.crud.block import block as crud_block
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.post('/create')
async def create_block(data_block: BlockData, db: AsyncSession = Depends(get_db)):
    hash_block = Block(data_block)
    data_block.hash_block = str(hash_block())
    await crud_block.create(db, obj_in=data_block)
