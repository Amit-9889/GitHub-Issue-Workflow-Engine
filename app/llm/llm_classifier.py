import json
from langchain_groq import ChatGroq
from app.config.settings import GROQ_API_KEY
import re

model = ChatGroq(model_name="llama-3.3-70b-versatile",temperature=0,api_key=GROQ_API_KEY)


def classify_issue_with_llm(title, body):
    prompt = f"""
                You are a classifier for GitHub issues.

                Return ONLY valid JSON.
                No markdown. No explanation.


                Schema :
                {{
                "issue_type": "bug|feature|documentation|question",
                "priority": "P1|P2|P3",
                "team": "frontend-team|backend-team|product-team",
                "reasoning": "short explanation"
                }}

                Title: {title}
                Body: {body}
                """

    output = model.invoke(prompt).content.strip()
    # print("LLM RAW:", output)

    # match = re.search(r"\{.*\}", output, re.DOTALL)
    # if not match:
    #     raise ValueError("No JSON in LLM output")

    if output.startswith("```"):
        output = re.sub(r"^```[a-zA-Z]*", "", output)
        output = re.sub(r"```$", "", output)
    print(f"Raw llm output:{output}")
    return json.loads(output)
