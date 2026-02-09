from langgraph.graph import StateGraph
from schemas.state import ProjectState

from agents.idea_agent import idea_agent
from agents.clarification_agent import clarification_agent
from agents.product_agent import product_agent
from agents.roadmap_agent import roadmap_agent
from agents.techstack_agent import techstack_agent
from agents.market_agent import market_agent

# -----------------------------
# 1. Initialize state
# -----------------------------
def init_state(state: dict):
    return {
        "user_idea": state["user_idea"],
        "is_clear": True,
        "questions": "",
        "refined_idea": "",
        "features": "",
        "roadmap": "",
        "techstack": "",
        "market_analysis": ""  
    }


# -----------------------------
# 2. Nodes (IMPORTANT: merge state)
# -----------------------------
def idea_node(state: ProjectState):
    result = idea_agent(state["user_idea"])   # result is a dict

    return {
        **state,
        "refined_idea": result.get("refined_idea", ""),
        "is_clear": result.get("is_clear", True),
        "questions": result.get("questions", "")
    }



def clarification_node(state: ProjectState):
    clarified = clarification_agent(state["questions"])
    return {
        **state,
        "questions": clarified
    }


def product_node(state: ProjectState):
    features = product_agent(state["refined_idea"])
    return {
        **state,
        "features": features
    }


def roadmap_node(state: ProjectState):
    roadmap = roadmap_agent(state["features"])
    return {
        **state,
        "roadmap": roadmap
    }

def techstack_node(state: ProjectState):
    techstack = techstack_agent(
        state["refined_idea"],
        state["features"]
    )

    return {
        **state,
        "techstack": techstack
    }


def market_node(state: ProjectState):
    market = market_agent(state["refined_idea"])

    return {
        **state,
        "market_analysis": market
    }


# -----------------------------
# 3. Condition
# -----------------------------
def clarity_check(state: ProjectState):
    return "continue" if state["is_clear"] else "clarify"


# -----------------------------
# 4. Build Graph
# -----------------------------
graph = StateGraph(ProjectState)

# Init node (VERY IMPORTANT)
graph.add_node("init", init_state)
graph.set_entry_point("init")

# Other nodes
graph.add_node("idea", idea_node)
graph.add_node("clarify", clarification_node)
graph.add_node("product", product_node)
graph.add_node("roadmap", roadmap_node)
graph.add_node("techstack", techstack_node)
graph.add_node("market", market_node)

# Flow
graph.add_edge("init", "idea")

graph.add_conditional_edges(
    "idea",
    clarity_check,
    {
        "clarify": "clarify",
        "continue": "product"
    }
)

# If clarification happens → end (no full plan yet)
graph.set_finish_point("clarify")

# Normal flow
graph.add_edge("product", "roadmap")
graph.add_edge("roadmap", "techstack")
graph.add_edge("techstack", "market")
graph.set_finish_point("market")

# Compile
workflow = graph.compile()
