📊 Financial Document Analyzer (Debugged & Improved)

This project is a fixed and improved version of the original CrewAI-based Financial Document Analyzer.

The original repository had multiple issues — broken tool calls, validation errors, LLM misconfiguration, and inefficient prompts that caused unreliable or hallucinated outputs.

My goal was to:
	•	Fix all deterministic bugs
	•	Improve prompt quality
	•	Make the system stable and production-ready
	•	Ensure outputs are grounded in the financial document

The system now runs cleanly and produces structured, reliable financial insights.

🐛 Bugs Found & How I Fixed Them

1. Tool Validation Errors (Pydantic Issues)

Problem

The system kept throwing errors like:

Input should be a valid string

This happened because tools were defined to accept a string, but the agent was passing a dictionary like:

{
  "financial_document_data": {
      "description": "..."
  }
}

CrewAI + Pydantic rejected this.

Fix

I corrected all tool calls to pass a pure string:

{
  "financial_document_data": "Full extracted financial text..."
}

This completely resolved:
	•	Validation errors
	•	Tool retries
	•	Execution loops

⸻

2. OpenAI Authentication Error

Problem

The app failed with:

litellm.AuthenticationError: Missing Authentication header

The OpenAI API key was not configured properly.

Fix
	•	Properly set up OPENAI_API_KEY
	•	Standardized environment variable usage
	•	Ensured model/provider configuration is correct

After this, LLM calls worked consistently.

⸻

3. Inefficient / Problematic Prompts

Problem

Some prompts in the original repo:
	•	Encouraged hallucinated content
	•	Produced unrealistic financial advice
	•	Were overly verbose
	•	Included unnecessary or misleading instructions

This made outputs unreliable.

Fix

I rewrote all agent prompts to:
	•	Strictly rely on the provided financial document
	•	Avoid speculation
	•	Produce structured and professional analysis
	•	Keep reasoning grounded and balanced

Now the outputs:
	•	Reflect actual financial metrics
	•	Avoid exaggerated claims
	•	Maintain professional tone

⸻

4. Repeated Tool Execution & Verbose Logs

Problem

Due to formatting issues, the agents repeatedly retried tool calls, cluttering logs and slowing execution.

Fix
	•	Cleaned tool schemas
	•	Fixed argument formatting
	•	Ensured one clean execution path per task

Now the flow is stable and predictable.

⸻

5. File Handling Issues

Problem

The system didn’t properly validate file paths before attempting to read PDFs.

Fix

Added safe checks:

if not os.path.exists(path):
    raise FileNotFoundError(...)

Also cleaned extracted PDF text to remove unnecessary spacing and formatting noise.

⸻

⚙️ Setup Instructions

1. Clone the Repository

git clone <your-repo-link>
cd financial-document-analyzer-debug


⸻

2. Create Virtual Environment

python3 -m venv .venv
source .venv/bin/activate   # Mac/Linux


⸻

3. Install Dependencies

pip install -r requirements.txt


⸻

4. Set Environment Variables

Create a .env file:

OPENAI_API_KEY=your_openai_key_here

Or export directly:

export OPENAI_API_KEY="your_key_here"


⸻

5. Run the Server

Production mode:

uvicorn main:app

Development mode:

uvicorn main:app --reload

Server runs at:

http://127.0.0.1:8000


⸻

📡 API Documentation

POST /analyze

Analyzes a financial PDF document.

Request Body

{
  "file_path": "data/financial_document.pdf"
}


⸻

Response Structure

{
  "verification": "...",
  "financial_analysis": "...",
  "investment_insights": "...",
  "risk_assessment": "..."
}


⸻

🧠 How the System Works
	1.	The user sends a file path to the API.
	2.	The PDF Reader Tool extracts and cleans text.
	3.	CrewAI orchestrates multiple agents:
	    •	Financial Document Verifier
	    •	Senior Financial Analyst
	    •	Investment Advisor
	    •	Risk Assessment Specialist
	4.	Each agent performs a specific task.
	5.	The system returns structured insights.

⸻

📁 Project Structure

financial-document-analyzer-debug/
│
├── agents.py
├── tools.py
├── main.py
├── data/
│   └── financial_document_xxx.pdf
├── requirements.txt
└── README.md


⸻

✅ What’s Improved Compared to the Original Version
	•	No tool validation errors
	•	Proper API key configuration
	•	Clean and grounded prompts
	•	Stable multi-agent execution
	•	Structured, realistic financial insights
	•	Cleaner logs and execution flow

⸻

🔮 Possible Future Improvements

If extended further, this system could include:
	•	Queue worker support (Celery/Redis) for concurrent requests
	•	Database integration to store analysis history
	•	File upload endpoint instead of file path
	•	Structured JSON extraction of key financial metrics

⸻

🏁 Final Notes

This version resolves all deterministic bugs and significantly improves prompt quality and tool reliability.

The system now:
	•	Runs without crashing
	•	Produces realistic and document-grounded insights
	•	Is clean enough to extend into production-level architecture
