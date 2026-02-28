import uuid
import json
from sqlalchemy.orm import Session
from core.persistence.database import SessionLocal
from core.persistence.models import Execution


class ExecutionStore:

    def create_execution(self):
        db: Session = SessionLocal()

        execution_id = str(uuid.uuid4())

        execution = Execution(
            execution_id=execution_id,
            status="running"
        )

        db.add(execution)
        db.commit()
        db.close()

        return execution_id

    def complete_execution(self, execution_id: str, result: dict):
        db: Session = SessionLocal()

        execution = db.query(Execution).filter(
            Execution.execution_id == execution_id
        ).first()

        if execution:
            execution.status = "completed"
            execution.result = json.dumps(result)
            db.commit()

        db.close()

    def list_executions(self):
        db: Session = SessionLocal()

        executions = db.query(Execution).all()

        result = [
            {
                "execution_id": e.execution_id,
                "status": e.status
            }
            for e in executions
        ]

        db.close()
        return result

    def get_execution(self, execution_id: str):
        db: Session = SessionLocal()

        execution = db.query(Execution).filter(
            Execution.execution_id == execution_id
        ).first()

        if not execution:
            db.close()
            return None

        result = {
            "execution_id": execution.execution_id,
            "status": execution.status,
            "result": execution.result
        }

        db.close()
        return result