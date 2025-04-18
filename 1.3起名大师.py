#起名大师，输出格式为一个数组
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import BaseOutputParser

#自定义类
class CommaSeparatedListOutputParser(BaseOutputParser):
    """Parse the output of an LLM call to a comma-separated list."""

    def parse(self, text: str):
        """Parse the output of an LLM call."""
        print(text)
        return text.strip().split(",")


api_base = os.getenv("OPENAI_API_BASE")
api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI(
    model="gpt-3.5-turbo-instruct",
    temperature=0,
    openai_api_key=api_key,
    openai_api_base=api_base
    )
prompt = PromptTemplate.from_template("你是一个起名大师,请模仿示例起3个具有{county}特色的名字,示例：男孩常用名{boy},女孩常用名{girl}。请返回以逗号分隔的列表形式。仅返回逗号分隔的列表，不要返回其他内容。")
message = prompt.format(county="美国男孩",boy="sam",girl="lucy")
print(message)
strs = llm.invoke(message)
CommaSeparatedListOutputParser().parse(strs)