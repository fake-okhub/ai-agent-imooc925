# 标准事件之结构化输出 - with_structured_output
# 影响LLM的输出

from typing import Optional
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
import os

llm = ChatOpenAI(
    model="gpt-4",
    temperature=0,
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_API_BASE"),
    )

class Joke(BaseModel):
    """Joke to tell user."""
    setup: str = Field(description="The setup of the joke")
    punchline: str = Field(description="The punchline to the joke")
    rating: Optional[int] = Field(
        default=None, description="How funny the joke is, from 1 to 10"
    )
structured_llm = llm.with_structured_output(Joke)
structured_llm.invoke("给我讲一个关于程序员的笑话")