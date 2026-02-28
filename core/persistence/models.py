from sqlalchemy import Column, String, Text
from core.persistence.database import Base


class Execution(Base):
    __tablename__ = "executions"

    execution_id = Column(String, primary_key=True, index=True)
    status = Column(String, default="running")
    result = Column(Text, nullable=True)