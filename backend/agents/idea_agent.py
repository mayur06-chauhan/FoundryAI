from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from agents._config import OPENAI_API_KEY

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.3,
    request_timeout=60,
    api_key=OPENAI_API_KEY
)


def idea_agent(user_idea: str):
    print("🧠 Idea Agent started")
    prompt = ChatPromptTemplate.from_template("""
You are a startup idea analyst.

Idea:
{idea}

Respond STRICTLY in this format:

CLARITY: CLEAR or UNCLEAR

REFINED_IDEA:
<clear explanation>

QUESTIONS:
<questions only if unclear>
""")

    response = (prompt | llm).invoke({"idea": user_idea})
    print("✅ Idea Agent finished")
    return {
    "refined_idea": response.content
}

