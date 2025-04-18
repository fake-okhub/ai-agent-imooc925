# 注意目前并不是所有大模型都遵从统一标准
# response_metadata中的字段可能每一家都不太一样
# 如果要使用一定要先自己试一试
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4",
    temperature=0,
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_API_BASE"),
)
aggregate = None
for chunk in llm.stream("LangChain作者是谁?", stream_usage=True):
    print(chunk)
    aggregate = chunk if aggregate is None else aggregate + chunk