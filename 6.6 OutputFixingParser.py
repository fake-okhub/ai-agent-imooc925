# 使用OutputFixingParser进行错误修复
from langchain.output_parsers import OutputFixingParser
from typing import List
from langchain_core.exceptions import OutputParserException
from langchain_core.output_parsers import PydanticOutputParser
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

# 定义一个演员模型，有两个字段
class Actor(BaseModel):
    name: str = Field(description="name of an actor")
    film_names: List[str] = Field(description="list of names of films they starred in")


actor_query = "Generate the filmography for a random actor."
parser = PydanticOutputParser(pydantic_object=Actor)

# 假设生成的错误值
misformatted = "{'name': 'Tom Hanks', 'film_names': ['Forrest Gump']}"
# 运行的时候抛出错误
#try:
#    parser.parse(misformatted)
#except OutputParserException as e:
#    print(e)

# 使用OutputFixingParser可以修复错误
# 定义修复所依赖的LLM
new_parser = OutputFixingParser.from_llm(parser=parser, llm=ChatOpenAI(temperature=0,api_key=os.environ.get("OPENAI_API_KEY"),base_url=os.environ.get("OPENAI_API_BASE"),))
# 传入报错信息
new_parser.parse(misformatted)