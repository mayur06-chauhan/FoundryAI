from langchain_openai import ChatOpenAI
from agents._config import OPENAI_API_KEY

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=OPENAI_API_KEY,
    temperature=0.3
)

def market_agent(refined_idea: str):
    print("📊 Market Agent started")

    prompt = f"""
You are a startup market analyst.

Analyze the following startup idea and provide:

1. Target customers
2. Market size (Small / Medium / Large with reason)
3. Competitors (2-4 examples)
4. Unique advantage suggestions
5. Monetization model

Idea:
{refined_idea}

Format clearly with bullet points.
"""

    response = llm.invoke(prompt)

    print("📊 Market Agent finished")
    return response.content
