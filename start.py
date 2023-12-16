import uvicorn

from app.core.config import settings

if __name__ == '__main__':
    uvicorn.run('app.main:app', port=settings.FASTAPI_HTTP_PORT, host='0.0.0.0', log_level='info', reload=True)
