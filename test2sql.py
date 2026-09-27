from openai import OpenAI
import os
from dotenv import load_dotenv
import re

load_dotenv()

def generate_sql(query: str) -> str:
    # call openai llm to generate sql
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
        base_url=os.environ.get("OPENAI_BASE_URL")
    )
    prompt = f"请根据以下自然语言查询生成对应的 SQL 语句：\n\n{query}\n\n请使用标准的 SQL 语法，并确保生成的 SQL 语句是正确的。"
    
    response = client.chat.completions.create(
        model=os.environ.get("LLM_MODEL"),
        messages=[
            {"role": "user", "content": prompt},
        ],
        temperature=0.1,
    )
    output = response.choices[0].message.content
    sql = re.sub(r'```sql|```', '', output).strip()
    return sql

if __name__ == "__main__":
    query = "各产品线的毛利率是多少 "
    print(generate_sql(query))
