from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
import os

#加法工具
class add(BaseModel):
    """Add two integers."""

    a: int = Field(..., description="First integer")
    b: int = Field(..., description="Second integer")

#乘法工具
class multiply(BaseModel):
    """Multiply two integers."""

    a: int = Field(..., description="First integer")
    b: int = Field(..., description="Second integer")

llm = ChatOpenAI(
    model="gpt-4",
    temperature=0,
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPEN_API_BASE"),
)

tools = [add,multiply]
llm_with_tools = llm.bind_tools(tools)
query="3乘以12是多少？"
llm_with_tools.invoke(query).tool_calls