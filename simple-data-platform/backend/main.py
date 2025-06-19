import os
from typing import Dict, List

from dotenv import load_dotenv
from fastapi import APIRouter, Depends, FastAPI
from sqlalchemy.orm import Session

from .crud import FileCRUD, ResultCRUD, generate_engine, generate_session
from .initialize_database import initialize_database
from .schema import Base, File, Result

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment variables.")

DATABASE_PATH = os.getenv("DATABASE_PATH")
if not DATABASE_PATH:
    raise ValueError("DATABASE_PATH is not set in the environment variables.")

app = FastAPI()
api_router = APIRouter(prefix="/api")


def get_db():
    if not os.path.exists(DATABASE_PATH):
        print("Database does not exist. Creating a new one.")
        initialize_database()
    engine = generate_engine(DATABASE_URL)
    session = generate_session(engine)

    try:
        yield session
    finally:
        session.close()


@api_router.get("/files")
def get_configurations(session: Session = Depends(get_db)):
    print("Getting all files")
    return FileCRUD.get_files(session)


@api_router.post("/files")
def register_file(file_data: Dict[str, str], session: Session = Depends(get_db)):
    print(f"Creating file: {file_data}")
    FileCRUD.create_file(
        name=file_data.get("name"), path=file_data.get("path"), session=session
    )


app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)
