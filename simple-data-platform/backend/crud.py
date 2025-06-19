from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .schema import File, Result


def generate_engine(db_url):
    return create_engine(db_url, echo=True, connect_args={"check_same_thread": False})


def generate_session(engine):
    SessionLocal = sessionmaker(bind=engine)
    return SessionLocal()


class FileCRUD:
    @staticmethod
    def create_file(path: str, name: str, session):
        new_file = File(path=path, name=name)
        session.add(new_file)
        session.commit()
        session.refresh(new_file)
        print(f"File created: {new_file}")
        return new_file

    @staticmethod
    def get_files(session):
        files = session.query(File).all()
        return files

    @staticmethod
    def get_file_by_id(file_id: int, session):
        file = session.query(File).filter(File.id == file_id).first()
        return file

    @staticmethod
    def update_file(file_id: int, path: str, name: str, session):
        file = session.query(File).filter(File.id == file_id).first()
        if file:
            if path:
                file.path = path
            if name:
                file.name = name
            session.commit()
            session.refresh(file)
            print(f"File updated: {file}")
            return file
        print("File not found")
        return None

    @staticmethod
    def delete_file(file_id: int, session):
        file = session.query(File).filter(File.id == file_id).first()
        if file:
            session.delete(file)
            session.commit()
            print(f"File deleted: {file}")
            return True
        print("File not found")
        return False


class ResultCRUD:
    @staticmethod
    def create_result(file_id: int, aggregation: str, value: float, session):
        new_result = Result(file_id=file_id, aggregation=aggregation, value=value)
        session.add(new_result)
        session.commit()
        session.refresh(new_result)
        print(f"Result created: {new_result}")
        return new_result

    @staticmethod
    def get_results_by_file_id(file_id: int, session):
        results = session.query(Result).filter(Result.file_id == file_id).all()
        return results

    @staticmethod
    def get_results_by_aggregation(file_id: int, aggregation: str, session):
        results = (
            session.query(Result)
            .filter(Result.file_id == file_id, Result.aggregation == aggregation)
            .all()
        )
        return results

    @staticmethod
    def update_result(result_id: int, aggregation: str, session):
        result = session.query(Result).filter(Result.id == result_id).first()
        if result:
            if aggregation:
                result.aggregation = aggregation
            session.commit()
            session.refresh(result)
            print(f"Result updated: {result}")
            return result
        print("Result not found")
        return None

    @staticmethod
    def delete_result(result_id: int, session):
        result = session.query(Result).filter(Result.id == result_id).first()
        if result:
            session.delete(result)
            session.commit()
            print(f"Result deleted: {result}")
            return True
        print("Result not found")
        return False


if __name__ == "__main__":
    pass
