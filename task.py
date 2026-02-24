from crewai import Task
from agents import financial_analyst, verifier, investment_advisor, risk_assessor
from tools import read_data_tool, analyze_investment_tool, create_risk_assessment_tool


# -------------------------
# Verification Task
# -------------------------
verification_task = Task(
    description=(
        "Verify whether the uploaded document at {file_path} is a valid financial document "
        "by reading its contents using the provided tool."
    ),
    expected_output=(
        "State clearly whether the document appears to be a financial document "
        "and provide reasoning based on its contents."
    ),
    agent=verifier,
    tools=[read_data_tool],
    async_execution=False,
)


# -------------------------
# Financial Analysis Task
# -------------------------
analysis_task = Task(
    description=(
        "Use the financial document located at {file_path} to answer the user's query: {query}. "
        "Carefully read the document using the provided tool before generating insights."
    ),
    expected_output=(
        "Provide structured analysis including:\n"
        "- Executive Summary\n"
        "- Revenue and Profitability Trends\n"
        "- Key Financial Metrics\n"
        "- Business Outlook"
    ),
    agent=financial_analyst,
    tools=[read_data_tool],
    async_execution=False,
)


# -------------------------
# Investment Analysis Task
# -------------------------
investment_task = Task(
    description=(
        "Based strictly on the financial document at {file_path}, provide balanced investment insights."
    ),
    expected_output=(
        "- Buy/Hold/Sell perspective\n"
        "- Supporting financial reasoning\n"
        "- Strengths and weaknesses\n"
        "- Short-term vs long-term outlook"
    ),
    agent=investment_advisor,
    tools=[analyze_investment_tool],
    async_execution=False,
)


# -------------------------
# Risk Assessment Task
# -------------------------
risk_task = Task(
    description=(
        "Using the financial document at {file_path}, evaluate financial and operational risks."
    ),
    expected_output=(
        "- Financial risks\n"
        "- Market risks\n"
        "- Liquidity & solvency risks\n"
        "- Operational risks"
    ),
    agent=risk_assessor,
    tools=[create_risk_assessment_tool],
    async_execution=False,
)