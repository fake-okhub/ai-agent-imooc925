from langchain_openai import ChatOpenAI
import os

llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.4,
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_API_BASE"),
    timeout=30,
    max_tokens=200,
    stop="我",
    max_retries = 3
    )
llm.invoke("介绍下你自己")