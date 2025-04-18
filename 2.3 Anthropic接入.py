from langchain_anthropic import ChatAnthropic
model = ChatAnthropic(
model='claude-3-5-sonnet-latest',
api_key=os.environ.get("ANTHROPIC_API_KEY"),
base_url=os.environ.get("ANTHROPIC_BASE_URL"),
)
model.invoke("介绍下自己")