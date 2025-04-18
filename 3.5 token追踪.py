from langchain_deepseek import ChatDeepSeek

llm = ChatDeepSeek(
    model="Pro/deepseek-ai/DeepSeek-R1",
    temperature=0,
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    api_base=os.environ.get("DEEPSEEK_API_BASE"),
)
res = llm.invoke("介绍下自己")
res.usage_metadata