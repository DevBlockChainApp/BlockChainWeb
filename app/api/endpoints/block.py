from fastapi import APIRouter

router = APIRouter()

@router.get('/main')
async def get_main():
    return 'Hello'
