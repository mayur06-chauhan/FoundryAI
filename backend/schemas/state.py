from typing import TypedDict, Optional

class ProjectState(TypedDict):
    user_idea: str
    refined_idea: Optional[str]
    questions: Optional[str]
    is_clear: Optional[bool]
    features: Optional[str]
    roadmap: Optional[str]
    techstack: Optional[str]
    market_analysis: Optional[str]  