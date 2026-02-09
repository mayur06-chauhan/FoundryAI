from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from agents._config import OPENAI_API_KEY

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.3,
    request_timeout=60,
    api_key=OPENAI_API_KEY
)


def roadmap_agent(features: str):
    print("✅ Roadmap Agent started")
    prompt = ChatPromptTemplate.from_template("""
You are a Tech Lead.

Based on these features:
{features}

Create a 6-week development roadmap.
""")

    response = (prompt | llm).invoke({"features": features})
    print("✅ Roadmap Agent finished")
    return {
    "refined_idea": response.content
}

