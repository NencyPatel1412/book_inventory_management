import uvicorn
from config.config import setting

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="localhost",
        port=8000,
        reload=setting.DEBUG
    )