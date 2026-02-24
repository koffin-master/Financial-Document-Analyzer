import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent

llm = "openai/gpt-4o-mini"

# -------------------------
# Financial Analyst
# -------------------------
financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Analyze financial documents and extract meaningful financial insights.",
    backstory="Expert in interpreting financial statements, revenue models, and company performance.",
    verbose=False,
    allow_delegation=True,
    llm=llm
)

# -------------------------
# Document Verifier
# -------------------------
verifier = Agent(
    role="Financial Document Verifier",
    goal="Verify whether the uploaded document is a valid financial document before analysis.",
    backstory="Experienced compliance officer ensuring document authenticity and relevance.",
    verbose=False,
    allow_delegation=False,
    llm=llm
)

# -------------------------
# Investment Advisor
# -------------------------
investment_advisor = Agent(
    role="Investment Advisor",
    goal="Provide balanced investment recommendations based on financial data.",
    backstory="Portfolio strategist focused on long-term, risk-adjusted returns.",
    verbose=False,
    allow_delegation=False,
    llm=llm
)

# -------------------------
# Risk Assessor
# -------------------------
risk_assessor = Agent(
    role="Risk Assessment Specialist",
    goal="Identify financial and market risks from the document.",
    backstory="Risk modeling expert analyzing volatility, leverage, and macroeconomic risks.",
    verbose=False,
    allow_delegation=False,
    llm=llm
)