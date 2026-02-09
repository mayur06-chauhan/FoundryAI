from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from agents._config import OPENAI_API_KEY

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.3,
    request_timeout=60,
    api_key=OPENAI_API_KEY
)


def product_agent(refined_idea: str):
    print("✅ Product Agent started")
    prompt = ChatPromptTemplate.from_template("""
You are a Product Manager.

Idea:
{idea}

Generate:
1. MVP Features
2. Future Features
""")

    response = (prompt | llm).invoke({"idea": refined_idea})
    print("✅ Product Agent finished")
    return {
    "refined_idea": response.content
}

