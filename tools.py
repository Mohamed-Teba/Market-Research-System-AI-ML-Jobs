from crewai_tools import ScrapeWebsiteTool, SerperDevTool, PDFSearchTool
import os
from dotenv import load_dotenv
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("\u2705 PDFSearchTool initialized.")

load_dotenv("envo.env")

os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')
os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

pdf_path = os.path.abspath("report.pdf")

if os.path.exists(pdf_path):
    pdf_tool = PDFSearchTool(
        config=dict(
            llm=dict(
                provider="google",
                config=dict(
                    model="gemini-1.5-flash-002",
                ),
            ),
            embedder=dict(
                provider="google",
                config=dict(
                    model="models/embedding-001",
                    task_type="retrieval_document",
                ),
            ),
        ),
        pdf=pdf_path
    )
    print("✅ PDFSearchTool initialized.")
else:
    print(f"⚠️ PDF not found at {pdf_path}. Skipping PDF tool setup.")
    pdf_tool = None
