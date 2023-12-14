from app.crud.base import CRUDBase
from app.models import Block
from app.schemas import BlockCreate, BlockUpdate


class CRUDBlock(CRUDBase[Block, BlockCreate, BlockUpdate]):
    pass


block = CRUDBlock(Block)
