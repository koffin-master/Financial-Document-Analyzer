import os
from pypdf import PdfReader
from crewai.tools import tool

# ----------------------
# PDF Reader Tool
# ----------------------
@tool("read_financial_document")
def read_data_tool(path: str) -> str:
    """
    Reads and returns cleaned text from a financial PDF document.
    """

    if not os.path.exists(path):
        raise FileNotFoundError(f"PDF file not found at path: {path}")

    reader = PdfReader(path)
    extracted_text = []

    for page in reader.pages:
        text = page.extract_text()
        if text:
            cleaned = text.strip().replace("\n\n", "\n")
            extracted_text.append(cleaned)

    return "\n".join(extracted_text)


# ----------------------
# Investment Analysis Tool
# ----------------------
@tool("analyze_investment")
def analyze_investment_tool(financial_document_data: str) -> str:
    """
    Placeholder investment analysis logic.
    """

    if not financial_document_data:
        return "No financial data provided for investment analysis."

    # Minimal safe logic (not hallucinated nonsense)
    return (
        "Basic Investment Insight:\n"
        "- Review revenue growth trends.\n"
        "- Check profit margins consistency.\n"
        "- Evaluate debt levels and cash flow.\n"
        "Further quantitative modeling recommended."
    )


# ----------------------
# Risk Assessment Tool
# ----------------------
@tool("create_risk_assessment")
def create_risk_assessment_tool(financial_document_data: str) -> str:
    """
    Placeholder risk assessment logic.
    """

    if not financial_document_data:
        return "No financial data provided for risk assessment."

    return (
        "Basic Risk Assessment:\n"
        "- Monitor market volatility.\n"
        "- Assess leverage and liquidity risk.\n"
        "- Evaluate sector-specific risks.\n"
        "Detailed financial risk modeling required."
    )