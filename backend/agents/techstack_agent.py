from langchain_openai import ChatOpenAI
from agents._config import OPENAI_API_KEY

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=OPENAI_API_KEY,
    temperature=0.3
)

def techstack_agent(refined_idea, features):
    prompt = f"""
Suggest a suitable modern technology stack for this startup idea.

Idea:
{refined_idea}

Features:
{features}

Provide:
- Frontend
- Backend
- Database
- AI/ML tools (if needed)
- Deployment
- Other useful tools

Keep it practical and startup-friendly.
"""

    response = llm.invoke(prompt)
    return response.content
