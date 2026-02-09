from sqlalchemy import Column, Integer, String, Text
from db.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    user_idea = Column(Text)
    refined_idea = Column(Text)
    features = Column(Text)
    roadmap = Column(Text)
    techstack = Column(Text)
    market_analysis = Column(Text)
    status = Column(String, default="completed")
