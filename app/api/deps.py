from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import assync_session



async def get_db() -> AsyncSession:
    async with assync_session() as session:
        yield session
