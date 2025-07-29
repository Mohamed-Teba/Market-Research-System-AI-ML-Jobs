# tasks.py
import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(CURRENT_DIR)

from crewai import Task
from agents import (
    industry_researcher,
    use_case_generator,
    resource_collector,
)

industry_research_task = Task(
    description=(
        "Research and analyse the company/industry: {company}. "
        "Gather information using the search and scrape tools first, then summarise. "
        "Identify key offerings, strategic focus areas, competitors, trends, and challenges."
    ),
    expected_output=(
        "1. High‑level overview\n"
        "2. Key products/services\n"
        "3. Strategic focus areas\n"
        "4. Major competitors\n"
        "5. Current market trends\n"
        "6. Industry challenges & growth opportunities"
    ),
    agent=industry_researcher,
)

use_case_generation_task = Task(
    description=(
        "Using insights from the research task, list 4‑5 GenAI / LLM / ML use‑cases "
        "that {company} could adopt. Use search, scrape, and PDF tools to collect "
        "evidence before writing."
    ),
    expected_output=(
        "For each use‑case:\n"
        "• 2‑3 line description\n"
        "• Objective\n"
        "• Implementation outline (libs / frameworks)\n"
        "• Cross‑functional benefits"
    ),
    agent=use_case_generator,
)

resource_collection_task = Task(
    description=(
        "For every proposed use‑case, find 2‑3 high‑quality public datasets, "
        "libraries, or tools (Kaggle, HuggingFace, GitHub, etc.). "
        "Use the search tool only; do not fabricate links."
    ),
    expected_output=(
        "For each use‑case provide:\n"
        "• Brief recap of use‑case\n"
        "• Implementation tip(s)\n"
        "• 2‑3 real links to datasets/libraries"
    ),
    agent=resource_collector,
)

print("✅  Tasks created successfully")
