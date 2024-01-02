import uuid
import base64
from datetime import datetime, timedelta
from litestar import Litestar, get, post
from sqlalchemy import create_engine, null, select
from sqlalchemy.orm import Session

from pluckwork.types import Task

engine = create_engine("sqlite:///pluckwork.db", echo=True)
session = Session(engine)

@post("/")
async def add_job(body: bytes) -> str:
    id = uuid.uuid4().hex
    task = Task(id=id, input=body)
    session.add(task)
    session.commit()
    return id

@get("/")
async def get_result(id: str) -> bytes | None:
    _task = select(Task).where(Task.id == id)
    task = session.scalar(_task)
    if task.output is None:
        return None
    return task.output

@get("/task")
async def get_task() -> dict | None:
    # Get the first task without a reserved_at timestamp
    # Or, if everything is reserved, find one where output is None and reserved_at is more than an hour ago
    # retry_cutoff_dt = datetime.utcnow() - timedelta(hours=1)
    _task = select(Task).where(Task.reserved_at == None).limit(1)  # noqa: E711
    task = session.scalar(_task)
    return {"id": task.id, "input": task.input}

@post("/task")
async def update_task(id: str, body: bytes) -> None:
    _task = select(Task).where(Task.id == id)
    task = session.scalar(_task)
    if task is not None:
        task.output = body
        session.commit()

app = Litestar([add_job, get_result, get_task, update_task])