from datetime import datetime
from sqlalchemy import null
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[str] = mapped_column(primary_key=True)
    input: Mapped[bytes] = mapped_column(nullable=False, default=b'')
    output: Mapped[bytes] = mapped_column(nullable=True)
    reserved_at: Mapped[datetime] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)