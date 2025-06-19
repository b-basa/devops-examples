from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


# File Table
class File(Base):
    __tablename__ = "file"

    id = Column(Integer, primary_key=True, autoincrement=True)
    path = Column(String, nullable=False)
    name = Column(String, nullable=False)

    # Relationship to Result
    results = relationship(
        "Result", back_populates="file", cascade="all, delete-orphan"
    )


# Result Table
class Result(Base):
    __tablename__ = "result"

    id = Column(Integer, primary_key=True, autoincrement=True)
    file_id = Column(Integer, ForeignKey("file.id"), nullable=False)
    aggregation = Column(String, nullable=False)
    value = Column(Float, nullable=False)

    # Relationship back to File
    file = relationship("File", back_populates="results")
