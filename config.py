import os

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "123456"),
    "database": os.getenv("DB_NAME", "chatbi_mvp"),
    "charset": "utf8mb4"
}

LLM_CONFIG = {
    "api_key": os.getenv("OPENAI_API_KEY"),
    "base_url": os.getenv("OPENAI_BASE_URL", "https://apihub.agnes-ai.cn/v1"),
    "model": os.getenv("LLM_MODEL", "agnes-2.5-flash"),
    "temperature": 0.1,
    "max_tokens": 1000
}
