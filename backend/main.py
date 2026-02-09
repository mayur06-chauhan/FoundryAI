from unittest import result
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from workflow.graph import workflow
from db.database import SessionLocal, engine
from db import models
from db.crud import create_project, get_all_projects

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FoundryAI",
    description="""
🚀 **FoundryAI – Your AI Project Co-Founder**

FoundryAI is an agentic AI-powered platform that transforms raw startup ideas into
clear execution plans. It uses multi-agent reasoning and workflow orchestration to:

• Refine vague ideas into clear problem statements  
• Ask intelligent clarification questions when needed  
• Generate MVP & future feature plans  
• Create structured development roadmaps  

Built using **FastAPI, LangChain, LangGraph, and LLMs**, FoundryAI behaves like a
real technical co-founder guiding founders from idea to execution.
""",
)

app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def serve_frontend():
    return FileResponse("frontend/index.html")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for development
    allow_credentials=True,
    allow_methods=["*"],  # allow POST, GET, OPTIONS
    allow_headers=["*"],
)

class IdeaInput(BaseModel):
    idea: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/start")
def start_project(data: IdeaInput, db: Session = Depends(get_db)):
    try:
        result = workflow.invoke({"user_idea": data.idea})

        print("WORKFLOW RESULT:", result)

        is_clear = result.get("is_clear", False)
        refined_idea = result.get("refined_idea")
        features = result.get("features")
        roadmap = result.get("roadmap")
        techstack = result.get("techstack")         
        market_analysis = result.get("market_analysis")
        questions = result.get("questions")


        # Convert dict → string (SQLite fix)
        if isinstance(refined_idea, dict):
            refined_idea = str(refined_idea)

        if isinstance(features, dict):
            features = str(features)

        if isinstance(roadmap, dict):
            roadmap = str(roadmap)

        if isinstance(techstack, dict):
            techstack = str(techstack)

        if isinstance(market_analysis, dict):
            market_analysis = str(market_analysis)

        # Save only if idea is clear
        if is_clear:
            create_project(
                db,
                user_idea=data.idea,
                refined_idea=refined_idea,
                features=features,
                roadmap=roadmap,
                techstack=techstack,
                market_analysis=market_analysis
            )

        return {
            "is_clear": is_clear,
            "questions": questions,
            "refined_idea": refined_idea,
            "features": features,
            "roadmap": roadmap,
            "techstack": techstack,
            "market_analysis": market_analysis
        }

    except Exception as e:
        print("❌ BACKEND ERROR:", e)
        return {
            "is_clear": False,
            "questions": "AI workflow failed. Please try again."
        }

@app.get("/projects")
def get_projects(db: Session = Depends(get_db)):
    try:
        return get_all_projects(db)
    except Exception as e:
        print("❌ DB ERROR:", e)
        return []

@app.get("/")
def home():
    return {"message": "FoundryAI backend is running"}
