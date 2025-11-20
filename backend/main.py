from database.orm import AsyncORM
import asyncio
import sys
import uvicorn
from api import create_fastapi_app




async def main():
    await AsyncORM.create_tables()
    await AsyncORM.insert_starting_data()

app = create_fastapi_app()

if __name__ == "__main__":
    asyncio.run(main())
    if "--webserver" in sys.argv:
        uvicorn.run(
            app="main:app",
            reload=True,
        )
