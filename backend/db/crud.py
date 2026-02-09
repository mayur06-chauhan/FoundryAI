from sqlalchemy.orm import Session
from db.models import Project

def create_project(db: Session, user_idea, refined_idea, features, roadmap, techstack, market_analysis):
    project = Project(
        user_idea=user_idea,
        refined_idea=refined_idea,
        features=features,
        roadmap=roadmap,
        techstack=techstack,
        market_analysis=market_analysis
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def get_all_projects(db: Session):
    return db.query(Project).all()
