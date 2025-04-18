# StrOutputParser可以大幅简化从LangChain中提取文本
# 假设有一个被绑定了工具的LLM
# 定义LLM使用claude
from langchain_anthropic import ChatAnthropic
import os
model = ChatAnthropic(
model='claude-3-5-sonnet-latest',
api_key=os.environ.get("ANTHROPIC_API_KEY"),
base_url=os.environ.get("ANTHROPIC_BASE_URL"),
)
# 定义一个假的实时天气预报工具
# 传入地名返回实时天气
from langchain_core.tools import tool
@tool
def get_weather(location: str) -> str:
    """根据location地名返回当地实时天气."""

    return "天气晴朗22度"

# 绑定工具
llm_with_tools = model.bind_tools([get_weather])
# 调用
response = llm_with_tools.invoke("北京市当前的天气如何?")
# 如果不使用输出解析器的结果
# 可能需要比较麻烦的方式才可以提取到结果
response.content