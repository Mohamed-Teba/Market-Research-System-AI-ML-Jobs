# agents.py
from crewai import Agent, LLM
import os
from dotenv import load_dotenv
from tools import search_tool, scrape_tool, pdf_tool

load_dotenv("envo.env")

together_api_key = os.getenv("TOGETHER_API_KEY")
if not together_api_key:
    raise ValueError(
        "TOGETHER_API_KEY not found. Set it in envo.env or your shell environment.")

llm = LLM(
    model="openai/Qwen/Qwen2.5-72B-Instruct-Turbo",
    api_key=together_api_key,
    api_base="https://api.together.xyz",
)

industry_researcher = Agent(
    role="Industry Research Specialist",
    goal=(
        "Conduct a comprehensive analysis of the {company} industry sector to identify "
        "current market trends, competitor strategies, and unique positioning opportunities."
    ),
    backstory=(
        "You are a seasoned industry analyst skilled at mapping competitive landscapes "
        "and spotting strategic gaps."
    ),
    tools=[search_tool, scrape_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False,
    max_rpm=20,
    max_iter=20,
)

use_case_generator = Agent(
    role="AI Use‑Case Strategist",
    goal=(
        "Generate innovative, high‑value AI / ML use‑cases for {company}, grounded in "
        "cutting‑edge industry trends."
    ),
    backstory=(
        "You translate AI research into practical business solutions with clear ROI."
    ),
    tools=[search_tool, scrape_tool, pdf_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False,
    max_rpm=20,
    max_retry_limit=20,
)

resource_collector = Agent(
    role="AI Resource Specialist",
    goal=(
        "Find the best datasets, libraries, and tools needed to implement the proposed "
        "AI / ML use‑cases for {company}."
    ),
    backstory=(
        "You maintain an extensive catalogue of AI resources and know where to locate "
        "domain‑specific data and code."
    ),
    tools=[search_tool, scrape_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False,
    max_rpm=20,
    max_retry_limit=20,
)

print("✅  Agents initialised successfully")
